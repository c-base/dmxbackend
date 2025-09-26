<script lang="ts">
  import { onMount } from 'svelte'
  let {channels, onUpdate, onFinished, channelState} = $props()

  let dim1 = $state(false)
  let dim2 = $state(false)
  let dim3 = $state(false)
  let dim4 = $state(false)

  let check1 = $state(null)
  let check2 = $state(null)
  let check3 = $state(null)
  let check4 = $state(null)

  const initialValue = () => {
    const dim1_channel: string = channels['dim1'][0]
    const dim2_channel: string = channels['dim2'][0]
    const dim3_channel: string = channels['dim3'][0]
    const dim4_channel: string = channels['dim3'][0]

    const state = $state.snapshot(channelState)
    
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

  const valueChanged = () => {
    const dim1_channel: string = channels['dim1'][0]
    const dim2_channel: string = channels['dim2'][0]
    const dim3_channel: string = channels['dim3'][0]
    const dim4_channel: string = channels['dim3'][0]

    onUpdate(dim1_channel, dim1 * 255)
    onUpdate(dim2_channel, dim2 * 255)
    onUpdate(dim3_channel, dim3 * 255)
    onUpdate(dim4_channel, dim4 * 255)
    onFinished()
  }
</script>
<div>
  <label for={check1}>1</label><input bind:this={check1} type="checkbox" bind:checked={dim1}  onchange={valueChanged}>
  <label for={check2}>2</label><input bind:this={check2} type="checkbox" bind:checked={dim2}  onchange={valueChanged}>
  <label for={check3}>3</label><input bind:this={check3} type="checkbox" bind:checked={dim3}  onchange={valueChanged}>
  <label for={check4}>4</label><input bind:this={check4} type="checkbox" bind:checked={dim4}  onchange={valueChanged}>
</div>

<style>

</style>