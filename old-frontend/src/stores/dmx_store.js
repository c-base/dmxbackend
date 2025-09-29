import Vue from 'vue'
import Vuex from 'vuex'

import fixtures from './modules/fixtures.js'

Vue.use(Vuex);

// A Vuex instance is created by combining the state, mutations, actions,
// and getters.
export default new Vuex.Store({
  modules: {
    fixtures,
  }
})
