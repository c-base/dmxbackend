'use strict';

define('dmx-frontend/tests/app.lint-test', [], function () {
  'use strict';

  QUnit.module('ESLint | app');

  QUnit.test('adapters/application.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/application.js should pass ESLint\n\n');
  });

  QUnit.test('adapters/color.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/color.js should pass ESLint\n\n');
  });

  QUnit.test('adapters/light-channel.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/light-channel.js should pass ESLint\n\n');
  });

  QUnit.test('adapters/light-fixture.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/light-fixture.js should pass ESLint\n\n');
  });

  QUnit.test('adapters/preset-channel.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/preset-channel.js should pass ESLint\n\n');
  });

  QUnit.test('adapters/preset.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/preset.js should pass ESLint\n\n');
  });

  QUnit.test('app.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'app.js should pass ESLint\n\n');
  });

  QUnit.test('components/c-base-map-light-element/component.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/c-base-map-light-element/component.js should pass ESLint\n\n');
  });

  QUnit.test('components/c-base-map-light/component.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'components/c-base-map-light/component.js should pass ESLint\n\n8:3 - Only string, number, symbol, boolean, null, undefined, and function are allowed as default properties (ember/avoid-leaking-state-in-ember-objects)\n10:10 - Use brace expansion (ember/use-brace-expansion)');
  });

  QUnit.test('components/c-base-map-multi-light-element/component.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/c-base-map-multi-light-element/component.js should pass ESLint\n\n');
  });

  QUnit.test('components/c-base-map/component.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'components/c-base-map/component.js should pass ESLint\n\n1:10 - \'all\' is defined but never used. (no-unused-vars)\n3:10 - \'set\' is defined but never used. (no-unused-vars)\n4:10 - \'task\' is defined but never used. (no-unused-vars)');
  });

  QUnit.test('components/color-picker/component.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'components/color-picker/component.js should pass ESLint\n\n3:10 - \'set\' is defined but never used. (no-unused-vars)');
  });

  QUnit.test('components/magic-pi/component.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/magic-pi/component.js should pass ESLint\n\n');
  });

  QUnit.test('helpers/build-css.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'helpers/build-css.js should pass ESLint\n\n5:31 - Unnecessary escape character: \\d. (no-useless-escape)');
  });

  QUnit.test('light-fixtures/controller.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'light-fixtures/controller.js should pass ESLint\n\n8:3 - Only string, number, symbol, boolean, null, undefined, and function are allowed as default properties (ember/avoid-leaking-state-in-ember-objects)');
  });

  QUnit.test('light-fixtures/route.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'light-fixtures/route.js should pass ESLint\n\n');
  });

  QUnit.test('models/color.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/color.js should pass ESLint\n\n');
  });

  QUnit.test('models/light-channel.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/light-channel.js should pass ESLint\n\n');
  });

  QUnit.test('models/light-element.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/light-element.js should pass ESLint\n\n');
  });

  QUnit.test('models/light-fixture.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'models/light-fixture.js should pass ESLint\n\n1:10 - \'get\' is defined but never used. (no-unused-vars)');
  });

  QUnit.test('models/light-presets.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/light-presets.js should pass ESLint\n\n');
  });

  QUnit.test('models/light-status.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/light-status.js should pass ESLint\n\n');
  });

  QUnit.test('models/preset-channel.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/preset-channel.js should pass ESLint\n\n');
  });

  QUnit.test('models/preset.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/preset.js should pass ESLint\n\n');
  });

  QUnit.test('resolver.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'resolver.js should pass ESLint\n\n');
  });

  QUnit.test('router.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'router.js should pass ESLint\n\n');
  });

  QUnit.test('serializers/application.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'serializers/application.js should pass ESLint\n\n');
  });

  QUnit.test('serializers/color.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'serializers/color.js should pass ESLint\n\n');
  });

  QUnit.test('serializers/light-channel.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'serializers/light-channel.js should pass ESLint\n\n');
  });

  QUnit.test('serializers/light-fixture.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'serializers/light-fixture.js should pass ESLint\n\n');
  });

  QUnit.test('serializers/preset-channel.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'serializers/preset-channel.js should pass ESLint\n\n');
  });

  QUnit.test('serializers/preset.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'serializers/preset.js should pass ESLint\n\n');
  });

  QUnit.test('services/magic.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'services/magic.js should pass ESLint\n\n');
  });

  QUnit.test('services/state.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'services/state.js should pass ESLint\n\n12:3 - Only string, number, symbol, boolean, null, undefined, and function are allowed as default properties (ember/avoid-leaking-state-in-ember-objects)\n40:9 - Unexpected console statement. (no-console)\n46:7 - Unexpected console statement. (no-console)\n64:5 - Unexpected console statement. (no-console)');
  });
});
define('dmx-frontend/tests/integration/components/c-base-map-light-element/component-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForComponent)('c-base-map-light-element', 'Integration | Component | c base map light element', {
    integration: true
  });

  (0, _emberQunit.test)('it renders', function (assert) {

    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.on('myAction', function(val) { ... });

    this.render(Ember.HTMLBars.template({
      "id": "lrk9ecjI",
      "block": "{\"symbols\":[],\"statements\":[[1,[20,\"c-base-map-light-element\"],false]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), '');

    // Template block usage:
    this.render(Ember.HTMLBars.template({
      "id": "AEL3N982",
      "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"c-base-map-light-element\",null,null,{\"statements\":[[0,\"      template block text\\n\"]],\"parameters\":[]},null],[0,\"  \"]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), 'template block text');
  });
});
define('dmx-frontend/tests/integration/components/c-base-map-light/component-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForComponent)('c-base-map-light', 'Integration | Component | c base map light', {
    integration: true
  });

  (0, _emberQunit.test)('it renders', function (assert) {

    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.on('myAction', function(val) { ... });

    this.render(Ember.HTMLBars.template({
      "id": "tYte8K/M",
      "block": "{\"symbols\":[],\"statements\":[[1,[20,\"c-base-map-light\"],false]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), '');

    // Template block usage:
    this.render(Ember.HTMLBars.template({
      "id": "Zg1+vXKQ",
      "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"c-base-map-light\",null,null,{\"statements\":[[0,\"      template block text\\n\"]],\"parameters\":[]},null],[0,\"  \"]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), 'template block text');
  });
});
define('dmx-frontend/tests/integration/components/c-base-map-multi-light-element/component-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForComponent)('c-base-map-multi-light-element', 'Integration | Component | c base map multi light element', {
    integration: true
  });

  (0, _emberQunit.test)('it renders', function (assert) {

    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.on('myAction', function(val) { ... });

    this.render(Ember.HTMLBars.template({
      "id": "UDi0m+dR",
      "block": "{\"symbols\":[],\"statements\":[[1,[20,\"c-base-map-multi-light-element\"],false]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), '');

    // Template block usage:
    this.render(Ember.HTMLBars.template({
      "id": "8TGpRDU3",
      "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"c-base-map-multi-light-element\",null,null,{\"statements\":[[0,\"      template block text\\n\"]],\"parameters\":[]},null],[0,\"  \"]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), 'template block text');
  });
});
define('dmx-frontend/tests/integration/components/c-base-map/component-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForComponent)('c-base-map', 'Integration | Component | c base map', {
    integration: true
  });

  (0, _emberQunit.test)('it renders', function (assert) {

    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.on('myAction', function(val) { ... });

    this.render(Ember.HTMLBars.template({
      "id": "BzY68JUq",
      "block": "{\"symbols\":[],\"statements\":[[1,[20,\"c-base-map\"],false]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), '');

    // Template block usage:
    this.render(Ember.HTMLBars.template({
      "id": "lZaffw9d",
      "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"c-base-map\",null,null,{\"statements\":[[0,\"      template block text\\n\"]],\"parameters\":[]},null],[0,\"  \"]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), 'template block text');
  });
});
define('dmx-frontend/tests/integration/components/color-picker/component-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForComponent)('color-picker', 'Integration | Component | color picker', {
    integration: true
  });

  (0, _emberQunit.test)('it renders', function (assert) {

    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.on('myAction', function(val) { ... });

    this.render(Ember.HTMLBars.template({
      "id": "UBQ9gJuc",
      "block": "{\"symbols\":[],\"statements\":[[1,[20,\"color-picker\"],false]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), '');

    // Template block usage:
    this.render(Ember.HTMLBars.template({
      "id": "C98HLpzu",
      "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"color-picker\",null,null,{\"statements\":[[0,\"      template block text\\n\"]],\"parameters\":[]},null],[0,\"  \"]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), 'template block text');
  });
});
define('dmx-frontend/tests/integration/components/magic-pi/component-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForComponent)('magic-pi', 'Integration | Component | magic pi', {
    integration: true
  });

  (0, _emberQunit.test)('it renders', function (assert) {

    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.on('myAction', function(val) { ... });

    this.render(Ember.HTMLBars.template({
      "id": "iRZA6l2P",
      "block": "{\"symbols\":[],\"statements\":[[1,[20,\"magic-pi\"],false]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), '');

    // Template block usage:
    this.render(Ember.HTMLBars.template({
      "id": "IG+u9hy8",
      "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"magic-pi\",null,null,{\"statements\":[[0,\"      template block text\\n\"]],\"parameters\":[]},null],[0,\"  \"]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), 'template block text');
  });
});
define('dmx-frontend/tests/test-helper', ['dmx-frontend/app', 'dmx-frontend/config/environment', '@ember/test-helpers', 'ember-qunit'], function (_app, _environment, _testHelpers, _emberQunit) {
  'use strict';

  (0, _testHelpers.setApplication)(_app.default.create(_environment.default.APP));

  (0, _emberQunit.start)();
});
define('dmx-frontend/tests/tests.lint-test', [], function () {
  'use strict';

  QUnit.module('ESLint | tests');

  QUnit.test('integration/components/c-base-map-light-element/component-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/c-base-map-light-element/component-test.js should pass ESLint\n\n');
  });

  QUnit.test('integration/components/c-base-map-light/component-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/c-base-map-light/component-test.js should pass ESLint\n\n');
  });

  QUnit.test('integration/components/c-base-map-multi-light-element/component-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/c-base-map-multi-light-element/component-test.js should pass ESLint\n\n');
  });

  QUnit.test('integration/components/c-base-map/component-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/c-base-map/component-test.js should pass ESLint\n\n');
  });

  QUnit.test('integration/components/color-picker/component-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/color-picker/component-test.js should pass ESLint\n\n');
  });

  QUnit.test('integration/components/magic-pi/component-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/magic-pi/component-test.js should pass ESLint\n\n');
  });

  QUnit.test('test-helper.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'test-helper.js should pass ESLint\n\n');
  });

  QUnit.test('unit/adapters/application-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/adapters/application-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/adapters/color-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/adapters/color-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/adapters/light-info-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/adapters/light-info-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/adapters/preset-channel-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/adapters/preset-channel-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/adapters/preset-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/adapters/preset-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/helpers/build-css-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/helpers/build-css-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/light-status/controller-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/light-status/controller-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/light-status/route-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/light-status/route-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/color-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/color-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/light-channel-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/light-channel-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/light-element-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/light-element-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/light-info-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/light-info-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/light-presets-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/light-presets-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/light-status-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/light-status-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/preset-channel-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/preset-channel-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/preset-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/preset-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/serializers/application-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/serializers/application-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/serializers/color-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/serializers/color-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/serializers/light-info-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/serializers/light-info-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/serializers/preset-channel-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/serializers/preset-channel-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/serializers/preset-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/serializers/preset-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/services/magic-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/services/magic-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/services/state-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/services/state-test.js should pass ESLint\n\n');
  });
});
define('dmx-frontend/tests/unit/adapters/application-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('adapter:application', 'Unit | Adapter | application', {
    // Specify the other units that are required for this test.
    // needs: ['serializer:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    let adapter = this.subject();
    assert.ok(adapter);
  });
});
define('dmx-frontend/tests/unit/adapters/color-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('adapter:color', 'Unit | Adapter | color', {
    // Specify the other units that are required for this test.
    // needs: ['serializer:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    let adapter = this.subject();
    assert.ok(adapter);
  });
});
define('dmx-frontend/tests/unit/adapters/light-info-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('adapter:light-info', 'Unit | Adapter | light info', {
    // Specify the other units that are required for this test.
    // needs: ['serializer:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    let adapter = this.subject();
    assert.ok(adapter);
  });
});
define('dmx-frontend/tests/unit/adapters/preset-channel-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Adapter | preset channel', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let adapter = this.owner.lookup('adapter:preset-channel');
      assert.ok(adapter);
    });
  });
});
define('dmx-frontend/tests/unit/adapters/preset-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Adapter | preset', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let adapter = this.owner.lookup('adapter:preset');
      assert.ok(adapter);
    });
  });
});
define('dmx-frontend/tests/unit/helpers/build-css-test', ['dmx-frontend/helpers/build-css', 'qunit'], function (_buildCss, _qunit) {
  'use strict';

  (0, _qunit.module)('Unit | Helper | build css');

  // Replace this with your real tests.
  (0, _qunit.test)('it works', function (assert) {
    let result = (0, _buildCss.buildCss)([42]);
    assert.ok(result);
  });
});
define('dmx-frontend/tests/unit/light-status/controller-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('controller:light-status', 'Unit | Controller | light status', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    let controller = this.subject();
    assert.ok(controller);
  });
});
define('dmx-frontend/tests/unit/light-status/route-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('route:light-status', 'Unit | Route | light status', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    let route = this.subject();
    assert.ok(route);
  });
});
define('dmx-frontend/tests/unit/models/color-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('color', 'Unit | Model | color', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    let model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('dmx-frontend/tests/unit/models/light-channel-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('light-channel', 'Unit | Model | light channel', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    let model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('dmx-frontend/tests/unit/models/light-element-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('light-element', 'Unit | Model | light element', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    let model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('dmx-frontend/tests/unit/models/light-info-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('light-info', 'Unit | Model | light info', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    let model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('dmx-frontend/tests/unit/models/light-presets-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('light-presets', 'Unit | Model | light presets', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    let model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('dmx-frontend/tests/unit/models/light-status-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('light-status', 'Unit | Model | light status', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    let model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('dmx-frontend/tests/unit/models/preset-channel-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | preset channel', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('preset-channel', {});
      assert.ok(model);
    });
  });
});
define('dmx-frontend/tests/unit/models/preset-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | preset', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('preset', {});
      assert.ok(model);
    });
  });
});
define('dmx-frontend/tests/unit/serializers/application-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('application', 'Unit | Serializer | application', {
    // Specify the other units that are required for this test.
    needs: ['serializer:application']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it serializes records', function (assert) {
    let record = this.subject();

    let serializedRecord = record.serialize();

    assert.ok(serializedRecord);
  });
});
define('dmx-frontend/tests/unit/serializers/color-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('color', 'Unit | Serializer | color', {
    // Specify the other units that are required for this test.
    needs: ['serializer:color']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it serializes records', function (assert) {
    let record = this.subject();

    let serializedRecord = record.serialize();

    assert.ok(serializedRecord);
  });
});
define('dmx-frontend/tests/unit/serializers/light-info-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('light-info', 'Unit | Serializer | light info', {
    // Specify the other units that are required for this test.
    needs: ['serializer:light-info']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it serializes records', function (assert) {
    let record = this.subject();

    let serializedRecord = record.serialize();

    assert.ok(serializedRecord);
  });
});
define('dmx-frontend/tests/unit/serializers/preset-channel-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Serializer | preset channel', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let serializer = store.serializerFor('preset-channel');

      assert.ok(serializer);
    });

    (0, _qunit.test)('it serializes records', function (assert) {
      let store = this.owner.lookup('service:store');
      let record = store.createRecord('preset-channel', {});

      let serializedRecord = record.serialize();

      assert.ok(serializedRecord);
    });
  });
});
define('dmx-frontend/tests/unit/serializers/preset-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Serializer | preset', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let serializer = store.serializerFor('preset');

      assert.ok(serializer);
    });

    (0, _qunit.test)('it serializes records', function (assert) {
      let store = this.owner.lookup('service:store');
      let record = store.createRecord('preset', {});

      let serializedRecord = record.serialize();

      assert.ok(serializedRecord);
    });
  });
});
define('dmx-frontend/tests/unit/services/magic-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('service:magic', 'Unit | Service | magic', {
    // Specify the other units that are required for this test.
    // needs: ['service:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    let service = this.subject();
    assert.ok(service);
  });
});
define('dmx-frontend/tests/unit/services/state-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('service:state', 'Unit | Service | state', {
    // Specify the other units that are required for this test.
    // needs: ['service:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    let service = this.subject();
    assert.ok(service);
  });
});
define('dmx-frontend/config/environment', [], function() {
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

require('dmx-frontend/tests/test-helper');
EmberENV.TESTS_FILE_LOADED = true;
//# sourceMappingURL=tests.map
