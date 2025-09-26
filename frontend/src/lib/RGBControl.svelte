<script lang="ts">
  import iro from '@jaames/iro'
  import { onMount } from 'svelte'

  let {channels, onUpdate, onFinished, channelStateByID} = $props()
  let pickerElement: HTMLElement
  let iroPicker: iro.ColorPicker

  const initialValue = () => {
    const r_channel: string = channels['r'][0]
    const g_channel: string = channels['g'][0]
    const b_channel: string = channels['b'][0]
    const state = $state.snapshot(channelStateByID)
    let r = channelStateByID[r_channel]
    let g = channelStateByID[g_channel]
    let b = channelStateByID[b_channel]
    const color = {"r": r, "g": g, "b": b}
    return color
  }

  const colorChanged = (val: object) => {
    for (const channel_id of channels['r']) {
      onUpdate(channel_id, val.rgb.r)
    }
    for (const channel_id of channels['g']) {
      onUpdate(channel_id, val.rgb.g)
    }
    for (const channel_id of channels['b']) {
      onUpdate(channel_id, val.rgb.b)
    }
    onFinished()
  }

  onMount(() => {
    iroPicker = new iro.ColorPicker(pickerElement)
    iroPicker.color.rgb = initialValue()
    //  = initialValue()
    iroPicker.on('color:change', colorChanged)
  })

</script>


<div>
  <div bind:this={pickerElement}></div>
</div>

<style>
  
</style>