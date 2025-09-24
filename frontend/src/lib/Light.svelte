<script lang="ts">
  let {fixture, selected, onToggle, channelState} = $props();

  const myColor = $derived.by(() => {
    let r:number = 0
    let g:number = 0
    let b:number = 0
    for(let i: number = 0; i < channelState.length; i++) {
      const chan = channelState[i]
      if (chan.channel_id.startsWith(fixture.fixture_id)) {
        const parts = chan.channel_id.split('/')
        if (parts[1] === 'rgb' || parts[1] === 'rgb1') {
          if (parts[2] === 'r') {
            r = chan.value  
          }
          if (parts[2] === 'g') {
            g = chan.value  
          }
          if (parts[2] === 'b') {
            b = chan.value  
          }
        }
      }
    }
    const color = `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`
    console.log("color " + color)
    return color
  })
</script>

<div role="checkbox" tabindex="0" aria-checked={selected}
     onclick={() => onToggle(fixture.fixture_id)}
     onkeydown={() => onToggle(fixture.fixture_id)}
     title="{fixture.model} ({fixture.fixture_id})" 
     class="light" 
     class:selected={selected} 
     style:background-color={myColor}
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