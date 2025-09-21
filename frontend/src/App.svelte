<script lang="ts">
  import { onMount } from "svelte"
  import Light from './lib/Light.svelte'

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

</script>

<main>
  <div class="mainhall-view">
    {#each fixtures as fixture}
      <Light fixture={fixture}
             channelState={channelState}
             selected={selectedFixtures.indexOf(fixture.fixture_id) !== -1}
             onToggle={onToggle}>
      </Light>
    {/each}
  </div>
</main>

<style>
  .mainhall-view {
    position: relative;
    width: 800px;
    height: 569px;
    background-color: transparent;
    background-image: url('assets/mainhall.png');
  }
</style>
