<script lang="ts">
  let {fixture, selected, onToggle, channelState} = $props();

  /*const myColor = $derived.by(() => {
    for(let i: number = 0; i < channelState.length; i++) {
      const chan = channelState[i]
      if (chan.channel_id.startsWith(fixture.fixture_id)) {
        console.log(fixture.fixture_id)
        console.log(fixture.fixture_idchan)
      }
    }
  })*/
</script>

<div role="checkbox" tabindex="0" aria-checked={selected}
     onclick={() => onToggle(fixture.fixture_id)}
     onkeydown={() => onToggle(fixture.fixture_id)}
     title="{fixture.model} ({fixture.fixture_id})" 
     class="light" 
     class:selected={selected} 
     style:left="{fixture.pos_x - 10}px"
     style:top="{fixture.pos_y - 10}px" >
</div>

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