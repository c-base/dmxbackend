"use strict";



;define('dmx-frontend/adapters/application', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberData.default.RESTAdapter.extend({});
});
;define('dmx-frontend/adapters/color', ['exports', 'ember-localstorage-adapter'], function (exports, _emberLocalstorageAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberLocalstorageAdapter.default.extend({});
});
;define('dmx-frontend/adapters/light-channel', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberData.default.Adapter.extend({
    state: Ember.inject.service(),
    updateRecord(store, type, snapshot) {
      const state = Ember.get(this, 'state');
      state.save(snapshot);

      return Ember.RSVP.resolve(undefined); // tell the store that all is OK.
    }
  });
});
;define('dmx-frontend/adapters/light-fixture', ['exports', 'dmx-frontend/adapters/application'], function (exports, _application) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _application.default.extend({
    urlForFindAll() {
      return 'api/v1/fixtures/';
    }
  });
});
;define('dmx-frontend/adapters/ls-adapter', ['exports', 'ember-localstorage-adapter/adapters/ls-adapter'], function (exports, _lsAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _lsAdapter.default;
});
;define('dmx-frontend/adapters/preset-channel', ['exports', 'ember-localstorage-adapter'], function (exports, _emberLocalstorageAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberLocalstorageAdapter.default.extend({});
});
;define('dmx-frontend/adapters/preset', ['exports', 'ember-localstorage-adapter'], function (exports, _emberLocalstorageAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberLocalstorageAdapter.default.extend({});
});
;define('dmx-frontend/app', ['exports', 'dmx-frontend/resolver', 'ember-load-initializers', 'dmx-frontend/config/environment'], function (exports, _resolver, _emberLoadInitializers, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  const App = Ember.Application.extend({
    modulePrefix: _environment.default.modulePrefix,
    podModulePrefix: _environment.default.podModulePrefix,
    Resolver: _resolver.default
  });

  (0, _emberLoadInitializers.default)(App, _environment.default.modulePrefix);

  exports.default = App;
});
;define("dmx-frontend/application/template", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "LI1k5VIU", "block": "{\"symbols\":[],\"statements\":[[1,[20,\"outlet\"],false],[0,\"\\n\"],[1,[20,\"magic-pi\"],false]],\"hasEval\":false}", "meta": { "moduleName": "dmx-frontend/application/template.hbs" } });
});
;define('dmx-frontend/components/c-base-map-light-element/component', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Component.extend({
    tagName: '',

    buttonStyle: Ember.computed('lightElement.simpleColor', {
      get() {
        return Ember.String.htmlSafe(`
        background: ${Ember.get(this, 'lightElement.simpleColor')};
      `);
      }
    }),

    selected: Ember.computed('selectedIds.[]', 'lightElement.id', {
      get() {
        return Ember.get(this, 'selectedIds').includes(Ember.get(this, 'lightElement.id'));
      }
    }),
    actions: {
      select() {
        if (Ember.get(this, 'selected')) {
          // unselect
          Ember.get(this, 'select')(Ember.get(this, 'selectedIds').without(Ember.get(this, 'lightElement.id')));
        } else {
          // select
          Ember.get(this, 'select')([Ember.get(this, 'lightElement.id'), ...Ember.get(this, 'selectedIds')]);
        }
      }
    }
  });
});
;define("dmx-frontend/components/c-base-map-light-element/styles", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    "button": "_button_d42vrc",
    "single-element": "_single-element_d42vrc",
    "multi-element": "_multi-element_d42vrc",
    "selected": "_selected_d42vrc"
  };
});
;define("dmx-frontend/components/c-base-map-light-element/template", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "P180fa78", "block": "{\"symbols\":[],\"statements\":[[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"select\"],null]],[11,\"style\",[20,\"buttonStyle\"]],[11,\"class\",[27,[[26,\"local-class\",[[26,\"concat\",[\"button \",[26,\"if\",[[22,[\"selected\"]],\"selected\"],null],\" \",[26,\"if\",[[22,[\"isSingleElement\"]],\"single-element\",\"multi-element\"],null]],null]],[[\"from\"],[[26,\"unbound\",[[22,[\"__styles__\"]]],null]]]]]]],[8],[0,\"\\n\"],[9]],\"hasEval\":false}", "meta": { "moduleName": "dmx-frontend/components/c-base-map-light-element/template.hbs" } });
});
;define('dmx-frontend/components/c-base-map-light/component', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Component.extend({
    attributeBindings: ['style'],
    localClassNames: ['light'],
    isSingleElement: Ember.computed.equal('lightFixture.elements.length', 1),
    style: Ember.computed('lightFixture.posY', 'lightFixture.posX', 'lightFixture.simpleColor', {
      get() {
        return Ember.String.htmlSafe(`
        top: ${Ember.get(this, 'lightFixture.posY')}px;
        left: ${Ember.get(this, 'lightFixture.posX')}px;
      `);
      }
    })
  });
});
;define("dmx-frontend/components/c-base-map-light/styles", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    "light": "_light_gnsbx7",
    "elements": "_elements_gnsbx7",
    "expand": "_expand_gnsbx7"
  };
});
;define("dmx-frontend/components/c-base-map-light/template", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "bd2OVL3s", "block": "{\"symbols\":[\"lightElement\"],\"statements\":[[6,\"div\"],[11,\"class\",[27,[[26,\"unbound\",[[22,[\"__styles__\",\"elements\"]]],null]]]],[8],[0,\"\\n\"],[4,\"if\",[[26,\"or\",[[22,[\"extend\"]],[22,[\"isSingleElement\"]]],null]],null,{\"statements\":[[4,\"each\",[[22,[\"lightFixture\",\"elements\"]]],null,{\"statements\":[[0,\"      \"],[1,[26,\"c-base-map-light-element\",null,[[\"selectedIds\",\"select\",\"lightElement\",\"isSingleElement\"],[[22,[\"selectedIds\"]],[22,[\"select\"]],[21,1,[]],[22,[\"isSingleElement\"]]]]],false],[0,\"\\n\"]],\"parameters\":[1]},null],[4,\"unless\",[[22,[\"isSingleElement\"]]],null,{\"statements\":[[0,\"      \"],[6,\"div\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],[26,\"mut\",[[22,[\"extend\"]]],null],false],null]],[11,\"class\",[27,[[26,\"unbound\",[[22,[\"__styles__\",\"expand\"]]],null]]]],[8],[0,\"\\n        \"],[1,[26,\"fa-icon\",[\"arrows-alt-h\"],null],false],[0,\"\\n      \"],[9],[0,\"\\n\"]],\"parameters\":[]},null]],\"parameters\":[]},{\"statements\":[[0,\"    \"],[6,\"div\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],[26,\"mut\",[[22,[\"extend\"]]],null],true],null]],[11,\"class\",[27,[[26,\"unbound\",[[22,[\"__styles__\",\"expand\"]]],null]]]],[8],[0,\"\\n      \"],[1,[26,\"fa-icon\",[\"arrows-alt-h\"],null],false],[0,\"\\n    \"],[9],[0,\"\\n    \"],[1,[26,\"c-base-map-multi-light-element\",null,[[\"selectedIds\",\"select\",\"lightElements\"],[[22,[\"selectedIds\"]],[22,[\"select\"]],[22,[\"lightFixture\",\"elements\"]]]]],false],[0,\"\\n\"]],\"parameters\":[]}],[9]],\"hasEval\":false}", "meta": { "moduleName": "dmx-frontend/components/c-base-map-light/template.hbs" } });
});
;define('dmx-frontend/components/c-base-map-multi-light-element/component', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Component.extend({
    tagName: '',
    selected: Ember.computed('selectedIds.[]', 'lightElements.@each.id', {
      get() {
        return this.lightElements.map(x => x.get('id')).any(x => this.selectedIds.includes(x));
      }
    }),
    actions: {
      select() {
        const ids = this.lightElements.map(le => le.get('id'));

        if (this.selected) {
          // unselect
          this.select(this.selectedIds.filter(x => !ids.includes(x)));
        } else {
          // select
          this.select([...this.selectedIds, ...ids]);
        }
      }
    }
  });
});
;define("dmx-frontend/components/c-base-map-multi-light-element/styles", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    "button": "_button_lpm5os",
    "single-element": "_single-element_lpm5os",
    "multi-element": "_multi-element_lpm5os",
    "selected": "_selected_lpm5os"
  };
});
;define("dmx-frontend/components/c-base-map-multi-light-element/template", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "OeErTeDv", "block": "{\"symbols\":[],\"statements\":[[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"select\"],null]],[11,\"class\",[27,[[26,\"local-class\",[[26,\"concat\",[\"button \",[26,\"if\",[[22,[\"selected\"]],\"selected\"],null]],null]],[[\"from\"],[[26,\"unbound\",[[22,[\"__styles__\"]]],null]]]]]]],[8],[0,\"\\n\"],[9]],\"hasEval\":false}", "meta": { "moduleName": "dmx-frontend/components/c-base-map-multi-light-element/template.hbs" } });
});
;define('dmx-frontend/components/c-base-map/component', ['exports', 'ember-concurrency'], function (exports, _emberConcurrency) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Component.extend({
    localClassNames: 'map',
    lightElements: Ember.computed('lightFixtures.@each.elements', {
      get() {
        return Ember.get(this, 'lightFixtures').map(f => Ember.get(f, 'elements').toArray()).reduce((a, b) => [...a, ...b], []);
      }
    }),
    selectedLightElements: Ember.computed('selectedIds.[]', 'lightElements.@each.id', {
      get() {
        return Ember.get(this, 'lightElements').filter(li => Ember.get(this, 'selectedIds').includes(Ember.get(li, 'id')));
      }
    }),
    // selectWhite: task(function * (on) {
    //   const vals = on
    //     ? { cw: 102, ww: 51, dim: 128 }
    //     : { cw: 0, ww: 0, dim: 0 };

    //   yield this.get('setVals').perform(vals);
    // }),
    // selectColor: task(function * (color) {
    //   const vals = {
    //     r: Number.parseInt([...color].slice(1, 3).join(''), 16),
    //     g: Number.parseInt([...color].slice(3, 5).join(''), 16),
    //     b: Number.parseInt([...color].slice(5, 7).join(''), 16),
    //   };

    //   yield this.get('setVals').perform(vals);
    // }),
    // setVals: task(function * (vals) {
    //   const channels = get(this, 'selectedLightElements')
    //     .reduce((arr, element) => [...get(element, 'channels').toArray(), ...arr], []);

    //   channels.forEach(c => {
    //     let name = get(c, 'name');
    //     if(vals[name] !== undefined) {
    //       set(c, 'value', vals[name]);
    //     }
    //   });

    //   yield all(channels.map(channel => channel.save()));
    // }),
    actions: {
      selectAll() {
        Ember.get(this, 'select')(Ember.get(this, 'lightElements').map(f => Ember.get(f, 'id')));
      },
      deselectAll() {
        Ember.get(this, 'select')([]);
      },
      setChannel(name, value) {
        const channels = Ember.get(this, 'selectedLightElements').reduce((arr, element) => [...Ember.get(element, 'channels').toArray(), ...arr], []);

        channels.filter(c => c.name === name).forEach(c => {
          c.set('value', value);
          c.save();
        });
      }
    }
  });
});
;define("dmx-frontend/components/c-base-map/styles", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    "map": "_map_cf85c8",
    "image": "_image_cf85c8"
  };
});
;define("dmx-frontend/components/c-base-map/template", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "8++JKBGb", "block": "{\"symbols\":[\"lightFixture\"],\"statements\":[[6,\"section\"],[8],[0,\"\\n  \"],[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"selectAll\"],null]],[8],[0,\"Select all\"],[9],[0,\"\\n  \"],[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"deselectAll\"],null]],[8],[0,\"Deselect all\"],[9],[0,\"\\n\"],[9],[0,\"\\n\"],[6,\"section\"],[11,\"class\",[27,[[26,\"unbound\",[[22,[\"__styles__\",\"image\"]]],null]]]],[8],[0,\"\\n\"],[4,\"each\",[[22,[\"lightFixtures\"]]],null,{\"statements\":[[0,\"    \"],[1,[26,\"c-base-map-light\",null,[[\"lightFixture\",\"selectedIds\",\"select\"],[[21,1,[]],[22,[\"selectedIds\"]],[22,[\"select\"]]]]],false],[0,\"\\n\"]],\"parameters\":[1]},null],[0,\"\\n  \"],[6,\"img\"],[10,\"src\",\"http://baseos.cbrp3.c-base.org/dmxdmon/mainhall.png\"],[8],[9],[0,\"\\n\"],[9],[0,\"\\n\\n\"],[6,\"section\"],[8],[0,\"\\n  \"],[1,[26,\"color-picker\",null,[[\"setChannel\"],[[26,\"action\",[[21,0,[]],\"setChannel\"],null]]]],false],[0,\"\\n\"],[9]],\"hasEval\":false}", "meta": { "moduleName": "dmx-frontend/components/c-base-map/template.hbs" } });
});
;define('dmx-frontend/components/color-picker/component', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Component.extend({
    values: null,
    store: Ember.inject.service(),
    init() {
      this._super(...arguments);
      this.set('values', []);
    },
    presets: Ember.computed({
      get() {
        return this.store.findAll('preset');
      }
    }),
    lightChannels: Ember.computed({
      get() {
        return Ember.get(this, 'store').peekAll('light-channel');
      }
    }),
    nonRgbChannels: Ember.computed('channels.@each.name', 'values.@each.{name,value}', {
      get() {
        return this.lightChannels.map(c => c.get('name')).uniq().filter(c => !['r', 'g', 'b'].includes(c)).map(name => {
          const value = this.values.find(v => v.name === name);
          if (value) {
            return value;
          }
          return { name, disabled: true };
        });
      }
    }),
    currentRgb: Ember.computed('channels.@each.name', 'values.@each.{name,value}', {
      get() {
        const colors = ['r', 'g', 'b'].map(c => this.values.find(v => v.name === c)).filter(x => x).map(c => c.value);
        if (colors.length !== 3) {
          return null;
        }

        return `#${colors.map(v => v.toString(16).padStart(2, '0')).join('')}`;
      }
    }),
    actions: {
      selectChannelValue(name, value, preventUpdate) {
        const other = this.values.filter(v => v.name !== name);
        if (value === null) {
          this.set('values', other);
        } else {
          value = parseInt(value);
          this.set('values', [{ name, value }, ...other]);
          if (!preventUpdate) {
            this.setChannel(name, value);
          }
        }
      },
      selectColor(color) {
        const vals = {
          r: Number.parseInt([...color].slice(1, 3).join(''), 16),
          g: Number.parseInt([...color].slice(3, 5).join(''), 16),
          b: Number.parseInt([...color].slice(5, 7).join(''), 16)
        };
        Object.keys(vals).forEach(k => this.send('selectChannelValue', k, vals[k]));
      },
      clear() {
        this.set('values', []);
      },
      enableRgb() {
        this.set('values', [{ name: 'r', value: 0 }, { name: 'g', value: 0 }, { name: 'b', value: 0 }, ...this.values]);
      },
      disableRgb() {
        this.set('values', this.values.filter(v => !['r', 'g', 'b'].includes(v.name)));
      },
      async save() {
        const id = Math.random().toString().substr(2);
        const preset = this.store.createRecord('preset', { id });
        await preset.save();

        await Ember.RSVP.all(this.values.map(value => this.store.createRecord('preset-channel', {
          id: `${id}-${value.name}`,
          value: value.value,
          name: value.name,
          preset
        }).save()));
      },
      activatePreset(preset) {
        preset.channels.forEach(c => {
          this.setChannel(c.name, c.value);
        });
      }
    }
  });
});
;define("dmx-frontend/components/color-picker/styles", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    "colors": "_colors_1p967g",
    "color": "_color_1p967g",
    "delete-color": "_delete-color_1p967g"
  };
});
;define("dmx-frontend/components/color-picker/template", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "oBru+jYp", "block": "{\"symbols\":[\"preset\",\"c\",\"channel\"],\"statements\":[[0,\"RGB:\\n\"],[4,\"if\",[[22,[\"currentRgb\"]]],null,{\"statements\":[[0,\"  \"],[6,\"input\"],[11,\"value\",[20,\"currentRgb\"]],[11,\"onchange\",[26,\"action\",[[21,0,[]],\"selectColor\"],[[\"value\"],[\"target.value\"]]]],[11,\"class\",[27,[[26,\"unbound\",[[22,[\"__styles__\",\"picker\"]]],null]]]],[10,\"type\",\"color\"],[8],[9],[0,\"\\n    \"],[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"disableRgb\"],null]],[8],[0,\"Disable\"],[9],[0,\"\\n\"]],\"parameters\":[]},{\"statements\":[[0,\"  \"],[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"enableRgb\"],null]],[8],[0,\"Enable\"],[9],[0,\"\\n\"]],\"parameters\":[]}],[0,\"\\n\"],[4,\"each\",[[21,0,[\"nonRgbChannels\"]]],null,{\"statements\":[[0,\"  \"],[6,\"div\"],[8],[0,\"\\n    \"],[1,[21,3,[\"name\"]],false],[0,\" (\"],[1,[21,3,[\"value\"]],false],[0,\")\\n\"],[4,\"if\",[[21,3,[\"disabled\"]]],null,{\"statements\":[[0,\"      \"],[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"selectChannelValue\",[21,3,[\"name\"]],0,true],null]],[8],[0,\"Enable\"],[9],[0,\"\\n\"]],\"parameters\":[]},{\"statements\":[[0,\"      \"],[6,\"input\"],[10,\"min\",\"0\"],[10,\"max\",\"254\"],[11,\"value\",[21,3,[\"value\"]]],[11,\"onchange\",[26,\"action\",[[21,0,[]],[26,\"action\",[[21,0,[]],\"selectChannelValue\",[21,3,[\"name\"]]],null]],[[\"value\"],[\"target.value\"]]]],[10,\"type\",\"range\"],[8],[9],[0,\"\\n      \"],[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"selectChannelValue\",[21,3,[\"name\"]],null],null]],[8],[0,\"Disable\"],[9],[0,\"\\n\"]],\"parameters\":[]}],[0,\"  \"],[9],[0,\"\\n\"]],\"parameters\":[3]},null],[0,\"\\n\"],[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"save\"],null]],[8],[0,\"Save\"],[9],[0,\"\\n\"],[6,\"button\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"clear\"],null]],[8],[0,\"Clear\"],[9],[0,\"\\n\\n\"],[4,\"each\",[[22,[\"presets\"]]],null,{\"statements\":[[0,\"  \"],[6,\"div\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"activatePreset\",[21,1,[]]],null]],[8],[0,\"\\n\"],[4,\"each\",[[21,1,[\"channels\"]]],null,{\"statements\":[[0,\"      \"],[1,[21,2,[\"name\"]],false],[0,\":\"],[1,[21,2,[\"value\"]],false],[0,\"\\n\"]],\"parameters\":[2]},null],[0,\"  \"],[9],[0,\"\\n\"]],\"parameters\":[1]},null]],\"hasEval\":false}", "meta": { "moduleName": "dmx-frontend/components/color-picker/template.hbs" } });
});
;define('dmx-frontend/components/ember-tether', ['exports', 'ember-tether/components/ember-tether'], function (exports, _emberTether) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _emberTether.default;
    }
  });
});
;define('dmx-frontend/components/fa-icon', ['exports', '@fortawesome/ember-fontawesome/components/fa-icon'], function (exports, _faIcon) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _faIcon.default;
    }
  });
});
;define('dmx-frontend/components/fontawesome-node', ['exports', '@fortawesome/ember-fontawesome/components/fontawesome-node'], function (exports, _fontawesomeNode) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _fontawesomeNode.default;
    }
  });
});
;define('dmx-frontend/components/magic-pi/component', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Component.extend({
    magic: Ember.inject.service(),
    actions: {
      pi(event) {
        if (event.shiftKey && event.ctrlKey && !Ember.get(this, 'magic.active')) {
          Ember.set(this, 'magic.active', true);
          Ember.set(this, 'showWarning', true);
        }

        return false;
      },
      continue() {
        Ember.set(this, 'showWarning', false);
      }
    }
  });
});
;define("dmx-frontend/components/magic-pi/styles", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    "pi": "_pi_1cj4fg",
    "warning": "_warning_1cj4fg"
  };
});
;define("dmx-frontend/components/magic-pi/template", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "9egaTnTI", "block": "{\"symbols\":[],\"statements\":[[6,\"span\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"pi\"],null]],[11,\"oncontextmenu\",[26,\"action\",[[21,0,[]],\"pi\"],null]],[11,\"class\",[27,[[26,\"unbound\",[[22,[\"__styles__\",\"pi\"]]],null]]]],[8],[0,\"π\"],[9],[0,\"\\n\\n\"],[4,\"if\",[[22,[\"showWarning\"]]],null,{\"statements\":[[0,\"  \"],[6,\"div\"],[11,\"onclick\",[26,\"action\",[[21,0,[]],\"continue\"],null]],[11,\"class\",[27,[[26,\"unbound\",[[22,[\"__styles__\",\"warning\"]]],null]]]],[8],[0,\"\\n    High Security Access Granted\\n  \"],[9],[0,\"\\n\"]],\"parameters\":[]},null]],\"hasEval\":false}", "meta": { "moduleName": "dmx-frontend/components/magic-pi/template.hbs" } });
});
;define('dmx-frontend/helpers/and', ['exports', 'ember-truth-helpers/helpers/and'], function (exports, _and) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _and.default;
    }
  });
  Object.defineProperty(exports, 'and', {
    enumerable: true,
    get: function () {
      return _and.and;
    }
  });
});
;define('dmx-frontend/helpers/app-version', ['exports', 'dmx-frontend/config/environment', 'ember-cli-app-version/utils/regexp'], function (exports, _environment, _regexp) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.appVersion = appVersion;
  function appVersion(_, hash = {}) {
    const version = _environment.default.APP.version;
    // e.g. 1.0.0-alpha.1+4jds75hf

    // Allow use of 'hideSha' and 'hideVersion' For backwards compatibility
    let versionOnly = hash.versionOnly || hash.hideSha;
    let shaOnly = hash.shaOnly || hash.hideVersion;

    let match = null;

    if (versionOnly) {
      if (hash.showExtended) {
        match = version.match(_regexp.versionExtendedRegExp); // 1.0.0-alpha.1
      }
      // Fallback to just version
      if (!match) {
        match = version.match(_regexp.versionRegExp); // 1.0.0
      }
    }

    if (shaOnly) {
      match = version.match(_regexp.shaRegExp); // 4jds75hf
    }

    return match ? match[0] : version;
  }

  exports.default = Ember.Helper.helper(appVersion);
});
;define('dmx-frontend/helpers/build-css', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.buildCss = buildCss;


  function normalizesite(val) {
    const regExp = new RegExp('^\d*(px|r?em|%)$');
    if (regExp.exec(val)) {
      return val;
    }

    let number = Number(val);
    if (!Number.isNaN(number)) {
      return `${number}px`;
    }
  }

  const normalizers = {
    height: normalizesite,
    width: normalizesite,
    left: normalizesite,
    right: normalizesite,
    top: normalizesite,
    bottom: normalizesite
  };

  function normalizeCssAttribute(attribute, value) {
    if (normalizers[attribute]) {
      return normalizers[attribute](value);
    } else {
      return value;
    }
  }

  function buildCss(params, hash) {
    let str = Object.keys(hash).map(key => `${key}:${normalizeCssAttribute(key, hash[key])};`).join('');

    return Ember.String.htmlSafe(str);
  }

  exports.default = Ember.Helper.helper(buildCss);
});
;define('dmx-frontend/helpers/cancel-all', ['exports', 'ember-concurrency/helpers/cancel-all'], function (exports, _cancelAll) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _cancelAll.default;
    }
  });
  Object.defineProperty(exports, 'cancelAll', {
    enumerable: true,
    get: function () {
      return _cancelAll.cancelAll;
    }
  });
});
;define('dmx-frontend/helpers/eq', ['exports', 'ember-truth-helpers/helpers/equal'], function (exports, _equal) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _equal.default;
    }
  });
  Object.defineProperty(exports, 'equal', {
    enumerable: true,
    get: function () {
      return _equal.equal;
    }
  });
});
;define('dmx-frontend/helpers/gt', ['exports', 'ember-truth-helpers/helpers/gt'], function (exports, _gt) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _gt.default;
    }
  });
  Object.defineProperty(exports, 'gt', {
    enumerable: true,
    get: function () {
      return _gt.gt;
    }
  });
});
;define('dmx-frontend/helpers/gte', ['exports', 'ember-truth-helpers/helpers/gte'], function (exports, _gte) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _gte.default;
    }
  });
  Object.defineProperty(exports, 'gte', {
    enumerable: true,
    get: function () {
      return _gte.gte;
    }
  });
});
;define('dmx-frontend/helpers/is-array', ['exports', 'ember-truth-helpers/helpers/is-array'], function (exports, _isArray) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _isArray.default;
    }
  });
  Object.defineProperty(exports, 'isArray', {
    enumerable: true,
    get: function () {
      return _isArray.isArray;
    }
  });
});
;define('dmx-frontend/helpers/is-equal', ['exports', 'ember-truth-helpers/helpers/is-equal'], function (exports, _isEqual) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _isEqual.default;
    }
  });
  Object.defineProperty(exports, 'isEqual', {
    enumerable: true,
    get: function () {
      return _isEqual.isEqual;
    }
  });
});
;define('dmx-frontend/helpers/local-class', ['exports', 'ember-css-modules/helpers/local-class'], function (exports, _localClass) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _localClass.default;
    }
  });
  Object.defineProperty(exports, 'localClass', {
    enumerable: true,
    get: function () {
      return _localClass.localClass;
    }
  });
});
;define('dmx-frontend/helpers/lt', ['exports', 'ember-truth-helpers/helpers/lt'], function (exports, _lt) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _lt.default;
    }
  });
  Object.defineProperty(exports, 'lt', {
    enumerable: true,
    get: function () {
      return _lt.lt;
    }
  });
});
;define('dmx-frontend/helpers/lte', ['exports', 'ember-truth-helpers/helpers/lte'], function (exports, _lte) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _lte.default;
    }
  });
  Object.defineProperty(exports, 'lte', {
    enumerable: true,
    get: function () {
      return _lte.lte;
    }
  });
});
;define('dmx-frontend/helpers/not-eq', ['exports', 'ember-truth-helpers/helpers/not-equal'], function (exports, _notEqual) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _notEqual.default;
    }
  });
  Object.defineProperty(exports, 'notEq', {
    enumerable: true,
    get: function () {
      return _notEqual.notEq;
    }
  });
});
;define('dmx-frontend/helpers/not', ['exports', 'ember-truth-helpers/helpers/not'], function (exports, _not) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _not.default;
    }
  });
  Object.defineProperty(exports, 'not', {
    enumerable: true,
    get: function () {
      return _not.not;
    }
  });
});
;define('dmx-frontend/helpers/or', ['exports', 'ember-truth-helpers/helpers/or'], function (exports, _or) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _or.default;
    }
  });
  Object.defineProperty(exports, 'or', {
    enumerable: true,
    get: function () {
      return _or.or;
    }
  });
});
;define('dmx-frontend/helpers/perform', ['exports', 'ember-concurrency/helpers/perform'], function (exports, _perform) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _perform.default;
    }
  });
  Object.defineProperty(exports, 'perform', {
    enumerable: true,
    get: function () {
      return _perform.perform;
    }
  });
});
;define('dmx-frontend/helpers/pluralize', ['exports', 'ember-inflector/lib/helpers/pluralize'], function (exports, _pluralize) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _pluralize.default;
});
;define('dmx-frontend/helpers/singularize', ['exports', 'ember-inflector/lib/helpers/singularize'], function (exports, _singularize) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _singularize.default;
});
;define('dmx-frontend/helpers/task', ['exports', 'ember-concurrency/helpers/task'], function (exports, _task) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _task.default;
    }
  });
  Object.defineProperty(exports, 'task', {
    enumerable: true,
    get: function () {
      return _task.task;
    }
  });
});
;define('dmx-frontend/helpers/xor', ['exports', 'ember-truth-helpers/helpers/xor'], function (exports, _xor) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _xor.default;
    }
  });
  Object.defineProperty(exports, 'xor', {
    enumerable: true,
    get: function () {
      return _xor.xor;
    }
  });
});
;define('dmx-frontend/initializers/app-version', ['exports', 'ember-cli-app-version/initializer-factory', 'dmx-frontend/config/environment'], function (exports, _initializerFactory, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  let name, version;
  if (_environment.default.APP) {
    name = _environment.default.APP.name;
    version = _environment.default.APP.version;
  }

  exports.default = {
    name: 'App Version',
    initialize: (0, _initializerFactory.default)(name, version)
  };
});
;define('dmx-frontend/initializers/container-debug-adapter', ['exports', 'ember-resolver/resolvers/classic/container-debug-adapter'], function (exports, _containerDebugAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: 'container-debug-adapter',

    initialize() {
      let app = arguments[1] || arguments[0];

      app.register('container-debug-adapter:main', _containerDebugAdapter.default);
      app.inject('container-debug-adapter:main', 'namespace', 'application:main');
    }
  };
});
;define('dmx-frontend/initializers/ember-cli-mirage', ['exports', 'dmx-frontend/config/environment', 'dmx-frontend/mirage/config', 'ember-cli-mirage/get-rfc232-test-context', 'ember-cli-mirage/start-mirage'], function (exports, _environment, _config, _getRfc232TestContext, _startMirage) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.startMirage = startMirage;
  exports.default = {
    name: 'ember-cli-mirage',
    initialize(application) {
      if (_config.default) {
        application.register('mirage:base-config', _config.default, { instantiate: false });
      }
      if (_config.testConfig) {
        application.register('mirage:test-config', _config.testConfig, { instantiate: false });
      }

      _environment.default['ember-cli-mirage'] = _environment.default['ember-cli-mirage'] || {};
      if (_shouldUseMirage(_environment.default.environment, _environment.default['ember-cli-mirage'])) {
        startMirage(_environment.default);
      }
    }
  };
  function startMirage(env = _environment.default) {
    return (0, _startMirage.default)(null, { env, baseConfig: _config.default, testConfig: _config.testConfig });
  }

  function _shouldUseMirage(env, addonConfig) {
    if (typeof FastBoot !== 'undefined') {
      return false;
    }
    if ((0, _getRfc232TestContext.default)()) {
      return false;
    }
    let userDeclaredEnabled = typeof addonConfig.enabled !== 'undefined';
    let defaultEnabled = _defaultEnabled(env, addonConfig);

    return userDeclaredEnabled ? addonConfig.enabled : defaultEnabled;
  }

  /*
    Returns a boolean specifying the default behavior for whether
    to initialize Mirage.
  */
  function _defaultEnabled(env, addonConfig) {
    let usingInDev = env === 'development' && !addonConfig.usingProxy;
    let usingInTest = env === 'test';

    return usingInDev || usingInTest;
  }
});
;define('dmx-frontend/initializers/ember-concurrency', ['exports', 'ember-concurrency/initializers/ember-concurrency'], function (exports, _emberConcurrency) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _emberConcurrency.default;
    }
  });
  Object.defineProperty(exports, 'initialize', {
    enumerable: true,
    get: function () {
      return _emberConcurrency.initialize;
    }
  });
});
;define('dmx-frontend/initializers/ember-data', ['exports', 'ember-data/setup-container', 'ember-data'], function (exports, _setupContainer) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: 'ember-data',
    initialize: _setupContainer.default
  };
});
;define('dmx-frontend/initializers/export-application-global', ['exports', 'dmx-frontend/config/environment'], function (exports, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.initialize = initialize;
  function initialize() {
    var application = arguments[1] || arguments[0];
    if (_environment.default.exportApplicationGlobal !== false) {
      var theGlobal;
      if (typeof window !== 'undefined') {
        theGlobal = window;
      } else if (typeof global !== 'undefined') {
        theGlobal = global;
      } else if (typeof self !== 'undefined') {
        theGlobal = self;
      } else {
        // no reasonable global, just bail
        return;
      }

      var value = _environment.default.exportApplicationGlobal;
      var globalName;

      if (typeof value === 'string') {
        globalName = value;
      } else {
        globalName = Ember.String.classify(_environment.default.modulePrefix);
      }

      if (!theGlobal[globalName]) {
        theGlobal[globalName] = application;

        application.reopen({
          willDestroy: function () {
            this._super.apply(this, arguments);
            delete theGlobal[globalName];
          }
        });
      }
    }
  }

  exports.default = {
    name: 'export-application-global',

    initialize: initialize
  };
});
;define('dmx-frontend/instance-initializers/ember-cli-mirage-autostart', ['exports', 'ember-cli-mirage/instance-initializers/ember-cli-mirage-autostart'], function (exports, _emberCliMirageAutostart) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _emberCliMirageAutostart.default;
    }
  });
});
;define("dmx-frontend/instance-initializers/ember-data", ["exports", "ember-data/initialize-store-service"], function (exports, _initializeStoreService) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    name: "ember-data",
    initialize: _initializeStoreService.default
  };
});
;define('dmx-frontend/light-fixtures/controller', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Controller.extend({
    lightFixtures: Ember.computed.alias('model'),
    queryParams: ['selectedIds'],
    selectedIds: [],
    actions: {
      select(selected) {
        Ember.set(this, 'selectedIds', selected);
      }
    }
  });
});
;define('dmx-frontend/light-fixtures/route', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Route.extend({
    state: Ember.inject.service(),
    async model() {
      await this.store.findAll('preset');
      await this.store.findAll('preset-channel');
      return this.store.findAll('light-fixture');
    },
    afterModel() {
      Ember.get(this, 'state').start();
    }
  });
});
;define("dmx-frontend/light-fixtures/styles", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {};
});
;define("dmx-frontend/light-fixtures/template", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.HTMLBars.template({ "id": "z/itrsrp", "block": "{\"symbols\":[],\"statements\":[[1,[26,\"c-base-map\",null,[[\"lightFixtures\",\"selectedIds\",\"select\"],[[22,[\"lightFixtures\"]],[22,[\"selectedIds\"]],[26,\"action\",[[21,0,[]],\"select\"],null]]]],false]],\"hasEval\":false}", "meta": { "moduleName": "dmx-frontend/light-fixtures/template.hbs" } });
});
;define("dmx-frontend/mirage/config", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });

  exports.default = function () {

    // These comments are here to help you get started. Feel free to delete them.

    /*
      Config (with defaults).
       Note: these only affect routes defined *after* them!
    */

    // this.urlPrefix = '';    // make this `http://localhost:8080`, for example, if your API is on a different server
    // this.namespace = '';    // make this `/api`, for example, if your API is namespaced
    // this.timing = 400;      // delay for each request, automatically set to 0 during testing

    /*
      Shorthand cheatsheet:
       this.get('/posts');
      this.post('/posts');
      this.get('/posts/:id');
      this.put('/posts/:id'); // or this.patch
      this.del('/posts/:id');
       http://www.ember-cli-mirage.com/docs/v0.3.x/shorthands/
    */

    // this.get('/light-infos');
    // this.get('/light-status/:id');

    // this.patch('/light-status/:id');

    this.passthrough();
  };
});
;define('dmx-frontend/mirage/factories/light-info', ['exports', 'ember-cli-mirage'], function (exports, _emberCliMirage) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberCliMirage.Factory.extend({
    posX: () => _emberCliMirage.faker.random.number({ min: 0, max: 800 }),
    posY: () => _emberCliMirage.faker.random.number({ min: 0, max: 569 })
  });
});
;define('dmx-frontend/mirage/factories/light-status', ['exports', 'ember-cli-mirage'], function (exports, _emberCliMirage) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberCliMirage.Factory.extend({
    rgbColor: () => _emberCliMirage.faker.internet.color()
  });
});
;define('dmx-frontend/mirage/models/light-info', ['exports', 'ember-cli-mirage'], function (exports, _emberCliMirage) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberCliMirage.Model.extend({
    status: (0, _emberCliMirage.belongsTo)('light-status')
  });
});
;define('dmx-frontend/mirage/models/light-status', ['exports', 'ember-cli-mirage'], function (exports, _emberCliMirage) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberCliMirage.Model.extend({
    info: (0, _emberCliMirage.belongsTo)('light-info')
  });
});
;define('dmx-frontend/mirage/scenarios/default', ['exports', 'ember-cli-mirage'], function (exports, _emberCliMirage) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });

  exports.default = function (server) {

    _emberCliMirage.faker.seed(3434);

    /*
      Seed your development database using your factories.
      This data will not be loaded in your tests.
       Make sure to define a factory for each model you want to create.
    */

    server.createList('light-info', 10).forEach(info => {
      server.create('light-status', { info });
    });
  };
});
;define('dmx-frontend/mirage/serializers/application', ['exports', 'ember-cli-mirage'], function (exports, _emberCliMirage) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberCliMirage.JSONAPISerializer.extend({});
});
;define('dmx-frontend/models/color', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberData.default.Model.extend({});
});
;define('dmx-frontend/models/light-channel', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  const { attr, belongsTo } = _emberData.default;

  exports.default = _emberData.default.Model.extend({
    name: attr('string'),
    offset: attr('number'),
    element: belongsTo('light-element'),

    value: attr('number')
  });
});
;define('dmx-frontend/models/light-element', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  const { attr, belongsTo, hasMany } = _emberData.default;

  exports.default = _emberData.default.Model.extend({
    name: attr('string'),
    channels: hasMany('light-channel'),
    fixture: belongsTo('light-fixture'),

    // isRGB: Ember.computed('channels.@each.name', {
    //   get() {
    //     let channels = get(this, 'channels').map(c => get(c, 'name'));
    //     return Ember.compare(channels.sort(), ['b', 'g', 'r']) === 0;
    //   }
    // }),
    simpleColor: Ember.computed('channels.@each.{name,value}', {
      get() {
        const channels = Ember.get(this, 'channels');

        const r = channels.findBy('name', 'r');
        const b = channels.findBy('name', 'b');
        const g = channels.findBy('name', 'g');

        if (Ember.get(channels, 'length') === 3 && r && g && b) {
          return '#' + [r, g, b].map(c => Ember.get(c, 'value') || 0).map(c => c.toString(16)).map(c => c.padStart(2, '0')).join('');
        }

        return `repeating-linear-gradient(
        45deg,
        white,
        white 5px,
        #aaa 5px,
        #aaa 10px
      )`;
      }
    })
  });
});
;define('dmx-frontend/models/light-fixture', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  const { attr, hasMany } = _emberData.default;

  exports.default = _emberData.default.Model.extend({
    posX: attr('number'),
    posY: attr('number'),
    name: attr('string'),
    elements: hasMany('light-elements')

    // simpleColor: Ember.computed('elements.@each.simpleColor', {
    //   get() {
    //     const elements = get(this, 'elements').map(e => get(e, 'simpleColor'));
    //     if(elements.length > 0 && elements.every(e => e === elements[0])) {
    //       return elements[0]
    //     }

    //     return `repeating-linear-gradient(
    //       45deg,
    //       ${elements.map(e => `${e} 1px`).join(',')}
    //     )`;
    //   }
    // }),
  });
});
;define('dmx-frontend/models/light-presets', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberData.default.Model.extend({});
});
;define('dmx-frontend/models/light-status', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  const { attr, belongsTo } = _emberData.default;

  exports.default = _emberData.default.Model.extend({
    rgbColor: attr('string'),
    info: belongsTo('light-fixture')
  });
});
;define('dmx-frontend/models/preset-channel', ['exports', 'ember-data', 'ember-data/attr', 'ember-data/relationships'], function (exports, _emberData, _attr, _relationships) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberData.default.Model.extend({
    name: (0, _attr.default)('string'),
    value: (0, _attr.default)('number'),

    preset: (0, _relationships.belongsTo)('preset')
  });
});
;define('dmx-frontend/models/preset', ['exports', 'ember-data', 'ember-data/relationships'], function (exports, _emberData, _relationships) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberData.default.Model.extend({
    channels: (0, _relationships.hasMany)('preset-channel')
  });
});
;define('dmx-frontend/resolver', ['exports', 'ember-resolver'], function (exports, _emberResolver) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberResolver.default;
});
;define('dmx-frontend/router', ['exports', 'dmx-frontend/config/environment'], function (exports, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  const Router = Ember.Router.extend({
    location: _environment.default.locationType,
    rootURL: _environment.default.rootURL
  });

  Router.map(function () {
    this.route('light-fixtures', { path: '/' });
  });

  exports.default = Router;
});
;define('dmx-frontend/serializers/application', ['exports', 'ember-data'], function (exports, _emberData) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberData.default.JSONAPISerializer.extend({
    normalize(typeClass, hash, parentId) {
      const type = typeClass.modelName;
      const id = this.extractId(typeClass, hash, parentId);

      const { relationships, included } = this.extractRelationships(typeClass, hash, id);

      return {
        data: { type, id },
        included: [{
          type,
          id,
          relationships,
          attributes: this.extractAttributes(typeClass, hash)
        }, ...included]
      };
    },

    normalizeArrayResponse(store, primaryModelClass, payload) {
      const dataArr = [];
      const includedArr = [];
      payload.forEach(element => {
        const { data, included } = this.normalize(primaryModelClass, element);
        dataArr.push(data);
        included.forEach(i => includedArr.push(i));
      });

      return { data: dataArr, included: includedArr };
    },
    extractRelationships(modelClass, resourceHash, elementId) {
      const relationships = {};
      const included = [];

      modelClass.eachRelationship((key, relationshipMeta) => {
        if (relationshipMeta.kind === 'hasMany') {
          const relationshipKey = this.keyForRelationship(key, relationshipMeta.kind, 'deserialize');
          const relationshipData = [];
          resourceHash[relationshipKey].forEach(item => {

            const relationshipModelClass = this.store.modelFor(relationshipMeta.type);

            const normalized = this.normalize(relationshipModelClass, item, elementId);

            relationshipData.push(normalized.data);
            normalized.included.forEach(i => included.push(i));
          });
          relationships[relationshipKey] = { data: relationshipData };
        }
      });

      return { relationships, included };
    },
    extractAttributes(modelClass, resourceHash) {
      return this._super(modelClass, { attributes: resourceHash });
    },
    keyForAttribute(attr) {
      return Ember.String.underscore(attr);
    },
    extractId(typeClass, hash, parentId) {
      let idKey = Object.keys(hash).find(key => key.endsWith('_id'));
      if (idKey) {
        return hash[idKey];
      }

      if (hash.name) {
        return `${parentId}/'#/${hash.name}`;
      }

      return Ember.guidFor(hash);
    }
  });
});
;define('dmx-frontend/serializers/color', ['exports', 'ember-localstorage-adapter'], function (exports, _emberLocalstorageAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberLocalstorageAdapter.LSSerializer.extend({});
});
;define('dmx-frontend/serializers/light-channel', ['exports', 'dmx-frontend/serializers/application'], function (exports, _application) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _application.default.extend({
    // pushPayload (store, payload) {


    //   const primaryModelClass = store.modelFor('light-channel');
    //   const p = this.normalizeArrayResponse(store, primaryModelClass, payload);
    //   console.log(JSON.stringify(p));
    //   return p;
    // }
  });
});
;define('dmx-frontend/serializers/light-fixture', ['exports', 'dmx-frontend/serializers/application'], function (exports, _application) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _application.default.extend({});
});
;define('dmx-frontend/serializers/ls-serializer', ['exports', 'ember-localstorage-adapter/serializers/ls-serializer'], function (exports, _lsSerializer) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _lsSerializer.default;
});
;define('dmx-frontend/serializers/preset-channel', ['exports', 'ember-localstorage-adapter'], function (exports, _emberLocalstorageAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberLocalstorageAdapter.LSSerializer.extend({});
});
;define('dmx-frontend/serializers/preset', ['exports', 'ember-localstorage-adapter'], function (exports, _emberLocalstorageAdapter) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = _emberLocalstorageAdapter.LSSerializer.extend({});
});
;define('dmx-frontend/services/ajax', ['exports', 'ember-ajax/services/ajax'], function (exports, _ajax) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  Object.defineProperty(exports, 'default', {
    enumerable: true,
    get: function () {
      return _ajax.default;
    }
  });
});
;define('dmx-frontend/services/magic', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Service.extend({
    active: false
  });
});
;define('dmx-frontend/services/state', ['exports', 'ember-concurrency'], function (exports, _emberConcurrency) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = Ember.Service.extend({
    store: Ember.inject.service(),
    start() {
      Ember.run.later(() => Ember.get(this, 'initWebSocketConn').perform());
    },

    toSave: [],

    save(snapshot) {
      Ember.get(this, 'toSave').pushObject(snapshot);

      Ember.get(this, 'flushSave').perform();
    },

    flushSave: (0, _emberConcurrency.task)(function* () {
      yield (0, _emberConcurrency.timeout)(1); // debounce flush

      let socket = Ember.get(this, 'socket');

      while (!socket) {
        yield (0, _emberConcurrency.timeout)(1000);
        socket = Ember.get(this, 'socket');
      }

      let toSave = Ember.get(this, 'toSave');
      Ember.set(this, 'toSave', []);

      try {
        if (Ember.get(toSave, 'length')) {
          let data = toSave.map(snapshot => ({
            'channel_id': snapshot.id,
            value: snapshot.attr('value')
          }));

          console.log('flush', data);
          socket.send(JSON.stringify(data));

          toSave = [];
        }
      } catch (e) {
        console.log('error during flush');
      } finally {
        Ember.set(this, 'toSave', [...Ember.get(this, 'toSave'), ...toSave]);
      }
    }).restartable(),

    initWebSocketConn: (0, _emberConcurrency.task)(function* (ms = 0) {
      yield (0, _emberConcurrency.timeout)(ms);

      const socket = new WebSocket(`ws://${window.location.host}/api/v1/websocket_state/`);
      socket.onopen = (...args) => this.onopen(...args);
      socket.onclose = (...args) => this.onclose(...args);
      socket.onmessage = (...args) => this.onmessage(...args);

      Ember.set(this, 'socket', socket);
    }).drop(),

    onclose() {
      console.log('lost socket');
      Ember.set(this, 'socket', null);
      // reopen
      Ember.run.later(() => Ember.get(this, 'initWebSocketConn').perform(1000));
    },

    onmessage(message) {
      const payload = JSON.parse(message.data);

      const store = Ember.get(this, 'store');

      const typeClass = store.modelFor('light-channel');
      const serializer = store.serializerFor('light-channel');
      const normalized = serializer.normalizeArrayResponse(store, typeClass, payload);

      store.push(normalized);
    },
    onopen() {}
  });
});
;define("dmx-frontend/styles/app", ["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {};
});
;define('dmx-frontend/tests/mirage/mirage.lint-test', [], function () {
  'use strict';

  QUnit.module('ESLint | mirage');

  QUnit.test('mirage/config.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'mirage/config.js should pass ESLint\n\n');
  });

  QUnit.test('mirage/factories/light-info.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'mirage/factories/light-info.js should pass ESLint\n\n');
  });

  QUnit.test('mirage/factories/light-status.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'mirage/factories/light-status.js should pass ESLint\n\n');
  });

  QUnit.test('mirage/models/light-info.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'mirage/models/light-info.js should pass ESLint\n\n');
  });

  QUnit.test('mirage/models/light-status.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'mirage/models/light-status.js should pass ESLint\n\n');
  });

  QUnit.test('mirage/scenarios/default.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'mirage/scenarios/default.js should pass ESLint\n\n');
  });

  QUnit.test('mirage/serializers/application.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'mirage/serializers/application.js should pass ESLint\n\n');
  });
});
;

;define('dmx-frontend/config/environment', [], function() {
  var prefix = 'dmx-frontend';
try {
  var metaName = prefix + '/config/environment';
  var rawConfig = document.querySelector('meta[name="' + metaName + '"]').getAttribute('content');
  var config = JSON.parse(unescape(rawConfig));

  var exports = { 'default': config };

  Object.defineProperty(exports, '__esModule', { value: true });

  return exports;
}
catch(err) {
  throw new Error('Could not read config from meta tag with name "' + metaName + '".');
}

});

;
          if (!runningTests) {
            require("dmx-frontend/app")["default"].create({"name":"dmx-frontend","version":"0.0.0+4bb4e0e5"});
          }
        
//# sourceMappingURL=dmx-frontend.map
