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
<!--<div>-->
    <!--<h5>{{ name }} <small>id="{{ fixtureId }}"</small></h5>

    <light-element v-for="el in elements"
                   :key="el.name"
                   :name="el.name"
                   :channels="el.channels">
    </light-element>-->
  <!--</div>-->
<script>
import LightElement from './LightElement.vue'
import RGBSpot from './RGBSpot.vue'

export default {
  name: 'fixture-item',
  components: {
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
