<template>
  <div @click="onChange">
    <span class="is-on" v-if="isOn">
      1
    </span>
    <span class="is-on" v-else="">
      0
    </span>
  </div>
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
    return {
      isOpen: false,
      myColor: '#000000',
      on: 0,
    }
  },
  computed: {
    ...mapGetters(['channelState']),
    myStyle() {
      return {
        top: `${ this.posY }px`,
        left: `${ this.posX }px`
      };
    },
    isOn() {
      if (this.on > 0) {
        return true;
      }
      else {
        return false;
      }
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
      if (this.on > 0) {
        this.on = 0;
      }
      else {
        this.on = 1;
      }
      let cw  = 102.0 * this.on;
      let ww  =  51.0 * this.on;
      let a   =  10.0 * this.on;
      let dim = 128.0 * this.on;

      for (let el of this.elements) {
        for (let chan of el.channels) {
          if (chan.name === 'cw') {
            this.updateChannel([chan.channel_id, cw])
          }
          if (chan.name === 'ww') {
            this.updateChannel([chan.channel_id, ww])
          }
          if (chan.name === 'a') {
            this.updateChannel([chan.channel_id, a])
          }
          if (chan.name === 'dim') {
            this.updateChannel([chan.channel_id, dim])
          }
        }
      }
    },
    doColor() {
      let cw  = 0;
      let ww  = 0;
      let a   = 0;
      let dim = 0;
      for (let el of this.elements) {
        for (let chan of el.channels) {
          if (chan.name === 'cw') {
            cw = this.channelState[chan.channel_id];
          }
          if (chan.name === 'ww') {
            ww = this.channelState[chan.channel_id];
          }
          if (chan.name === 'a') {
            a = this.channelState[chan.channel_id];
          }
          if (chan.name === 'dim') {
            dim = this.channelState[chan.channel_id];
          }
        }
      }
      if (dim > 1) {
        this.on = true;
      }
      else {
        this.on = false;
      }
    }
  },
  watch: {
    channelState: function(oldValue, newValue) {
      this.doColor();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .is-on {
    color: #c82333;
  }
</style>
