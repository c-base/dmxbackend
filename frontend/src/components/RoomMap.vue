<template>
  <div id="map">
    <fixture-item v-for="fix in fixtures"
                  :key="fix.fixture_id"
                  :fixture-id="fix.fixture_id"
                  :name="fix.name"
                  :model="fix.model"
                  :elements="fix.elements"
                  :pos-x="fix.pos_x"
                  :pos-y="fix.pos_y">
    </fixture-item>
  </div>
</template>

<script>
import FixtureItem from './FixtureItem.vue'

export default {
  name: 'room-map',
  components: {
    FixtureItem,
  },
  props: [
    'fixtures',
  ],
  computed: {
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map {
	position: absolute;
	width: 800px;
	height: 569px;
	background-repeat: no-repeat;
	background-image: url('/static/img/mainhall.png');
	top: 30px;
	left: 110px;
	z-index: 1;
}
</style>
