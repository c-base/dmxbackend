<script lang="ts">
  import iro from '@jaames/iro'
  import { onMount } from 'svelte'

  let {channels, onUpdate, onFinished, channelStateByID, channelName} = $props()
  let faderValue = $state(0)

  const initialValue = () => {
    console.log(channelName)
    const r_channel: string = channels[channelName][0]
    return channelStateByID[r_channel]
  }

  const valueChanged = (val: object) => {
    for (const channel_id of channels[channelName]) {
      onUpdate(channel_id, val)
    }
    onFinished()
  }

  onMount(() => {
    faderValue = initialValue()
  })

</script>


<div>
  <label for="bla">{channelName}</label>
  <input id="bla" type="range" min="0" max="255" bind:value={faderValue} onchange={() => valueChanged} class="fader">
</div>

<style>
  .fader {
    width: 100%;
  }
</style>