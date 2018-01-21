<template>
  <div class="container" v-if="fixturesLoaded">

    <div class="row">
      <div class="col-12">
        <h1>c-base dmx</h1>
      </div>
    </div>

    <div class="row">
      <div class="col-12">
        <fixture-list :fixtures="fixtures"></fixture-list>
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
import FixtureList from './components/FixtureList.vue'

// 20% kaltweis
// 40% warmmweiss
// am ganz aus.

export default {
  components: {
    Spinner,
    FixtureList,
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
    ...mapGetters(['fixtures', 'fixturesLoaded'])
  },
  created: function() {
    this.loadFixtures();
    this.loadChannelState();
    this.connect();
  }
}
</script>
