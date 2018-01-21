<template>
  <input class="spot" type="color" @change="onChange" v-model="myColor"/>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import chroma from 'chroma-js'
// import LightElement from './LightElement.vue'

export default {
  name: 'rgb-spot',
  components: {
    // LightElement
  },
  props: [
    'fixtureId',
    'name',
    'model',
    'elements'
  ],
  data: function() {
    let r = 0;
    let g = 0;
    let b = 0;
    for (let el of this.elements) {
      for (let chan of el.channels) {
        if (chan.name === 'r') {
          r = chan.value;
        }
        if (chan.name === 'g') {
          g = chan.value;
        }
        if (chan.name === 'b') {
          r = chan.value;
        }
      }
    }

    return {
      isOpen: false,
      myColor: chroma([r,g,b]).hex()
    }
  },
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
    myColorStyle() {
      return {
        backgroundColor: this.myColor
      }
    }
  },
  methods: {
    ...mapActions(['updateChannel']),
    onOpen() {
      this.isOpen = true;
    },
    onChange() {
      let color = chroma(this.myColor);
      console.log(color);
      let [r, g, b] = color.rgb();
      this.isOpen = false;
      //
      for (let el of this.elements) {
        for (let chan of el.channels) {
          if (chan.name === 'r') {
            this.updateChannel([chan.name, r])
          }
          if (chan.name === 'g') {
            this.updateChannel([chan.name, g])
          }
          if (chan.name === 'b') {
            this.updateChannel([chan.name, g])
          }
        }
      }
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.spot {
	height: 40px;
	width: 40px;
	position: relative;
  left: -10px;
  top: -10px;
	z-index: 99;

	color: white;
	text-align: center;
	border: 0px solid black;
	cursor: crosshair;
}
</style>
