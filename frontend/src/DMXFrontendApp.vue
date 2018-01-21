<template>
  <div class="container" v-if="fixturesLoaded">

    <div class="row">
      <div class="col-6">
        <h1>c-base dmx</h1>
      </div>
      <div class="col-6 text-right">
        WebSocket:
        <template v-if="isConnected">
          Connected.
        </template>
        <template v-else>
          Offline.
        </template>
      </div>
    </div>

    <div class="row">
      <div class="col-12">
        <room-map :fixtures="fixtures"></room-map>
      </div>
    </div>

  </div>
  <div class="container" v-else>
    <div class="row">
      <div class="col-12 text-center">
        <spinner></spinner>
        Loading fixtures …
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Spinner from './components/Spinner.vue'
import RoomMap from './components/RoomMap.vue'

// 20% kaltweis
// 40% warmmweiss
// am ganz aus.

export default {
  components: {
    Spinner,
    RoomMap,
  },
  data: function() {
    return {
      socket: null,
    };
  },
  methods: {
    ...mapActions(['loadFixtures', 'loadChannelState', 'connect']),
  },
  computed: {
    ...mapGetters(['fixtures', 'fixturesLoaded', 'isConnected',])
  },
  created: function() {
    this.loadFixtures();
    this.loadChannelState();
    this.connect();
  }
}
</script>
