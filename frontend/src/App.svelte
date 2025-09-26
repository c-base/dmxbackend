<script lang="ts">
  import { onMount } from "svelte"
  import Light from './lib/Light.svelte'
  import RGBControl from "./lib/RGBControl.svelte"
  import DimmerPackControl from "./lib/DimmerPackControl.svelte"
  import GenericControl from "./lib/GenericControl.svelte"

  let fixtures = $state<object[]>([])
  let selectedFixtures = $state<string[]>([])
  let channelState = $state<object[]>([])
  let channelStateByID = $state({})
  let socket: Websocket = null;

  onMount(async function () {
    const response = await fetch('/api/v1/fixtures/')
    fixtures = await response.json()
    console.log($state.snapshot(fixtures))

    socket = new WebSocket('/api/v1/websocket_state/')

    // Connection opened
    socket.addEventListener("open", (event: any) => {
      console.log("websocket open")
      console.log(event)
      // do nothing
    });

    // Connection opened
    socket.addEventListener("close", (event: any) => {
      console.log("websocket close")
      console.log(event)
      // do nothing
    });

    // Listen for messages
    socket.addEventListener("message", (event: any) => {onMessage(event)})
  });

  const onMessage = (event: any) => {
    const channel_data = JSON.parse(event.data)
    channelState = channel_data
    for(let chan of channel_data) {
      channelStateByID[chan.channel_id] = chan.value
    }
  }

  const onToggle = (id: string) => {
    console.log("toggle " + id)
    const hasIndex = $state.snapshot(selectedFixtures).indexOf(id)
    console.log(hasIndex)
    if (hasIndex !== -1) {
      selectedFixtures = $state.snapshot(selectedFixtures).filter(m => m !== id);
    }
    else {
      selectedFixtures.push(id)
    }
    console.log("selected: " + JSON.stringify($state.snapshot(selectedFixtures)))
  }

  const onDeselect = () => {
    selectedFixtures = []
  }

  const updateChannel = (channel_id: string, value: number) => {
    console.log(`updating channel ${channel_id} to value ${value}`)
    let state = $state.snapshot(channelState)
    for (let channel of state) {
      if (channel.channel_id === channel_id) {
        channel.value = value
      }
    }
    channelState = state
    channelStateByID[chan.channel_id] = chan.value
  }

  const finnishUpdate = () => {
    const state = $state.snapshot(channelState)
    console.log("finnish")
    socket.send(JSON.stringify(state))
  }


  /* Example fixture:
  {
    "fixture_id": "dmx-1-1",
    "name": "LED PAR56 S\u00e4ulen #1",
    "model": "LED PAR56",
    "pos_x": 607,
    "pos_y": 511,
    "elements": [
        {
            "name": "rgb",
            "pixel": 0,
            "channels": [
                {
                    "name": "r",
                    "channel_id": "dmx-1-1/rgb/r"
                },
                {
                    "name": "g",
                    "channel_id": "dmx-1-1/rgb/g"
                },
                {
                    "name": "b",
                    "channel_id": "dmx-1-1/rgb/b"
                }
            ]
        }
    ]
  } */

  const visibleControls = $derived.by(() => {
    const elements: {[index: string]:any} = {}
    for (let fixture of fixtures) {
      // is the fixture selected?
      if (selectedFixtures.indexOf(fixture.fixture_id) !== -1) {
        for (let el of fixture.elements) {
          // is this the first element of this type that we encounter?
          if (elements[el.name] === undefined) {
            elements[el.name] = {}
            for (let channel of el.channels) {
              elements[el.name][channel.name] = [channel.channel_id]
            } 
          // is this the second (or more-nd) element that we encounter?
          } else {
            for (let channel of el.channels) {
              elements[el.name][channel.name].push(channel.channel_id)  
            } 
          }
        }
      }
    }
    return elements
  })

</script>

<main>
  <div class="main-row">
    <div class="mainhall-view">
      {#each fixtures as fixture}
        <Light fixture={fixture}
              channelState={channelState}
              selected={selectedFixtures.indexOf(fixture.fixture_id) !== -1}
              onToggle={onToggle}>
        </Light>
      {/each}
    </div>
    <div class="main-controls">
      {#each Object.entries(visibleControls) as [element, channels]}
      <div class="control-row">
        <div class="control-label">
          {element}
        </div>
        <div class="control-element">
          {#if element == 'rgb'}
          <RGBControl 
            channelStateByID={channelStateByID} 
            channels={channels}
            onUpdate={(id: string, val: number) => updateChannel(id, val)} onFinished={() => finnishUpdate()}></RGBControl>
          {:else if element == 'dimmerpack'}
          <DimmerPackControl 
            channelStateByID={channelStateByID} 
            channelState={channelState}
            channels={channels}
            onUpdate={(id: string, val: number) => updateChannel(id, val)} onFinished={() => finnishUpdate()}></DimmerPackControl>
          {:else if element == 'dimmer'}
          <GenericControl
            channelName="dim"
            channelStateByID={channelStateByID} 
            channels={channels} 
            onUpdate={(id: string, val: number) => updateChannel(id, val)} onFinished={() => finnishUpdate()}></GenericControl>
          {:else if element == 'strobe'}
          <GenericControl
            channelName="str"
            channelStateByID={channelStateByID} 
            channels={channels} 
            onUpdate={(id: string, val: number) => updateChannel(id, val)} onFinished={() => finnishUpdate()}></GenericControl>
          {:else if element == 'white'}
          <GenericControl
            channelName="whi"
            channelStateByID={channelStateByID} 
            channels={channels} 
            onUpdate={(id: string, val: number) => updateChannel(id, val)} onFinished={() => finnishUpdate()}></GenericControl>
          {:else if element == 'amber'}
          <GenericControl
            channelName="amb"
            channelStateByID={channelStateByID} 
            channels={channels} 
            onUpdate={(id: string, val: number) => updateChannel(id, val)} onFinished={() => finnishUpdate()}></GenericControl>
          {:else if element == 'uv'}
          <GenericControl
            channelName="uv"
            channelStateByID={channelStateByID} 
            channels={channels} 
            onUpdate={(id: string, val: number) => updateChannel(id, val)} onFinished={() => finnishUpdate()}></GenericControl>
          {/if}
        </div>
      </div>
      {/each}
      
    </div>
  </div>
  <div class="button-row">
    <div class="button-left">
      <button onclick={() => onDeselect()} disabled={selectedFixtures.length === 0  }>Select none</button>
    </div>
    <div class="button-right">
      {selectedFixtures.length} selected.
    </div>
  </div>
</main>

<style>
  .main-row {
    display: flex;
    flex-direction: row;
  }
  .mainhall-view {
    position: relative;
    width: 800px;
    height: 569px;
    background-color: transparent;
    background-image: url('assets/mainhall.png');
  }
  .main-controls {
    width: 250px;
  }

  .control-row {
    width: 250px;
    display: flex;
    flex-direction: column;
  }
  .control-label {
    width: 100%;
    text-transform: uppercase;
  }
  .control-element {
    width: 100%;
  }

  .button-row {
    margin-top: 10px;
    display: flex;
    flex-direction: row;
    padding: 0 5px;
  }
  .button-left {
    flex-basis: 50%;
    text-align: left;
  }
  .button-right {
    margin-top: 5px;
    flex-basis: 50%;
    text-align: right;
  }
</style>
