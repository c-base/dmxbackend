<template>
  <div>
    Light-Element {{ name }}
    <channel v-for="channel in channels"
             :key="channel.channel_id"
             :name="channel.name"
             :channel-id="channel.channel_id">
    </channel>
  </div>
</template>

<script>
import Channel from './Channel.vue'

export default {
  name: 'light-element',
  components: {
    Channel
  },
  props: [
    'name',
    'channels'
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
