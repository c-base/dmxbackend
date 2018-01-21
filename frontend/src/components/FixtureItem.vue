<template>
  <div>
    <h5>{{ name }} <small>id="{{ fixtureId }}"</small></h5>
    <light-element v-for="el in elements"
                   :key="el.name"
                   :name="el.name"
                   :channels="el.channels">
    </light-element>
  </div>
</template>

<script>
import LightElement from './LightElement.vue'

export default {
  name: 'fixture-item',
  components: {
    LightElement
  },
  props: [
    'fixtureId',
    'name',
    'posX',
    'posY',
    'elements'
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
