import{f as Ve,S as Be,i as h,b as y,a as E,A as $e,_ as ze,r as F,c as je,j as He,O as Ue}from"./indexhtml-QdwCrdL8.js";import"./commonjsHelpers-CqkleIqs.js";/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */window.Vaadin||={};window.Vaadin.featureFlags||={};function qe(i){return i.replace(/-[a-z]/gu,e=>e[1].toUpperCase())}const v={};function A(i,e="25.0.3"){if(Object.defineProperty(i,"version",{get(){return e}}),i.experimental){const n=typeof i.experimental=="string"?i.experimental:`${qe(i.is.split("-").slice(1).join("-"))}Component`;if(!window.Vaadin.featureFlags[n]&&!v[n]){v[n]=new Set,v[n].add(i),Object.defineProperty(window.Vaadin.featureFlags,n,{get(){return v[n].size===0},set(s){s&&v[n].size>0&&(v[n].forEach(o=>{customElements.define(o.is,o)}),v[n].clear())}});return}else if(v[n]){v[n].add(i);return}}const t=customElements.get(i.is);if(!t)customElements.define(i.is,i);else{const n=t.version;n&&i.version&&n===i.version?console.warn(`The component ${i.is} has been loaded twice`):console.error(`Tried to define ${i.is} version ${i.version} when version ${t.version} is already in use. Something will probably break.`)}}const We=/\/\*[\*!]\s+vaadin-dev-mode:start([\s\S]*)vaadin-dev-mode:end\s+\*\*\//i,j=window.Vaadin&&window.Vaadin.Flow&&window.Vaadin.Flow.clients;function Ke(){function i(){return!0}return Qt(i)}function Ge(){try{return Ye()?!0:Xe()?j?!Ze():!Ke():!1}catch{return!1}}function Ye(){return localStorage.getItem("vaadin.developmentmode.force")}function Xe(){return["localhost","127.0.0.1"].indexOf(window.location.hostname)>=0}function Ze(){return!!(j&&Object.keys(j).map(e=>j[e]).filter(e=>e.productionMode).length>0)}function Qt(i,e){if(typeof i!="function")return;const t=We.exec(i.toString());if(t)try{i=new Function(t[1])}catch(n){console.log("vaadin-development-mode-detector: uncommentAndRun() failed",n)}return i(e)}window.Vaadin=window.Vaadin||{};const Dt=function(i,e){if(window.Vaadin.developmentMode)return Qt(i,e)};window.Vaadin.developmentMode===void 0&&(window.Vaadin.developmentMode=Ge());function Je(){/*! vaadin-dev-mode:start
  (function () {
'use strict';

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) {
  return typeof obj;
} : function (obj) {
  return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj;
};

var classCallCheck = function (instance, Constructor) {
  if (!(instance instanceof Constructor)) {
    throw new TypeError("Cannot call a class as a function");
  }
};

var createClass = function () {
  function defineProperties(target, props) {
    for (var i = 0; i < props.length; i++) {
      var descriptor = props[i];
      descriptor.enumerable = descriptor.enumerable || false;
      descriptor.configurable = true;
      if ("value" in descriptor) descriptor.writable = true;
      Object.defineProperty(target, descriptor.key, descriptor);
    }
  }

  return function (Constructor, protoProps, staticProps) {
    if (protoProps) defineProperties(Constructor.prototype, protoProps);
    if (staticProps) defineProperties(Constructor, staticProps);
    return Constructor;
  };
}();

var getPolymerVersion = function getPolymerVersion() {
  return window.Polymer && window.Polymer.version;
};

var StatisticsGatherer = function () {
  function StatisticsGatherer(logger) {
    classCallCheck(this, StatisticsGatherer);

    this.now = new Date().getTime();
    this.logger = logger;
  }

  createClass(StatisticsGatherer, [{
    key: 'frameworkVersionDetectors',
    value: function frameworkVersionDetectors() {
      return {
        'Flow': function Flow() {
          if (window.Vaadin && window.Vaadin.Flow && window.Vaadin.Flow.clients) {
            var flowVersions = Object.keys(window.Vaadin.Flow.clients).map(function (key) {
              return window.Vaadin.Flow.clients[key];
            }).filter(function (client) {
              return client.getVersionInfo;
            }).map(function (client) {
              return client.getVersionInfo().flow;
            });
            if (flowVersions.length > 0) {
              return flowVersions[0];
            }
          }
        },
        'Vaadin Framework': function VaadinFramework() {
          if (window.vaadin && window.vaadin.clients) {
            var frameworkVersions = Object.values(window.vaadin.clients).filter(function (client) {
              return client.getVersionInfo;
            }).map(function (client) {
              return client.getVersionInfo().vaadinVersion;
            });
            if (frameworkVersions.length > 0) {
              return frameworkVersions[0];
            }
          }
        },
        'AngularJs': function AngularJs() {
          if (window.angular && window.angular.version && window.angular.version) {
            return window.angular.version.full;
          }
        },
        'Angular': function Angular() {
          if (window.ng) {
            var tags = document.querySelectorAll("[ng-version]");
            if (tags.length > 0) {
              return tags[0].getAttribute("ng-version");
            }
            return "Unknown";
          }
        },
        'Backbone.js': function BackboneJs() {
          if (window.Backbone) {
            return window.Backbone.VERSION;
          }
        },
        'React': function React() {
          var reactSelector = '[data-reactroot], [data-reactid]';
          if (!!document.querySelector(reactSelector)) {
            // React does not publish the version by default
            return "unknown";
          }
        },
        'Ember': function Ember() {
          if (window.Em && window.Em.VERSION) {
            return window.Em.VERSION;
          } else if (window.Ember && window.Ember.VERSION) {
            return window.Ember.VERSION;
          }
        },
        'jQuery': function (_jQuery) {
          function jQuery() {
            return _jQuery.apply(this, arguments);
          }

          jQuery.toString = function () {
            return _jQuery.toString();
          };

          return jQuery;
        }(function () {
          if (typeof jQuery === 'function' && jQuery.prototype.jquery !== undefined) {
            return jQuery.prototype.jquery;
          }
        }),
        'Polymer': function Polymer() {
          var version = getPolymerVersion();
          if (version) {
            return version;
          }
        },
        'LitElement': function LitElement() {
          var version = window.litElementVersions && window.litElementVersions[0];
          if (version) {
            return version;
          }
        },
        'LitHtml': function LitHtml() {
          var version = window.litHtmlVersions && window.litHtmlVersions[0];
          if (version) {
            return version;
          }
        },
        'Vue.js': function VueJs() {
          if (window.Vue) {
            return window.Vue.version;
          }
        }
      };
    }
  }, {
    key: 'getUsedVaadinElements',
    value: function getUsedVaadinElements(elements) {
      var version = getPolymerVersion();
      var elementClasses = void 0;
      // NOTE: In case you edit the code here, YOU MUST UPDATE any statistics reporting code in Flow.
      // Check all locations calling the method getEntries() in
      // https://github.com/vaadin/flow/blob/master/flow-server/src/main/java/com/vaadin/flow/internal/UsageStatistics.java#L106
      // Currently it is only used by BootstrapHandler.
      if (version && version.indexOf('2') === 0) {
        // Polymer 2: components classes are stored in window.Vaadin
        elementClasses = Object.keys(window.Vaadin).map(function (c) {
          return window.Vaadin[c];
        }).filter(function (c) {
          return c.is;
        });
      } else {
        // Polymer 3: components classes are stored in window.Vaadin.registrations
        elementClasses = window.Vaadin.registrations || [];
      }
      elementClasses.forEach(function (klass) {
        var version = klass.version ? klass.version : "0.0.0";
        elements[klass.is] = { version: version };
      });
    }
  }, {
    key: 'getUsedVaadinThemes',
    value: function getUsedVaadinThemes(themes) {
      ['Lumo', 'Material'].forEach(function (themeName) {
        var theme;
        var version = getPolymerVersion();
        if (version && version.indexOf('2') === 0) {
          // Polymer 2: themes are stored in window.Vaadin
          theme = window.Vaadin[themeName];
        } else {
          // Polymer 3: themes are stored in custom element registry
          theme = customElements.get('vaadin-' + themeName.toLowerCase() + '-styles');
        }
        if (theme && theme.version) {
          themes[themeName] = { version: theme.version };
        }
      });
    }
  }, {
    key: 'getFrameworks',
    value: function getFrameworks(frameworks) {
      var detectors = this.frameworkVersionDetectors();
      Object.keys(detectors).forEach(function (framework) {
        var detector = detectors[framework];
        try {
          var version = detector();
          if (version) {
            frameworks[framework] = { version: version };
          }
        } catch (e) {}
      });
    }
  }, {
    key: 'gather',
    value: function gather(storage) {
      var storedStats = storage.read();
      var gatheredStats = {};
      var types = ["elements", "frameworks", "themes"];

      types.forEach(function (type) {
        gatheredStats[type] = {};
        if (!storedStats[type]) {
          storedStats[type] = {};
        }
      });

      var previousStats = JSON.stringify(storedStats);

      this.getUsedVaadinElements(gatheredStats.elements);
      this.getFrameworks(gatheredStats.frameworks);
      this.getUsedVaadinThemes(gatheredStats.themes);

      var now = this.now;
      types.forEach(function (type) {
        var keys = Object.keys(gatheredStats[type]);
        keys.forEach(function (key) {
          if (!storedStats[type][key] || _typeof(storedStats[type][key]) != _typeof({})) {
            storedStats[type][key] = { firstUsed: now };
          }
          // Discards any previously logged version number
          storedStats[type][key].version = gatheredStats[type][key].version;
          storedStats[type][key].lastUsed = now;
        });
      });

      var newStats = JSON.stringify(storedStats);
      storage.write(newStats);
      if (newStats != previousStats && Object.keys(storedStats).length > 0) {
        this.logger.debug("New stats: " + newStats);
      }
    }
  }]);
  return StatisticsGatherer;
}();

var StatisticsStorage = function () {
  function StatisticsStorage(key) {
    classCallCheck(this, StatisticsStorage);

    this.key = key;
  }

  createClass(StatisticsStorage, [{
    key: 'read',
    value: function read() {
      var localStorageStatsString = localStorage.getItem(this.key);
      try {
        return JSON.parse(localStorageStatsString ? localStorageStatsString : '{}');
      } catch (e) {
        return {};
      }
    }
  }, {
    key: 'write',
    value: function write(data) {
      localStorage.setItem(this.key, data);
    }
  }, {
    key: 'clear',
    value: function clear() {
      localStorage.removeItem(this.key);
    }
  }, {
    key: 'isEmpty',
    value: function isEmpty() {
      var storedStats = this.read();
      var empty = true;
      Object.keys(storedStats).forEach(function (key) {
        if (Object.keys(storedStats[key]).length > 0) {
          empty = false;
        }
      });

      return empty;
    }
  }]);
  return StatisticsStorage;
}();

var StatisticsSender = function () {
  function StatisticsSender(url, logger) {
    classCallCheck(this, StatisticsSender);

    this.url = url;
    this.logger = logger;
  }

  createClass(StatisticsSender, [{
    key: 'send',
    value: function send(data, errorHandler) {
      var logger = this.logger;

      if (navigator.onLine === false) {
        logger.debug("Offline, can't send");
        errorHandler();
        return;
      }
      logger.debug("Sending data to " + this.url);

      var req = new XMLHttpRequest();
      req.withCredentials = true;
      req.addEventListener("load", function () {
        // Stats sent, nothing more to do
        logger.debug("Response: " + req.responseText);
      });
      req.addEventListener("error", function () {
        logger.debug("Send failed");
        errorHandler();
      });
      req.addEventListener("abort", function () {
        logger.debug("Send aborted");
        errorHandler();
      });
      req.open("POST", this.url);
      req.setRequestHeader("Content-Type", "application/json");
      req.send(data);
    }
  }]);
  return StatisticsSender;
}();

var StatisticsLogger = function () {
  function StatisticsLogger(id) {
    classCallCheck(this, StatisticsLogger);

    this.id = id;
  }

  createClass(StatisticsLogger, [{
    key: '_isDebug',
    value: function _isDebug() {
      return localStorage.getItem("vaadin." + this.id + ".debug");
    }
  }, {
    key: 'debug',
    value: function debug(msg) {
      if (this._isDebug()) {
        console.info(this.id + ": " + msg);
      }
    }
  }]);
  return StatisticsLogger;
}();

var UsageStatistics = function () {
  function UsageStatistics() {
    classCallCheck(this, UsageStatistics);

    this.now = new Date();
    this.timeNow = this.now.getTime();
    this.gatherDelay = 10; // Delay between loading this file and gathering stats
    this.initialDelay = 24 * 60 * 60;

    this.logger = new StatisticsLogger("statistics");
    this.storage = new StatisticsStorage("vaadin.statistics.basket");
    this.gatherer = new StatisticsGatherer(this.logger);
    this.sender = new StatisticsSender("https://tools.vaadin.com/usage-stats/submit", this.logger);
  }

  createClass(UsageStatistics, [{
    key: 'maybeGatherAndSend',
    value: function maybeGatherAndSend() {
      var _this = this;

      if (localStorage.getItem(UsageStatistics.optOutKey)) {
        return;
      }
      this.gatherer.gather(this.storage);
      setTimeout(function () {
        _this.maybeSend();
      }, this.gatherDelay * 1000);
    }
  }, {
    key: 'lottery',
    value: function lottery() {
      return true;
    }
  }, {
    key: 'currentMonth',
    value: function currentMonth() {
      return this.now.getYear() * 12 + this.now.getMonth();
    }
  }, {
    key: 'maybeSend',
    value: function maybeSend() {
      var firstUse = Number(localStorage.getItem(UsageStatistics.firstUseKey));
      var monthProcessed = Number(localStorage.getItem(UsageStatistics.monthProcessedKey));

      if (!firstUse) {
        // Use a grace period to avoid interfering with tests, incognito mode etc
        firstUse = this.timeNow;
        localStorage.setItem(UsageStatistics.firstUseKey, firstUse);
      }

      if (this.timeNow < firstUse + this.initialDelay * 1000) {
        this.logger.debug("No statistics will be sent until the initial delay of " + this.initialDelay + "s has passed");
        return;
      }
      if (this.currentMonth() <= monthProcessed) {
        this.logger.debug("This month has already been processed");
        return;
      }
      localStorage.setItem(UsageStatistics.monthProcessedKey, this.currentMonth());
      // Use random sampling
      if (this.lottery()) {
        this.logger.debug("Congratulations, we have a winner!");
      } else {
        this.logger.debug("Sorry, no stats from you this time");
        return;
      }

      this.send();
    }
  }, {
    key: 'send',
    value: function send() {
      // Ensure we have the latest data
      this.gatherer.gather(this.storage);

      // Read, send and clean up
      var data = this.storage.read();
      data["firstUse"] = Number(localStorage.getItem(UsageStatistics.firstUseKey));
      data["usageStatisticsVersion"] = UsageStatistics.version;
      var info = 'This request contains usage statistics gathered from the application running in development mode. \n\nStatistics gathering is automatically disabled and excluded from production builds.\n\nFor details and to opt-out, see https://github.com/vaadin/vaadin-usage-statistics.\n\n\n\n';
      var self = this;
      this.sender.send(info + JSON.stringify(data), function () {
        // Revert the 'month processed' flag
        localStorage.setItem(UsageStatistics.monthProcessedKey, self.currentMonth() - 1);
      });
    }
  }], [{
    key: 'version',
    get: function get$1() {
      return '2.1.2';
    }
  }, {
    key: 'firstUseKey',
    get: function get$1() {
      return 'vaadin.statistics.firstuse';
    }
  }, {
    key: 'monthProcessedKey',
    get: function get$1() {
      return 'vaadin.statistics.monthProcessed';
    }
  }, {
    key: 'optOutKey',
    get: function get$1() {
      return 'vaadin.statistics.optout';
    }
  }]);
  return UsageStatistics;
}();

try {
  window.Vaadin = window.Vaadin || {};
  window.Vaadin.usageStatsChecker = window.Vaadin.usageStatsChecker || new UsageStatistics();
  window.Vaadin.usageStatsChecker.maybeGatherAndSend();
} catch (e) {
  // Intentionally ignored as this is not a problem in the app being developed
}

}());

  vaadin-dev-mode:end **/}const Qe=function(){if(typeof Dt=="function")return Dt(Je)};/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
 */let Pt=0,te=0;const M=[];let ct=!1;function ti(){ct=!1;const i=M.length;for(let e=0;e<i;e++){const t=M[e];if(t)try{t()}catch(n){setTimeout(()=>{throw n})}}M.splice(0,i),te+=i}const ei={after(i){return{run(e){return window.setTimeout(e,i)},cancel(e){window.clearTimeout(e)}}},run(i,e){return window.setTimeout(i,e)},cancel(i){window.clearTimeout(i)}},ii={run(i){return window.requestAnimationFrame(i)},cancel(i){window.cancelAnimationFrame(i)}},ni={run(i){return window.requestIdleCallback?window.requestIdleCallback(i):window.setTimeout(i,16)},cancel(i){window.cancelIdleCallback?window.cancelIdleCallback(i):window.clearTimeout(i)}},ee={run(i){ct||(ct=!0,queueMicrotask(()=>ti())),M.push(i);const e=Pt;return Pt+=1,e},cancel(i){const e=i-te;if(e>=0){if(!M[e])throw new Error(`invalid async handle: ${i}`);M[e]=null}}};/**
@license
Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/const ht=new Set;class C{static debounce(e,t,n){return e instanceof C?e._cancelAsync():e=new C,e.setConfig(t,n),e}constructor(){this._asyncModule=null,this._callback=null,this._timer=null}setConfig(e,t){this._asyncModule=e,this._callback=t,this._timer=this._asyncModule.run(()=>{this._timer=null,ht.delete(this),this._callback()})}cancel(){this.isActive()&&(this._cancelAsync(),ht.delete(this))}_cancelAsync(){this.isActive()&&(this._asyncModule.cancel(this._timer),this._timer=null)}flush(){this.isActive()&&(this.cancel(),this._callback())}isActive(){return this._timer!=null}}function si(i){ht.add(i)}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const _=[];function pt(i,e,t=i.getAttribute("dir")){e?i.setAttribute("dir",e):t!=null&&i.removeAttribute("dir")}function ft(){return document.documentElement.getAttribute("dir")}function oi(){const i=ft();_.forEach(e=>{pt(e,i)})}const ri=new MutationObserver(oi);ri.observe(document.documentElement,{attributes:!0,attributeFilter:["dir"]});const wt=i=>class extends i{static get properties(){return{dir:{type:String,value:"",reflectToAttribute:!0,converter:{fromAttribute:t=>t||"",toAttribute:t=>t===""?null:t}}}}get __isRTL(){return this.getAttribute("dir")==="rtl"}connectedCallback(){super.connectedCallback(),(!this.hasAttribute("dir")||this.__restoreSubscription)&&(this.__subscribe(),pt(this,ft(),null))}attributeChangedCallback(t,n,s){if(super.attributeChangedCallback(t,n,s),t!=="dir")return;const o=ft(),r=s===o&&_.indexOf(this)===-1,a=!s&&n&&_.indexOf(this)===-1;r||a?(this.__subscribe(),pt(this,o,s)):s!==o&&n===o&&this.__unsubscribe()}disconnectedCallback(){super.disconnectedCallback(),this.__restoreSubscription=_.includes(this),this.__unsubscribe()}_valueToNodeAttribute(t,n,s){s==="dir"&&n===""&&!t.hasAttribute("dir")||super._valueToNodeAttribute(t,n,s)}_attributeToProperty(t,n,s){t==="dir"&&!n?this.dir="":super._attributeToProperty(t,n,s)}__subscribe(){_.includes(this)||_.push(this)}__unsubscribe(){_.includes(this)&&_.splice(_.indexOf(this),1)}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */window.Vaadin||(window.Vaadin={});window.Vaadin.registrations||(window.Vaadin.registrations=[]);window.Vaadin.developmentModeCallback||(window.Vaadin.developmentModeCallback={});window.Vaadin.developmentModeCallback["vaadin-usage-statistics"]=function(){Qe()};let J;const Ft=new Set,$=i=>class extends wt(i){static finalize(){super.finalize();const{is:t}=this;if(t&&!Ft.has(t)){window.Vaadin.registrations.push(this),Ft.add(t);const n=window.Vaadin.developmentModeCallback;n&&(J=C.debounce(J,ni,()=>{n["vaadin-usage-statistics"]()}),si(J))}}constructor(){super(),document.doctype===null&&console.warn('Vaadin components require the "standards mode" declaration. Please add <!DOCTYPE html> to the HTML document.')}},ie=new WeakMap;function ai(i,e){let t=e;for(;t;){if(ie.get(t)===i)return!0;t=Object.getPrototypeOf(t)}return!1}function f(i){return e=>{if(ai(i,e))return e;const t=i(e);return ie.set(t,i),t}}/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function li(i,e){return i.split(".").reduce((t,n)=>t?t[n]:void 0,e)}function di(i,e,t){const n=i.split("."),s=n.pop(),o=n.reduce((r,a)=>r[a],t);o[s]=e}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Q={},ui=/([A-Z])/gu;function Rt(i){return Q[i]||(Q[i]=i.replace(ui,"-$1").toLowerCase()),Q[i]}function Vt(i){return i[0].toUpperCase()+i.substring(1)}function tt(i){const[e,t]=i.split("("),n=t.replace(")","").split(",").map(s=>s.trim());return{method:e,observerProps:n}}function et(i,e){return Object.prototype.hasOwnProperty.call(i,e)||(i[e]=new Map(i[e])),i[e]}const ci=i=>{class e extends i{static enabledWarnings=[];static createProperty(n,s){[String,Boolean,Number,Array].includes(s)&&(s={type:s}),s&&s.reflectToAttribute&&(s.reflect=!0),super.createProperty(n,s)}static getOrCreateMap(n){return et(this,n)}static finalize(){if(window.litIssuedWarnings&&(window.litIssuedWarnings.add("no-override-create-property"),window.litIssuedWarnings.add("no-override-get-property-descriptor")),super.finalize(),Array.isArray(this.observers)){const n=this.getOrCreateMap("__complexObservers");this.observers.forEach(s=>{const{method:o,observerProps:r}=tt(s);n.set(o,r)})}}static addCheckedInitializer(n){super.addInitializer(s=>{s instanceof this&&n(s)})}static getPropertyDescriptor(n,s,o){const r=super.getPropertyDescriptor(n,s,o);let a=r;if(this.getOrCreateMap("__propKeys").set(n,s),o.sync&&(a={get:r.get,set(l){const d=this[n];Ve(l,d)&&(this[s]=l,this.requestUpdate(n,d,o),this.hasUpdated&&this.performUpdate())},configurable:!0,enumerable:!0}),o.readOnly){const l=a.set;this.addCheckedInitializer(d=>{d[`_set${Vt(n)}`]=function(c){l.call(d,c)}}),a={get:a.get,set(){},configurable:!0,enumerable:!0}}if("value"in o&&this.addCheckedInitializer(l=>{const d=typeof o.value=="function"?o.value.call(l):o.value;o.readOnly?l[`_set${Vt(n)}`](d):l[n]=d}),o.observer){const l=o.observer;this.getOrCreateMap("__observers").set(n,l),this.addCheckedInitializer(d=>{d[l]||console.warn(`observer method ${l} not defined`)})}if(o.notify){if(!this.__notifyProps)this.__notifyProps=new Set;else if(!this.hasOwnProperty("__notifyProps")){const l=this.__notifyProps;this.__notifyProps=new Set(l)}this.__notifyProps.add(n)}if(o.computed){const l=`__assignComputed${n}`,d=tt(o.computed);this.prototype[l]=function(...c){this[n]=this[d.method](...c)},this.getOrCreateMap("__computedObservers").set(l,d.observerProps)}return o.attribute||(o.attribute=Rt(n)),a}static get polylitConfig(){return{asyncFirstRender:!1}}connectedCallback(){super.connectedCallback();const{polylitConfig:n}=this.constructor;!this.hasUpdated&&!n.asyncFirstRender&&this.performUpdate()}firstUpdated(){super.firstUpdated(),this.$||(this.$={}),this.renderRoot.querySelectorAll("[id]").forEach(n=>{this.$[n.id]=n})}ready(){}willUpdate(n){this.constructor.__computedObservers&&this.__runComplexObservers(n,this.constructor.__computedObservers)}updated(n){const s=this.__isReadyInvoked;this.__isReadyInvoked=!0,this.constructor.__observers&&this.__runObservers(n,this.constructor.__observers),this.constructor.__complexObservers&&this.__runComplexObservers(n,this.constructor.__complexObservers),this.__dynamicPropertyObservers&&this.__runDynamicObservers(n,this.__dynamicPropertyObservers),this.__dynamicMethodObservers&&this.__runComplexObservers(n,this.__dynamicMethodObservers),this.constructor.__notifyProps&&this.__runNotifyProps(n,this.constructor.__notifyProps),s||this.ready()}setProperties(n){Object.entries(n).forEach(([s,o])=>{const r=this.constructor.__propKeys.get(s),a=this[r];this[r]=o,this.requestUpdate(s,a)}),this.hasUpdated&&this.performUpdate()}_createMethodObserver(n){const s=et(this,"__dynamicMethodObservers"),{method:o,observerProps:r}=tt(n);s.set(o,r)}_createPropertyObserver(n,s){et(this,"__dynamicPropertyObservers").set(s,n)}__runComplexObservers(n,s){s.forEach((o,r)=>{o.some(a=>n.has(a))&&(this[r]?this[r](...o.map(a=>this[a])):console.warn(`observer method ${r} not defined`))})}__runDynamicObservers(n,s){s.forEach((o,r)=>{n.has(o)&&this[r]&&this[r](this[o],n.get(o))})}__runObservers(n,s){n.forEach((o,r)=>{const a=s.get(r);a!==void 0&&this[a]&&this[a](this[r],o)})}__runNotifyProps(n,s){n.forEach((o,r)=>{s.has(r)&&this.dispatchEvent(new CustomEvent(`${Rt(r)}-changed`,{detail:{value:this[r]}}))})}_get(n,s){return li(n,s)}_set(n,s,o){di(n,s,o)}}return e},k=f(ci);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class xt extends EventTarget{#t;#n=new Set;#i;#e=!1;constructor(e){super(),this.#t=e,this.#i=new CSSStyleSheet}#o(e){const{propertyName:t}=e;this.#n.has(t)&&this.dispatchEvent(new CustomEvent("property-changed",{detail:{propertyName:t}}))}observe(e){this.connect(),!this.#n.has(e)&&(this.#n.add(e),this.#i.replaceSync(`
      :root::before, :host::before {
        content: '' !important;
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
        visibility: hidden !important;
        transition: 1ms allow-discrete step-end !important;
        transition-property: ${[...this.#n].join(", ")} !important;
      }
    `))}connect(){this.#e||(this.#t.adoptedStyleSheets.unshift(this.#i),this.#s.addEventListener("transitionstart",e=>this.#o(e)),this.#s.addEventListener("transitionend",e=>this.#o(e)),this.#e=!0)}disconnect(){this.#n.clear(),this.#t.adoptedStyleSheets=this.#t.adoptedStyleSheets.filter(e=>e!==this.#i),this.#s.removeEventListener("transitionstart",this.#o),this.#s.removeEventListener("transitionend",this.#o),this.#e=!1}get#s(){return this.#t.documentElement??this.#t.host}static for(e){return e.__cssPropertyObserver||=new xt(e),e.__cssPropertyObserver}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function hi(i){const{baseStyles:e,themeStyles:t,elementStyles:n,lumoInjector:s}=i.constructor,o=i.__lumoStyleSheet;return o&&(e||t)?[...s.includeBaseStyles?e:[],o,...t]:[o,...n].filter(Boolean)}function ne(i){Be(i.shadowRoot,hi(i))}function Bt(i,e){i.__lumoStyleSheet=e,ne(i)}function it(i){i.__lumoStyleSheet=void 0,ne(i)}/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const $t=new Set;function se(i){$t.has(i)||($t.add(i),console.warn(i))}/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const zt=new WeakMap;function jt(i){try{return i.media.mediaText}catch{return se('[LumoInjector] Browser denied to access property "mediaText" for some CSS rules, so they were skipped.'),""}}function pi(i){try{return i.cssRules}catch{return se('[LumoInjector] Browser denied to access property "cssRules" for some CSS stylesheets, so they were skipped.'),[]}}function oe(i,e={tags:new Map,modules:new Map}){for(const t of pi(i)){if(t instanceof CSSImportRule){const n=jt(t);n.startsWith("lumo_")?e.modules.set(n,[...t.styleSheet.cssRules]):oe(t.styleSheet,e);continue}if(t instanceof CSSMediaRule){const n=jt(t);n.startsWith("lumo_")&&e.modules.set(n,[...t.cssRules]);continue}if(t instanceof CSSStyleRule&&t.cssText.includes("-inject")){for(const n of t.style){const s=n.match(/^--_lumo-(.*)-inject-modules$/u)?.[1];if(!s)continue;const o=t.style.getPropertyValue(n);e.tags.set(s,o.split(",").map(r=>r.trim().replace(/'|"/gu,"")))}continue}}return e}function fi(i){let e=new Map,t=new Map;for(const n of i){let s=zt.get(n);s||(s=oe(n),zt.set(n,s)),e=new Map([...e,...s.tags]),t=new Map([...t,...s.modules])}return{tags:e,modules:t}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function re(i){return`--_lumo-${i.is}-inject`}class vi{#t;#n;#i=new Map;#e=new Map;constructor(e=document){this.#t=e,this.handlePropertyChange=this.handlePropertyChange.bind(this),this.#n=xt.for(e),this.#n.addEventListener("property-changed",this.handlePropertyChange)}disconnect(){this.#n.removeEventListener("property-changed",this.handlePropertyChange),this.#i.clear(),this.#e.values().forEach(e=>e.forEach(it))}forceUpdate(){for(const e of this.#i.keys())this.#s(e)}componentConnected(e){const{lumoInjector:t}=e.constructor,{is:n}=t;this.#e.set(n,this.#e.get(n)??new Set),this.#e.get(n).add(e);const s=this.#i.get(n);if(s){s.cssRules.length>0&&Bt(e,s);return}this.#o(n);const o=re(t);this.#n.observe(o)}componentDisconnected(e){const{is:t}=e.constructor.lumoInjector;this.#e.get(t)?.delete(e),it(e)}handlePropertyChange(e){const{propertyName:t}=e.detail,n=t.match(/^--_lumo-(.*)-inject$/u)?.[1];n&&this.#s(n)}#o(e){this.#i.set(e,new CSSStyleSheet),this.#s(e)}#s(e){const{tags:t,modules:n}=fi(this.#r),s=(t.get(e)??[]).flatMap(r=>n.get(r)??[]).map(r=>r.cssText).join(`
`),o=this.#i.get(e);o.replaceSync(s),this.#e.get(e)?.forEach(r=>{s?Bt(r,o):it(r)})}get#r(){let e=new Set;for(const t of[this.#t,document])e=e.union(new Set(t.styleSheets)),e=e.union(new Set(t.adoptedStyleSheets));return[...e]}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ht=new Set;function ae(i){const e=i.getRootNode();return e.host&&e.host.constructor.version?ae(e.host):e}const L=i=>class extends i{static finalize(){super.finalize();const t=re(this.lumoInjector);this.is&&!Ht.has(t)&&(Ht.add(t),CSS.registerProperty({name:t,syntax:"<number>",inherits:!0,initialValue:"0"}))}static get lumoInjector(){return{is:this.is,includeBaseStyles:!1}}connectedCallback(){super.connectedCallback();const t=ae(this);t.__lumoInjectorDisabled||this.isConnected&&(t.__lumoInjector||=new vi(t),this.__lumoInjector=t.__lumoInjector,this.__lumoInjector.componentConnected(this))}disconnectedCallback(){super.disconnectedCallback(),this.__lumoInjector&&(this.__lumoInjector.componentDisconnected(this),this.__lumoInjector=void 0)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const le=i=>class extends i{static get properties(){return{_theme:{type:String,readOnly:!0}}}static get observedAttributes(){return[...super.observedAttributes,"theme"]}attributeChangedCallback(t,n,s){super.attributeChangedCallback(t,n,s),t==="theme"&&this._set_theme(s)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const vt=[],_i=new Set,gi=new Set;function mi(i){return i&&Object.prototype.hasOwnProperty.call(i,"__themes")}function bi(i,e){return(i||"").split(" ").some(t=>new RegExp(`^${t.split("*").join(".*")}$`,"u").test(e))}function yi(i){return i.map(e=>e.cssText).join(`
`)}const wi="vaadin-themable-mixin-style";function xi(i,e){const t=document.createElement("style");t.id=wi,t.textContent=yi(i),e.content.appendChild(t)}function Ci(i=""){let e=0;return i.startsWith("lumo-")||i.startsWith("material-")?e=1:i.startsWith("vaadin-")&&(e=2),e}function de(i){const e=[];return i.include&&[].concat(i.include).forEach(t=>{const n=vt.find(s=>s.moduleId===t);n?e.push(...de(n),...n.styles):console.warn(`Included moduleId ${t} not found in style registry`)},i.styles),e}function Ei(i){const e=`${i}-default-theme`,t=vt.filter(n=>n.moduleId!==e&&bi(n.themeFor,i)).map(n=>({...n,styles:[...de(n),...n.styles],includePriority:Ci(n.moduleId)})).sort((n,s)=>s.includePriority-n.includePriority);return t.length>0?t:vt.filter(n=>n.moduleId===e)}const N=i=>class extends le(i){constructor(){super(),_i.add(new WeakRef(this))}static finalize(){if(super.finalize(),this.is&&gi.add(this.is),this.elementStyles)return;const t=this.prototype._template;!t||mi(this)||xi(this.getStylesForThis(),t)}static finalizeStyles(t){return this.baseStyles=t?[t].flat(1/0):[],this.themeStyles=this.getStylesForThis(),[...this.baseStyles,...this.themeStyles]}static getStylesForThis(){const t=i.__themes||[],n=Object.getPrototypeOf(this.prototype),s=(n?n.constructor.__themes:[])||[];this.__themes=[...t,...s,...Ei(this.is)];const o=this.__themes.flatMap(r=>r.styles);return o.filter((r,a)=>a===o.lastIndexOf(r))}};/**
 * @license
 * Copyright (c) 2026 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ai=(i,...e)=>{const t=document.createElement("style");t.id=i,t.textContent=e.map(n=>n.toString()).join(`
`),document.head.insertAdjacentElement("afterbegin",t)};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */["--vaadin-text-color","--vaadin-text-color-disabled","--vaadin-text-color-secondary","--vaadin-border-color","--vaadin-border-color-secondary","--vaadin-background-color"].forEach(i=>{CSS.registerProperty({name:i,syntax:"<color>",inherits:!0,initialValue:"light-dark(black, white)"})});Ai("vaadin-base",h`
    @layer vaadin.base {
      html {
        /* Background color */
        --vaadin-background-color: light-dark(#fff, #222);

        /* Container colors */
        --vaadin-background-container: color-mix(in oklab, var(--vaadin-text-color) 5%, var(--vaadin-background-color));
        --vaadin-background-container-strong: color-mix(
          in oklab,
          var(--vaadin-text-color) 10%,
          var(--vaadin-background-color)
        );

        /* Border colors */
        --vaadin-border-color-secondary: color-mix(in oklab, var(--vaadin-text-color) 24%, transparent);
        --vaadin-border-color: color-mix(in oklab, var(--vaadin-text-color) 48%, transparent); /* Above 3:1 contrast */

        /* Text colors */
        /* Above 3:1 contrast */
        --vaadin-text-color-disabled: color-mix(in oklab, var(--vaadin-text-color) 48%, transparent);
        /* Above 4.5:1 contrast */
        --vaadin-text-color-secondary: color-mix(in oklab, var(--vaadin-text-color) 68%, transparent);
        /* Above 7:1 contrast */
        --vaadin-text-color: light-dark(#1f1f1f, white);

        /* Padding */
        --vaadin-padding-xs: 6px;
        --vaadin-padding-s: 8px;
        --vaadin-padding-m: 12px;
        --vaadin-padding-l: 16px;
        --vaadin-padding-xl: 24px;
        --vaadin-padding-block-container: var(--vaadin-padding-xs);
        --vaadin-padding-inline-container: var(--vaadin-padding-s);

        /* Gap/spacing */
        --vaadin-gap-xs: 6px;
        --vaadin-gap-s: 8px;
        --vaadin-gap-m: 12px;
        --vaadin-gap-l: 16px;
        --vaadin-gap-xl: 24px;

        /* Border radius */
        --vaadin-radius-s: 3px;
        --vaadin-radius-m: 6px;
        --vaadin-radius-l: 12px;

        /* Focus outline */
        --vaadin-focus-ring-width: 2px;
        --vaadin-focus-ring-color: var(--vaadin-text-color);

        /* Icons, used as mask-image */
        --_vaadin-icon-arrow-up: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 7-7 7 7"/><path d="M12 19V5"/></svg>');
        --_vaadin-icon-calendar: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/></svg>');
        --_vaadin-icon-checkmark: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5" /></svg>');
        --_vaadin-icon-chevron-down: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>');
        --_vaadin-icon-clock: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6v6l4 2"/><circle cx="12" cy="12" r="10"/></svg>');
        --_vaadin-icon-cross: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" /></svg>');
        --_vaadin-icon-drag: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"><path d="M11 7c0 .82843-.6716 1.5-1.5 1.5C8.67157 8.5 8 7.82843 8 7s.67157-1.5 1.5-1.5c.8284 0 1.5.67157 1.5 1.5Zm0 5c0 .8284-.6716 1.5-1.5 1.5-.82843 0-1.5-.6716-1.5-1.5s.67157-1.5 1.5-1.5c.8284 0 1.5.6716 1.5 1.5Zm0 5c0 .8284-.6716 1.5-1.5 1.5-.82843 0-1.5-.6716-1.5-1.5s.67157-1.5 1.5-1.5c.8284 0 1.5.6716 1.5 1.5Zm5-10c0 .82843-.6716 1.5-1.5 1.5S13 7.82843 13 7s.6716-1.5 1.5-1.5S16 6.17157 16 7Zm0 5c0 .8284-.6716 1.5-1.5 1.5S13 12.8284 13 12s.6716-1.5 1.5-1.5 1.5.6716 1.5 1.5Zm0 5c0 .8284-.6716 1.5-1.5 1.5S13 17.8284 13 17s.6716-1.5 1.5-1.5 1.5.6716 1.5 1.5Z" fill="currentColor"/></svg>');
        --_vaadin-icon-eye: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" /><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" /></svg>');
        --_vaadin-icon-eye-slash: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.242 4.242L9.88 9.88" /></svg>');
        --_vaadin-icon-fullscreen: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" /></svg>');
        --_vaadin-icon-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>');
        --_vaadin-icon-link: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>');
        --_vaadin-icon-menu: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" /></svg>');
        --_vaadin-icon-minus: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/></svg>');
        --_vaadin-icon-paper-airplane: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" /></svg>');
        --_vaadin-icon-pen: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/></svg>');
        --_vaadin-icon-play: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M5.25 5.653c0-.856.917-1.398 1.667-.986l11.54 6.347a1.125 1.125 0 0 1 0 1.972l-11.54 6.347a1.125 1.125 0 0 1-1.667-.986V5.653Z" /></svg>');
        --_vaadin-icon-plus: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>');
        --_vaadin-icon-redo: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 7v6h-6"/><path d="M3 17a9 9 0 0 1 9-9 9 9 0 0 1 6 2.3l3 2.7"/></svg>');
        --_vaadin-icon-refresh: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"><path d="M22 10C22 10 19.995 7.26822 18.3662 5.63824C16.7373 4.00827 14.4864 3 12 3C7.02944 3 3 7.02944 3 12C3 16.9706 7.02944 21 12 21C16.1031 21 19.5649 18.2543 20.6482 14.5M22 10V4M22 10H16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>');
        --_vaadin-icon-resize: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M18.5303 7.46967c.2929.29289.2929.76777 0 1.06066L8.53033 18.5304c-.29289.2929-.76777.2929-1.06066 0s-.29289-.7678 0-1.0607L17.4697 7.46967c.2929-.29289.7677-.29289 1.0606 0Zm0 4.50003c.2929.2929.2929.7678 0 1.0607l-5.5 5.5c-.2929.2928-.7677.2928-1.0606 0-.2929-.2929-.2929-.7678 0-1.0607l5.4999-5.5c.2929-.2929.7678-.2929 1.0607 0Zm0 4.5c.2929.2928.2929.7677 0 1.0606l-1 1.0001c-.2929.2928-.7677.2929-1.0606 0-.2929-.2929-.2929-.7678 0-1.0607l1-1c.2929-.2929.7677-.2929 1.0606 0Z" fill="currentColor"/></svg>');
        --_vaadin-icon-sort: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="8" height="12" viewBox="0 0 8 12" fill="none"><path d="M7.49854 6.99951C7.92795 6.99951 8.15791 7.50528 7.87549 7.82861L4.37646 11.8296C4.17728 12.0571 3.82272 12.0571 3.62354 11.8296L0.125488 7.82861C-0.157248 7.50531 0.0719873 6.99956 0.501465 6.99951H7.49854ZM3.62354 0.17041C3.82275 -0.0573875 4.17725 -0.0573848 4.37646 0.17041L7.87549 4.17041C8.15825 4.49373 7.92806 5.00049 7.49854 5.00049L0.501465 4.99951C0.0719873 4.99946 -0.157248 4.49371 0.125488 4.17041L3.62354 0.17041Z" fill="black"/></svg>');
        --_vaadin-icon-undo: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7v6h6"/><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"/></svg>');
        --_vaadin-icon-upload: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="m17 8-5-5-5 5"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/></svg>');
        --_vaadin-icon-user: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>');
        --_vaadin-icon-warn: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg>');

        /* Cursors for interactive elements */
        --vaadin-clickable-cursor: pointer;
        --vaadin-disabled-cursor: not-allowed;

        /* Use units so that the values can be used in calc() */
        --safe-area-inset-top: env(safe-area-inset-top, 0px);
        --safe-area-inset-right: env(safe-area-inset-right, 0px);
        --safe-area-inset-bottom: env(safe-area-inset-bottom, 0px);
        --safe-area-inset-left: env(safe-area-inset-left, 0px);
      }

      @supports not (color: hsl(0 0 0)) {
        html {
          --_vaadin-safari-17-deg: 1deg;
        }
      }

      @media (forced-colors: active) {
        html {
          --vaadin-background-color: Canvas;
          --vaadin-border-color: CanvasText;
          --vaadin-border-color-secondary: CanvasText;
          --vaadin-text-color-disabled: CanvasText;
          --vaadin-text-color-secondary: CanvasText;
          --vaadin-text-color: CanvasText;
          --vaadin-icon-color: CanvasText;
          --vaadin-focus-ring-color: Highlight;
        }
      }
    }
  `);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ut=h`
  :host {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    box-sizing: border-box;
  }

  :host([hidden]) {
    display: none !important;
  }

  /* Theme variations */
  :host([theme~='margin']) {
    margin: var(--vaadin-vertical-layout-margin, var(--vaadin-padding-m));
  }

  :host([theme~='padding']) {
    padding: var(--vaadin-vertical-layout-padding, var(--vaadin-padding-m));
  }

  :host([theme~='spacing']) {
    gap: var(--vaadin-vertical-layout-gap, var(--vaadin-gap-s));
  }

  :host([theme~='wrap']) {
    flex-wrap: wrap;
  }
`,ki=window.Vaadin.featureFlags.layoutComponentImprovements,Ti=h`
  ::slotted([data-height-full]) {
    flex: 1;
  }

  ::slotted(vaadin-horizontal-layout[data-height-full]),
  ::slotted(vaadin-vertical-layout[data-height-full]) {
    min-height: 0;
  }
`,Si=ki?[Ut,Ti]:[Ut];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Mi extends N($(k(L(E)))){static get is(){return"vaadin-vertical-layout"}static get styles(){return Si}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return y`<slot></slot>`}}A(Mi);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Oi=h`
  :host {
    display: flex;
    align-items: center;
    --_radius: var(--vaadin-input-field-border-radius, var(--vaadin-radius-m));
    border-radius:
      /* See https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius */
      var(--vaadin-input-field-top-start-radius, var(--_radius))
      var(--vaadin-input-field-top-end-radius, var(--_radius))
      var(--vaadin-input-field-bottom-end-radius, var(--_radius))
      var(--vaadin-input-field-bottom-start-radius, var(--_radius));
    border: var(--vaadin-input-field-border-width, 1px) solid
      var(--vaadin-input-field-border-color, var(--vaadin-border-color));
    box-sizing: border-box;
    cursor: text;
    padding: var(
      --vaadin-input-field-padding,
      var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container)
    );
    gap: var(--vaadin-input-field-gap, var(--vaadin-gap-s));
    background: var(--vaadin-input-field-background, var(--vaadin-background-color));
    color: var(--vaadin-input-field-value-color, var(--vaadin-text-color));
    font-size: var(--vaadin-input-field-value-font-size, inherit);
    line-height: var(--vaadin-input-field-value-line-height, inherit);
    font-weight: var(--vaadin-input-field-value-font-weight, 400);
  }

  :host([dir='rtl']) {
    --_radius: var(--vaadin-input-field-border-radius, var(--vaadin-radius-m));
    border-radius:
      /* Don't use logical props, see https://github.com/vaadin/vaadin-time-picker/issues/145 */
      var(--vaadin-input-field-top-end-radius, var(--_radius))
      var(--vaadin-input-field-top-start-radius, var(--_radius))
      var(--vaadin-input-field-bottom-start-radius, var(--_radius))
      var(--vaadin-input-field-bottom-end-radius, var(--_radius));
  }

  :host([hidden]) {
    display: none !important;
  }

  /* Reset the native input styles */
  ::slotted(:is(input, textarea)) {
    appearance: none;
    align-self: stretch;
    box-sizing: border-box;
    flex: auto;
    white-space: nowrap;
    overflow: hidden;
    width: 100%;
    height: auto;
    outline: none;
    margin: 0;
    padding: 0;
    border: 0;
    border-radius: 0;
    min-width: 0;
    font: inherit;
    font-size: 1em;
    color: inherit;
    background: transparent;
    cursor: inherit;
    text-align: inherit;
    caret-color: var(--vaadin-input-field-value-color);
  }

  ::slotted(*) {
    flex: none;
  }

  slot[name$='fix'] {
    cursor: auto;
  }

  ::slotted(:is(input, textarea))::placeholder {
    /* Use ::slotted(:is(input, textarea):placeholder-shown) to style the placeholder */
    /* because ::slotted(...)::placeholder does not work in Safari. */
    font: inherit;
    color: inherit;
  }

  ::slotted(:is(input, textarea):placeholder-shown) {
    color: var(--vaadin-input-field-placeholder-color, var(--vaadin-text-color-secondary));
  }

  :host(:focus-within) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--vaadin-input-field-border-width, 1px) * -1);
  }

  :host([invalid]) {
    --vaadin-input-field-border-color: var(--vaadin-input-field-error-color, var(--vaadin-text-color));
  }

  :host([readonly]) {
    border-style: dashed;
  }

  :host([readonly]:focus-within) {
    outline-style: dashed;
    --vaadin-input-field-border-color: transparent;
  }

  :host([disabled]) {
    --vaadin-input-field-value-color: var(--vaadin-input-field-disabled-text-color, var(--vaadin-text-color-disabled));
    --vaadin-input-field-background: var(
      --vaadin-input-field-disabled-background,
      var(--vaadin-background-container-strong)
    );
    --vaadin-input-field-border-color: transparent;
  }

  :host([theme~='align-start']) slot:not([name])::slotted(*) {
    text-align: start;
  }

  :host([theme~='align-center']) slot:not([name])::slotted(*) {
    text-align: center;
  }

  :host([theme~='align-end']) slot:not([name])::slotted(*) {
    text-align: end;
  }

  :host([theme~='align-left']) slot:not([name])::slotted(*) {
    text-align: left;
  }

  :host([theme~='align-right']) slot:not([name])::slotted(*) {
    text-align: right;
  }

  @media (forced-colors: active) {
    :host {
      --vaadin-input-field-background: Field;
      --vaadin-input-field-value-color: FieldText;
      --vaadin-input-field-placeholder-color: GrayText;
    }

    :host([disabled]) {
      --vaadin-input-field-value-color: GrayText;
      --vaadin-icon-color: GrayText;
    }
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ii extends N(wt(k(L(E)))){static get is(){return"vaadin-input-container"}static get styles(){return Oi}static get properties(){return{disabled:{type:Boolean,reflectToAttribute:!0},readonly:{type:Boolean,reflectToAttribute:!0},invalid:{type:Boolean,reflectToAttribute:!0}}}render(){return y`
      <slot name="prefix"></slot>
      <slot></slot>
      <slot name="suffix"></slot>
    `}ready(){super.ready(),this.addEventListener("pointerdown",e=>{e.target===this&&e.preventDefault()}),this.addEventListener("click",e=>{e.target===this&&this.shadowRoot.querySelector("slot:not([name])").assignedNodes({flatten:!0}).forEach(t=>t.focus&&t.focus())})}}A(Ii);/**
 * @license
 * Copyright 2018 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const ue=i=>i??$e;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Li(i){const e=[];for(;i;){if(i.nodeType===Node.DOCUMENT_NODE){e.push(i);break}if(i.nodeType===Node.DOCUMENT_FRAGMENT_NODE){e.push(i),i=i.host;continue}if(i.assignedSlot){i=i.assignedSlot;continue}i=i.parentNode}return e}function Ct(i){return i?new Set(i.split(" ")):new Set}function K(i){return i?[...i].join(" "):""}function Et(i,e,t){const n=Ct(i.getAttribute(e));n.add(t),i.setAttribute(e,K(n))}function ce(i,e,t){const n=Ct(i.getAttribute(e));if(n.delete(t),n.size===0){i.removeAttribute(e);return}i.setAttribute(e,K(n))}function he(i){return i.nodeType===Node.TEXT_NODE&&i.textContent.trim()===""}/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class H{constructor(e,t){this.slot=e,this.callback=t,this._storedNodes=[],this._connected=!1,this._scheduled=!1,this._boundSchedule=()=>{this._schedule()},this.connect(),this._schedule()}connect(){this.slot.addEventListener("slotchange",this._boundSchedule),this._connected=!0}disconnect(){this.slot.removeEventListener("slotchange",this._boundSchedule),this._connected=!1}_schedule(){this._scheduled||(this._scheduled=!0,queueMicrotask(()=>{this.flush()}))}flush(){this._connected&&(this._scheduled=!1,this._processNodes())}_processNodes(){const e=this.slot.assignedNodes({flatten:!0});let t=[];const n=[],s=[];e.length&&(t=e.filter(o=>!this._storedNodes.includes(o))),this._storedNodes.length&&this._storedNodes.forEach((o,r)=>{const a=e.indexOf(o);a===-1?n.push(o):a!==r&&s.push(o)}),(t.length||n.length||s.length)&&this.callback({addedNodes:t,currentNodes:e,movedNodes:s,removedNodes:n}),this._storedNodes=e}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let Ni=0;function pe(){return Ni++}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class G extends EventTarget{static generateId(e,t="default"){return`${t}-${e.localName}-${pe()}`}constructor(e,t,n,s={}){super();const{initializer:o,multiple:r,observe:a,useUniqueId:l,uniqueIdPrefix:d}=s;this.host=e,this.slotName=t,this.tagName=n,this.observe=typeof a=="boolean"?a:!0,this.multiple=typeof r=="boolean"?r:!1,this.slotInitializer=o,r&&(this.nodes=[]),l&&(this.defaultId=this.constructor.generateId(e,d||t))}hostConnected(){this.initialized||(this.multiple?this.initMultiple():this.initSingle(),this.observe&&this.observeSlot(),this.initialized=!0)}initSingle(){let e=this.getSlotChild();e?(this.node=e,this.initAddedNode(e)):(e=this.attachDefaultNode(),this.initNode(e))}initMultiple(){const e=this.getSlotChildren();if(e.length===0){const t=this.attachDefaultNode();t&&(this.nodes=[t],this.initNode(t))}else this.nodes=e,e.forEach(t=>{this.initAddedNode(t)})}attachDefaultNode(){const{host:e,slotName:t,tagName:n}=this;let s=this.defaultNode;return!s&&n&&(s=document.createElement(n),s instanceof Element&&(t!==""&&s.setAttribute("slot",t),this.defaultNode=s)),s&&(this.node=s,e.appendChild(s)),s}getSlotChildren(){const{slotName:e}=this;return Array.from(this.host.childNodes).filter(t=>t.nodeType===Node.ELEMENT_NODE&&t.hasAttribute("data-slot-ignore")?!1:t.nodeType===Node.ELEMENT_NODE&&t.slot===e||t.nodeType===Node.TEXT_NODE&&t.textContent.trim()&&e==="")}getSlotChild(){return this.getSlotChildren()[0]}initNode(e){const{slotInitializer:t}=this;t&&t(e,this.host)}initCustomNode(e){}teardownNode(e){}initAddedNode(e){e!==this.defaultNode&&(this.initCustomNode(e),this.initNode(e))}observeSlot(){const{slotName:e}=this,t=e===""?"slot:not([name])":`slot[name=${e}]`,n=this.host.shadowRoot.querySelector(t);this.__slotObserver=new H(n,({addedNodes:s,removedNodes:o})=>{const r=this.multiple?this.nodes:[this.node],a=s.filter(l=>!he(l)&&!r.includes(l)&&!(l.nodeType===Node.ELEMENT_NODE&&l.hasAttribute("data-slot-ignore")));o.length&&(this.nodes=r.filter(l=>!o.includes(l)),o.forEach(l=>{this.teardownNode(l)})),a&&a.length>0&&(this.multiple?(this.defaultNode&&this.defaultNode.remove(),this.nodes=[...r,...a].filter(l=>l!==this.defaultNode),a.forEach(l=>{this.initAddedNode(l)})):(this.node&&this.node.remove(),this.node=a[0],this.initAddedNode(this.node)))})}}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class fe extends G{constructor(e){super(e,"tooltip"),this.setTarget(e),this.__onContentChange=this.__onContentChange.bind(this)}initCustomNode(e){e.target=this.target,this.ariaTarget!==void 0&&(e.ariaTarget=this.ariaTarget),this.context!==void 0&&(e.context=this.context),this.manual!==void 0&&(e.manual=this.manual),this.opened!==void 0&&(e.opened=this.opened),this.position!==void 0&&(e._position=this.position),this.shouldShow!==void 0&&(e.shouldShow=this.shouldShow),this.manual||this.host.setAttribute("has-tooltip",""),this.__notifyChange(e),e.addEventListener("content-changed",this.__onContentChange)}teardownNode(e){this.manual||this.host.removeAttribute("has-tooltip"),e.removeEventListener("content-changed",this.__onContentChange),this.__notifyChange(null)}setAriaTarget(e){this.ariaTarget=e;const t=this.node;t&&(t.ariaTarget=e)}setContext(e){this.context=e;const t=this.node;t&&(t.context=e)}setManual(e){this.manual=e;const t=this.node;t&&(t.manual=e)}setOpened(e){this.opened=e;const t=this.node;t&&(t.opened=e)}setPosition(e){this.position=e;const t=this.node;t&&(t._position=e)}setShouldShow(e){this.shouldShow=e;const t=this.node;t&&(t.shouldShow=e)}setTarget(e){this.target=e;const t=this.node;t&&(t.target=e)}__onContentChange(e){this.__notifyChange(e.target)}__notifyChange(e){this.dispatchEvent(new CustomEvent("tooltip-changed",{detail:{node:e}}))}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Di=h`
  [part$='button'] {
    color: var(--vaadin-input-field-button-text-color, var(--vaadin-text-color-secondary));
    cursor: var(--vaadin-clickable-cursor);
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    -webkit-user-select: none;
    user-select: none;
    /* Ensure minimum click target (WCAG) */
    padding: max(0px, (24px - 1lh) / 2);
    margin: min(0px, (24px - 1lh) / -2);
  }

  /* Icon */
  [part$='button']::before {
    background: currentColor;
    content: '';
    display: block;
    height: var(--vaadin-icon-size, 1lh);
    width: var(--vaadin-icon-size, 1lh);
    mask-size: var(--vaadin-icon-visual-size, 100%);
    mask-position: 50%;
    mask-repeat: no-repeat;
  }

  :host(:is(:not([clear-button-visible][has-value]), [disabled], [readonly])) [part~='clear-button'] {
    display: none;
  }

  [part~='clear-button']::before {
    mask-image: var(--_vaadin-icon-cross);
  }

  :host(:is([readonly], [disabled])) [part$='button'] {
    color: var(--vaadin-text-color-disabled);
    cursor: var(--vaadin-disabled-cursor);
  }

  @media (forced-colors: active) {
    [part$='button']::before {
      background: CanvasText;
    }

    :host([disabled]) [part$='button'] {
      color: GrayText;
    }

    :host([disabled]) [part$='button']::before {
      background: GrayText;
    }
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Pi=h`
  :host {
    --_helper-below-field: initial;
    --_helper-above-field: ;
    --_no-label: initial;
    --_has-label: ;
    --_no-helper: initial;
    --_has-helper: ;
    --_no-error: initial;
    --_has-error: ;
    --_gap: var(--vaadin-input-field-container-gap, var(--vaadin-gap-xs));
    --_gap-s: round(var(--_gap) / 3, 2px);
    display: inline-grid;
    grid-template:
      'label' auto var(--_helper-above-field, 'helper' auto) 'baseline' 0 'input' 1fr var(
        --_helper-below-field,
        'helper' auto
      )
      'error' auto / 100%;
    outline: none;
    cursor: default;
    -webkit-tap-highlight-color: transparent;
  }

  :host([has-label]) {
    --_has-label: initial;
    --_no-label: ;
  }

  :host([has-helper]) {
    --_has-helper: initial;
    --_no-helper: ;
  }

  :host([has-error-message]) {
    --_has-error: initial;
    --_no-error: ;
  }

  :host([hidden]) {
    display: none !important;
  }

  :host(:not([has-label])) [part='label'],
  :host(:not([has-helper])) [part='helper-text'],
  :host(:not([has-error-message])) [part='error-message'] {
    display: none;
  }

  /* Baseline alignment guide */
  :host::before {
    content: '\\2003' / '';
    grid-column: 1;
    grid-row: var(--_has-label, label / baseline) var(--_no-label, label / input);
    align-self: var(--_has-label, end) var(--_no-label, start);
    font-size: var(--vaadin-input-field-value-font-size, inherit);
    line-height: var(--vaadin-input-field-value-line-height, inherit);
    padding: var(
      --vaadin-input-field-padding,
      var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container)
    );
    border: var(--vaadin-input-field-border-width, 1px) solid transparent;
    pointer-events: none;
    margin-bottom: var(--_no-label, 0)
      var(
        --_has-label,
        calc(
          var(
              --vaadin-field-baseline-input-height,
              (1lh + var(--vaadin-padding-block-container) * 2 + var(--vaadin-input-field-border-width, 1px) * 2)
            ) *
            -1
        )
      );
  }

  [class$='container'] {
    display: contents;
  }

  [part] {
    grid-column: 1;
  }

  [part='label'] {
    font-size: var(--vaadin-input-field-label-font-size, inherit);
    line-height: var(--vaadin-input-field-label-line-height, inherit);
    font-weight: var(--vaadin-input-field-label-font-weight, 500);
    color: var(--vaadin-input-field-label-color, var(--vaadin-text-color));
    word-break: break-word;
    position: relative;
    grid-area: label;
    margin-bottom: var(--_helper-below-field, var(--_gap)) var(--_helper-above-field, var(--_no-helper, var(--_gap)));
  }

  ::slotted(label) {
    cursor: inherit;
  }

  :host([disabled]) [part='label'],
  :host([disabled]) ::slotted(label) {
    opacity: 0.5;
  }

  :host([disabled]) [part='label'] ::slotted(label) {
    opacity: 1;
  }

  :host([required]) [part='label'] {
    padding-inline-end: 1em;
  }

  [part='required-indicator'] {
    display: inline-block;
    position: absolute;
    width: 1em;
    text-align: center;
    color: var(--vaadin-input-field-required-indicator-color, var(--vaadin-text-color-secondary));
  }

  [part='required-indicator']::after {
    content: var(--vaadin-input-field-required-indicator, '*');
  }

  :host(:not([required])) [part='required-indicator'] {
    display: none;
  }

  [part='label'],
  [part='helper-text'],
  [part='error-message'] {
    width: min-content;
    min-width: 100%;
    box-sizing: border-box;
  }

  [part='input-field'],
  [part='group-field'],
  [part='input-fields'] {
    grid-area: input;
  }

  [part='input-field'] {
    width: var(--vaadin-field-default-width, 12em);
    max-width: 100%;
    min-width: 100%;
  }

  :host([readonly]) [part='input-field'] {
    cursor: default;
  }

  :host([disabled]) [part='input-field'] {
    cursor: var(--vaadin-disabled-cursor);
  }

  [part='helper-text'] {
    font-size: var(--vaadin-input-field-helper-font-size, inherit);
    line-height: var(--vaadin-input-field-helper-line-height, inherit);
    font-weight: var(--vaadin-input-field-helper-font-weight, 400);
    color: var(--vaadin-input-field-helper-color, var(--vaadin-text-color-secondary));
    grid-area: helper;
    margin-top: var(--_helper-above-field, var(--_gap-s)) var(--_helper-below-field, var(--_gap));
    margin-bottom: var(--_helper-above-field, var(--_gap));
  }

  [part='error-message'] {
    font-size: var(--vaadin-input-field-error-font-size, inherit);
    line-height: var(--vaadin-input-field-error-line-height, inherit);
    font-weight: var(--vaadin-input-field-error-font-weight, 400);
    color: var(--vaadin-input-field-error-color, var(--vaadin-text-color));
    display: flex;
    gap: var(--vaadin-gap-xs);
    grid-area: error;
    margin-top: var(--_has-helper, var(--_helper-below-field, var(--_gap-s)) var(--_helper-above-field, var(--_gap)))
      var(--_no-helper, var(--_gap));
  }

  [part='error-message']::before {
    content: '';
    display: inline-block;
    flex: none;
    width: var(--vaadin-icon-size, 1lh);
    height: var(--vaadin-icon-size, 1lh);
    mask: var(--_vaadin-icon-warn) 50% / var(--vaadin-icon-visual-size, 100%) no-repeat;
    background: currentColor;
  }

  :host([theme~='helper-above-field']) {
    --_helper-above-field: initial;
    --_helper-below-field: ;
  }

  @media (forced-colors: active) {
    [part='error-message']::before {
      background: CanvasText;
    }
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Fi=[Pi,Di];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ri extends G{constructor(e,t,n={}){const{uniqueIdPrefix:s}=n;super(e,"input","input",{initializer:(o,r)=>{r.value&&(o.value=r.value),r.type&&o.setAttribute("type",r.type),o.id=this.defaultId,typeof t=="function"&&t(o)},useUniqueId:!0,uniqueIdPrefix:s})}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let At=!1;window.addEventListener("keydown",()=>{At=!0},{capture:!0});window.addEventListener("mousedown",()=>{At=!1},{capture:!0});function _t(){let i=document.activeElement||document.body;for(;i.shadowRoot&&i.shadowRoot.activeElement;)i=i.shadowRoot.activeElement;return i}function Y(){return At}function ve(i){const e=i.style;if(e.visibility==="hidden"||e.display==="none")return!0;const t=window.getComputedStyle(i);return t.visibility==="hidden"||t.display==="none"}function Vi(i,e){const t=Math.max(i.tabIndex,0),n=Math.max(e.tabIndex,0);return t===0||n===0?n>t:t>n}function Bi(i,e){const t=[];for(;i.length>0&&e.length>0;)Vi(i[0],e[0])?t.push(e.shift()):t.push(i.shift());return t.concat(i,e)}function gt(i){const e=i.length;if(e<2)return i;const t=Math.ceil(e/2),n=gt(i.slice(0,t)),s=gt(i.slice(t));return Bi(n,s)}function $i(i){return i.checkVisibility?!i.checkVisibility({visibilityProperty:!0}):i.offsetParent===null&&i.clientWidth===0&&i.clientHeight===0?!0:ve(i)}function zi(i){return i.matches('[tabindex="-1"]')?!1:i.matches("input, select, textarea, button, object")?i.matches(":not([disabled])"):i.matches("a[href], area[href], iframe, [tabindex], [contentEditable]")}function _e(i){return i.getRootNode().activeElement===i}function ji(i){if(!zi(i))return-1;const e=i.getAttribute("tabindex")||0;return Number(e)}function ge(i,e){if(i.nodeType!==Node.ELEMENT_NODE||ve(i))return!1;const t=i,n=ji(t);let s=n>0;n>=0&&e.push(t);let o=[];return t.localName==="slot"?o=t.assignedNodes({flatten:!0}):o=(t.shadowRoot||t).children,[...o].forEach(r=>{s=ge(r,e)||s}),s}function Hi(i){const e=[];return ge(i,e)?gt(e):e}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const me=f(i=>class extends i{get _keyboardActive(){return Y()}ready(){this.addEventListener("focusin",t=>{this._shouldSetFocus(t)&&this._setFocused(!0)}),this.addEventListener("focusout",t=>{this._shouldRemoveFocus(t)&&this._setFocused(!1)}),super.ready()}disconnectedCallback(){super.disconnectedCallback(),this.hasAttribute("focused")&&this._setFocused(!1)}focus(t){super.focus(t),t&&t.focusVisible===!1||this.setAttribute("focus-ring","")}_setFocused(t){this.toggleAttribute("focused",t),this.toggleAttribute("focus-ring",t&&this._keyboardActive)}_shouldSetFocus(t){return!0}_shouldRemoveFocus(t){return!0}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const be=f(i=>class extends i{static get properties(){return{disabled:{type:Boolean,value:!1,observer:"_disabledChanged",reflectToAttribute:!0,sync:!0}}}_disabledChanged(t){this._setAriaDisabled(t)}_setAriaDisabled(t){t?this.setAttribute("aria-disabled","true"):this.removeAttribute("aria-disabled")}click(){this.disabled||super.click()}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ye=i=>class extends be(i){static get properties(){return{tabindex:{type:Number,reflectToAttribute:!0,observer:"_tabindexChanged",sync:!0},_lastTabIndex:{type:Number}}}_disabledChanged(t,n){super._disabledChanged(t,n),!this.__shouldAllowFocusWhenDisabled()&&(t?(this.tabindex!==void 0&&(this._lastTabIndex=this.tabindex),this.setAttribute("tabindex","-1")):n&&(this._lastTabIndex!==void 0?this.setAttribute("tabindex",this._lastTabIndex):this.tabindex=void 0))}_tabindexChanged(t){this.__shouldAllowFocusWhenDisabled()||this.disabled&&t!==-1&&(this._lastTabIndex=t,this.setAttribute("tabindex","-1"))}focus(t){(!this.disabled||this.__shouldAllowFocusWhenDisabled())&&super.focus(t)}__shouldAllowFocusWhenDisabled(){return!1}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ui=f(i=>class extends me(ye(i)){static get properties(){return{autofocus:{type:Boolean},focusElement:{type:Object,readOnly:!0,observer:"_focusElementChanged",sync:!0},_lastTabIndex:{value:0}}}constructor(){super(),this._boundOnBlur=this._onBlur.bind(this),this._boundOnFocus=this._onFocus.bind(this)}ready(){super.ready(),this.autofocus&&!this.disabled&&requestAnimationFrame(()=>{this.focus()})}focus(t){this.focusElement&&!this.disabled&&(this.focusElement.focus(),t&&t.focusVisible===!1||this.setAttribute("focus-ring",""))}blur(){this.focusElement&&this.focusElement.blur()}click(){this.focusElement&&!this.disabled&&this.focusElement.click()}_focusElementChanged(t,n){t?(t.disabled=this.disabled,this._addFocusListeners(t),this.__forwardTabIndex(this.tabindex)):n&&this._removeFocusListeners(n)}_addFocusListeners(t){t.addEventListener("blur",this._boundOnBlur),t.addEventListener("focus",this._boundOnFocus)}_removeFocusListeners(t){t.removeEventListener("blur",this._boundOnBlur),t.removeEventListener("focus",this._boundOnFocus)}_onFocus(t){t.stopPropagation(),this.dispatchEvent(new Event("focus"))}_onBlur(t){t.stopPropagation(),this.dispatchEvent(new Event("blur"))}_shouldSetFocus(t){return t.target===this.focusElement}_shouldRemoveFocus(t){return t.target===this.focusElement}_disabledChanged(t,n){super._disabledChanged(t,n),this.focusElement&&(this.focusElement.disabled=t),t&&this.blur()}_tabindexChanged(t){this.__forwardTabIndex(t)}__forwardTabIndex(t){t!==void 0&&this.focusElement&&(this.focusElement.tabIndex=t,t!==-1&&(this.tabindex=void 0)),this.disabled&&t&&(t!==-1&&(this._lastTabIndex=t),this.tabindex=void 0),t===void 0&&this.hasAttribute("tabindex")&&this.removeAttribute("tabindex")}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const kt=f(i=>class extends i{ready(){super.ready(),this.addEventListener("keydown",t=>{this._onKeyDown(t)}),this.addEventListener("keyup",t=>{this._onKeyUp(t)})}_onKeyDown(t){switch(t.key){case"Enter":this._onEnter(t);break;case"Escape":this._onEscape(t);break}}_onKeyUp(t){}_onEnter(t){}_onEscape(t){}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const nt=new WeakMap;function qi(i){return nt.has(i)||nt.set(i,new Set),nt.get(i)}function Wi(i,e){const t=document.createElement("style");t.textContent=i,e===document?document.head.appendChild(t):e.insertBefore(t,e.firstChild)}const Ki=f(i=>class extends i{get slotStyles(){return[]}connectedCallback(){super.connectedCallback(),this.__applySlotStyles()}__applySlotStyles(){const t=this.getRootNode(),n=qi(t);this.slotStyles.forEach(s=>{n.has(s)||(Wi(s,t),n.add(s))})}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const X=i=>i.test(navigator.userAgent),mt=i=>i.test(navigator.platform),Gi=i=>i.test(navigator.vendor);X(/Android/u);X(/Chrome/u)&&Gi(/Google Inc/u);X(/Firefox/u);const Yi=mt(/^iPad/u)||mt(/^Mac/u)&&navigator.maxTouchPoints>1,Xi=mt(/^iPhone/u),Zi=Xi||Yi;X(/^((?!chrome|android).)*safari/iu);const Ji=(()=>{try{return document.createEvent("TouchEvent"),!0}catch{return!1}})();/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const we=f(i=>class extends i{static get properties(){return{inputElement:{type:Object,readOnly:!0,observer:"_inputElementChanged",sync:!0},type:{type:String,readOnly:!0},value:{type:String,value:"",observer:"_valueChanged",notify:!0,sync:!0}}}constructor(){super(),this._boundOnInput=this._onInput.bind(this),this._boundOnChange=this._onChange.bind(this)}get _hasValue(){return this.value!=null&&this.value!==""}get _inputElementValueProperty(){return"value"}get _inputElementValue(){return this.inputElement?this.inputElement[this._inputElementValueProperty]:void 0}set _inputElementValue(t){this.inputElement&&(this.inputElement[this._inputElementValueProperty]=t)}clear(){this.value="",this._inputElementValue=""}_addInputListeners(t){t.addEventListener("input",this._boundOnInput),t.addEventListener("change",this._boundOnChange)}_removeInputListeners(t){t.removeEventListener("input",this._boundOnInput),t.removeEventListener("change",this._boundOnChange)}_forwardInputValue(t){this.inputElement&&(this._inputElementValue=t??"")}_inputElementChanged(t,n){t?this._addInputListeners(t):n&&this._removeInputListeners(n)}_onInput(t){const n=t.composedPath()[0];this.__userInput=t.isTrusted,this.value=n.value,this.__userInput=!1}_onChange(t){}_toggleHasValue(t){this.toggleAttribute("has-value",t)}_valueChanged(t,n){this._toggleHasValue(this._hasValue),!(t===""&&n===void 0)&&(this.__userInput||this._forwardInputValue(t))}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Qi=i=>class extends we(kt(i)){static get properties(){return{clearButtonVisible:{type:Boolean,reflectToAttribute:!0,value:!1}}}get clearElement(){return console.warn(`Please implement the 'clearElement' property in <${this.localName}>`),null}ready(){super.ready(),this.clearElement&&(this.clearElement.addEventListener("mousedown",t=>this._onClearButtonMouseDown(t)),this.clearElement.addEventListener("click",t=>this._onClearButtonClick(t)))}_onClearButtonClick(t){t.preventDefault(),this._onClearAction()}_onClearButtonMouseDown(t){this._shouldKeepFocusOnClearMousedown()&&t.preventDefault(),Ji||this.inputElement.focus()}_onEscape(t){super._onEscape(t),this.clearButtonVisible&&this.value&&!this.readonly&&(t.stopPropagation(),this._onClearAction())}_onClearAction(){this._inputElementValue="",this.inputElement.dispatchEvent(new Event("input",{bubbles:!0,composed:!0})),this.inputElement.dispatchEvent(new Event("change",{bubbles:!0}))}_shouldKeepFocusOnClearMousedown(){return _e(this.inputElement)}};/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const st=new Map;function Tt(i){return st.has(i)||st.set(i,new WeakMap),st.get(i)}function xe(i,e){i&&i.removeAttribute(e)}function Ce(i,e){if(!i||!e)return;const t=Tt(e);if(t.has(i))return;const n=Ct(i.getAttribute(e));t.set(i,new Set(n))}function tn(i,e){if(!i||!e)return;const t=Tt(e),n=t.get(i);!n||n.size===0?i.removeAttribute(e):Et(i,e,K(n)),t.delete(i)}function ot(i,e,t={newId:null,oldId:null,fromUser:!1}){if(!i||!e)return;const{newId:n,oldId:s,fromUser:o}=t,r=Tt(e),a=r.get(i);if(!o&&a){s&&a.delete(s),n&&a.add(n);return}o&&(a?n||r.delete(i):Ce(i,e),xe(i,e)),ce(i,e,s);const l=n||K(a);l&&Et(i,e,l)}function en(i,e){Ce(i,e),xe(i,e)}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class nn{constructor(e){this.host=e,this.__required=!1}setTarget(e){this.__target=e,this.__setAriaRequiredAttribute(this.__required),this.__setLabelIdToAriaAttribute(this.__labelId,this.__labelId),this.__labelIdFromUser!=null&&this.__setLabelIdToAriaAttribute(this.__labelIdFromUser,this.__labelIdFromUser,!0),this.__setErrorIdToAriaAttribute(this.__errorId),this.__setHelperIdToAriaAttribute(this.__helperId),this.setAriaLabel(this.__label)}setRequired(e){this.__setAriaRequiredAttribute(e),this.__required=e}setAriaLabel(e){this.__setAriaLabelToAttribute(e),this.__label=e}setLabelId(e,t=!1){const n=t?this.__labelIdFromUser:this.__labelId;this.__setLabelIdToAriaAttribute(e,n,t),t?this.__labelIdFromUser=e:this.__labelId=e}setErrorId(e){this.__setErrorIdToAriaAttribute(e,this.__errorId),this.__errorId=e}setHelperId(e){this.__setHelperIdToAriaAttribute(e,this.__helperId),this.__helperId=e}__setAriaLabelToAttribute(e){this.__target&&(e?(en(this.__target,"aria-labelledby"),this.__target.setAttribute("aria-label",e)):this.__label&&(tn(this.__target,"aria-labelledby"),this.__target.removeAttribute("aria-label")))}__setLabelIdToAriaAttribute(e,t,n){ot(this.__target,"aria-labelledby",{newId:e,oldId:t,fromUser:n})}__setErrorIdToAriaAttribute(e,t){ot(this.__target,"aria-describedby",{newId:e,oldId:t,fromUser:!1})}__setHelperIdToAriaAttribute(e,t){ot(this.__target,"aria-describedby",{newId:e,oldId:t,fromUser:!1})}__setAriaRequiredAttribute(e){this.__target&&(["input","textarea"].includes(this.__target.localName)||(e?this.__target.setAttribute("aria-required","true"):this.__target.removeAttribute("aria-required")))}}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const p=document.createElement("div");p.style.position="fixed";p.style.clip="rect(0px, 0px, 0px, 0px)";p.setAttribute("aria-live","polite");document.body.appendChild(p);let z;function sn(i,e={}){const t=e.mode||"polite",n=e.timeout===void 0?150:e.timeout;t==="alert"?(p.removeAttribute("aria-live"),p.removeAttribute("role"),z=C.debounce(z,ii,()=>{p.setAttribute("role","alert")})):(z&&z.cancel(),p.removeAttribute("role"),p.setAttribute("aria-live",t)),p.textContent="",setTimeout(()=>{p.textContent=i},n)}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class St extends G{constructor(e,t,n,s={}){super(e,t,n,{...s,useUniqueId:!0})}initCustomNode(e){this.__updateNodeId(e),this.__notifyChange(e)}teardownNode(e){const t=this.getSlotChild();t&&t!==this.defaultNode?this.__notifyChange(t):(this.restoreDefaultNode(),this.updateDefaultNode(this.node))}attachDefaultNode(){const e=super.attachDefaultNode();return e&&this.__updateNodeId(e),e}restoreDefaultNode(){}updateDefaultNode(e){this.__notifyChange(e)}observeNode(e){this.__nodeObserver&&this.__nodeObserver.disconnect(),this.__nodeObserver=new MutationObserver(t=>{t.forEach(n=>{const s=n.target,o=s===this.node;n.type==="attributes"?o&&this.__updateNodeId(s):(o||s.parentElement===this.node)&&this.__notifyChange(this.node)})}),this.__nodeObserver.observe(e,{attributes:!0,attributeFilter:["id"],childList:!0,subtree:!0,characterData:!0})}__hasContent(e){return e?e.nodeType===Node.ELEMENT_NODE&&(customElements.get(e.localName)||e.children.length>0)||e.textContent&&e.textContent.trim()!=="":!1}__notifyChange(e){this.dispatchEvent(new CustomEvent("slot-content-changed",{detail:{hasContent:this.__hasContent(e),node:e}}))}__updateNodeId(e){const t=!this.nodes||e===this.nodes[0];e.nodeType===Node.ELEMENT_NODE&&(!this.multiple||t)&&!e.id&&(e.id=this.defaultId)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class on extends St{constructor(e){super(e,"error-message","div")}setErrorMessage(e){this.errorMessage=e,this.updateDefaultNode(this.node)}setInvalid(e){this.invalid=e,this.updateDefaultNode(this.node)}initAddedNode(e){e!==this.defaultNode&&this.initCustomNode(e)}initNode(e){this.updateDefaultNode(e)}initCustomNode(e){e.textContent&&!this.errorMessage&&(this.errorMessage=e.textContent.trim()),super.initCustomNode(e)}restoreDefaultNode(){this.attachDefaultNode()}updateDefaultNode(e){const{errorMessage:t,invalid:n}=this,s=!!(n&&t&&t.trim()!=="");e&&(e.textContent=s?t:"",e.hidden=!s,s&&sn(t,{mode:"assertive"})),super.updateDefaultNode(e)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class rn extends St{constructor(e){super(e,"helper",null)}setHelperText(e){this.helperText=e,this.getSlotChild()||this.restoreDefaultNode(),this.node===this.defaultNode&&this.updateDefaultNode(this.node)}restoreDefaultNode(){const{helperText:e}=this;if(e&&e.trim()!==""){this.tagName="div";const t=this.attachDefaultNode();this.observeNode(t)}}updateDefaultNode(e){e&&(e.textContent=this.helperText),super.updateDefaultNode(e)}initCustomNode(e){super.initCustomNode(e),this.observeNode(e)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class an extends St{constructor(e){super(e,"label","label")}setLabel(e){this.label=e,this.getSlotChild()||this.restoreDefaultNode(),this.node===this.defaultNode&&this.updateDefaultNode(this.node)}restoreDefaultNode(){const{label:e}=this;if(e&&e.trim()!==""){const t=this.attachDefaultNode();this.observeNode(t)}}updateDefaultNode(e){e&&(e.textContent=this.label),super.updateDefaultNode(e)}initCustomNode(e){super.initCustomNode(e),this.observeNode(e)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ln=f(i=>class extends i{static get properties(){return{label:{type:String,observer:"_labelChanged"}}}constructor(){super(),this._labelController=new an(this),this._labelController.addEventListener("slot-content-changed",t=>{this.toggleAttribute("has-label",t.detail.hasContent)})}get _labelId(){const t=this._labelNode;return t&&t.id}get _labelNode(){return this._labelController.node}ready(){super.ready(),this.addController(this._labelController)}_labelChanged(t){this._labelController.setLabel(t)}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ee=f(i=>class extends i{static get properties(){return{invalid:{type:Boolean,reflectToAttribute:!0,notify:!0,value:!1,sync:!0},manualValidation:{type:Boolean,value:!1},required:{type:Boolean,reflectToAttribute:!0,sync:!0}}}validate(){const t=this.checkValidity();return this._setInvalid(!t),this.dispatchEvent(new CustomEvent("validated",{detail:{valid:t}})),t}checkValidity(){return!this.required||!!this.value}_setInvalid(t){this._shouldSetInvalid(t)&&(this.invalid=t)}_shouldSetInvalid(t){return!0}_requestValidation(){this.manualValidation||this.validate()}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const dn=i=>class extends Ee(ln(i)){static get properties(){return{ariaTarget:{type:Object,observer:"_ariaTargetChanged"},errorMessage:{type:String,observer:"_errorMessageChanged"},helperText:{type:String,observer:"_helperTextChanged"},accessibleName:{type:String,observer:"_accessibleNameChanged"},accessibleNameRef:{type:String,observer:"_accessibleNameRefChanged"}}}static get observers(){return["_invalidChanged(invalid)","_requiredChanged(required)"]}constructor(){super(),this._fieldAriaController=new nn(this),this._helperController=new rn(this),this._errorController=new on(this),this._errorController.addEventListener("slot-content-changed",t=>{this.toggleAttribute("has-error-message",t.detail.hasContent)}),this._labelController.addEventListener("slot-content-changed",t=>{const{hasContent:n,node:s}=t.detail;this.__labelChanged(n,s)}),this._helperController.addEventListener("slot-content-changed",t=>{const{hasContent:n,node:s}=t.detail;this.toggleAttribute("has-helper",n),this.__helperChanged(n,s)})}get _errorNode(){return this._errorController.node}get _helperNode(){return this._helperController.node}ready(){super.ready(),this.addController(this._fieldAriaController),this.addController(this._helperController),this.addController(this._errorController)}__helperChanged(t,n){t?this._fieldAriaController.setHelperId(n.id):this._fieldAriaController.setHelperId(null)}_accessibleNameChanged(t){this._fieldAriaController.setAriaLabel(t)}_accessibleNameRefChanged(t){this._fieldAriaController.setLabelId(t,!0)}__labelChanged(t,n){t?this._fieldAriaController.setLabelId(n.id):this._fieldAriaController.setLabelId(null)}_errorMessageChanged(t){this._errorController.setErrorMessage(t)}_helperTextChanged(t){this._helperController.setHelperText(t)}_ariaTargetChanged(t){t&&this._fieldAriaController.setTarget(t)}_requiredChanged(t){this._fieldAriaController.setRequired(t)}_invalidChanged(t){this._errorController.setInvalid(t),setTimeout(()=>{if(t){const n=this._errorNode;this._fieldAriaController.setErrorId(n&&n.id)}else this._fieldAriaController.setErrorId(null)})}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const un=f(i=>class extends i{static get properties(){return{stateTarget:{type:Object,observer:"_stateTargetChanged"}}}static get delegateAttrs(){return[]}static get delegateProps(){return[]}ready(){super.ready(),this._createDelegateAttrsObserver(),this._createDelegatePropsObserver()}_stateTargetChanged(t){t&&(this._ensureAttrsDelegated(),this._ensurePropsDelegated())}_createDelegateAttrsObserver(){this._createMethodObserver(`_delegateAttrsChanged(${this.constructor.delegateAttrs.join(", ")})`)}_createDelegatePropsObserver(){this._createMethodObserver(`_delegatePropsChanged(${this.constructor.delegateProps.join(", ")})`)}_ensureAttrsDelegated(){this.constructor.delegateAttrs.forEach(t=>{this._delegateAttribute(t,this[t])})}_ensurePropsDelegated(){this.constructor.delegateProps.forEach(t=>{this._delegateProperty(t,this[t])})}_delegateAttrsChanged(...t){this.constructor.delegateAttrs.forEach((n,s)=>{this._delegateAttribute(n,t[s])})}_delegatePropsChanged(...t){this.constructor.delegateProps.forEach((n,s)=>{this._delegateProperty(n,t[s])})}_delegateAttribute(t,n){this.stateTarget&&(t==="invalid"&&this._delegateAttribute("aria-invalid",n?"true":!1),typeof n=="boolean"?this.stateTarget.toggleAttribute(t,n):n?this.stateTarget.setAttribute(t,n):this.stateTarget.removeAttribute(t))}_delegateProperty(t,n){this.stateTarget&&(this.stateTarget[t]=n)}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const cn=f(i=>class extends un(Ee(we(i))){static get constraints(){return["required"]}static get delegateAttrs(){return[...super.delegateAttrs,"required"]}ready(){super.ready(),this._createConstraintsObserver()}checkValidity(){return this.inputElement&&this._hasValidConstraints(this.constructor.constraints.map(t=>this[t]))?this.inputElement.checkValidity():!this.invalid}_hasValidConstraints(t){return t.some(n=>this.__isValidConstraint(n))}_createConstraintsObserver(){this._createMethodObserver(`_constraintsChanged(stateTarget, ${this.constructor.constraints.join(", ")})`)}_constraintsChanged(t,...n){if(!t)return;const s=this._hasValidConstraints(n),o=this.__previousHasConstraints&&!s;(this._hasValue||this.invalid)&&s?this._requestValidation():o&&!this.manualValidation&&this._setInvalid(!1),this.__previousHasConstraints=s}_onChange(t){t.stopPropagation(),this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{detail:{sourceEvent:t},bubbles:t.bubbles,cancelable:t.cancelable}))}__isValidConstraint(t){return!!t||t===0}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const hn=i=>class extends Ki(Ui(cn(dn(Qi(kt(i)))))){static get properties(){return{allowedCharPattern:{type:String,observer:"_allowedCharPatternChanged"},autoselect:{type:Boolean,value:!1},name:{type:String,reflectToAttribute:!0},placeholder:{type:String,reflectToAttribute:!0},readonly:{type:Boolean,value:!1,reflectToAttribute:!0},title:{type:String,reflectToAttribute:!0}}}static get delegateAttrs(){return[...super.delegateAttrs,"name","type","placeholder","readonly","invalid","title"]}constructor(){super(),this._boundOnPaste=this._onPaste.bind(this),this._boundOnDrop=this._onDrop.bind(this),this._boundOnBeforeInput=this._onBeforeInput.bind(this)}get slotStyles(){const t=this.localName;return[`
          /* Needed for Safari, where ::slotted(...)::placeholder does not work */
          ${t} > :is(input[slot='input'], textarea[slot='textarea'])::placeholder {
            font: inherit;
            color: inherit;
          }

          /* Override built-in autofill styles */
          ${t} > input[slot='input']:autofill {
            -webkit-text-fill-color: var(--vaadin-input-field-autofill-color, black) !important;
            background-clip: text !important;
          }

          ${t}:has(> input[slot='input']:autofill)::part(input-field) {
            --vaadin-input-field-background: var(--vaadin-input-field-autofill-background, lightyellow) !important;
            --vaadin-input-field-value-color: var(--vaadin-input-field-autofill-color, black) !important;
            --vaadin-input-field-button-text-color: var(--vaadin-input-field-autofill-color, black) !important;
          }
        `]}_onFocus(t){super._onFocus(t),this.autoselect&&this.inputElement&&this.inputElement.select()}_addInputListeners(t){super._addInputListeners(t),t.addEventListener("paste",this._boundOnPaste),t.addEventListener("drop",this._boundOnDrop),t.addEventListener("beforeinput",this._boundOnBeforeInput)}_removeInputListeners(t){super._removeInputListeners(t),t.removeEventListener("paste",this._boundOnPaste),t.removeEventListener("drop",this._boundOnDrop),t.removeEventListener("beforeinput",this._boundOnBeforeInput)}_onKeyDown(t){super._onKeyDown(t),this.allowedCharPattern&&!this.__shouldAcceptKey(t)&&t.target===this.inputElement&&(t.preventDefault(),this._markInputPrevented())}_markInputPrevented(){this.setAttribute("input-prevented",""),this._preventInputDebouncer=C.debounce(this._preventInputDebouncer,ei.after(200),()=>{this.removeAttribute("input-prevented")})}__shouldAcceptKey(t){return t.metaKey||t.ctrlKey||!t.key||t.key.length!==1||this.__allowedCharRegExp.test(t.key)}_onPaste(t){if(this.allowedCharPattern){const n=t.clipboardData.getData("text");this.__allowedTextRegExp.test(n)||(t.preventDefault(),this._markInputPrevented())}}_onDrop(t){if(this.allowedCharPattern){const n=t.dataTransfer.getData("text");this.__allowedTextRegExp.test(n)||(t.preventDefault(),this._markInputPrevented())}}_onBeforeInput(t){this.allowedCharPattern&&t.data&&!this.__allowedTextRegExp.test(t.data)&&(t.preventDefault(),this._markInputPrevented())}_allowedCharPatternChanged(t){if(t)try{this.__allowedCharRegExp=new RegExp(`^${t}$`,"u"),this.__allowedTextRegExp=new RegExp(`^${t}*$`,"u")}catch(n){console.error(n)}}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const pn=i=>class extends hn(i){static get properties(){return{autocomplete:{type:String},autocorrect:{type:String,reflectToAttribute:!0},autocapitalize:{type:String,reflectToAttribute:!0}}}static get delegateAttrs(){return[...super.delegateAttrs,"autocapitalize","autocomplete","autocorrect"]}_inputElementChanged(t){super._inputElementChanged(t),t&&(t.value&&t.value!==this.value&&(console.warn(`Please define value on the <${this.localName}> component!`),t.value=""),this.value&&(t.value=this.value))}_setFocused(t){super._setFocused(t),!t&&document.hasFocus()&&this._requestValidation()}_onInput(t){super._onInput(t),this.invalid&&this._requestValidation()}_valueChanged(t,n){super._valueChanged(t,n),n!==void 0&&this.invalid&&this._requestValidation()}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class fn{constructor(e,t){this.input=e,this.__preventDuplicateLabelClick=this.__preventDuplicateLabelClick.bind(this),t.addEventListener("slot-content-changed",n=>{this.__initLabel(n.detail.node)}),this.__initLabel(t.node)}__initLabel(e){e&&(e.addEventListener("click",this.__preventDuplicateLabelClick),this.input&&e.setAttribute("for",this.input.id))}__preventDuplicateLabelClick(){const e=t=>{t.stopImmediatePropagation(),this.input.removeEventListener("click",e)};this.input.addEventListener("click",e)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const vn=i=>class extends pn(i){static get properties(){return{maxlength:{type:Number},minlength:{type:Number},pattern:{type:String}}}static get delegateAttrs(){return[...super.delegateAttrs,"maxlength","minlength","pattern"]}static get constraints(){return[...super.constraints,"maxlength","minlength","pattern"]}constructor(){super(),this._setType("text")}get clearElement(){return this.$.clearButton}ready(){super.ready(),this.addController(new Ri(this,t=>{this._setInputElement(t),this._setFocusElement(t),this.stateTarget=t,this.ariaTarget=t})),this.addController(new fn(this.inputElement,this._labelController))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class _n extends vn(N($(k(L(E))))){static get is(){return"vaadin-text-field"}static get styles(){return[Fi]}render(){return y`
      <div class="vaadin-field-container">
        <div part="label">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true" @click="${this.focus}"></span>
        </div>

        <vaadin-input-container
          part="input-field"
          .readonly="${this.readonly}"
          .disabled="${this.disabled}"
          .invalid="${this.invalid}"
          theme="${ue(this._theme)}"
        >
          <slot name="prefix" slot="prefix"></slot>
          <slot name="input"></slot>
          ${this._renderSuffix()}
        </vaadin-input-container>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>
        <slot name="tooltip"></slot>
      </div>
    `}ready(){super.ready(),this._tooltipController=new fe(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}_renderSuffix(){return y`
      <slot name="suffix" slot="suffix"></slot>
      <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
    `}}A(_n);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const gn=h`
  :host {
    z-index: 200;
    position: fixed;

    /* Despite of what the names say, <vaadin-overlay> is just a container
          for position/sizing/alignment. The actual overlay is the overlay part. */

    /* Default position constraints. Themes can
          override this to adjust the gap between the overlay and the viewport. */
    inset: max(env(safe-area-inset-top, 0px), var(--vaadin-overlay-viewport-inset, 8px))
      max(env(safe-area-inset-right, 0px), var(--vaadin-overlay-viewport-inset, 8px))
      max(env(safe-area-inset-bottom, 0px), var(--vaadin-overlay-viewport-bottom))
      max(env(safe-area-inset-left, 0px), var(--vaadin-overlay-viewport-inset, 8px));

    /* Override native [popover] user agent styles */
    width: auto;
    height: auto;
    border: none;
    padding: 0;
    background-color: transparent;
    overflow: visible;

    /* Use flexbox alignment for the overlay part. */
    display: flex;
    flex-direction: column; /* makes dropdowns sizing easier */
    /* Align to center by default. */
    align-items: center;
    justify-content: center;

    /* Allow centering when max-width/max-height applies. */
    margin: auto;

    /* The host is not clickable, only the overlay part is. */
    pointer-events: none;

    /* Remove tap highlight on touch devices. */
    -webkit-tap-highlight-color: transparent;

    /* CSS API for host */
    --vaadin-overlay-viewport-bottom: 8px;
  }

  :host([hidden]),
  :host(:not([opened]):not([closing])),
  :host(:not([opened]):not([closing])) [part='overlay'] {
    display: none !important;
  }

  [part='overlay'] {
    background: var(--vaadin-overlay-background, var(--vaadin-background-color));
    border: var(--vaadin-overlay-border-width, 1px) solid
      var(--vaadin-overlay-border-color, var(--vaadin-border-color-secondary));
    border-radius: var(--vaadin-overlay-border-radius, var(--vaadin-radius-m));
    box-shadow: var(--vaadin-overlay-shadow, 0 8px 24px -4px rgba(0, 0, 0, 0.3));
    box-sizing: border-box;
    max-width: 100%;
    overflow: auto;
    overscroll-behavior: contain;
    pointer-events: auto;
    -webkit-tap-highlight-color: initial;

    /* CSS reset for font styles */
    color: initial;
    font: initial;
    letter-spacing: initial;
    text-align: initial;
    text-decoration: initial;
    text-indent: initial;
    text-transform: initial;
    user-select: text;
    white-space: initial;
    word-spacing: initial;

    /* Inherit font-family */
    font-family: inherit;
  }

  [part='backdrop'] {
    background: var(--vaadin-overlay-backdrop-background, rgba(0, 0, 0, 0.2));
    content: '';
    inset: 0;
    pointer-events: auto;
    position: fixed;
    z-index: -1;
  }

  [part='overlay']:focus-visible {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
  }

  @media (forced-colors: active) {
    [part='overlay'] {
      border: 3px solid !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class mn{saveFocus(e){this.focusNode=e||_t()}restoreFocus(e){const t=this.focusNode;if(!t)return;const n={preventScroll:e?e.preventScroll:!1,focusVisible:e?e.focusVisible:!1};_t()===document.body?setTimeout(()=>t.focus(n)):t.focus(n),this.focusNode=null}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const rt=[];class bn{constructor(e){this.host=e,this.__trapNode=null,this.__onKeyDown=this.__onKeyDown.bind(this)}get __focusableElements(){return Hi(this.__trapNode)}get __focusedElementIndex(){const e=this.__focusableElements;return e.indexOf(e.filter(_e).pop())}hostConnected(){document.addEventListener("keydown",this.__onKeyDown)}hostDisconnected(){document.removeEventListener("keydown",this.__onKeyDown)}trapFocus(e){if(this.__trapNode=e,this.__focusableElements.length===0)throw this.__trapNode=null,new Error("The trap node should have at least one focusable descendant or be focusable itself.");rt.push(this),this.__focusedElementIndex===-1&&this.__focusableElements[0].focus({focusVisible:Y()})}releaseFocus(){this.__trapNode=null,rt.pop()}__onKeyDown(e){if(this.__trapNode&&this===Array.from(rt).pop()&&e.key==="Tab"){e.preventDefault();const t=e.shiftKey;this.__focusNextElement(t)}}__focusNextElement(e=!1){const t=this.__focusableElements,n=e?-1:1,s=this.__focusedElementIndex,o=(t.length+s+n)%t.length,r=t[o];r.focus({focusVisible:!0}),r.localName==="input"&&r.select()}}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const yn=i=>class extends i{static get properties(){return{focusTrap:{type:Boolean,value:!1},restoreFocusOnClose:{type:Boolean,value:!1},restoreFocusNode:{type:HTMLElement}}}constructor(){super(),this.__focusTrapController=new bn(this),this.__focusRestorationController=new mn}get _contentRoot(){return this}ready(){super.ready(),this.addController(this.__focusTrapController),this.addController(this.__focusRestorationController)}get _focusTrapRoot(){return this.$.overlay}_resetFocus(){if(this.focusTrap&&this.__focusTrapController.releaseFocus(),this.restoreFocusOnClose&&this._shouldRestoreFocus()){const t=Y(),n=!t;this.__focusRestorationController.restoreFocus({preventScroll:n,focusVisible:t})}}_saveFocus(){this.restoreFocusOnClose&&this.__focusRestorationController.saveFocus(this.restoreFocusNode)}_trapFocus(){this.focusTrap&&!$i(this._focusTrapRoot)&&this.__focusTrapController.trapFocus(this._focusTrapRoot)}_shouldRestoreFocus(){const t=_t();return t===document.body||this._deepContains(t)}_deepContains(t){if(this._contentRoot.contains(t))return!0;let n=t;const s=t.ownerDocument;for(;n&&n!==s&&n!==this._contentRoot;)n=n.parentNode||n.host;return n===this._contentRoot}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const U=new Set,q=()=>[...U].filter(i=>!i.hasAttribute("closing")),Ae=i=>{const e=q(),t=e[e.indexOf(i)+1];return t?i._deepContains(t)?Ae(t):!1:!0},qt=(i,e=t=>!0)=>{const t=q().filter(e);return i===t.pop()},wn=i=>class extends i{get _last(){return qt(this)}get _isAttached(){return U.has(this)}bringToFront(){qt(this)||Ae(this)||(this.matches(":popover-open")&&(this.hidePopover(),this.showPopover()),this._removeAttachedInstance(),this._appendAttachedInstance())}_enterModalState(){document.body.style.pointerEvents!=="none"&&(this._previousDocumentPointerEvents=document.body.style.pointerEvents,document.body.style.pointerEvents="none"),q().forEach(t=>{t!==this&&(t.$.overlay.style.pointerEvents="none")})}_exitModalState(){this._previousDocumentPointerEvents!==void 0&&(document.body.style.pointerEvents=this._previousDocumentPointerEvents,delete this._previousDocumentPointerEvents);const t=q();let n;for(;(n=t.pop())&&!(n!==this&&(n.$.overlay.style.removeProperty("pointer-events"),!n.modeless)););}_appendAttachedInstance(){U.add(this)}_removeAttachedInstance(){this._isAttached&&U.delete(this)}};/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function xn(i,e){let t=null,n;const s=document.documentElement;function o(){n&&clearTimeout(n),t&&t.disconnect(),t=null}function r(a=!1,l=1){o();const{left:d,top:c,width:m,height:D}=i.getBoundingClientRect();if(a||e(),!m||!D)return;const P=Math.floor(c),Le=Math.floor(s.clientWidth-(d+m)),Ne=Math.floor(s.clientHeight-(c+D)),De=Math.floor(d),Pe={rootMargin:`${-P}px ${-Le}px ${-Ne}px ${-De}px`,threshold:Math.max(0,Math.min(1,l))||1};let Nt=!0;function Fe(Re){const Z=Re[0].intersectionRatio;if(Z!==l){if(!Nt)return r();Z?r(!1,Z):n=setTimeout(()=>{r(!1,1e-7)},1e3)}Nt=!1}t=new IntersectionObserver(Fe,Pe),t.observe(i)}return r(!0),o}function u(i,e,t){const n=[i];i.owner&&n.push(i.owner),typeof t=="string"?n.forEach(s=>{s.setAttribute(e,t)}):t?n.forEach(s=>{s.setAttribute(e,"")}):n.forEach(s=>{s.removeAttribute(e)})}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Cn=i=>class extends yn(wn(i)){static get properties(){return{opened:{type:Boolean,notify:!0,observer:"_openedChanged",reflectToAttribute:!0,sync:!0},owner:{type:Object,sync:!0},model:{type:Object,sync:!0},renderer:{type:Object,sync:!0},modeless:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_modelessChanged",sync:!0},hidden:{type:Boolean,reflectToAttribute:!0,observer:"_hiddenChanged",sync:!0},withBackdrop:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_withBackdropChanged",sync:!0}}}static get observers(){return["_rendererOrDataChanged(renderer, owner, model, opened)"]}get _rendererRoot(){return this}constructor(){super(),this._boundMouseDownListener=this._mouseDownListener.bind(this),this._boundMouseUpListener=this._mouseUpListener.bind(this),this._boundOutsideClickListener=this._outsideClickListener.bind(this),this._boundKeydownListener=this._keydownListener.bind(this),Zi&&(this._boundIosResizeListener=()=>this._detectIosNavbar())}firstUpdated(){super.firstUpdated(),this.popover="manual",this.addEventListener("click",()=>{}),this.$.backdrop&&this.$.backdrop.addEventListener("click",()=>{}),this.addEventListener("mouseup",()=>{document.activeElement===document.body&&this.$.overlay.getAttribute("tabindex")==="0"&&this.$.overlay.focus()}),this.addEventListener("animationcancel",()=>{this._flushAnimation("opening"),this._flushAnimation("closing")})}connectedCallback(){super.connectedCallback(),this._boundIosResizeListener&&(this._detectIosNavbar(),window.addEventListener("resize",this._boundIosResizeListener))}disconnectedCallback(){super.disconnectedCallback(),this.__scheduledOpen&&(cancelAnimationFrame(this.__scheduledOpen),this.__scheduledOpen=null),this._boundIosResizeListener&&window.removeEventListener("resize",this._boundIosResizeListener)}requestContentUpdate(){this.renderer&&this.renderer.call(this.owner,this._rendererRoot,this.owner,this.model)}close(t){const n=new CustomEvent("vaadin-overlay-close",{bubbles:!0,cancelable:!0,detail:{overlay:this,sourceEvent:t}});this.dispatchEvent(n),document.body.dispatchEvent(n),n.defaultPrevented||(this.opened=!1)}setBounds(t,n=!0){const s=this.$.overlay,o={...t};n&&s.style.position!=="absolute"&&(s.style.position="absolute"),Object.keys(o).forEach(r=>{o[r]!==null&&!isNaN(o[r])&&(o[r]=`${o[r]}px`)}),Object.assign(s.style,o)}_detectIosNavbar(){if(!this.opened)return;const t=window.innerHeight,s=window.innerWidth>t,o=document.documentElement.clientHeight;s&&o>t?this.style.setProperty("--vaadin-overlay-viewport-bottom",`${o-t}px`):this.style.setProperty("--vaadin-overlay-viewport-bottom","0")}_shouldAddGlobalListeners(){return!this.modeless}_addGlobalListeners(){this.__hasGlobalListeners||(this.__hasGlobalListeners=!0,document.addEventListener("mousedown",this._boundMouseDownListener),document.addEventListener("mouseup",this._boundMouseUpListener),document.documentElement.addEventListener("click",this._boundOutsideClickListener,!0))}_removeGlobalListeners(){this.__hasGlobalListeners&&(this.__hasGlobalListeners=!1,document.removeEventListener("mousedown",this._boundMouseDownListener),document.removeEventListener("mouseup",this._boundMouseUpListener),document.documentElement.removeEventListener("click",this._boundOutsideClickListener,!0))}_rendererOrDataChanged(t,n,s,o){const r=this._oldOwner!==n||this._oldModel!==s;this._oldModel=s,this._oldOwner=n;const a=this._oldRenderer!==t,l=this._oldRenderer!==void 0;this._oldRenderer=t;const d=this._oldOpened!==o;this._oldOpened=o,a&&l&&(this._rendererRoot.innerHTML="",delete this._rendererRoot._$litPart$),o&&t&&(a||d||r)&&this.requestContentUpdate()}_modelessChanged(t){this.opened&&(this._shouldAddGlobalListeners()?this._addGlobalListeners():this._removeGlobalListeners()),t?this._exitModalState():this.opened&&this._enterModalState(),u(this,"modeless",t)}_withBackdropChanged(t){u(this,"with-backdrop",t)}_openedChanged(t,n){if(t){if(!this.isConnected){this.opened=!1;return}this._saveFocus(),this._animatedOpening(),this.__scheduledOpen=requestAnimationFrame(()=>{setTimeout(()=>{this._trapFocus();const s=new CustomEvent("vaadin-overlay-open",{detail:{overlay:this},bubbles:!0});this.dispatchEvent(s),document.body.dispatchEvent(s)})}),document.addEventListener("keydown",this._boundKeydownListener),this._shouldAddGlobalListeners()&&this._addGlobalListeners()}else n&&(this.__scheduledOpen&&(cancelAnimationFrame(this.__scheduledOpen),this.__scheduledOpen=null),this._resetFocus(),this._animatedClosing(),document.removeEventListener("keydown",this._boundKeydownListener),this._shouldAddGlobalListeners()&&this._removeGlobalListeners())}_hiddenChanged(t){t&&this.hasAttribute("closing")&&this._flushAnimation("closing")}_shouldAnimate(){const t=getComputedStyle(this),n=t.getPropertyValue("animation-name");return!(t.getPropertyValue("display")==="none")&&n&&n!=="none"}_enqueueAnimation(t,n){const s=`__${t}Handler`,o=r=>{r&&r.target!==this||(n(),this.removeEventListener("animationend",o),delete this[s])};this[s]=o,this.addEventListener("animationend",o)}_flushAnimation(t){const n=`__${t}Handler`;typeof this[n]=="function"&&this[n]()}_animatedOpening(){this._isAttached&&this.hasAttribute("closing")&&this._flushAnimation("closing"),this._attachOverlay(),this._appendAttachedInstance(),this.bringToFront(),this.modeless||this._enterModalState(),u(this,"opening",!0),this._shouldAnimate()?this._enqueueAnimation("opening",()=>{this._finishOpening()}):this._finishOpening()}_attachOverlay(){this.showPopover()}_finishOpening(){u(this,"opening",!1)}_finishClosing(){this._detachOverlay(),this._removeAttachedInstance(),this.$.overlay.style.removeProperty("pointer-events"),u(this,"closing",!1),this.dispatchEvent(new CustomEvent("vaadin-overlay-closed"))}_animatedClosing(){this.hasAttribute("opening")&&this._flushAnimation("opening"),this._isAttached&&(this._exitModalState(),u(this,"closing",!0),this.dispatchEvent(new CustomEvent("vaadin-overlay-closing")),this._shouldAnimate()?this._enqueueAnimation("closing",()=>{this._finishClosing()}):this._finishClosing())}_detachOverlay(){this.hidePopover()}_mouseDownListener(t){this._mouseDownInside=t.composedPath().indexOf(this.$.overlay)>=0}_mouseUpListener(t){this._mouseUpInside=t.composedPath().indexOf(this.$.overlay)>=0}_shouldCloseOnOutsideClick(t){return this._last}_outsideClickListener(t){if(t.composedPath().includes(this.$.overlay)||this._mouseDownInside||this._mouseUpInside){this._mouseDownInside=!1,this._mouseUpInside=!1;return}if(!this._shouldCloseOnOutsideClick(t))return;const n=new CustomEvent("vaadin-overlay-outside-click",{cancelable:!0,detail:{sourceEvent:t}});this.dispatchEvent(n),this.opened&&!n.defaultPrevented&&this.close(t)}_keydownListener(t){if(!(!this._last||t.defaultPrevented)&&!(!this._shouldAddGlobalListeners()&&!t.composedPath().includes(this._focusTrapRoot))&&t.key==="Escape"){const n=new CustomEvent("vaadin-overlay-escape-press",{cancelable:!0,detail:{sourceEvent:t}});this.dispatchEvent(n),this.opened&&!n.defaultPrevented&&this.close(t)}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const at={start:"top",end:"bottom"},lt={start:"left",end:"right"},Wt=new ResizeObserver(i=>{setTimeout(()=>{i.forEach(e=>{e.target.__overlay&&e.target.__overlay._updatePosition()})})}),En=i=>class extends i{static get properties(){return{positionTarget:{type:Object,value:null,sync:!0},horizontalAlign:{type:String,value:"start",sync:!0},verticalAlign:{type:String,value:"top",sync:!0},noHorizontalOverlap:{type:Boolean,value:!1,sync:!0},noVerticalOverlap:{type:Boolean,value:!1,sync:!0},requiredVerticalSpace:{type:Number,value:0,sync:!0}}}constructor(){super(),this.__onScroll=this.__onScroll.bind(this),this._updatePosition=this._updatePosition.bind(this)}connectedCallback(){super.connectedCallback(),this.opened&&this.__addUpdatePositionEventListeners()}disconnectedCallback(){super.disconnectedCallback(),this.__removeUpdatePositionEventListeners()}updated(t){if(super.updated(t),t.has("positionTarget")){const s=t.get("positionTarget");(!this.positionTarget&&s||this.positionTarget&&!s&&this.__margins)&&this.__resetPosition()}(t.has("opened")||t.has("positionTarget"))&&this.__updatePositionSettings(this.opened,this.positionTarget),["horizontalAlign","verticalAlign","noHorizontalOverlap","noVerticalOverlap","requiredVerticalSpace"].some(s=>t.has(s))&&this._updatePosition()}__addUpdatePositionEventListeners(){window.visualViewport.addEventListener("resize",this._updatePosition),window.visualViewport.addEventListener("scroll",this.__onScroll,!0),this.__positionTargetAncestorRootNodes=Li(this.positionTarget),this.__positionTargetAncestorRootNodes.forEach(t=>{t.addEventListener("scroll",this.__onScroll,!0)}),this.positionTarget&&(this.__observePositionTargetMove=xn(this.positionTarget,()=>{this._updatePosition()}))}__removeUpdatePositionEventListeners(){window.visualViewport.removeEventListener("resize",this._updatePosition),window.visualViewport.removeEventListener("scroll",this.__onScroll,!0),this.__positionTargetAncestorRootNodes&&(this.__positionTargetAncestorRootNodes.forEach(t=>{t.removeEventListener("scroll",this.__onScroll,!0)}),this.__positionTargetAncestorRootNodes=null),this.__observePositionTargetMove&&(this.__observePositionTargetMove(),this.__observePositionTargetMove=null)}__updatePositionSettings(t,n){if(this.__removeUpdatePositionEventListeners(),n&&(n.__overlay=null,Wt.unobserve(n),t&&(this.__addUpdatePositionEventListeners(),n.__overlay=this,Wt.observe(n))),t){const s=getComputedStyle(this);this.__margins||(this.__margins={},["top","bottom","left","right"].forEach(o=>{this.__margins[o]=parseInt(s[o],10)})),this._updatePosition(),requestAnimationFrame(()=>this._updatePosition())}}__onScroll(t){t.target instanceof Node&&this._deepContains(t.target)||this._updatePosition()}__resetPosition(){this.__margins=null,Object.assign(this.style,{justifyContent:"",alignItems:"",top:"",bottom:"",left:"",right:""}),u(this,"bottom-aligned",!1),u(this,"top-aligned",!1),u(this,"end-aligned",!1),u(this,"start-aligned",!1)}_updatePosition(){if(!this.positionTarget||!this.opened||!this.__margins)return;const t=this.positionTarget.getBoundingClientRect();if(t.width===0&&t.height===0&&this.opened){this.opened=!1;return}const n=this.__shouldAlignStartVertically(t);this.style.justifyContent=n?"flex-start":"flex-end";const s=this.__isRTL,o=this.__shouldAlignStartHorizontally(t,s),r=!s&&o||s&&!o;this.style.alignItems=r?"flex-start":"flex-end";const a=this.getBoundingClientRect(),l=this.__calculatePositionInOneDimension(t,a,this.noVerticalOverlap,at,this,n),d=this.__calculatePositionInOneDimension(t,a,this.noHorizontalOverlap,lt,this,o);Object.assign(this.style,l,d),u(this,"bottom-aligned",!n),u(this,"top-aligned",n),u(this,"end-aligned",!r),u(this,"start-aligned",r)}__shouldAlignStartHorizontally(t,n){const s=Math.max(this.__oldContentWidth||0,this.$.overlay.offsetWidth);this.__oldContentWidth=this.$.overlay.offsetWidth;const o=Math.min(window.innerWidth,document.documentElement.clientWidth),r=!n&&this.horizontalAlign==="start"||n&&this.horizontalAlign==="end";return this.__shouldAlignStart(t,s,o,this.__margins,r,this.noHorizontalOverlap,lt)}__shouldAlignStartVertically(t){const n=this.requiredVerticalSpace||Math.max(this.__oldContentHeight||0,this.$.overlay.offsetHeight);this.__oldContentHeight=this.$.overlay.offsetHeight;const s=Math.min(window.innerHeight,document.documentElement.clientHeight),o=this.verticalAlign==="top";return this.__shouldAlignStart(t,n,s,this.__margins,o,this.noVerticalOverlap,at)}__shouldAlignStart(t,n,s,o,r,a,l){const d=s-t[a?l.end:l.start]-o[l.end],c=t[a?l.start:l.end]-o[l.start],m=r?d:c,P=m>(r?c:d)||m>n;return r===P}__adjustBottomProperty(t,n,s){let o;if(t===n.end){if(n.end===at.end){const r=Math.min(window.innerHeight,document.documentElement.clientHeight);if(s>r&&this.__oldViewportHeight){const a=this.__oldViewportHeight-r;o=s-a}this.__oldViewportHeight=r}if(n.end===lt.end){const r=Math.min(window.innerWidth,document.documentElement.clientWidth);if(s>r&&this.__oldViewportWidth){const a=this.__oldViewportWidth-r;o=s-a}this.__oldViewportWidth=r}}return o}__calculatePositionInOneDimension(t,n,s,o,r,a){const l=a?o.start:o.end,d=a?o.end:o.start,c=parseFloat(r.style[l]||getComputedStyle(r)[l]),m=this.__adjustBottomProperty(l,o,c),D=n[a?o.start:o.end]-t[s===a?o.end:o.start],P=m?`${m}px`:`${c+D*(a?-1:1)}px`;return{[l]:P,[d]:""}}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const An=i=>class extends En(Cn(i)){static get properties(){return{position:{type:String,reflectToAttribute:!0}}}_updatePosition(){if(super._updatePosition(),!this.positionTarget||!this.opened)return;this.removeAttribute("arrow-centered");const t=this.positionTarget.getBoundingClientRect(),n=this.$.overlay.getBoundingClientRect(),s=Math.min(window.innerWidth,document.documentElement.clientWidth);let o=!1;if(n.left<0?(this.style.left="0px",this.style.right="",o=!0):n.right>s&&(this.style.right="0px",this.style.left="",o=!0),!o&&(this.position==="bottom"||this.position==="top")){const r=t.width/2-n.width/2;if(this.style.left){const a=n.left+r;a>0&&(this.style.left=`${a}px`,this.setAttribute("arrow-centered",""))}if(this.style.right){const a=parseFloat(this.style.right)+r;a>0&&(this.style.right=`${a}px`,this.setAttribute("arrow-centered",""))}}if(this.position==="start"||this.position==="end"){const r=t.height/2-n.height/2;this.style.top=`${n.top+r}px`}}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const kn=h`
  :host {
    --_vaadin-tooltip-default-offset: 4px;
    line-height: normal;
  }

  [part='overlay'] {
    max-width: var(--vaadin-tooltip-max-width, 40ch);
    padding: var(
      --vaadin-tooltip-padding,
      var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container)
    );
    border: var(--vaadin-tooltip-border-width, var(--vaadin-overlay-border-width, 1px)) solid
      var(--vaadin-tooltip-border-color, var(--vaadin-overlay-border-color, var(--vaadin-border-color-secondary)));
    border-radius: var(--vaadin-tooltip-border-radius, var(--vaadin-radius-m));
    background: var(--vaadin-tooltip-background, var(--vaadin-background-color));
    color: var(--vaadin-tooltip-text-color, inherit);
    font-size: var(--vaadin-tooltip-font-size, 0.9em);
    font-weight: var(--vaadin-tooltip-font-weight, inherit);
    line-height: var(--vaadin-tooltip-line-height, inherit);
    box-shadow: var(--vaadin-tooltip-shadow, 0 3px 8px -1px rgba(0, 0, 0, 0.2));
  }

  :host(:not([markdown])) [part='content'] {
    white-space: pre-wrap;
  }

  :host([position^='top'][top-aligned]) [part='overlay'],
  :host([position^='bottom'][top-aligned]) [part='overlay'] {
    margin-top: var(--vaadin-tooltip-offset-top, var(--_vaadin-tooltip-default-offset));
  }

  :host([position^='top'][bottom-aligned]) [part='overlay'],
  :host([position^='bottom'][bottom-aligned]) [part='overlay'] {
    margin-bottom: var(--vaadin-tooltip-offset-bottom, var(--_vaadin-tooltip-default-offset));
  }

  :host([position^='start'][start-aligned]) [part='overlay'],
  :host([position^='end'][start-aligned]) [part='overlay'] {
    margin-inline-start: var(--vaadin-tooltip-offset-start, var(--_vaadin-tooltip-default-offset));
  }

  :host([position^='start'][end-aligned]) [part='overlay'],
  :host([position^='end'][end-aligned]) [part='overlay'] {
    margin-inline-end: var(--vaadin-tooltip-offset-end, var(--_vaadin-tooltip-default-offset));
  }

  @media (forced-colors: active) {
    [part='overlay'] {
      border: 1px dashed !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Tn extends An(wt(N(k(L(E))))){static get is(){return"vaadin-tooltip-overlay"}static get styles(){return[gn,kn]}render(){return y`
      <div part="overlay" id="overlay">
        <div part="content" id="content"><slot></slot></div>
      </div>
    `}}A(Tn);/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Sn=i=>class extends i{static get properties(){return{position:{type:String},_position:{type:String,value:"bottom"},__effectivePosition:{type:String,computed:"__computePosition(position, _position)"}}}__computeHorizontalAlign(t){return["top-end","bottom-end","start-top","start","start-bottom"].includes(t)?"end":"start"}__computeNoHorizontalOverlap(t){return["start-top","start","start-bottom","end-top","end","end-bottom"].includes(t)}__computeNoVerticalOverlap(t){return["top-start","top-end","top","bottom-start","bottom","bottom-end"].includes(t)}__computeVerticalAlign(t){return["top-start","top-end","top","start-bottom","end-bottom"].includes(t)?"bottom":"top"}__computePosition(t,n){return t||n}};/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Mn=i=>class extends i{static get properties(){return{for:{type:String,observer:"__forChanged"},target:{type:Object},__isConnected:{type:Boolean,sync:!0}}}static get observers(){return["__targetOrConnectedChanged(target, __isConnected)"]}connectedCallback(){super.connectedCallback(),this.__isConnected=!0}disconnectedCallback(){super.disconnectedCallback(),this.__isConnected=!1}__forChanged(t){t&&(this.__setTargetByIdDebouncer=C.debounce(this.__setTargetByIdDebouncer,ee,()=>this.__setTargetById(t)))}__setTargetById(t){if(!this.isConnected)return;const n=this.getRootNode().getElementById(t);n?this.target=n:console.warn(`No element with id="${t}" set via "for" property found on the page.`)}__targetOrConnectedChanged(t,n){this.__previousTarget&&(this.__previousTarget!==t||!n)&&this._removeTargetListeners(this.__previousTarget),t&&n&&this._addTargetListeners(t),this.__previousTarget=t}_addTargetListeners(t){}_removeTargetListeners(t){}},O=500;let ke=O,Te=O,Se=O;const T=new Set;let R=!1,S=null,V=null;class On{constructor(e){this.host=e}get focusDelay(){const e=this.host;return e.focusDelay!=null&&e.focusDelay>=0?e.focusDelay:ke}get hoverDelay(){const e=this.host;return e.hoverDelay!=null&&e.hoverDelay>=0?e.hoverDelay:Te}get hideDelay(){const e=this.host;return e.hideDelay!=null&&e.hideDelay>=0?e.hideDelay:Se}get isClosing(){return T.has(this.host)}open(e={immediate:!1}){const{immediate:t,hover:n,focus:s}=e,o=n&&this.hoverDelay>0,r=s&&this.focusDelay>0;!t&&(o||r)&&!this.__closeTimeout?this.__warmupTooltip(r):this.__showTooltip()}close(e){!e&&this.hideDelay>0?this.__scheduleClose():(this.__abortClose(),this._setOpened(!1)),this.__abortWarmUp(),R&&(this.__abortCooldown(),this.__scheduleCooldown())}_isOpened(){return this.host.opened}_setOpened(e){this.host.opened=e}__flushClosingTooltips(){T.forEach(e=>{e._stateController.close(!0),T.delete(e)})}__showTooltip(){this.__abortClose(),this.__flushClosingTooltips(),this._setOpened(!0),R=!0,this.__abortWarmUp(),this.__abortCooldown()}__warmupTooltip(e){this._isOpened()||(R?this.__showTooltip():S==null&&this.__scheduleWarmUp(e))}__abortClose(){this.__closeTimeout&&(clearTimeout(this.__closeTimeout),this.__closeTimeout=null),this.isClosing&&T.delete(this.host)}__abortCooldown(){V&&(clearTimeout(V),V=null)}__abortWarmUp(){S&&(clearTimeout(S),S=null)}__scheduleClose(){this._isOpened()&&!this.isClosing&&(T.add(this.host),this.__closeTimeout=setTimeout(()=>{T.delete(this.host),this.__closeTimeout=null,this._setOpened(!1)},this.hideDelay))}__scheduleCooldown(){V=setTimeout(()=>{V=null,R=!1},this.hideDelay)}__scheduleWarmUp(e){const t=e?this.focusDelay:this.hoverDelay;S=setTimeout(()=>{S=null,R=!0,this.__showTooltip()},t)}}const In=i=>class extends Sn(Mn(i)){static get properties(){return{ariaTarget:{type:Object},context:{type:Object,value:()=>({})},focusDelay:{type:Number},generator:{type:Object},hideDelay:{type:Number},hoverDelay:{type:Number},manual:{type:Boolean,value:!1,sync:!0},opened:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"__openedChanged",sync:!0},shouldShow:{type:Object,value:()=>(t,n)=>!0},text:{type:String},markdown:{type:Boolean,value:!1,reflectToAttribute:!0},_effectiveAriaTarget:{type:Object,computed:"__computeAriaTarget(ariaTarget, target)",observer:"__effectiveAriaTargetChanged"},__isTargetHidden:{type:Boolean,value:!1},_isConnected:{type:Boolean,sync:!0}}}static setDefaultFocusDelay(t){ke=t!=null&&t>=0?t:O}static setDefaultHideDelay(t){Se=t!=null&&t>=0?t:O}static setDefaultHoverDelay(t){Te=t!=null&&t>=0?t:O}constructor(){super(),this._uniqueId=`vaadin-tooltip-${pe()}`,this.__onFocusin=this.__onFocusin.bind(this),this.__onFocusout=this.__onFocusout.bind(this),this.__onMouseDown=this.__onMouseDown.bind(this),this.__onMouseEnter=this.__onMouseEnter.bind(this),this.__onMouseLeave=this.__onMouseLeave.bind(this),this.__onKeyDown=this.__onKeyDown.bind(this),this.__onOverlayOpen=this.__onOverlayOpen.bind(this),this.__targetVisibilityObserver=new IntersectionObserver(t=>{t.forEach(n=>this.__onTargetVisibilityChange(n.isIntersecting))},{threshold:0}),this._stateController=new On(this)}connectedCallback(){super.connectedCallback(),this._isConnected=!0,document.body.addEventListener("vaadin-overlay-open",this.__onOverlayOpen)}disconnectedCallback(){super.disconnectedCallback(),this.opened&&!this.manual&&this._stateController.close(!0),this._isConnected=!1,document.body.removeEventListener("vaadin-overlay-open",this.__onOverlayOpen)}ready(){super.ready(),this._overlayElement=this.$.overlay,this.__contentController=new G(this,"overlay","div",{initializer:t=>{t.id=this._uniqueId,t.setAttribute("role","tooltip"),this.__contentNode=t}}),this.addController(this.__contentController)}updated(t){super.updated(t),(t.has("text")||t.has("generator")||t.has("context")||t.has("markdown"))&&this.__updateContent()}__openedChanged(t,n){t?document.addEventListener("keydown",this.__onKeyDown,!0):n&&document.removeEventListener("keydown",this.__onKeyDown,!0)}_addTargetListeners(t){t.addEventListener("mouseenter",this.__onMouseEnter),t.addEventListener("mouseleave",this.__onMouseLeave),t.addEventListener("focusin",this.__onFocusin),t.addEventListener("focusout",this.__onFocusout),t.addEventListener("mousedown",this.__onMouseDown),requestAnimationFrame(()=>{this.__targetVisibilityObserver.observe(t)})}_removeTargetListeners(t){t.removeEventListener("mouseenter",this.__onMouseEnter),t.removeEventListener("mouseleave",this.__onMouseLeave),t.removeEventListener("focusin",this.__onFocusin),t.removeEventListener("focusout",this.__onFocusout),t.removeEventListener("mousedown",this.__onMouseDown),this.__targetVisibilityObserver.unobserve(t)}__onFocusin(t){this.manual||Y()&&(this.target.contains(t.relatedTarget)||this.__isShouldShow()&&(this._overlayElement.hasAttribute("hidden")||(this.__focusInside=!0,!this.__isTargetHidden&&(!this.__hoverInside||!this.opened)&&this._stateController.open({focus:!0}))))}__onFocusout(t){this.manual||this.target.contains(t.relatedTarget)||(this.__focusInside=!1,this.__hoverInside||this._stateController.close(!0))}__onKeyDown(t){this.manual||t.key==="Escape"&&(t.stopPropagation(),this._stateController.close(!0))}__onMouseDown(){this.manual||this._stateController.close(!0)}__onMouseEnter(){this.manual||this.__isShouldShow()&&(this._overlayElement.hasAttribute("hidden")||this.__hoverInside||(this.__hoverInside=!0,!this.__isTargetHidden&&(!this.__focusInside||!this.opened)&&this._stateController.open({hover:!0})))}__onMouseLeave(t){t.relatedTarget!==this._overlayElement&&this.__handleMouseLeave()}__onOverlayMouseEnter(){this.manual||this._stateController.isClosing&&this._stateController.open({immediate:!0})}__onOverlayMouseLeave(t){t.relatedTarget!==this.target&&this.__handleMouseLeave()}__onOverlayMouseDown(t){t.stopPropagation()}__onOverlayClick(t){t.stopPropagation()}__handleMouseLeave(){this.manual||(this.__hoverInside=!1,this.__focusInside||this._stateController.close())}__onOverlayOpen(){this.manual||this._overlayElement.opened&&!this._overlayElement._last&&this._stateController.close(!0)}__onTargetVisibilityChange(t){if(this.manual)return;const n=this.__isTargetHidden;if(this.__isTargetHidden=!t,n&&t&&(this.__focusInside||this.__hoverInside)){this._stateController.open({immediate:!0});return}!t&&this.opened&&this._stateController.close(!0)}__isShouldShow(){return!(typeof this.shouldShow=="function"&&this.shouldShow(this.target,this.context)!==!0)}async __updateContent(){const t=typeof this.generator=="function"?this.generator(this.context):this.text;this.markdown&&t?(await this.constructor.__importMarkdownHelpers()).renderMarkdownToElement(this.__contentNode,t):this.__contentNode.textContent=t||"",this.$.overlay.toggleAttribute("hidden",this.__contentNode.textContent.trim()===""),this.dispatchEvent(new CustomEvent("content-changed",{detail:{content:this.__contentNode.textContent}}))}__computeAriaTarget(t,n){const s=r=>r&&r.nodeType===Node.ELEMENT_NODE,o=Array.isArray(t)?t.some(s):t;return t===null||o?t:n}__effectiveAriaTargetChanged(t,n){n&&[n].flat().forEach(s=>{ce(s,"aria-describedby",this._uniqueId)}),t&&[t].flat().forEach(s=>{Et(s,"aria-describedby",this._uniqueId)})}static __importMarkdownHelpers(){return this.__markdownHelpers||(this.__markdownHelpers=ze(()=>import("./markdown-helpers-RM02npbm.js"),[],import.meta.url)),this.__markdownHelpers}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ln extends In(le($(k(E)))){static get is(){return"vaadin-tooltip"}static get styles(){return h`
      :host {
        display: contents;
      }
    `}render(){const e=this.__effectivePosition;return y`
      <vaadin-tooltip-overlay
        id="overlay"
        .owner="${this}"
        theme="${ue(this._theme)}"
        .opened="${this._isConnected&&this.opened}"
        .positionTarget="${this.target}"
        .position="${e}"
        ?no-horizontal-overlap="${this.__computeNoHorizontalOverlap(e)}"
        ?no-vertical-overlap="${this.__computeNoVerticalOverlap(e)}"
        .horizontalAlign="${this.__computeHorizontalAlign(e)}"
        .verticalAlign="${this.__computeVerticalAlign(e)}"
        @click="${this.__onOverlayClick}"
        @mousedown="${this.__onOverlayMouseDown}"
        @mouseenter="${this.__onOverlayMouseEnter}"
        @mouseleave="${this.__onOverlayMouseLeave}"
        modeless
        ?markdown="${this.markdown}"
        exportparts="overlay, content"
        ><slot name="overlay"></slot
      ></vaadin-tooltip-overlay>
    `}}A(Ln);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Nn=h`
  :host {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    gap: var(--vaadin-button-gap, 0 var(--vaadin-gap-s));
    white-space: nowrap;
    -webkit-tap-highlight-color: transparent;
    -webkit-user-select: none;
    user-select: none;
    cursor: var(--vaadin-clickable-cursor);
    box-sizing: border-box;
    flex-shrink: 0;
    height: var(--vaadin-button-height, auto);
    margin: var(--vaadin-button-margin, 0);
    padding: var(--vaadin-button-padding, var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container));
    font-family: var(--vaadin-button-font-family, inherit);
    font-size: var(--vaadin-button-font-size, inherit);
    line-height: var(--vaadin-button-line-height, inherit);
    font-weight: var(--vaadin-button-font-weight, 500);
    color: var(--vaadin-button-text-color, var(--vaadin-text-color));
    background: var(--vaadin-button-background, var(--vaadin-background-container));
    background-origin: border-box;
    border: var(--vaadin-button-border-width, 1px) solid
      var(--vaadin-button-border-color, var(--vaadin-border-color-secondary));
    border-radius: var(--vaadin-button-border-radius, var(--vaadin-radius-m));
    touch-action: manipulation;
  }

  :host([hidden]) {
    display: none !important;
  }

  .vaadin-button-container,
  [part='prefix'],
  [part='suffix'] {
    display: contents;
  }

  [part='label'] {
    display: inline-flex;
  }

  :host(:is([focus-ring], :focus-visible)) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: 1px;
  }

  :host([theme~='primary']) {
    --vaadin-button-background: var(--vaadin-text-color);
    --vaadin-button-text-color: var(--vaadin-background-color);
    --vaadin-button-border-color: transparent;
  }

  :host([theme~='tertiary']) {
    background: transparent;
    border-color: transparent;
  }

  :host([disabled]) {
    pointer-events: var(--_vaadin-button-disabled-pointer-events, none);
    cursor: var(--vaadin-disabled-cursor);
    opacity: 0.5;
  }

  :host([disabled][theme~='primary']) {
    --vaadin-button-text-color: var(--vaadin-background-container-strong);
    --vaadin-button-background: var(--vaadin-text-color-disabled);
  }

  @media (forced-colors: active) {
    :host {
      --vaadin-button-border-width: 1px;
      --vaadin-button-background: ButtonFace;
      --vaadin-button-text-color: ButtonText;
    }

    :host([theme~='primary']) {
      forced-color-adjust: none;
      --vaadin-button-background: CanvasText;
      --vaadin-button-text-color: Canvas;
      --vaadin-icon-color: Canvas;
    }

    ::slotted(*) {
      forced-color-adjust: auto;
    }

    :host([disabled]) {
      --vaadin-button-background: transparent !important;
      --vaadin-button-border-color: GrayText !important;
      --vaadin-button-text-color: GrayText !important;
      opacity: 1;
    }
  }
`;/**
@license
Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/const Dn=i=>i,Me=typeof document.head.style.touchAction=="string",bt="__polymerGestures",dt="__polymerGesturesHandled",yt="__polymerGesturesTouchAction",Kt=25,Gt=5,Pn=2,Fn=["mousedown","mousemove","mouseup","click"],Rn=[0,1,4,2],Vn=(function(){try{return new MouseEvent("test",{buttons:1}).buttons===1}catch{return!1}})();function Mt(i){return Fn.indexOf(i)>-1}let Bn=!1;(function(){try{const i=Object.defineProperty({},"passive",{get(){Bn=!0}});window.addEventListener("test",null,i),window.removeEventListener("test",null,i)}catch{}})();function $n(i){Mt(i)}const zn=navigator.userAgent.match(/iP(?:[oa]d|hone)|Android/u),jn={button:!0,command:!0,fieldset:!0,input:!0,keygen:!0,optgroup:!0,option:!0,select:!0,textarea:!0};function x(i){const e=i.type;if(!Mt(e))return!1;if(e==="mousemove"){let n=i.buttons===void 0?1:i.buttons;return i instanceof window.MouseEvent&&!Vn&&(n=Rn[i.which]||0),!!(n&1)}return(i.button===void 0?0:i.button)===0}function Hn(i){if(i.type==="click"){if(i.detail===0)return!0;const e=b(i);if(!e.nodeType||e.nodeType!==Node.ELEMENT_NODE)return!0;const t=e.getBoundingClientRect(),n=i.pageX,s=i.pageY;return!(n>=t.left&&n<=t.right&&s>=t.top&&s<=t.bottom)}return!1}const g={touch:{x:0,y:0,id:-1,scrollDecided:!1}};function Un(i){let e="auto";const t=Ie(i);for(let n=0,s;n<t.length;n++)if(s=t[n],s[yt]){e=s[yt];break}return e}function Oe(i,e,t){i.movefn=e,i.upfn=t,document.addEventListener("mousemove",e),document.addEventListener("mouseup",t)}function I(i){document.removeEventListener("mousemove",i.movefn),document.removeEventListener("mouseup",i.upfn),i.movefn=null,i.upfn=null}const Ie=window.ShadyDOM&&window.ShadyDOM.noPatch?window.ShadyDOM.composedPath:i=>i.composedPath&&i.composedPath()||[],Ot={},w=[];function qn(i,e){let t=document.elementFromPoint(i,e),n=t;for(;n&&n.shadowRoot&&!window.ShadyDOM;){const s=n;if(n=n.shadowRoot.elementFromPoint(i,e),s===n)break;n&&(t=n)}return t}function b(i){const e=Ie(i);return e.length>0?e[0]:i.target}function Wn(i){const e=i.type,n=i.currentTarget[bt];if(!n)return;const s=n[e];if(!s)return;if(!i[dt]&&(i[dt]={},e.startsWith("touch"))){const r=i.changedTouches[0];if(e==="touchstart"&&i.touches.length===1&&(g.touch.id=r.identifier),g.touch.id!==r.identifier)return;Me||(e==="touchstart"||e==="touchmove")&&Kn(i)}const o=i[dt];if(!o.skip){for(let r=0,a;r<w.length;r++)a=w[r],s[a.name]&&!o[a.name]&&a.flow&&a.flow.start.indexOf(i.type)>-1&&a.reset&&a.reset();for(let r=0,a;r<w.length;r++)a=w[r],s[a.name]&&!o[a.name]&&(o[a.name]=!0,a[e](i))}}function Kn(i){const e=i.changedTouches[0],t=i.type;if(t==="touchstart")g.touch.x=e.clientX,g.touch.y=e.clientY,g.touch.scrollDecided=!1;else if(t==="touchmove"){if(g.touch.scrollDecided)return;g.touch.scrollDecided=!0;const n=Un(i);let s=!1;const o=Math.abs(g.touch.x-e.clientX),r=Math.abs(g.touch.y-e.clientY);i.cancelable&&(n==="none"?s=!0:n==="pan-x"?s=r>o:n==="pan-y"&&(s=o>r)),s?i.preventDefault():W("track")}}function Yt(i,e,t){return Ot[e]?(Gn(i,e,t),!0):!1}function Gn(i,e,t){const n=Ot[e],s=n.deps,o=n.name;let r=i[bt];r||(i[bt]=r={});for(let a=0,l,d;a<s.length;a++)l=s[a],!(zn&&Mt(l)&&l!=="click")&&(d=r[l],d||(r[l]=d={_count:0}),d._count===0&&i.addEventListener(l,Wn,$n(l)),d[o]=(d[o]||0)+1,d._count=(d._count||0)+1);i.addEventListener(e,t),n.touchAction&&Xn(i,n.touchAction)}function It(i){w.push(i),i.emits.forEach(e=>{Ot[e]=i})}function Yn(i){for(let e=0,t;e<w.length;e++){t=w[e];for(let n=0,s;n<t.emits.length;n++)if(s=t.emits[n],s===i)return t}return null}function Xn(i,e){Me&&i instanceof HTMLElement&&ee.run(()=>{i.style.touchAction=e}),i[yt]=e}function Lt(i,e,t){const n=new Event(e,{bubbles:!0,cancelable:!0,composed:!0});if(n.detail=t,Dn(i).dispatchEvent(n),n.defaultPrevented){const s=t.preventer||t.sourceEvent;s&&s.preventDefault&&s.preventDefault()}}function W(i){const e=Yn(i);e.info&&(e.info.prevent=!0)}It({name:"downup",deps:["mousedown","touchstart","touchend"],flow:{start:["mousedown","touchstart"],end:["mouseup","touchend"]},emits:["down","up"],info:{movefn:null,upfn:null},reset(){I(this.info)},mousedown(i){if(!x(i))return;const e=b(i),t=this,n=o=>{x(o)||(B("up",e,o),I(t.info))},s=o=>{x(o)&&B("up",e,o),I(t.info)};Oe(this.info,n,s),B("down",e,i)},touchstart(i){B("down",b(i),i.changedTouches[0],i)},touchend(i){B("up",b(i),i.changedTouches[0],i)}});function B(i,e,t,n){e&&Lt(e,i,{x:t.clientX,y:t.clientY,sourceEvent:t,preventer:n,prevent(s){return W(s)}})}It({name:"track",touchAction:"none",deps:["mousedown","touchstart","touchmove","touchend"],flow:{start:["mousedown","touchstart"],end:["mouseup","touchend"]},emits:["track"],info:{x:0,y:0,state:"start",started:!1,moves:[],addMove(i){this.moves.length>Pn&&this.moves.shift(),this.moves.push(i)},movefn:null,upfn:null,prevent:!1},reset(){this.info.state="start",this.info.started=!1,this.info.moves=[],this.info.x=0,this.info.y=0,this.info.prevent=!1,I(this.info)},mousedown(i){if(!x(i))return;const e=b(i),t=this,n=o=>{const r=o.clientX,a=o.clientY;Xt(t.info,r,a)&&(t.info.state=t.info.started?o.type==="mouseup"?"end":"track":"start",t.info.state==="start"&&W("tap"),t.info.addMove({x:r,y:a}),x(o)||(t.info.state="end",I(t.info)),e&&ut(t.info,e,o),t.info.started=!0)},s=o=>{t.info.started&&n(o),I(t.info)};Oe(this.info,n,s),this.info.x=i.clientX,this.info.y=i.clientY},touchstart(i){const e=i.changedTouches[0];this.info.x=e.clientX,this.info.y=e.clientY},touchmove(i){const e=b(i),t=i.changedTouches[0],n=t.clientX,s=t.clientY;Xt(this.info,n,s)&&(this.info.state==="start"&&W("tap"),this.info.addMove({x:n,y:s}),ut(this.info,e,t),this.info.state="track",this.info.started=!0)},touchend(i){const e=b(i),t=i.changedTouches[0];this.info.started&&(this.info.state="end",this.info.addMove({x:t.clientX,y:t.clientY}),ut(this.info,e,t))}});function Xt(i,e,t){if(i.prevent)return!1;if(i.started)return!0;const n=Math.abs(i.x-e),s=Math.abs(i.y-t);return n>=Gt||s>=Gt}function ut(i,e,t){if(!e)return;const n=i.moves[i.moves.length-2],s=i.moves[i.moves.length-1],o=s.x-i.x,r=s.y-i.y;let a,l=0;n&&(a=s.x-n.x,l=s.y-n.y),Lt(e,"track",{state:i.state,x:t.clientX,y:t.clientY,dx:o,dy:r,ddx:a,ddy:l,sourceEvent:t,hover(){return qn(t.clientX,t.clientY)}})}It({name:"tap",deps:["mousedown","click","touchstart","touchend"],flow:{start:["mousedown","touchstart"],end:["click","touchend"]},emits:["tap"],info:{x:NaN,y:NaN,prevent:!1},reset(){this.info.x=NaN,this.info.y=NaN,this.info.prevent=!1},mousedown(i){x(i)&&(this.info.x=i.clientX,this.info.y=i.clientY)},click(i){x(i)&&Zt(this.info,i)},touchstart(i){const e=i.changedTouches[0];this.info.x=e.clientX,this.info.y=e.clientY},touchend(i){Zt(this.info,i.changedTouches[0],i)}});function Zt(i,e,t){const n=Math.abs(e.clientX-i.x),s=Math.abs(e.clientY-i.y),o=b(t||e);!o||jn[o.localName]&&o.hasAttribute("disabled")||(isNaN(n)||isNaN(s)||n<=Kt&&s<=Kt||Hn(e))&&(i.prevent||Lt(o,"tap",{x:e.clientX,y:e.clientY,sourceEvent:e,preventer:t}))}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Zn=i=>class extends be(kt(i)){get _activeKeys(){return[" "]}ready(){super.ready(),Yt(this,"down",t=>{this._shouldSetActive(t)&&this._setActive(!0)}),Yt(this,"up",()=>{this._setActive(!1)})}disconnectedCallback(){super.disconnectedCallback(),this._setActive(!1)}_shouldSetActive(t){return!this.disabled}_onKeyDown(t){super._onKeyDown(t),this._shouldSetActive(t)&&this._activeKeys.includes(t.key)&&(this._setActive(!0),document.addEventListener("keyup",n=>{this._activeKeys.includes(n.key)&&this._setActive(!1)},{once:!0}))}_setActive(t){this.toggleAttribute("active",t)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Jn=["mousedown","mouseup","click","dblclick","keypress","keydown","keyup"],Qn=i=>class extends Zn(ye(me(i))){constructor(){super(),this.__onInteractionEvent=this.__onInteractionEvent.bind(this),Jn.forEach(t=>{this.addEventListener(t,this.__onInteractionEvent,!0)}),this.tabindex=0}get _activeKeys(){return["Enter"," "]}ready(){super.ready(),this.hasAttribute("role")||this.setAttribute("role","button"),this.__shouldAllowFocusWhenDisabled()&&this.style.setProperty("--_vaadin-button-disabled-pointer-events","auto")}_onKeyDown(t){super._onKeyDown(t),!(t.altKey||t.shiftKey||t.ctrlKey||t.metaKey)&&this._activeKeys.includes(t.key)&&(t.preventDefault(),this.click())}__onInteractionEvent(t){this.__shouldSuppressInteractionEvent(t)&&t.stopImmediatePropagation()}__shouldSuppressInteractionEvent(t){return this.disabled}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ts extends Qn($(N(k(L(E))))){static get is(){return"vaadin-button"}static get styles(){return Nn}static get properties(){return{disabled:{type:Boolean,value:!1,observer:"_disabledChanged",reflectToAttribute:!0,sync:!0}}}render(){return y`
      <div class="vaadin-button-container">
        <span part="prefix" aria-hidden="true">
          <slot name="prefix"></slot>
        </span>
        <span part="label">
          <slot></slot>
        </span>
        <span part="suffix" aria-hidden="true">
          <slot name="suffix"></slot>
        </span>

        <slot name="tooltip"></slot>
      </div>
    `}ready(){super.ready(),this._tooltipController=new fe(this),this.addController(this._tooltipController)}__shouldAllowFocusWhenDisabled(){return window.Vaadin.featureFlags.accessibleDisabledButtons}}A(ts);document.addEventListener("click",i=>{const e=i.composedPath().find(t=>t.hasAttribute&&t.hasAttribute("disableonclick"));e&&(e.disabled=!0)});/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Jt=h`
  :host {
    display: flex;
    box-sizing: border-box;
  }

  :host([hidden]) {
    display: none !important;
  }

  /* Theme variations */
  :host([theme~='margin']) {
    margin: var(--vaadin-horizontal-layout-margin, var(--vaadin-padding-m));
  }

  :host([theme~='padding']) {
    padding: var(--vaadin-horizontal-layout-padding, var(--vaadin-padding-m));
  }

  :host([theme~='spacing']) {
    gap: var(--vaadin-horizontal-layout-gap, var(--vaadin-gap-s));
  }

  :host([theme~='wrap']) {
    flex-wrap: wrap;
  }

  :host([has-end]:not([has-middle])) ::slotted([last-start-child]) {
    margin-inline-end: auto;
  }

  ::slotted([first-middle-child]) {
    margin-inline-start: auto;
  }

  ::slotted([last-middle-child]) {
    margin-inline-end: auto;
  }

  :host(:not([has-middle])) ::slotted([first-end-child]) {
    margin-inline-start: auto;
  }
`,es=window.Vaadin.featureFlags.layoutComponentImprovements,is=h`
  ::slotted([data-width-full]) {
    flex: 1;
  }

  ::slotted(vaadin-horizontal-layout[data-width-full]),
  ::slotted(vaadin-vertical-layout[data-width-full]) {
    min-width: 0;
  }
`,ns=es?[Jt,is]:[Jt];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ss=i=>class extends i{ready(){super.ready();const e=this.shadowRoot.querySelector("slot:not([name])");this.__startSlotObserver=new H(e,({currentNodes:s,removedNodes:o})=>{o.length&&this.__clearAttribute(o,"last-start-child");const r=s.filter(l=>l.nodeType===Node.ELEMENT_NODE);this.__updateAttributes(r,"start",!1,!0);const a=s.filter(l=>!he(l));this.toggleAttribute("has-start",a.length>0)});const t=this.shadowRoot.querySelector('[name="end"]');this.__endSlotObserver=new H(t,({currentNodes:s,removedNodes:o})=>{o.length&&this.__clearAttribute(o,"first-end-child"),this.__updateAttributes(s,"end",!0,!1),this.toggleAttribute("has-end",s.length>0)});const n=this.shadowRoot.querySelector('[name="middle"]');this.__middleSlotObserver=new H(n,({currentNodes:s,removedNodes:o})=>{o.length&&(this.__clearAttribute(o,"first-middle-child"),this.__clearAttribute(o,"last-middle-child")),this.__updateAttributes(s,"middle",!0,!0),this.toggleAttribute("has-middle",s.length>0)})}__clearAttribute(e,t){const n=e.find(s=>s.nodeType===Node.ELEMENT_NODE&&s.hasAttribute(t));n&&n.removeAttribute(t)}__updateAttributes(e,t,n,s){e.forEach((o,r)=>{if(n){const a=`first-${t}-child`;r===0?o.setAttribute(a,""):o.hasAttribute(a)&&o.removeAttribute(a)}if(s){const a=`last-${t}-child`;r===e.length-1?o.setAttribute(a,""):o.hasAttribute(a)&&o.removeAttribute(a)}})}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class os extends ss(N($(k(L(E))))){static get is(){return"vaadin-horizontal-layout"}static get styles(){return ns}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return y`
      <slot></slot>
      <slot name="middle"></slot>
      <slot name="end"></slot>
    `}}A(os);function rs(i,e){if(e.type==="stateKeyChanged"){const{value:t}=e;return{...i,key:t}}else return i}const as=()=>{};class ls extends HTMLElement{#t=void 0;#n=!1;#i=void 0;#e=Object.create(null);#o=new Map;#s=new Map;#r=as;#d=new Map;#u;#a;#l;constructor(){super(),this.#u={useState:this.useState.bind(this),useCustomEvent:this.useCustomEvent.bind(this),useContent:this.useContent.bind(this)},this.#a=this.#h.bind(this),this.#p()}async connectedCallback(){this.#i=F.createElement(this.#a),!(!this.dispatchEvent(new CustomEvent("flow-portal-add",{bubbles:!0,cancelable:!0,composed:!0,detail:{children:this.#i,domNode:this}}))||this.#t)&&(await this.#l,this.#t=je.createRoot(this),this.#c(),this.#t.render(this.#i))}addReadyCallback(e,t){this.#d.set(e,t)}async disconnectedCallback(){this.#t?(this.#l=Promise.resolve(),await this.#l,this.#t.unmount(),this.#t=void 0):this.dispatchEvent(new CustomEvent("flow-portal-remove",{bubbles:!0,cancelable:!0,composed:!0,detail:{children:this.#i,domNode:this}})),this.#n=!1,this.#i=void 0}useState(e,t){if(this.#o.has(e))return[this.#e[e],this.#o.get(e)];const n=this[e]??t;this.#e[e]=n,Object.defineProperty(this,e,{enumerable:!0,get(){return this.#e[e]},set(r){this.#e[e]=r,this.#r({type:"stateKeyChanged",key:e,value:n})}});const s=this.useCustomEvent(`${e}-changed`,{detail:{value:n}}),o=r=>{this.#e[e]=r,s({value:r}),this.#r({type:"stateKeyChanged",key:e,value:r})};return this.#o.set(e,o),[n,o]}useCustomEvent(e,t={}){if(!this.#s.has(e)){const n=(s=>{const o=s===void 0?t:{...t,detail:s},r=new CustomEvent(e,o);return this.dispatchEvent(r)});return this.#s.set(e,n),n}return this.#s.get(e)}useContent(e){return F.useEffect(()=>{this.#d.get(e)?.()},[]),F.createElement("flow-content-container",{name:e,style:{display:"contents"}})}#c(){this.#n||!this.#t||(this.#t.render(F.createElement(this.#a)),this.#n=!0)}#h(){const[e,t]=F.useReducer(rs,this.#e);return this.#e=e,this.#r=t,this.render(this.#u)}#p(){let e=window.Vaadin||{};e.developmentMode&&(e.registrations=e.registrations||[],e.registrations.push({is:"ReactAdapterElement",version:"25.0.5"}))}}class ds extends ls{async connectedCallback(){await super.connectedCallback(),this.style.display="contents"}render(){return He.jsx(Ue,{})}}customElements.define("react-router-outlet",ds);const us=i=>Promise.resolve(0);window.Vaadin=window.Vaadin||{};window.Vaadin.Flow=window.Vaadin.Flow||{};window.Vaadin.Flow.loadOnDemand=us;window.Vaadin.Flow.resetFocus=()=>{let i=document.activeElement;for(;i&&i.shadowRoot;)i=i.shadowRoot.activeElement;return!i||i.blur()||i.focus()||!0};
