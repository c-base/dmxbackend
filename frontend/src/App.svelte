<script lang="ts">
  import Counter from './lib/Counter.svelte'
</script>

<main>
  <div class="mainhall-view">
    
  </div>

  <div class="card">
    <Counter />
  </div>

</main>

<style>
  .mainhall-view {
    position: relative;
    width: 800px;
    height: 569px;
    background-color: transparent;
    background-image: url('/mainhall.png');
  }

  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
</style>
