<script lang="ts">
  let {fixture, selected, onToggle, channelState} = $props();

  const myColor = $derived.by(() => {
    const r:number = 0
    const g:number = 0
    const b:number = 0
    for(let i: number = 0; i < channelState.length; i++) {
      const chan = channelState[i]
      if (chan.channel_id.startsWith(fixture.fixture_id)) {
        console.log(fixture.fixture_id)
        console.log(chan.value)
      }
    }
    return `#${r.toString(16)}${g.toString(16)}${b.toString(16)}`
  })
</script>

<div role="checkbox" tabindex="0" aria-checked={selected}
     onclick={() => onToggle(fixture.fixture_id)}
     onkeydown={() => onToggle(fixture.fixture_id)}
     title="{fixture.model} ({fixture.fixture_id})" 
     class="light" 
     class:selected={selected} 
     style:background-color="{myColor}"
     style:left="{fixture.pos_x - 10}px"
     style:top="{fixture.pos_y - 10}px"></div>

<style>
  .light {
    display: block;
    cursor: pointer;
    position: absolute;
    width: 20px;
    height: 20px;
    border: 1px solid black;
    border-radius: 20px;
  }
  .light.selected {
    box-shadow: 0 0 5px #000,0 0 0 1px #fff inset;
  }
</style>