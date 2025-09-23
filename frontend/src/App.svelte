<script lang="ts">
  import { onMount } from "svelte"
  import Light from './lib/Light.svelte'
    import RGBControl from "./lib/RGBControl.svelte";

  let fixtures = $state<object[]>([])
  let selectedFixtures = $state<string[]>([])
  let channelState = $state<object[]>([])

  onMount(async function () {
    const response = await fetch('/api/v1/fixtures/')
    fixtures = await response.json()
    console.log($state.snapshot(fixtures))

    const socket = new WebSocket('/api/v1/websocket_state/')

    // Connection opened
    socket.addEventListener("open", (event) => {
      console.log("websocket open")
      console.log(event)
      // do nothing
    });

    // Listen for messages
    socket.addEventListener("message", (event) => {onMessage(event)})
  });

  const onMessage = (event: any) => {
    console.log(event)
    channelState = JSON.parse(event.data)
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
    console.log("selected: " +JSON.stringify($state.snapshot(selectedFixtures)))
  }

  const onDeselect = () => {
    selectedFixtures = []
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
      {#each Object.entries(visibleControls) as [bla, blub]}
        {#if bla == 'rgb'}
        <RGBControl element={blub}></RGBControl>
        {/if}
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
    width: 150px;
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
