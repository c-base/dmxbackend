<template>
  <div class="spot" :id="myId" :style="myStyle">
    <component :is="lightType"
               :fixture-id="fixtureId"
               :name="name"
               :model="model"
               :elements="elements">
    </component>
  </div>
</template>
<script>
import LightElement from './LightElement.vue'
import Octagon from './Octagon.vue'
import RGBSpot from './RGBSpot.vue'

export default {
  name: 'fixture-item',
  components: {
    Octagon,
    RGBSpot,
    LightElement
  },
  props: [
    'fixtureId',
    'name',
    'model',
    'posX',
    'posY',
    'elements'
  ],
  computed: {
    myStyle() {
      return {
        top: `${ this.posY }px`,
        left: `${ this.posX }px`
      };
    },
    myId() {
      return `spot-${ this.fixtureId }`;
    },
    lightType() {
      if (this.model === 'Octagon') {
        return Octagon;
      }
      return RGBSpot;
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.spot {
	height: 20px;
	width: 20px;
	min-height: 20px;
	min-width: 20px;
	position: absolute;
	z-index: 99;
	border-radius: 20px;
	-moz-border-radius: 20px;
	color: white;
	text-align: center;
	border: 1px solid black;
	cursor: crosshair;
  overflow: hidden;
}
</style>
