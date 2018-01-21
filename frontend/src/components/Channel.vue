<template>
  <form>
    <label :for="inputId">{{ name }}:</label>
    <input type="number"
           :id="inputId"
           :value="channelValue"
           @change="onValueChange">
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'channel',
  components: {
  },
  props: [
    'name',
    'channelId'
  ],
  computed: {
    ...mapGetters(['channelState', 'channelStateLoaded']),
    channelValue() {
      if (this.channelStateLoaded) {
        return this.channelState[this.channelId];
      }
      return 0;
    },
    inputId() {
      return `id_${ this.channelId }`;
    }
  },
  methods: {
    ...mapActions(['updateChannel']),
    onValueChange(ev) {
      let val = parseInt(ev.target.value);
      console.log('Update channel');
      console.log([this.channelId, val]);
      this.updateChannel([this.channelId, val]);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
