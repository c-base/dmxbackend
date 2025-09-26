<script lang="ts">
  import iro from '@jaames/iro'
  import { onMount } from 'svelte'

  let {channels, onUpdate, onFinished, channelState} = $props()
  let pickerElement: HTMLElement
  let iroPicker: iro.ColorPicker

  const initialValue = () => {
    const r_channel: string = channels['r'][0]
    const g_channel: string = channels['g'][0]
    const b_channel: string = channels['b'][0]
    const state = $state.snapshot(channelState)
    let r = 0
    let g = 0
    let b = 0
    for (const channel of state) {
      if (channel.channel_id === r_channel) {
        r = channel.value
      }
      if (channel.channel_id === g_channel) {
        g = channel.value
      }
      if (channel.channel_id === b_channel) {
        b = channel.value
      }
    }
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