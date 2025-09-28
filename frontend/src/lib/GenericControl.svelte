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

  const valueChanged = (ev) => {
    for (const channel_id of channels[channelName]) {
      onUpdate(channel_id, parseInt(ev.target.value))
    }
    onFinished()
  }

  onMount(() => {
    faderValue = initialValue()
  })

</script>


<div class="fader-wrapper">
  <input type="range" min="0" max="255" bind:value={faderValue} onchange={(ev) => valueChanged(ev)} class="fader">
</div>

<style>
  .fader-wrapper {
    height: 24px;
    border: 1px solid #000;
    padding-top: 3px;
    padding-left: 3px;
    padding-right: 8px;
    border-radius: 24px;
  }
  .fader {
    width: 100%;
  }
</style>