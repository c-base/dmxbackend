import Vue from 'vue'
import DMXFrontendApp from './DMXFrontendApp.vue'
import store from './stores/dmx_store.js'

// https://gist.github.com/paltman/490049a64fa4115a2cea
// var axios = require("axios");
// var axiosDefaults = require("axios/lib/defaults");

// axiosDefaults.xsrfCookieName = "csrftoken";
// axiosDefaults.xsrfHeaderName = "X-CSRFToken";

new Vue({
  el: '#dmx-app',
  store,
  render: h => h(DMXFrontendApp),
});
