import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex);
const wsUrl = `ws://${window.location.host}/api/v1/websocket_state/`;
let socket = undefined;

/**
 * START the connection to the websocket and try to reconnect when the
 * connection is lost.
 * @param commit The commit function of the fixtures store.
 * @param websocketServerLocation The URL that the Websocket server is responding to.
 */
function start(commit, websocketServerLocation){
    socket = new WebSocket(websocketServerLocation);

    socket.onmessage = function(response) {
      console.log(response.data); // upon message
      commit('updateMultipleChannels', response.data)
    };

    socket.onclose = function(){
      commit('setConnected', false);
      // Try to reconnect in 5 seconds
      setTimeout(function(){
      start(commit, websocketServerLocation)}, 5000);
    };

    socket.onopen = function() {
      commit('setConnected', true);
      console.log("Websocket opened");
      // set message callbacks
    };
}

// root state object.
// each Vuex instance is just a single state tree.
const state = {
  fixtures: [],
  fixturesLoaded: false,
  channelState: {},
  channelStateLoaded: false,
  isConnected: false,
};

// mutations are operations that actually mutates the state.
// each mutation handler gets the entire state tree as the
// first argument, followed by additional payload arguments.
// mutations must be synchronous and can be recorded by plugins
// for debugging purposes.
const mutations = {
  setFixturesLoading (state) {
    state.wishListsLoaded = false;
  },
  setFixtures (state, newFixtures) {
    state.fixtures = newFixtures;
    state.fixturesLoaded = true;
  },
  setChannelStateLoading (state) {
    state.wishListsLoaded = false;
  },
  setChannelState (state, newState) {
    state.channelState = newState;
    state.channelStateLoaded = true;
  },
  setChannel(state, [channel_id, value]) {
    state.channelState[channel_id] = value;
  },
  setConnected(state, value) {
    state.isConnected = value;
  },
  updateMultipleChannels(state, channelList) {
    for (let newChannel of channelList) {
      let channelId = newChannel['channel_id'];
      let newValue = newChannel['value'];
      if (state.channelState[channelId] !== newValue) {
        state.channelState[channelId] = newValue;
      }
    }
  }
};

// actions are functions that cause side effects and can involve
// asynchronous operations.
const actions = {
  loadFixtures ({ commit }) {
    axios.get('/api/v1/fixtures/')
    .then(function (response) {
      commit('setFixtures', response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
  },
  loadChannelState ({ commit }) {
    axios.get('/api/v1/state/')
    .then(function (response) {
      commit('setChannelState', response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
  },
  updateChannel ({ commit }, [channel_id, value]) {
    if (value > 255) {
      value = 255;
    }
    if (value < 0) {
      value = 0;
    }
    commit('setChannel', [channel_id, value]);
    if (socket.readyState === 1) {
      socket.send( JSON.stringify([{'channel_id': channel_id, 'value': value}]) )
    }

  },
  connect({ commit }) {
    start(commit, wsUrl);
  }
};

// getters are functions
const getters = {
  fixtures: state => state.fixtures,
  fixturesLoaded: state => state.fixturesLoaded,
  channelState: state => state.channelState,
  channelStateLoaded: state => state.channelStateLoaded,
  isConnected: state => state.isConnected,
};

// A Vuex instance is created by combining the state, mutations, actions,
// and getters.
export default {
  state,
  getters,
  actions,
  mutations
}
