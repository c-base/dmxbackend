<script lang="ts">
  import { onMount } from 'svelte'

  let {channels, onUpdate, onFinished, channelStateByID, channelName, disabled} = $props()
  let faderValue = $state(0)

  const initialValue = () => {
    const channel_id: string = channels[channelName][0]
    const value = channelStateByID[channel_id]
    if (value == 0) {
      return 128
    } else {
      return value
    }
  }

  const valueChanged = (ev: Event) => {
    for (const channel_id of channels[channelName]) {
      onUpdate(channel_id, parseInt(ev.target.value))
    }
    onFinished()
  }

  function turnOff() {
    faderValue = 128
    for (const channel_id of channels[channelName]) {
      onUpdate(channel_id, 128)
    }
    onFinished()
  }

  onMount(() => {
    faderValue = initialValue()
  })
</script>
<div class="rotation-fader-wrapper">
  <input type="range" min="1" max="255" disabled={disabled} bind:value={faderValue} onchange={(ev) => valueChanged(ev)} class="rotation-fader" list="rotation-fader-values">
  <button onclick={turnOff}>Stop rotation</button>

  <datalist id="rotation-fader-values">
    <option value="128" label="Off"></option>
  </datalist>
</div>

<style>
  .rotation-fader-wrapper {
    height: 24px;
    border: 1px solid #000;
    padding-top: 3px;
    padding-left: 3px;
    padding-right: 8px;
    border-radius: 24px;
  }
  .rotation-fader {
    width: 100%;
  }
</style>
