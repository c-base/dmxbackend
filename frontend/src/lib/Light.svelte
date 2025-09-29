<script lang="ts">
  let {fixture, selected, onToggle, channelState} = $props();


  let myRotation = $derived(`rotate(${fixture.rot}deg)`)

  const myColor = $derived.by(() => {
    let r:number = 0
    let g:number = 0
    let b:number = 0
    for(let i: number = 0; i < channelState.length; i++) {
      const chan = channelState[i]
      if (chan.channel_id.startsWith(fixture.fixture_id + '/')) {
        const parts = chan.channel_id.split('/')
        if (parts[1] === 'rgb' || parts[1] === 'rgb1') {
          if (parts[2] === 'r') {
            console.log(chan)
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
    return color
  })
</script>

{#if fixture.model === 'Octagon' || fixture.model === 'RevueLED 120 COB'}
<div role="checkbox" tabindex="0" aria-checked={selected}
     onclick={() => onToggle(fixture.fixture_id)}
     onkeydown={() => onToggle(fixture.fixture_id)}
     title="{fixture.name} ({fixture.model}, {fixture.fixture_id})" 
     class="octagon" 
     class:selected={selected} 
     style:transform={myRotation}
     style:left="{fixture.pos_x - 10}px"
     style:top="{fixture.pos_y - 10}px">
  <svg
    width="15"
    height="24"
    viewBox="0 0 31.301041 46.153561"
    version="1.1"
    id="svg1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:svg="http://www.w3.org/2000/svg">
    <defs
      id="defs1" />
    <g
      id="layer1"
      transform="translate(-40.919922,-33.297196)">
      <rect
        style="fill:none;stroke:#000000;stroke-width:4"
        id="rect1"
        width="30.989601"
        height="29.88932"
        x="41.075642"
        y="49.405712" />
      <path
        style="fill:none;stroke:#000000;stroke-width:4"
        d="m 41.381166,33.422197 8.72596,15.113809"
        id="path1" />
      <path
        style="fill:none;stroke:#000000;stroke-width:4"
        d="M 71.760831,33.422197 63.034867,48.536004"
        id="path3" />
    </g>
  </svg>
</div>
{:else if fixture.model === 'LED PAR 36 COB RGBW 12W'}
<div role="checkbox" tabindex="0" aria-checked={selected}
     onclick={() => onToggle(fixture.fixture_id)}
     onkeydown={() => onToggle(fixture.fixture_id)}
     title="{fixture.name} ({fixture.model}, {fixture.fixture_id})" 
     class="bar"
     class:selected={selected}
     style:transform={myRotation}
     style:background-color={myColor}
     style:left="{fixture.pos_x - 10}px"
     style:top="{fixture.pos_y - 10}px"></div>
{:else}
<div role="checkbox" tabindex="0" aria-checked={selected}
     onclick={() => onToggle(fixture.fixture_id)}
     onkeydown={() => onToggle(fixture.fixture_id)}
     title="{fixture.name} ({fixture.model}, {fixture.fixture_id})"
     class="light" 
     class:selected={selected}
     style:background-color={myColor}
     style:left="{fixture.pos_x - 10}px"
     style:top="{fixture.pos_y - 10}px"></div>
{/if}
<style>
  .bar {
    display: block;
    cursor: pointer;
    position: absolute;
    width: 40px;
    height: 10px;
    border: 1px solid black;
  }
  .bar.selected {
    box-shadow: 0 0 4px 2px #000, 0 0 0 2px #fff inset;
  }
  .octagon {
    display: block;
    cursor: pointer;
    position: absolute;
    width: 20px;
    height: 26px;
    border: none;
  }
  .octagon.selected {
    box-shadow: 0 0 4px 2px #000, 0 0 0 2px #fff inset;
  }
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
    box-shadow: 0 0 4px 2px #000, 0 0 0 2px #fff inset;
  }
</style>