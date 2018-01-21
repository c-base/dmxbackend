<template>
  <div>
  <fixture-item v-for="fix in fixtures"
                :key="fix.fixture_id"
                :fixture-id="fix.fixture_id"
                :name="fix.name"
                :elements="fix.elements"
                :pos-x="fix.pos_x"
                :pos-y="fix.pos_y">
  </fixture-item>
  </div>
</template>

<script>
import FixtureItem from './FixtureItem.vue'

export default {
  name: 'fixture-list',
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
</style>
