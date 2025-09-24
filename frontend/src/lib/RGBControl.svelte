<script lang="ts">

  let {channels, onUpdate, onFinished, channelState} = $props();

  const initialValue = $derived.by(() => {
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
    
    const color: string = `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`
    return color
  })

  const colorChanged = (ev: Event) => {
    let val = ev.target.value
    console.log(val)
    const r = Number(`0x${val.substr(1,2)}`)
    const g = Number(`0x${val.substr(3,2)}`)
    const b = Number(`0x${val.substr(5,2)}`)
    for (const channel_id of channels['r']) {
      onUpdate(channel_id, r)
    }
    for (const channel_id of channels['g']) {
      onUpdate(channel_id, g)
    }
    for (const channel_id of channels['b']) {
      onUpdate(channel_id, b)
    }
    onFinished()
  }

</script>


<div>
  {JSON.stringify(channels)}
  <input type="color" value={initialValue} onchange={(ev) => colorChanged(ev)}/>
</div>

<style>
  
</style>