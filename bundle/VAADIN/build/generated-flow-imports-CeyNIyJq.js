import{f as hi,S as ci,i as c,b as p,a as _,A as ui,_ as pi,r as h,c as vi,t as vt,e as fi,E as _i,D as ft,d as R,g as gi,j as mi,O as bi}from"./indexhtml-jQDByxiF.js";import"./commonjsHelpers-CqkleIqs.js";/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */window.Vaadin||={};window.Vaadin.featureFlags||={};function yi(i){return i.replace(/-[a-z]/gu,t=>t[1].toUpperCase())}const E={};function f(i,t="25.0.3"){if(Object.defineProperty(i,"version",{get(){return t}}),i.experimental){const n=typeof i.experimental=="string"?i.experimental:`${yi(i.is.split("-").slice(1).join("-"))}Component`;if(!window.Vaadin.featureFlags[n]&&!E[n]){E[n]=new Set,E[n].add(i),Object.defineProperty(window.Vaadin.featureFlags,n,{get(){return E[n].size===0},set(s){s&&E[n].size>0&&(E[n].forEach(o=>{customElements.define(o.is,o)}),E[n].clear())}});return}else if(E[n]){E[n].add(i);return}}const e=customElements.get(i.is);if(!e)customElements.define(i.is,i);else{const n=e.version;n&&i.version&&n===i.version?console.warn(`The component ${i.is} has been loaded twice`):console.error(`Tried to define ${i.is} version ${i.version} when version ${e.version} is already in use. Something will probably break.`)}}const wi=/\/\*[\*!]\s+vaadin-dev-mode:start([\s\S]*)vaadin-dev-mode:end\s+\*\*\//i,G=window.Vaadin&&window.Vaadin.Flow&&window.Vaadin.Flow.clients;function xi(){function i(){return!0}return _t(i)}function Ci(){try{return Ei()?!0:ki()?G?!Ai():!xi():!1}catch{return!1}}function Ei(){return localStorage.getItem("vaadin.developmentmode.force")}function ki(){return["localhost","127.0.0.1"].indexOf(window.location.hostname)>=0}function Ai(){return!!(G&&Object.keys(G).map(t=>G[t]).filter(t=>t.productionMode).length>0)}function _t(i,t){if(typeof i!="function")return;const e=wi.exec(i.toString());if(e)try{i=new Function(e[1])}catch(n){console.log("vaadin-development-mode-detector: uncommentAndRun() failed",n)}return i(t)}window.Vaadin=window.Vaadin||{};const Ge=function(i,t){if(window.Vaadin.developmentMode)return _t(i,t)};window.Vaadin.developmentMode===void 0&&(window.Vaadin.developmentMode=Ci());function Ti(){/*! vaadin-dev-mode:start
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

  vaadin-dev-mode:end **/}const Si=function(){if(typeof Ge=="function")return Ge(Ti)};/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
 */let Ye=0,gt=0;const D=[];let xe=!1;function Mi(){xe=!1;const i=D.length;for(let t=0;t<i;t++){const e=D[t];if(e)try{e()}catch(n){setTimeout(()=>{throw n})}}D.splice(0,i),gt+=i}const Oi={after(i){return{run(t){return window.setTimeout(t,i)},cancel(t){window.clearTimeout(t)}}},run(i,t){return window.setTimeout(i,t)},cancel(i){window.clearTimeout(i)}},Li={run(i){return window.requestAnimationFrame(i)},cancel(i){window.cancelAnimationFrame(i)}},Ii={run(i){return window.requestIdleCallback?window.requestIdleCallback(i):window.setTimeout(i,16)},cancel(i){window.cancelIdleCallback?window.cancelIdleCallback(i):window.clearTimeout(i)}},mt={run(i){xe||(xe=!0,queueMicrotask(()=>Mi())),D.push(i);const t=Ye;return Ye+=1,t},cancel(i){const t=i-gt;if(t>=0){if(!D[t])throw new Error(`invalid async handle: ${i}`);D[t]=null}}};/**
@license
Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/const Ce=new Set;class L{static debounce(t,e,n){return t instanceof L?t._cancelAsync():t=new L,t.setConfig(e,n),t}constructor(){this._asyncModule=null,this._callback=null,this._timer=null}setConfig(t,e){this._asyncModule=t,this._callback=e,this._timer=this._asyncModule.run(()=>{this._timer=null,Ce.delete(this),this._callback()})}cancel(){this.isActive()&&(this._cancelAsync(),Ce.delete(this))}_cancelAsync(){this.isActive()&&(this._asyncModule.cancel(this._timer),this._timer=null)}flush(){this.isActive()&&(this.cancel(),this._callback())}isActive(){return this._timer!=null}}function Ni(i){Ce.add(i)}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const k=[];function Ee(i,t,e=i.getAttribute("dir")){t?i.setAttribute("dir",t):e!=null&&i.removeAttribute("dir")}function ke(){return document.documentElement.getAttribute("dir")}function Di(){const i=ke();k.forEach(t=>{Ee(t,i)})}const $i=new MutationObserver(Di);$i.observe(document.documentElement,{attributes:!0,attributeFilter:["dir"]});const ie=i=>class extends i{static get properties(){return{dir:{type:String,value:"",reflectToAttribute:!0,converter:{fromAttribute:e=>e||"",toAttribute:e=>e===""?null:e}}}}get __isRTL(){return this.getAttribute("dir")==="rtl"}connectedCallback(){super.connectedCallback(),(!this.hasAttribute("dir")||this.__restoreSubscription)&&(this.__subscribe(),Ee(this,ke(),null))}attributeChangedCallback(e,n,s){if(super.attributeChangedCallback(e,n,s),e!=="dir")return;const o=ke(),r=s===o&&k.indexOf(this)===-1,a=!s&&n&&k.indexOf(this)===-1;r||a?(this.__subscribe(),Ee(this,o,s)):s!==o&&n===o&&this.__unsubscribe()}disconnectedCallback(){super.disconnectedCallback(),this.__restoreSubscription=k.includes(this),this.__unsubscribe()}_valueToNodeAttribute(e,n,s){s==="dir"&&n===""&&!e.hasAttribute("dir")||super._valueToNodeAttribute(e,n,s)}_attributeToProperty(e,n,s){e==="dir"&&!n?this.dir="":super._attributeToProperty(e,n,s)}__subscribe(){k.includes(this)||k.push(this)}__unsubscribe(){k.includes(this)&&k.splice(k.indexOf(this),1)}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */window.Vaadin||(window.Vaadin={});window.Vaadin.registrations||(window.Vaadin.registrations=[]);window.Vaadin.developmentModeCallback||(window.Vaadin.developmentModeCallback={});window.Vaadin.developmentModeCallback["vaadin-usage-statistics"]=function(){Si()};let de;const Xe=new Set,C=i=>class extends ie(i){static finalize(){super.finalize();const{is:e}=this;if(e&&!Xe.has(e)){window.Vaadin.registrations.push(this),Xe.add(e);const n=window.Vaadin.developmentModeCallback;n&&(de=L.debounce(de,Ii,()=>{n["vaadin-usage-statistics"]()}),Ni(de))}}constructor(){super(),document.doctype===null&&console.warn('Vaadin components require the "standards mode" declaration. Please add <!DOCTYPE html> to the HTML document.')}},bt=new WeakMap;function Pi(i,t){let e=t;for(;e;){if(bt.get(e)===i)return!0;e=Object.getPrototypeOf(e)}return!1}function m(i){return t=>{if(Pi(i,t))return t;const e=i(t);return bt.set(e,i),e}}/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function zi(i,t){return i.split(".").reduce((e,n)=>e?e[n]:void 0,t)}function Fi(i,t,e){const n=i.split("."),s=n.pop(),o=n.reduce((r,a)=>r[a],e);o[s]=t}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const he={},Ri=/([A-Z])/gu;function Ze(i){return he[i]||(he[i]=i.replace(Ri,"-$1").toLowerCase()),he[i]}function Je(i){return i[0].toUpperCase()+i.substring(1)}function ce(i){const[t,e]=i.split("("),n=e.replace(")","").split(",").map(s=>s.trim());return{method:t,observerProps:n}}function ue(i,t){return Object.prototype.hasOwnProperty.call(i,t)||(i[t]=new Map(i[t])),i[t]}const Bi=i=>{class t extends i{static enabledWarnings=[];static createProperty(n,s){[String,Boolean,Number,Array].includes(s)&&(s={type:s}),s&&s.reflectToAttribute&&(s.reflect=!0),super.createProperty(n,s)}static getOrCreateMap(n){return ue(this,n)}static finalize(){if(window.litIssuedWarnings&&(window.litIssuedWarnings.add("no-override-create-property"),window.litIssuedWarnings.add("no-override-get-property-descriptor")),super.finalize(),Array.isArray(this.observers)){const n=this.getOrCreateMap("__complexObservers");this.observers.forEach(s=>{const{method:o,observerProps:r}=ce(s);n.set(o,r)})}}static addCheckedInitializer(n){super.addInitializer(s=>{s instanceof this&&n(s)})}static getPropertyDescriptor(n,s,o){const r=super.getPropertyDescriptor(n,s,o);let a=r;if(this.getOrCreateMap("__propKeys").set(n,s),o.sync&&(a={get:r.get,set(l){const d=this[n];hi(l,d)&&(this[s]=l,this.requestUpdate(n,d,o),this.hasUpdated&&this.performUpdate())},configurable:!0,enumerable:!0}),o.readOnly){const l=a.set;this.addCheckedInitializer(d=>{d[`_set${Je(n)}`]=function(v){l.call(d,v)}}),a={get:a.get,set(){},configurable:!0,enumerable:!0}}if("value"in o&&this.addCheckedInitializer(l=>{const d=typeof o.value=="function"?o.value.call(l):o.value;o.readOnly?l[`_set${Je(n)}`](d):l[n]=d}),o.observer){const l=o.observer;this.getOrCreateMap("__observers").set(n,l),this.addCheckedInitializer(d=>{d[l]||console.warn(`observer method ${l} not defined`)})}if(o.notify){if(!this.__notifyProps)this.__notifyProps=new Set;else if(!this.hasOwnProperty("__notifyProps")){const l=this.__notifyProps;this.__notifyProps=new Set(l)}this.__notifyProps.add(n)}if(o.computed){const l=`__assignComputed${n}`,d=ce(o.computed);this.prototype[l]=function(...v){this[n]=this[d.method](...v)},this.getOrCreateMap("__computedObservers").set(l,d.observerProps)}return o.attribute||(o.attribute=Ze(n)),a}static get polylitConfig(){return{asyncFirstRender:!1}}connectedCallback(){super.connectedCallback();const{polylitConfig:n}=this.constructor;!this.hasUpdated&&!n.asyncFirstRender&&this.performUpdate()}firstUpdated(){super.firstUpdated(),this.$||(this.$={}),this.renderRoot.querySelectorAll("[id]").forEach(n=>{this.$[n.id]=n})}ready(){}willUpdate(n){this.constructor.__computedObservers&&this.__runComplexObservers(n,this.constructor.__computedObservers)}updated(n){const s=this.__isReadyInvoked;this.__isReadyInvoked=!0,this.constructor.__observers&&this.__runObservers(n,this.constructor.__observers),this.constructor.__complexObservers&&this.__runComplexObservers(n,this.constructor.__complexObservers),this.__dynamicPropertyObservers&&this.__runDynamicObservers(n,this.__dynamicPropertyObservers),this.__dynamicMethodObservers&&this.__runComplexObservers(n,this.__dynamicMethodObservers),this.constructor.__notifyProps&&this.__runNotifyProps(n,this.constructor.__notifyProps),s||this.ready()}setProperties(n){Object.entries(n).forEach(([s,o])=>{const r=this.constructor.__propKeys.get(s),a=this[r];this[r]=o,this.requestUpdate(s,a)}),this.hasUpdated&&this.performUpdate()}_createMethodObserver(n){const s=ue(this,"__dynamicMethodObservers"),{method:o,observerProps:r}=ce(n);s.set(o,r)}_createPropertyObserver(n,s){ue(this,"__dynamicPropertyObservers").set(s,n)}__runComplexObservers(n,s){s.forEach((o,r)=>{o.some(a=>n.has(a))&&(this[r]?this[r](...o.map(a=>this[a])):console.warn(`observer method ${r} not defined`))})}__runDynamicObservers(n,s){s.forEach((o,r)=>{n.has(o)&&this[r]&&this[r](this[o],n.get(o))})}__runObservers(n,s){n.forEach((o,r)=>{const a=s.get(r);a!==void 0&&this[a]&&this[a](this[r],o)})}__runNotifyProps(n,s){n.forEach((o,r)=>{s.has(r)&&this.dispatchEvent(new CustomEvent(`${Ze(r)}-changed`,{detail:{value:this[r]}}))})}_get(n,s){return zi(n,s)}_set(n,s,o){Fi(n,s,o)}}return t},g=m(Bi);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Le extends EventTarget{#e;#n=new Set;#i;#t=!1;constructor(t){super(),this.#e=t,this.#i=new CSSStyleSheet}#o(t){const{propertyName:e}=t;this.#n.has(e)&&this.dispatchEvent(new CustomEvent("property-changed",{detail:{propertyName:e}}))}observe(t){this.connect(),!this.#n.has(t)&&(this.#n.add(t),this.#i.replaceSync(`
      :root::before, :host::before {
        content: '' !important;
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
        visibility: hidden !important;
        transition: 1ms allow-discrete step-end !important;
        transition-property: ${[...this.#n].join(", ")} !important;
      }
    `))}connect(){this.#t||(this.#e.adoptedStyleSheets.unshift(this.#i),this.#s.addEventListener("transitionstart",t=>this.#o(t)),this.#s.addEventListener("transitionend",t=>this.#o(t)),this.#t=!0)}disconnect(){this.#n.clear(),this.#e.adoptedStyleSheets=this.#e.adoptedStyleSheets.filter(t=>t!==this.#i),this.#s.removeEventListener("transitionstart",this.#o),this.#s.removeEventListener("transitionend",this.#o),this.#t=!1}get#s(){return this.#e.documentElement??this.#e.host}static for(t){return t.__cssPropertyObserver||=new Le(t),t.__cssPropertyObserver}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Vi(i){const{baseStyles:t,themeStyles:e,elementStyles:n,lumoInjector:s}=i.constructor,o=i.__lumoStyleSheet;return o&&(t||e)?[...s.includeBaseStyles?t:[],o,...e]:[o,...n].filter(Boolean)}function yt(i){ci(i.shadowRoot,Vi(i))}function Qe(i,t){i.__lumoStyleSheet=t,yt(i)}function pe(i){i.__lumoStyleSheet=void 0,yt(i)}/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const et=new Set;function wt(i){et.has(i)||(et.add(i),console.warn(i))}/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const tt=new WeakMap;function it(i){try{return i.media.mediaText}catch{return wt('[LumoInjector] Browser denied to access property "mediaText" for some CSS rules, so they were skipped.'),""}}function Hi(i){try{return i.cssRules}catch{return wt('[LumoInjector] Browser denied to access property "cssRules" for some CSS stylesheets, so they were skipped.'),[]}}function xt(i,t={tags:new Map,modules:new Map}){for(const e of Hi(i)){if(e instanceof CSSImportRule){const n=it(e);n.startsWith("lumo_")?t.modules.set(n,[...e.styleSheet.cssRules]):xt(e.styleSheet,t);continue}if(e instanceof CSSMediaRule){const n=it(e);n.startsWith("lumo_")&&t.modules.set(n,[...e.cssRules]);continue}if(e instanceof CSSStyleRule&&e.cssText.includes("-inject")){for(const n of e.style){const s=n.match(/^--_lumo-(.*)-inject-modules$/u)?.[1];if(!s)continue;const o=e.style.getPropertyValue(n);t.tags.set(s,o.split(",").map(r=>r.trim().replace(/'|"/gu,"")))}continue}}return t}function ji(i){let t=new Map,e=new Map;for(const n of i){let s=tt.get(n);s||(s=xt(n),tt.set(n,s)),t=new Map([...t,...s.tags]),e=new Map([...e,...s.modules])}return{tags:t,modules:e}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Ct(i){return`--_lumo-${i.is}-inject`}class Ui{#e;#n;#i=new Map;#t=new Map;constructor(t=document){this.#e=t,this.handlePropertyChange=this.handlePropertyChange.bind(this),this.#n=Le.for(t),this.#n.addEventListener("property-changed",this.handlePropertyChange)}disconnect(){this.#n.removeEventListener("property-changed",this.handlePropertyChange),this.#i.clear(),this.#t.values().forEach(t=>t.forEach(pe))}forceUpdate(){for(const t of this.#i.keys())this.#s(t)}componentConnected(t){const{lumoInjector:e}=t.constructor,{is:n}=e;this.#t.set(n,this.#t.get(n)??new Set),this.#t.get(n).add(t);const s=this.#i.get(n);if(s){s.cssRules.length>0&&Qe(t,s);return}this.#o(n);const o=Ct(e);this.#n.observe(o)}componentDisconnected(t){const{is:e}=t.constructor.lumoInjector;this.#t.get(e)?.delete(t),pe(t)}handlePropertyChange(t){const{propertyName:e}=t.detail,n=e.match(/^--_lumo-(.*)-inject$/u)?.[1];n&&this.#s(n)}#o(t){this.#i.set(t,new CSSStyleSheet),this.#s(t)}#s(t){const{tags:e,modules:n}=ji(this.#r),s=(e.get(t)??[]).flatMap(r=>n.get(r)??[]).map(r=>r.cssText).join(`
`),o=this.#i.get(t);o.replaceSync(s),this.#t.get(t)?.forEach(r=>{s?Qe(r,o):pe(r)})}get#r(){let t=new Set;for(const e of[this.#e,document])t=t.union(new Set(e.styleSheets)),t=t.union(new Set(e.adoptedStyleSheets));return[...t]}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const nt=new Set;function Et(i){const t=i.getRootNode();return t.host&&t.host.constructor.version?Et(t.host):t}const y=i=>class extends i{static finalize(){super.finalize();const e=Ct(this.lumoInjector);this.is&&!nt.has(e)&&(nt.add(e),CSS.registerProperty({name:e,syntax:"<number>",inherits:!0,initialValue:"0"}))}static get lumoInjector(){return{is:this.is,includeBaseStyles:!1}}connectedCallback(){super.connectedCallback();const e=Et(this);e.__lumoInjectorDisabled||this.isConnected&&(e.__lumoInjector||=new Ui(e),this.__lumoInjector=e.__lumoInjector,this.__lumoInjector.componentConnected(this))}disconnectedCallback(){super.disconnectedCallback(),this.__lumoInjector&&(this.__lumoInjector.componentDisconnected(this),this.__lumoInjector=void 0)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ne=i=>class extends i{static get properties(){return{_theme:{type:String,readOnly:!0}}}static get observedAttributes(){return[...super.observedAttributes,"theme"]}attributeChangedCallback(e,n,s){super.attributeChangedCallback(e,n,s),e==="theme"&&this._set_theme(s)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ae=[],qi=new Set,Wi=new Set;function Ki(i){return i&&Object.prototype.hasOwnProperty.call(i,"__themes")}function Gi(i,t){return(i||"").split(" ").some(e=>new RegExp(`^${e.split("*").join(".*")}$`,"u").test(t))}function Yi(i){return i.map(t=>t.cssText).join(`
`)}const Xi="vaadin-themable-mixin-style";function Zi(i,t){const e=document.createElement("style");e.id=Xi,e.textContent=Yi(i),t.content.appendChild(e)}function Ji(i=""){let t=0;return i.startsWith("lumo-")||i.startsWith("material-")?t=1:i.startsWith("vaadin-")&&(t=2),t}function kt(i){const t=[];return i.include&&[].concat(i.include).forEach(e=>{const n=Ae.find(s=>s.moduleId===e);n?t.push(...kt(n),...n.styles):console.warn(`Included moduleId ${e} not found in style registry`)},i.styles),t}function Qi(i){const t=`${i}-default-theme`,e=Ae.filter(n=>n.moduleId!==t&&Gi(n.themeFor,i)).map(n=>({...n,styles:[...kt(n),...n.styles],includePriority:Ji(n.moduleId)})).sort((n,s)=>s.includePriority-n.includePriority);return e.length>0?e:Ae.filter(n=>n.moduleId===t)}const b=i=>class extends ne(i){constructor(){super(),qi.add(new WeakRef(this))}static finalize(){if(super.finalize(),this.is&&Wi.add(this.is),this.elementStyles)return;const e=this.prototype._template;!e||Ki(this)||Zi(this.getStylesForThis(),e)}static finalizeStyles(e){return this.baseStyles=e?[e].flat(1/0):[],this.themeStyles=this.getStylesForThis(),[...this.baseStyles,...this.themeStyles]}static getStylesForThis(){const e=i.__themes||[],n=Object.getPrototypeOf(this.prototype),s=(n?n.constructor.__themes:[])||[];this.__themes=[...e,...s,...Qi(this.is)];const o=this.__themes.flatMap(r=>r.styles);return o.filter((r,a)=>a===o.lastIndexOf(r))}};/**
 * @license
 * Copyright (c) 2026 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const en=(i,...t)=>{const e=document.createElement("style");e.id=i,e.textContent=t.map(n=>n.toString()).join(`
`),document.head.insertAdjacentElement("afterbegin",e)};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */["--vaadin-text-color","--vaadin-text-color-disabled","--vaadin-text-color-secondary","--vaadin-border-color","--vaadin-border-color-secondary","--vaadin-background-color"].forEach(i=>{CSS.registerProperty({name:i,syntax:"<color>",inherits:!0,initialValue:"light-dark(black, white)"})});en("vaadin-base",c`
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
 */const st=c`
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
`,tn=window.Vaadin.featureFlags.layoutComponentImprovements,nn=c`
  ::slotted([data-height-full]) {
    flex: 1;
  }

  ::slotted(vaadin-horizontal-layout[data-height-full]),
  ::slotted(vaadin-vertical-layout[data-height-full]) {
    min-height: 0;
  }
`,sn=tn?[st,nn]:[st];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class on extends b(C(g(y(_)))){static get is(){return"vaadin-vertical-layout"}static get styles(){return sn}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return p`<slot></slot>`}}f(on);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const rn=c`
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
 */class an extends b(ie(g(y(_)))){static get is(){return"vaadin-input-container"}static get styles(){return rn}static get properties(){return{disabled:{type:Boolean,reflectToAttribute:!0},readonly:{type:Boolean,reflectToAttribute:!0},invalid:{type:Boolean,reflectToAttribute:!0}}}render(){return p`
      <slot name="prefix"></slot>
      <slot></slot>
      <slot name="suffix"></slot>
    `}ready(){super.ready(),this.addEventListener("pointerdown",t=>{t.target===this&&t.preventDefault()}),this.addEventListener("click",t=>{t.target===this&&this.shadowRoot.querySelector("slot:not([name])").assignedNodes({flatten:!0}).forEach(e=>e.focus&&e.focus())})}}f(an);/**
 * @license
 * Copyright 2018 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const z=i=>i??ui;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function ln(i){const t=[];for(;i;){if(i.nodeType===Node.DOCUMENT_NODE){t.push(i);break}if(i.nodeType===Node.DOCUMENT_FRAGMENT_NODE){t.push(i),i=i.host;continue}if(i.assignedSlot){i=i.assignedSlot;continue}i=i.parentNode}return t}function Ie(i){return i?new Set(i.split(" ")):new Set}function se(i){return i?[...i].join(" "):""}function Ne(i,t,e){const n=Ie(i.getAttribute(t));n.add(e),i.setAttribute(t,se(n))}function At(i,t,e){const n=Ie(i.getAttribute(t));if(n.delete(e),n.size===0){i.removeAttribute(t);return}i.setAttribute(t,se(n))}function Tt(i){return i.nodeType===Node.TEXT_NODE&&i.textContent.trim()===""}/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Y{constructor(t,e){this.slot=t,this.callback=e,this._storedNodes=[],this._connected=!1,this._scheduled=!1,this._boundSchedule=()=>{this._schedule()},this.connect(),this._schedule()}connect(){this.slot.addEventListener("slotchange",this._boundSchedule),this._connected=!0}disconnect(){this.slot.removeEventListener("slotchange",this._boundSchedule),this._connected=!1}_schedule(){this._scheduled||(this._scheduled=!0,queueMicrotask(()=>{this.flush()}))}flush(){this._connected&&(this._scheduled=!1,this._processNodes())}_processNodes(){const t=this.slot.assignedNodes({flatten:!0});let e=[];const n=[],s=[];t.length&&(e=t.filter(o=>!this._storedNodes.includes(o))),this._storedNodes.length&&this._storedNodes.forEach((o,r)=>{const a=t.indexOf(o);a===-1?n.push(o):a!==r&&s.push(o)}),(e.length||n.length||s.length)&&this.callback({addedNodes:e,currentNodes:t,movedNodes:s,removedNodes:n}),this._storedNodes=t}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let dn=0;function St(){return dn++}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class U extends EventTarget{static generateId(t,e="default"){return`${e}-${t.localName}-${St()}`}constructor(t,e,n,s={}){super();const{initializer:o,multiple:r,observe:a,useUniqueId:l,uniqueIdPrefix:d}=s;this.host=t,this.slotName=e,this.tagName=n,this.observe=typeof a=="boolean"?a:!0,this.multiple=typeof r=="boolean"?r:!1,this.slotInitializer=o,r&&(this.nodes=[]),l&&(this.defaultId=this.constructor.generateId(t,d||e))}hostConnected(){this.initialized||(this.multiple?this.initMultiple():this.initSingle(),this.observe&&this.observeSlot(),this.initialized=!0)}initSingle(){let t=this.getSlotChild();t?(this.node=t,this.initAddedNode(t)):(t=this.attachDefaultNode(),this.initNode(t))}initMultiple(){const t=this.getSlotChildren();if(t.length===0){const e=this.attachDefaultNode();e&&(this.nodes=[e],this.initNode(e))}else this.nodes=t,t.forEach(e=>{this.initAddedNode(e)})}attachDefaultNode(){const{host:t,slotName:e,tagName:n}=this;let s=this.defaultNode;return!s&&n&&(s=document.createElement(n),s instanceof Element&&(e!==""&&s.setAttribute("slot",e),this.defaultNode=s)),s&&(this.node=s,t.appendChild(s)),s}getSlotChildren(){const{slotName:t}=this;return Array.from(this.host.childNodes).filter(e=>e.nodeType===Node.ELEMENT_NODE&&e.hasAttribute("data-slot-ignore")?!1:e.nodeType===Node.ELEMENT_NODE&&e.slot===t||e.nodeType===Node.TEXT_NODE&&e.textContent.trim()&&t==="")}getSlotChild(){return this.getSlotChildren()[0]}initNode(t){const{slotInitializer:e}=this;e&&e(t,this.host)}initCustomNode(t){}teardownNode(t){}initAddedNode(t){t!==this.defaultNode&&(this.initCustomNode(t),this.initNode(t))}observeSlot(){const{slotName:t}=this,e=t===""?"slot:not([name])":`slot[name=${t}]`,n=this.host.shadowRoot.querySelector(e);this.__slotObserver=new Y(n,({addedNodes:s,removedNodes:o})=>{const r=this.multiple?this.nodes:[this.node],a=s.filter(l=>!Tt(l)&&!r.includes(l)&&!(l.nodeType===Node.ELEMENT_NODE&&l.hasAttribute("data-slot-ignore")));o.length&&(this.nodes=r.filter(l=>!o.includes(l)),o.forEach(l=>{this.teardownNode(l)})),a&&a.length>0&&(this.multiple?(this.defaultNode&&this.defaultNode.remove(),this.nodes=[...r,...a].filter(l=>l!==this.defaultNode),a.forEach(l=>{this.initAddedNode(l)})):(this.node&&this.node.remove(),this.node=a[0],this.initAddedNode(this.node)))})}}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class q extends U{constructor(t){super(t,"tooltip"),this.setTarget(t),this.__onContentChange=this.__onContentChange.bind(this)}initCustomNode(t){t.target=this.target,this.ariaTarget!==void 0&&(t.ariaTarget=this.ariaTarget),this.context!==void 0&&(t.context=this.context),this.manual!==void 0&&(t.manual=this.manual),this.opened!==void 0&&(t.opened=this.opened),this.position!==void 0&&(t._position=this.position),this.shouldShow!==void 0&&(t.shouldShow=this.shouldShow),this.manual||this.host.setAttribute("has-tooltip",""),this.__notifyChange(t),t.addEventListener("content-changed",this.__onContentChange)}teardownNode(t){this.manual||this.host.removeAttribute("has-tooltip"),t.removeEventListener("content-changed",this.__onContentChange),this.__notifyChange(null)}setAriaTarget(t){this.ariaTarget=t;const e=this.node;e&&(e.ariaTarget=t)}setContext(t){this.context=t;const e=this.node;e&&(e.context=t)}setManual(t){this.manual=t;const e=this.node;e&&(e.manual=t)}setOpened(t){this.opened=t;const e=this.node;e&&(e.opened=t)}setPosition(t){this.position=t;const e=this.node;e&&(e._position=t)}setShouldShow(t){this.shouldShow=t;const e=this.node;e&&(e.shouldShow=t)}setTarget(t){this.target=t;const e=this.node;e&&(e.target=t)}__onContentChange(t){this.__notifyChange(t.target)}__notifyChange(t){this.dispatchEvent(new CustomEvent("tooltip-changed",{detail:{node:t}}))}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const hn=c`
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
 */const Mt=c`
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
 */const De=[Mt,hn];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class $e extends U{constructor(t,e,n={}){const{uniqueIdPrefix:s}=n;super(t,"input","input",{initializer:(o,r)=>{r.value&&(o.value=r.value),r.type&&o.setAttribute("type",r.type),o.id=this.defaultId,typeof e=="function"&&e(o)},useUniqueId:!0,uniqueIdPrefix:s})}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let Pe=!1;window.addEventListener("keydown",()=>{Pe=!0},{capture:!0});window.addEventListener("mousedown",()=>{Pe=!1},{capture:!0});function Z(){let i=document.activeElement||document.body;for(;i.shadowRoot&&i.shadowRoot.activeElement;)i=i.shadowRoot.activeElement;return i}function oe(){return Pe}function Ot(i){const t=i.style;if(t.visibility==="hidden"||t.display==="none")return!0;const e=window.getComputedStyle(i);return e.visibility==="hidden"||e.display==="none"}function cn(i,t){const e=Math.max(i.tabIndex,0),n=Math.max(t.tabIndex,0);return e===0||n===0?n>e:e>n}function un(i,t){const e=[];for(;i.length>0&&t.length>0;)cn(i[0],t[0])?e.push(t.shift()):e.push(i.shift());return e.concat(i,t)}function Te(i){const t=i.length;if(t<2)return i;const e=Math.ceil(t/2),n=Te(i.slice(0,e)),s=Te(i.slice(e));return un(n,s)}function pn(i){return i.checkVisibility?!i.checkVisibility({visibilityProperty:!0}):i.offsetParent===null&&i.clientWidth===0&&i.clientHeight===0?!0:Ot(i)}function vn(i){return i.matches('[tabindex="-1"]')?!1:i.matches("input, select, textarea, button, object")?i.matches(":not([disabled])"):i.matches("a[href], area[href], iframe, [tabindex], [contentEditable]")}function Lt(i){return i.getRootNode().activeElement===i}function fn(i){if(!vn(i))return-1;const t=i.getAttribute("tabindex")||0;return Number(t)}function It(i,t){if(i.nodeType!==Node.ELEMENT_NODE||Ot(i))return!1;const e=i,n=fn(e);let s=n>0;n>=0&&t.push(e);let o=[];return e.localName==="slot"?o=e.assignedNodes({flatten:!0}):o=(e.shadowRoot||e).children,[...o].forEach(r=>{s=It(r,t)||s}),s}function _n(i){const t=[];return It(i,t)?Te(t):t}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Nt=m(i=>class extends i{get _keyboardActive(){return oe()}ready(){this.addEventListener("focusin",e=>{this._shouldSetFocus(e)&&this._setFocused(!0)}),this.addEventListener("focusout",e=>{this._shouldRemoveFocus(e)&&this._setFocused(!1)}),super.ready()}disconnectedCallback(){super.disconnectedCallback(),this.hasAttribute("focused")&&this._setFocused(!1)}focus(e){super.focus(e),e&&e.focusVisible===!1||this.setAttribute("focus-ring","")}_setFocused(e){this.toggleAttribute("focused",e),this.toggleAttribute("focus-ring",e&&this._keyboardActive)}_shouldSetFocus(e){return!0}_shouldRemoveFocus(e){return!0}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ze=m(i=>class extends i{static get properties(){return{disabled:{type:Boolean,value:!1,observer:"_disabledChanged",reflectToAttribute:!0,sync:!0}}}_disabledChanged(e){this._setAriaDisabled(e)}_setAriaDisabled(e){e?this.setAttribute("aria-disabled","true"):this.removeAttribute("aria-disabled")}click(){this.disabled||super.click()}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Dt=i=>class extends ze(i){static get properties(){return{tabindex:{type:Number,reflectToAttribute:!0,observer:"_tabindexChanged",sync:!0},_lastTabIndex:{type:Number}}}_disabledChanged(e,n){super._disabledChanged(e,n),!this.__shouldAllowFocusWhenDisabled()&&(e?(this.tabindex!==void 0&&(this._lastTabIndex=this.tabindex),this.setAttribute("tabindex","-1")):n&&(this._lastTabIndex!==void 0?this.setAttribute("tabindex",this._lastTabIndex):this.tabindex=void 0))}_tabindexChanged(e){this.__shouldAllowFocusWhenDisabled()||this.disabled&&e!==-1&&(this._lastTabIndex=e,this.setAttribute("tabindex","-1"))}focus(e){(!this.disabled||this.__shouldAllowFocusWhenDisabled())&&super.focus(e)}__shouldAllowFocusWhenDisabled(){return!1}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const $t=m(i=>class extends Nt(Dt(i)){static get properties(){return{autofocus:{type:Boolean},focusElement:{type:Object,readOnly:!0,observer:"_focusElementChanged",sync:!0},_lastTabIndex:{value:0}}}constructor(){super(),this._boundOnBlur=this._onBlur.bind(this),this._boundOnFocus=this._onFocus.bind(this)}ready(){super.ready(),this.autofocus&&!this.disabled&&requestAnimationFrame(()=>{this.focus()})}focus(e){this.focusElement&&!this.disabled&&(this.focusElement.focus(),e&&e.focusVisible===!1||this.setAttribute("focus-ring",""))}blur(){this.focusElement&&this.focusElement.blur()}click(){this.focusElement&&!this.disabled&&this.focusElement.click()}_focusElementChanged(e,n){e?(e.disabled=this.disabled,this._addFocusListeners(e),this.__forwardTabIndex(this.tabindex)):n&&this._removeFocusListeners(n)}_addFocusListeners(e){e.addEventListener("blur",this._boundOnBlur),e.addEventListener("focus",this._boundOnFocus)}_removeFocusListeners(e){e.removeEventListener("blur",this._boundOnBlur),e.removeEventListener("focus",this._boundOnFocus)}_onFocus(e){e.stopPropagation(),this.dispatchEvent(new Event("focus"))}_onBlur(e){e.stopPropagation(),this.dispatchEvent(new Event("blur"))}_shouldSetFocus(e){return e.target===this.focusElement}_shouldRemoveFocus(e){return e.target===this.focusElement}_disabledChanged(e,n){super._disabledChanged(e,n),this.focusElement&&(this.focusElement.disabled=e),e&&this.blur()}_tabindexChanged(e){this.__forwardTabIndex(e)}__forwardTabIndex(e){e!==void 0&&this.focusElement&&(this.focusElement.tabIndex=e,e!==-1&&(this.tabindex=void 0)),this.disabled&&e&&(e!==-1&&(this._lastTabIndex=e),this.tabindex=void 0),e===void 0&&this.hasAttribute("tabindex")&&this.removeAttribute("tabindex")}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Fe=m(i=>class extends i{ready(){super.ready(),this.addEventListener("keydown",e=>{this._onKeyDown(e)}),this.addEventListener("keyup",e=>{this._onKeyUp(e)})}_onKeyDown(e){switch(e.key){case"Enter":this._onEnter(e);break;case"Escape":this._onEscape(e);break}}_onKeyUp(e){}_onEnter(e){}_onEscape(e){}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ve=new WeakMap;function gn(i){return ve.has(i)||ve.set(i,new Set),ve.get(i)}function mn(i,t){const e=document.createElement("style");e.textContent=i,t===document?document.head.appendChild(e):t.insertBefore(e,t.firstChild)}const Pt=m(i=>class extends i{get slotStyles(){return[]}connectedCallback(){super.connectedCallback(),this.__applySlotStyles()}__applySlotStyles(){const e=this.getRootNode(),n=gn(e);this.slotStyles.forEach(s=>{n.has(s)||(mn(s,e),n.add(s))})}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const re=i=>i.test(navigator.userAgent),Se=i=>i.test(navigator.platform),bn=i=>i.test(navigator.vendor);re(/Android/u);re(/Chrome/u)&&bn(/Google Inc/u);re(/Firefox/u);const yn=Se(/^iPad/u)||Se(/^Mac/u)&&navigator.maxTouchPoints>1,wn=Se(/^iPhone/u),zt=wn||yn;re(/^((?!chrome|android).)*safari/iu);const Ft=(()=>{try{return document.createEvent("TouchEvent"),!0}catch{return!1}})();/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Re=m(i=>class extends i{static get properties(){return{inputElement:{type:Object,readOnly:!0,observer:"_inputElementChanged",sync:!0},type:{type:String,readOnly:!0},value:{type:String,value:"",observer:"_valueChanged",notify:!0,sync:!0}}}constructor(){super(),this._boundOnInput=this._onInput.bind(this),this._boundOnChange=this._onChange.bind(this)}get _hasValue(){return this.value!=null&&this.value!==""}get _inputElementValueProperty(){return"value"}get _inputElementValue(){return this.inputElement?this.inputElement[this._inputElementValueProperty]:void 0}set _inputElementValue(e){this.inputElement&&(this.inputElement[this._inputElementValueProperty]=e)}clear(){this.value="",this._inputElementValue=""}_addInputListeners(e){e.addEventListener("input",this._boundOnInput),e.addEventListener("change",this._boundOnChange)}_removeInputListeners(e){e.removeEventListener("input",this._boundOnInput),e.removeEventListener("change",this._boundOnChange)}_forwardInputValue(e){this.inputElement&&(this._inputElementValue=e??"")}_inputElementChanged(e,n){e?this._addInputListeners(e):n&&this._removeInputListeners(n)}_onInput(e){const n=e.composedPath()[0];this.__userInput=e.isTrusted,this.value=n.value,this.__userInput=!1}_onChange(e){}_toggleHasValue(e){this.toggleAttribute("has-value",e)}_valueChanged(e,n){this._toggleHasValue(this._hasValue),!(e===""&&n===void 0)&&(this.__userInput||this._forwardInputValue(e))}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const xn=i=>class extends Re(Fe(i)){static get properties(){return{clearButtonVisible:{type:Boolean,reflectToAttribute:!0,value:!1}}}get clearElement(){return console.warn(`Please implement the 'clearElement' property in <${this.localName}>`),null}ready(){super.ready(),this.clearElement&&(this.clearElement.addEventListener("mousedown",e=>this._onClearButtonMouseDown(e)),this.clearElement.addEventListener("click",e=>this._onClearButtonClick(e)))}_onClearButtonClick(e){e.preventDefault(),this._onClearAction()}_onClearButtonMouseDown(e){this._shouldKeepFocusOnClearMousedown()&&e.preventDefault(),Ft||this.inputElement.focus()}_onEscape(e){super._onEscape(e),this.clearButtonVisible&&this.value&&!this.readonly&&(e.stopPropagation(),this._onClearAction())}_onClearAction(){this._inputElementValue="",this.inputElement.dispatchEvent(new Event("input",{bubbles:!0,composed:!0})),this.inputElement.dispatchEvent(new Event("change",{bubbles:!0}))}_shouldKeepFocusOnClearMousedown(){return Lt(this.inputElement)}};/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const fe=new Map;function Be(i){return fe.has(i)||fe.set(i,new WeakMap),fe.get(i)}function Rt(i,t){i&&i.removeAttribute(t)}function Bt(i,t){if(!i||!t)return;const e=Be(t);if(e.has(i))return;const n=Ie(i.getAttribute(t));e.set(i,new Set(n))}function Cn(i,t){if(!i||!t)return;const e=Be(t),n=e.get(i);!n||n.size===0?i.removeAttribute(t):Ne(i,t,se(n)),e.delete(i)}function _e(i,t,e={newId:null,oldId:null,fromUser:!1}){if(!i||!t)return;const{newId:n,oldId:s,fromUser:o}=e,r=Be(t),a=r.get(i);if(!o&&a){s&&a.delete(s),n&&a.add(n);return}o&&(a?n||r.delete(i):Bt(i,t),Rt(i,t)),At(i,t,s);const l=n||se(a);l&&Ne(i,t,l)}function En(i,t){Bt(i,t),Rt(i,t)}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class kn{constructor(t){this.host=t,this.__required=!1}setTarget(t){this.__target=t,this.__setAriaRequiredAttribute(this.__required),this.__setLabelIdToAriaAttribute(this.__labelId,this.__labelId),this.__labelIdFromUser!=null&&this.__setLabelIdToAriaAttribute(this.__labelIdFromUser,this.__labelIdFromUser,!0),this.__setErrorIdToAriaAttribute(this.__errorId),this.__setHelperIdToAriaAttribute(this.__helperId),this.setAriaLabel(this.__label)}setRequired(t){this.__setAriaRequiredAttribute(t),this.__required=t}setAriaLabel(t){this.__setAriaLabelToAttribute(t),this.__label=t}setLabelId(t,e=!1){const n=e?this.__labelIdFromUser:this.__labelId;this.__setLabelIdToAriaAttribute(t,n,e),e?this.__labelIdFromUser=t:this.__labelId=t}setErrorId(t){this.__setErrorIdToAriaAttribute(t,this.__errorId),this.__errorId=t}setHelperId(t){this.__setHelperIdToAriaAttribute(t,this.__helperId),this.__helperId=t}__setAriaLabelToAttribute(t){this.__target&&(t?(En(this.__target,"aria-labelledby"),this.__target.setAttribute("aria-label",t)):this.__label&&(Cn(this.__target,"aria-labelledby"),this.__target.removeAttribute("aria-label")))}__setLabelIdToAriaAttribute(t,e,n){_e(this.__target,"aria-labelledby",{newId:t,oldId:e,fromUser:n})}__setErrorIdToAriaAttribute(t,e){_e(this.__target,"aria-describedby",{newId:t,oldId:e,fromUser:!1})}__setHelperIdToAriaAttribute(t,e){_e(this.__target,"aria-describedby",{newId:t,oldId:e,fromUser:!1})}__setAriaRequiredAttribute(t){this.__target&&(["input","textarea"].includes(this.__target.localName)||(t?this.__target.setAttribute("aria-required","true"):this.__target.removeAttribute("aria-required")))}}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const x=document.createElement("div");x.style.position="fixed";x.style.clip="rect(0px, 0px, 0px, 0px)";x.setAttribute("aria-live","polite");document.body.appendChild(x);let W;function An(i,t={}){const e=t.mode||"polite",n=t.timeout===void 0?150:t.timeout;e==="alert"?(x.removeAttribute("aria-live"),x.removeAttribute("role"),W=L.debounce(W,Li,()=>{x.setAttribute("role","alert")})):(W&&W.cancel(),x.removeAttribute("role"),x.setAttribute("aria-live",e)),x.textContent="",setTimeout(()=>{x.textContent=i},n)}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ve extends U{constructor(t,e,n,s={}){super(t,e,n,{...s,useUniqueId:!0})}initCustomNode(t){this.__updateNodeId(t),this.__notifyChange(t)}teardownNode(t){const e=this.getSlotChild();e&&e!==this.defaultNode?this.__notifyChange(e):(this.restoreDefaultNode(),this.updateDefaultNode(this.node))}attachDefaultNode(){const t=super.attachDefaultNode();return t&&this.__updateNodeId(t),t}restoreDefaultNode(){}updateDefaultNode(t){this.__notifyChange(t)}observeNode(t){this.__nodeObserver&&this.__nodeObserver.disconnect(),this.__nodeObserver=new MutationObserver(e=>{e.forEach(n=>{const s=n.target,o=s===this.node;n.type==="attributes"?o&&this.__updateNodeId(s):(o||s.parentElement===this.node)&&this.__notifyChange(this.node)})}),this.__nodeObserver.observe(t,{attributes:!0,attributeFilter:["id"],childList:!0,subtree:!0,characterData:!0})}__hasContent(t){return t?t.nodeType===Node.ELEMENT_NODE&&(customElements.get(t.localName)||t.children.length>0)||t.textContent&&t.textContent.trim()!=="":!1}__notifyChange(t){this.dispatchEvent(new CustomEvent("slot-content-changed",{detail:{hasContent:this.__hasContent(t),node:t}}))}__updateNodeId(t){const e=!this.nodes||t===this.nodes[0];t.nodeType===Node.ELEMENT_NODE&&(!this.multiple||e)&&!t.id&&(t.id=this.defaultId)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Tn extends Ve{constructor(t){super(t,"error-message","div")}setErrorMessage(t){this.errorMessage=t,this.updateDefaultNode(this.node)}setInvalid(t){this.invalid=t,this.updateDefaultNode(this.node)}initAddedNode(t){t!==this.defaultNode&&this.initCustomNode(t)}initNode(t){this.updateDefaultNode(t)}initCustomNode(t){t.textContent&&!this.errorMessage&&(this.errorMessage=t.textContent.trim()),super.initCustomNode(t)}restoreDefaultNode(){this.attachDefaultNode()}updateDefaultNode(t){const{errorMessage:e,invalid:n}=this,s=!!(n&&e&&e.trim()!=="");t&&(t.textContent=s?e:"",t.hidden=!s,s&&An(e,{mode:"assertive"})),super.updateDefaultNode(t)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Sn extends Ve{constructor(t){super(t,"helper",null)}setHelperText(t){this.helperText=t,this.getSlotChild()||this.restoreDefaultNode(),this.node===this.defaultNode&&this.updateDefaultNode(this.node)}restoreDefaultNode(){const{helperText:t}=this;if(t&&t.trim()!==""){this.tagName="div";const e=this.attachDefaultNode();this.observeNode(e)}}updateDefaultNode(t){t&&(t.textContent=this.helperText),super.updateDefaultNode(t)}initCustomNode(t){super.initCustomNode(t),this.observeNode(t)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Mn extends Ve{constructor(t){super(t,"label","label")}setLabel(t){this.label=t,this.getSlotChild()||this.restoreDefaultNode(),this.node===this.defaultNode&&this.updateDefaultNode(this.node)}restoreDefaultNode(){const{label:t}=this;if(t&&t.trim()!==""){const e=this.attachDefaultNode();this.observeNode(e)}}updateDefaultNode(t){t&&(t.textContent=this.label),super.updateDefaultNode(t)}initCustomNode(t){super.initCustomNode(t),this.observeNode(t)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const On=m(i=>class extends i{static get properties(){return{label:{type:String,observer:"_labelChanged"}}}constructor(){super(),this._labelController=new Mn(this),this._labelController.addEventListener("slot-content-changed",e=>{this.toggleAttribute("has-label",e.detail.hasContent)})}get _labelId(){const e=this._labelNode;return e&&e.id}get _labelNode(){return this._labelController.node}ready(){super.ready(),this.addController(this._labelController)}_labelChanged(e){this._labelController.setLabel(e)}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Vt=m(i=>class extends i{static get properties(){return{invalid:{type:Boolean,reflectToAttribute:!0,notify:!0,value:!1,sync:!0},manualValidation:{type:Boolean,value:!1},required:{type:Boolean,reflectToAttribute:!0,sync:!0}}}validate(){const e=this.checkValidity();return this._setInvalid(!e),this.dispatchEvent(new CustomEvent("validated",{detail:{valid:e}})),e}checkValidity(){return!this.required||!!this.value}_setInvalid(e){this._shouldSetInvalid(e)&&(this.invalid=e)}_shouldSetInvalid(e){return!0}_requestValidation(){this.manualValidation||this.validate()}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ht=i=>class extends Vt(On(i)){static get properties(){return{ariaTarget:{type:Object,observer:"_ariaTargetChanged"},errorMessage:{type:String,observer:"_errorMessageChanged"},helperText:{type:String,observer:"_helperTextChanged"},accessibleName:{type:String,observer:"_accessibleNameChanged"},accessibleNameRef:{type:String,observer:"_accessibleNameRefChanged"}}}static get observers(){return["_invalidChanged(invalid)","_requiredChanged(required)"]}constructor(){super(),this._fieldAriaController=new kn(this),this._helperController=new Sn(this),this._errorController=new Tn(this),this._errorController.addEventListener("slot-content-changed",e=>{this.toggleAttribute("has-error-message",e.detail.hasContent)}),this._labelController.addEventListener("slot-content-changed",e=>{const{hasContent:n,node:s}=e.detail;this.__labelChanged(n,s)}),this._helperController.addEventListener("slot-content-changed",e=>{const{hasContent:n,node:s}=e.detail;this.toggleAttribute("has-helper",n),this.__helperChanged(n,s)})}get _errorNode(){return this._errorController.node}get _helperNode(){return this._helperController.node}ready(){super.ready(),this.addController(this._fieldAriaController),this.addController(this._helperController),this.addController(this._errorController)}__helperChanged(e,n){e?this._fieldAriaController.setHelperId(n.id):this._fieldAriaController.setHelperId(null)}_accessibleNameChanged(e){this._fieldAriaController.setAriaLabel(e)}_accessibleNameRefChanged(e){this._fieldAriaController.setLabelId(e,!0)}__labelChanged(e,n){e?this._fieldAriaController.setLabelId(n.id):this._fieldAriaController.setLabelId(null)}_errorMessageChanged(e){this._errorController.setErrorMessage(e)}_helperTextChanged(e){this._helperController.setHelperText(e)}_ariaTargetChanged(e){e&&this._fieldAriaController.setTarget(e)}_requiredChanged(e){this._fieldAriaController.setRequired(e)}_invalidChanged(e){this._errorController.setInvalid(e),setTimeout(()=>{if(e){const n=this._errorNode;this._fieldAriaController.setErrorId(n&&n.id)}else this._fieldAriaController.setErrorId(null)})}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const jt=m(i=>class extends i{static get properties(){return{stateTarget:{type:Object,observer:"_stateTargetChanged"}}}static get delegateAttrs(){return[]}static get delegateProps(){return[]}ready(){super.ready(),this._createDelegateAttrsObserver(),this._createDelegatePropsObserver()}_stateTargetChanged(e){e&&(this._ensureAttrsDelegated(),this._ensurePropsDelegated())}_createDelegateAttrsObserver(){this._createMethodObserver(`_delegateAttrsChanged(${this.constructor.delegateAttrs.join(", ")})`)}_createDelegatePropsObserver(){this._createMethodObserver(`_delegatePropsChanged(${this.constructor.delegateProps.join(", ")})`)}_ensureAttrsDelegated(){this.constructor.delegateAttrs.forEach(e=>{this._delegateAttribute(e,this[e])})}_ensurePropsDelegated(){this.constructor.delegateProps.forEach(e=>{this._delegateProperty(e,this[e])})}_delegateAttrsChanged(...e){this.constructor.delegateAttrs.forEach((n,s)=>{this._delegateAttribute(n,e[s])})}_delegatePropsChanged(...e){this.constructor.delegateProps.forEach((n,s)=>{this._delegateProperty(n,e[s])})}_delegateAttribute(e,n){this.stateTarget&&(e==="invalid"&&this._delegateAttribute("aria-invalid",n?"true":!1),typeof n=="boolean"?this.stateTarget.toggleAttribute(e,n):n?this.stateTarget.setAttribute(e,n):this.stateTarget.removeAttribute(e))}_delegateProperty(e,n){this.stateTarget&&(this.stateTarget[e]=n)}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ln=m(i=>class extends jt(Vt(Re(i))){static get constraints(){return["required"]}static get delegateAttrs(){return[...super.delegateAttrs,"required"]}ready(){super.ready(),this._createConstraintsObserver()}checkValidity(){return this.inputElement&&this._hasValidConstraints(this.constructor.constraints.map(e=>this[e]))?this.inputElement.checkValidity():!this.invalid}_hasValidConstraints(e){return e.some(n=>this.__isValidConstraint(n))}_createConstraintsObserver(){this._createMethodObserver(`_constraintsChanged(stateTarget, ${this.constructor.constraints.join(", ")})`)}_constraintsChanged(e,...n){if(!e)return;const s=this._hasValidConstraints(n),o=this.__previousHasConstraints&&!s;(this._hasValue||this.invalid)&&s?this._requestValidation():o&&!this.manualValidation&&this._setInvalid(!1),this.__previousHasConstraints=s}_onChange(e){e.stopPropagation(),this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{detail:{sourceEvent:e},bubbles:e.bubbles,cancelable:e.cancelable}))}__isValidConstraint(e){return!!e||e===0}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const In=i=>class extends Pt($t(Ln(Ht(xn(Fe(i)))))){static get properties(){return{allowedCharPattern:{type:String,observer:"_allowedCharPatternChanged"},autoselect:{type:Boolean,value:!1},name:{type:String,reflectToAttribute:!0},placeholder:{type:String,reflectToAttribute:!0},readonly:{type:Boolean,value:!1,reflectToAttribute:!0},title:{type:String,reflectToAttribute:!0}}}static get delegateAttrs(){return[...super.delegateAttrs,"name","type","placeholder","readonly","invalid","title"]}constructor(){super(),this._boundOnPaste=this._onPaste.bind(this),this._boundOnDrop=this._onDrop.bind(this),this._boundOnBeforeInput=this._onBeforeInput.bind(this)}get slotStyles(){const e=this.localName;return[`
          /* Needed for Safari, where ::slotted(...)::placeholder does not work */
          ${e} > :is(input[slot='input'], textarea[slot='textarea'])::placeholder {
            font: inherit;
            color: inherit;
          }

          /* Override built-in autofill styles */
          ${e} > input[slot='input']:autofill {
            -webkit-text-fill-color: var(--vaadin-input-field-autofill-color, black) !important;
            background-clip: text !important;
          }

          ${e}:has(> input[slot='input']:autofill)::part(input-field) {
            --vaadin-input-field-background: var(--vaadin-input-field-autofill-background, lightyellow) !important;
            --vaadin-input-field-value-color: var(--vaadin-input-field-autofill-color, black) !important;
            --vaadin-input-field-button-text-color: var(--vaadin-input-field-autofill-color, black) !important;
          }
        `]}_onFocus(e){super._onFocus(e),this.autoselect&&this.inputElement&&this.inputElement.select()}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("paste",this._boundOnPaste),e.addEventListener("drop",this._boundOnDrop),e.addEventListener("beforeinput",this._boundOnBeforeInput)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("paste",this._boundOnPaste),e.removeEventListener("drop",this._boundOnDrop),e.removeEventListener("beforeinput",this._boundOnBeforeInput)}_onKeyDown(e){super._onKeyDown(e),this.allowedCharPattern&&!this.__shouldAcceptKey(e)&&e.target===this.inputElement&&(e.preventDefault(),this._markInputPrevented())}_markInputPrevented(){this.setAttribute("input-prevented",""),this._preventInputDebouncer=L.debounce(this._preventInputDebouncer,Oi.after(200),()=>{this.removeAttribute("input-prevented")})}__shouldAcceptKey(e){return e.metaKey||e.ctrlKey||!e.key||e.key.length!==1||this.__allowedCharRegExp.test(e.key)}_onPaste(e){if(this.allowedCharPattern){const n=e.clipboardData.getData("text");this.__allowedTextRegExp.test(n)||(e.preventDefault(),this._markInputPrevented())}}_onDrop(e){if(this.allowedCharPattern){const n=e.dataTransfer.getData("text");this.__allowedTextRegExp.test(n)||(e.preventDefault(),this._markInputPrevented())}}_onBeforeInput(e){this.allowedCharPattern&&e.data&&!this.__allowedTextRegExp.test(e.data)&&(e.preventDefault(),this._markInputPrevented())}_allowedCharPatternChanged(e){if(e)try{this.__allowedCharRegExp=new RegExp(`^${e}$`,"u"),this.__allowedTextRegExp=new RegExp(`^${e}*$`,"u")}catch(n){console.error(n)}}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const He=i=>class extends In(i){static get properties(){return{autocomplete:{type:String},autocorrect:{type:String,reflectToAttribute:!0},autocapitalize:{type:String,reflectToAttribute:!0}}}static get delegateAttrs(){return[...super.delegateAttrs,"autocapitalize","autocomplete","autocorrect"]}_inputElementChanged(e){super._inputElementChanged(e),e&&(e.value&&e.value!==this.value&&(console.warn(`Please define value on the <${this.localName}> component!`),e.value=""),this.value&&(e.value=this.value))}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}_onInput(e){super._onInput(e),this.invalid&&this._requestValidation()}_valueChanged(e,n){super._valueChanged(e,n),n!==void 0&&this.invalid&&this._requestValidation()}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ae{constructor(t,e){this.input=t,this.__preventDuplicateLabelClick=this.__preventDuplicateLabelClick.bind(this),e.addEventListener("slot-content-changed",n=>{this.__initLabel(n.detail.node)}),this.__initLabel(e.node)}__initLabel(t){t&&(t.addEventListener("click",this.__preventDuplicateLabelClick),this.input&&t.setAttribute("for",this.input.id))}__preventDuplicateLabelClick(){const t=e=>{e.stopImmediatePropagation(),this.input.removeEventListener("click",t)};this.input.addEventListener("click",t)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Nn=i=>class extends He(i){static get properties(){return{maxlength:{type:Number},minlength:{type:Number},pattern:{type:String}}}static get delegateAttrs(){return[...super.delegateAttrs,"maxlength","minlength","pattern"]}static get constraints(){return[...super.constraints,"maxlength","minlength","pattern"]}constructor(){super(),this._setType("text")}get clearElement(){return this.$.clearButton}ready(){super.ready(),this.addController(new $e(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new ae(this.inputElement,this._labelController))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Dn extends Nn(b(C(g(y(_))))){static get is(){return"vaadin-text-field"}static get styles(){return[De]}render(){return p`
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
          theme="${z(this._theme)}"
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
    `}ready(){super.ready(),this._tooltipController=new q(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}_renderSuffix(){return p`
      <slot name="suffix" slot="suffix"></slot>
      <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
    `}}f(Dn);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ut=c`
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
 */class $n{saveFocus(t){this.focusNode=t||Z()}restoreFocus(t){const e=this.focusNode;if(!e)return;const n={preventScroll:t?t.preventScroll:!1,focusVisible:t?t.focusVisible:!1};Z()===document.body?setTimeout(()=>e.focus(n)):e.focus(n),this.focusNode=null}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ge=[];class Pn{constructor(t){this.host=t,this.__trapNode=null,this.__onKeyDown=this.__onKeyDown.bind(this)}get __focusableElements(){return _n(this.__trapNode)}get __focusedElementIndex(){const t=this.__focusableElements;return t.indexOf(t.filter(Lt).pop())}hostConnected(){document.addEventListener("keydown",this.__onKeyDown)}hostDisconnected(){document.removeEventListener("keydown",this.__onKeyDown)}trapFocus(t){if(this.__trapNode=t,this.__focusableElements.length===0)throw this.__trapNode=null,new Error("The trap node should have at least one focusable descendant or be focusable itself.");ge.push(this),this.__focusedElementIndex===-1&&this.__focusableElements[0].focus({focusVisible:oe()})}releaseFocus(){this.__trapNode=null,ge.pop()}__onKeyDown(t){if(this.__trapNode&&this===Array.from(ge).pop()&&t.key==="Tab"){t.preventDefault();const e=t.shiftKey;this.__focusNextElement(e)}}__focusNextElement(t=!1){const e=this.__focusableElements,n=t?-1:1,s=this.__focusedElementIndex,o=(e.length+s+n)%e.length,r=e[o];r.focus({focusVisible:!0}),r.localName==="input"&&r.select()}}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const zn=i=>class extends i{static get properties(){return{focusTrap:{type:Boolean,value:!1},restoreFocusOnClose:{type:Boolean,value:!1},restoreFocusNode:{type:HTMLElement}}}constructor(){super(),this.__focusTrapController=new Pn(this),this.__focusRestorationController=new $n}get _contentRoot(){return this}ready(){super.ready(),this.addController(this.__focusTrapController),this.addController(this.__focusRestorationController)}get _focusTrapRoot(){return this.$.overlay}_resetFocus(){if(this.focusTrap&&this.__focusTrapController.releaseFocus(),this.restoreFocusOnClose&&this._shouldRestoreFocus()){const e=oe(),n=!e;this.__focusRestorationController.restoreFocus({preventScroll:n,focusVisible:e})}}_saveFocus(){this.restoreFocusOnClose&&this.__focusRestorationController.saveFocus(this.restoreFocusNode)}_trapFocus(){this.focusTrap&&!pn(this._focusTrapRoot)&&this.__focusTrapController.trapFocus(this._focusTrapRoot)}_shouldRestoreFocus(){const e=Z();return e===document.body||this._deepContains(e)}_deepContains(e){if(this._contentRoot.contains(e))return!0;let n=e;const s=e.ownerDocument;for(;n&&n!==s&&n!==this._contentRoot;)n=n.parentNode||n.host;return n===this._contentRoot}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const X=new Set,J=()=>[...X].filter(i=>!i.hasAttribute("closing")),qt=i=>{const t=J(),e=t[t.indexOf(i)+1];return e?i._deepContains(e)?qt(e):!1:!0},ot=(i,t=e=>!0)=>{const e=J().filter(t);return i===e.pop()},Fn=i=>class extends i{get _last(){return ot(this)}get _isAttached(){return X.has(this)}bringToFront(){ot(this)||qt(this)||(this.matches(":popover-open")&&(this.hidePopover(),this.showPopover()),this._removeAttachedInstance(),this._appendAttachedInstance())}_enterModalState(){document.body.style.pointerEvents!=="none"&&(this._previousDocumentPointerEvents=document.body.style.pointerEvents,document.body.style.pointerEvents="none"),J().forEach(e=>{e!==this&&(e.$.overlay.style.pointerEvents="none")})}_exitModalState(){this._previousDocumentPointerEvents!==void 0&&(document.body.style.pointerEvents=this._previousDocumentPointerEvents,delete this._previousDocumentPointerEvents);const e=J();let n;for(;(n=e.pop())&&!(n!==this&&(n.$.overlay.style.removeProperty("pointer-events"),!n.modeless)););}_appendAttachedInstance(){X.add(this)}_removeAttachedInstance(){this._isAttached&&X.delete(this)}};/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Rn(i,t){let e=null,n;const s=document.documentElement;function o(){n&&clearTimeout(n),e&&e.disconnect(),e=null}function r(a=!1,l=1){o();const{left:d,top:v,width:w,height:T}=i.getBoundingClientRect();if(a||t(),!w||!T)return;const F=Math.floor(v),si=Math.floor(s.clientWidth-(d+w)),oi=Math.floor(s.clientHeight-(v+T)),ri=Math.floor(d),ai={rootMargin:`${-F}px ${-si}px ${-oi}px ${-ri}px`,threshold:Math.max(0,Math.min(1,l))||1};let Ke=!0;function li(di){const le=di[0].intersectionRatio;if(le!==l){if(!Ke)return r();le?r(!1,le):n=setTimeout(()=>{r(!1,1e-7)},1e3)}Ke=!1}e=new IntersectionObserver(li,ai),e.observe(i)}return r(!0),o}function u(i,t,e){const n=[i];i.owner&&n.push(i.owner),typeof e=="string"?n.forEach(s=>{s.setAttribute(t,e)}):e?n.forEach(s=>{s.setAttribute(t,"")}):n.forEach(s=>{s.removeAttribute(t)})}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Wt=i=>class extends zn(Fn(i)){static get properties(){return{opened:{type:Boolean,notify:!0,observer:"_openedChanged",reflectToAttribute:!0,sync:!0},owner:{type:Object,sync:!0},model:{type:Object,sync:!0},renderer:{type:Object,sync:!0},modeless:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_modelessChanged",sync:!0},hidden:{type:Boolean,reflectToAttribute:!0,observer:"_hiddenChanged",sync:!0},withBackdrop:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_withBackdropChanged",sync:!0}}}static get observers(){return["_rendererOrDataChanged(renderer, owner, model, opened)"]}get _rendererRoot(){return this}constructor(){super(),this._boundMouseDownListener=this._mouseDownListener.bind(this),this._boundMouseUpListener=this._mouseUpListener.bind(this),this._boundOutsideClickListener=this._outsideClickListener.bind(this),this._boundKeydownListener=this._keydownListener.bind(this),zt&&(this._boundIosResizeListener=()=>this._detectIosNavbar())}firstUpdated(){super.firstUpdated(),this.popover="manual",this.addEventListener("click",()=>{}),this.$.backdrop&&this.$.backdrop.addEventListener("click",()=>{}),this.addEventListener("mouseup",()=>{document.activeElement===document.body&&this.$.overlay.getAttribute("tabindex")==="0"&&this.$.overlay.focus()}),this.addEventListener("animationcancel",()=>{this._flushAnimation("opening"),this._flushAnimation("closing")})}connectedCallback(){super.connectedCallback(),this._boundIosResizeListener&&(this._detectIosNavbar(),window.addEventListener("resize",this._boundIosResizeListener))}disconnectedCallback(){super.disconnectedCallback(),this.__scheduledOpen&&(cancelAnimationFrame(this.__scheduledOpen),this.__scheduledOpen=null),this._boundIosResizeListener&&window.removeEventListener("resize",this._boundIosResizeListener)}requestContentUpdate(){this.renderer&&this.renderer.call(this.owner,this._rendererRoot,this.owner,this.model)}close(e){const n=new CustomEvent("vaadin-overlay-close",{bubbles:!0,cancelable:!0,detail:{overlay:this,sourceEvent:e}});this.dispatchEvent(n),document.body.dispatchEvent(n),n.defaultPrevented||(this.opened=!1)}setBounds(e,n=!0){const s=this.$.overlay,o={...e};n&&s.style.position!=="absolute"&&(s.style.position="absolute"),Object.keys(o).forEach(r=>{o[r]!==null&&!isNaN(o[r])&&(o[r]=`${o[r]}px`)}),Object.assign(s.style,o)}_detectIosNavbar(){if(!this.opened)return;const e=window.innerHeight,s=window.innerWidth>e,o=document.documentElement.clientHeight;s&&o>e?this.style.setProperty("--vaadin-overlay-viewport-bottom",`${o-e}px`):this.style.setProperty("--vaadin-overlay-viewport-bottom","0")}_shouldAddGlobalListeners(){return!this.modeless}_addGlobalListeners(){this.__hasGlobalListeners||(this.__hasGlobalListeners=!0,document.addEventListener("mousedown",this._boundMouseDownListener),document.addEventListener("mouseup",this._boundMouseUpListener),document.documentElement.addEventListener("click",this._boundOutsideClickListener,!0))}_removeGlobalListeners(){this.__hasGlobalListeners&&(this.__hasGlobalListeners=!1,document.removeEventListener("mousedown",this._boundMouseDownListener),document.removeEventListener("mouseup",this._boundMouseUpListener),document.documentElement.removeEventListener("click",this._boundOutsideClickListener,!0))}_rendererOrDataChanged(e,n,s,o){const r=this._oldOwner!==n||this._oldModel!==s;this._oldModel=s,this._oldOwner=n;const a=this._oldRenderer!==e,l=this._oldRenderer!==void 0;this._oldRenderer=e;const d=this._oldOpened!==o;this._oldOpened=o,a&&l&&(this._rendererRoot.innerHTML="",delete this._rendererRoot._$litPart$),o&&e&&(a||d||r)&&this.requestContentUpdate()}_modelessChanged(e){this.opened&&(this._shouldAddGlobalListeners()?this._addGlobalListeners():this._removeGlobalListeners()),e?this._exitModalState():this.opened&&this._enterModalState(),u(this,"modeless",e)}_withBackdropChanged(e){u(this,"with-backdrop",e)}_openedChanged(e,n){if(e){if(!this.isConnected){this.opened=!1;return}this._saveFocus(),this._animatedOpening(),this.__scheduledOpen=requestAnimationFrame(()=>{setTimeout(()=>{this._trapFocus();const s=new CustomEvent("vaadin-overlay-open",{detail:{overlay:this},bubbles:!0});this.dispatchEvent(s),document.body.dispatchEvent(s)})}),document.addEventListener("keydown",this._boundKeydownListener),this._shouldAddGlobalListeners()&&this._addGlobalListeners()}else n&&(this.__scheduledOpen&&(cancelAnimationFrame(this.__scheduledOpen),this.__scheduledOpen=null),this._resetFocus(),this._animatedClosing(),document.removeEventListener("keydown",this._boundKeydownListener),this._shouldAddGlobalListeners()&&this._removeGlobalListeners())}_hiddenChanged(e){e&&this.hasAttribute("closing")&&this._flushAnimation("closing")}_shouldAnimate(){const e=getComputedStyle(this),n=e.getPropertyValue("animation-name");return!(e.getPropertyValue("display")==="none")&&n&&n!=="none"}_enqueueAnimation(e,n){const s=`__${e}Handler`,o=r=>{r&&r.target!==this||(n(),this.removeEventListener("animationend",o),delete this[s])};this[s]=o,this.addEventListener("animationend",o)}_flushAnimation(e){const n=`__${e}Handler`;typeof this[n]=="function"&&this[n]()}_animatedOpening(){this._isAttached&&this.hasAttribute("closing")&&this._flushAnimation("closing"),this._attachOverlay(),this._appendAttachedInstance(),this.bringToFront(),this.modeless||this._enterModalState(),u(this,"opening",!0),this._shouldAnimate()?this._enqueueAnimation("opening",()=>{this._finishOpening()}):this._finishOpening()}_attachOverlay(){this.showPopover()}_finishOpening(){u(this,"opening",!1)}_finishClosing(){this._detachOverlay(),this._removeAttachedInstance(),this.$.overlay.style.removeProperty("pointer-events"),u(this,"closing",!1),this.dispatchEvent(new CustomEvent("vaadin-overlay-closed"))}_animatedClosing(){this.hasAttribute("opening")&&this._flushAnimation("opening"),this._isAttached&&(this._exitModalState(),u(this,"closing",!0),this.dispatchEvent(new CustomEvent("vaadin-overlay-closing")),this._shouldAnimate()?this._enqueueAnimation("closing",()=>{this._finishClosing()}):this._finishClosing())}_detachOverlay(){this.hidePopover()}_mouseDownListener(e){this._mouseDownInside=e.composedPath().indexOf(this.$.overlay)>=0}_mouseUpListener(e){this._mouseUpInside=e.composedPath().indexOf(this.$.overlay)>=0}_shouldCloseOnOutsideClick(e){return this._last}_outsideClickListener(e){if(e.composedPath().includes(this.$.overlay)||this._mouseDownInside||this._mouseUpInside){this._mouseDownInside=!1,this._mouseUpInside=!1;return}if(!this._shouldCloseOnOutsideClick(e))return;const n=new CustomEvent("vaadin-overlay-outside-click",{cancelable:!0,detail:{sourceEvent:e}});this.dispatchEvent(n),this.opened&&!n.defaultPrevented&&this.close(e)}_keydownListener(e){if(!(!this._last||e.defaultPrevented)&&!(!this._shouldAddGlobalListeners()&&!e.composedPath().includes(this._focusTrapRoot))&&e.key==="Escape"){const n=new CustomEvent("vaadin-overlay-escape-press",{cancelable:!0,detail:{sourceEvent:e}});this.dispatchEvent(n),this.opened&&!n.defaultPrevented&&this.close(e)}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const me={start:"top",end:"bottom"},be={start:"left",end:"right"},rt=new ResizeObserver(i=>{setTimeout(()=>{i.forEach(t=>{t.target.__overlay&&t.target.__overlay._updatePosition()})})}),Bn=i=>class extends i{static get properties(){return{positionTarget:{type:Object,value:null,sync:!0},horizontalAlign:{type:String,value:"start",sync:!0},verticalAlign:{type:String,value:"top",sync:!0},noHorizontalOverlap:{type:Boolean,value:!1,sync:!0},noVerticalOverlap:{type:Boolean,value:!1,sync:!0},requiredVerticalSpace:{type:Number,value:0,sync:!0}}}constructor(){super(),this.__onScroll=this.__onScroll.bind(this),this._updatePosition=this._updatePosition.bind(this)}connectedCallback(){super.connectedCallback(),this.opened&&this.__addUpdatePositionEventListeners()}disconnectedCallback(){super.disconnectedCallback(),this.__removeUpdatePositionEventListeners()}updated(e){if(super.updated(e),e.has("positionTarget")){const s=e.get("positionTarget");(!this.positionTarget&&s||this.positionTarget&&!s&&this.__margins)&&this.__resetPosition()}(e.has("opened")||e.has("positionTarget"))&&this.__updatePositionSettings(this.opened,this.positionTarget),["horizontalAlign","verticalAlign","noHorizontalOverlap","noVerticalOverlap","requiredVerticalSpace"].some(s=>e.has(s))&&this._updatePosition()}__addUpdatePositionEventListeners(){window.visualViewport.addEventListener("resize",this._updatePosition),window.visualViewport.addEventListener("scroll",this.__onScroll,!0),this.__positionTargetAncestorRootNodes=ln(this.positionTarget),this.__positionTargetAncestorRootNodes.forEach(e=>{e.addEventListener("scroll",this.__onScroll,!0)}),this.positionTarget&&(this.__observePositionTargetMove=Rn(this.positionTarget,()=>{this._updatePosition()}))}__removeUpdatePositionEventListeners(){window.visualViewport.removeEventListener("resize",this._updatePosition),window.visualViewport.removeEventListener("scroll",this.__onScroll,!0),this.__positionTargetAncestorRootNodes&&(this.__positionTargetAncestorRootNodes.forEach(e=>{e.removeEventListener("scroll",this.__onScroll,!0)}),this.__positionTargetAncestorRootNodes=null),this.__observePositionTargetMove&&(this.__observePositionTargetMove(),this.__observePositionTargetMove=null)}__updatePositionSettings(e,n){if(this.__removeUpdatePositionEventListeners(),n&&(n.__overlay=null,rt.unobserve(n),e&&(this.__addUpdatePositionEventListeners(),n.__overlay=this,rt.observe(n))),e){const s=getComputedStyle(this);this.__margins||(this.__margins={},["top","bottom","left","right"].forEach(o=>{this.__margins[o]=parseInt(s[o],10)})),this._updatePosition(),requestAnimationFrame(()=>this._updatePosition())}}__onScroll(e){e.target instanceof Node&&this._deepContains(e.target)||this._updatePosition()}__resetPosition(){this.__margins=null,Object.assign(this.style,{justifyContent:"",alignItems:"",top:"",bottom:"",left:"",right:""}),u(this,"bottom-aligned",!1),u(this,"top-aligned",!1),u(this,"end-aligned",!1),u(this,"start-aligned",!1)}_updatePosition(){if(!this.positionTarget||!this.opened||!this.__margins)return;const e=this.positionTarget.getBoundingClientRect();if(e.width===0&&e.height===0&&this.opened){this.opened=!1;return}const n=this.__shouldAlignStartVertically(e);this.style.justifyContent=n?"flex-start":"flex-end";const s=this.__isRTL,o=this.__shouldAlignStartHorizontally(e,s),r=!s&&o||s&&!o;this.style.alignItems=r?"flex-start":"flex-end";const a=this.getBoundingClientRect(),l=this.__calculatePositionInOneDimension(e,a,this.noVerticalOverlap,me,this,n),d=this.__calculatePositionInOneDimension(e,a,this.noHorizontalOverlap,be,this,o);Object.assign(this.style,l,d),u(this,"bottom-aligned",!n),u(this,"top-aligned",n),u(this,"end-aligned",!r),u(this,"start-aligned",r)}__shouldAlignStartHorizontally(e,n){const s=Math.max(this.__oldContentWidth||0,this.$.overlay.offsetWidth);this.__oldContentWidth=this.$.overlay.offsetWidth;const o=Math.min(window.innerWidth,document.documentElement.clientWidth),r=!n&&this.horizontalAlign==="start"||n&&this.horizontalAlign==="end";return this.__shouldAlignStart(e,s,o,this.__margins,r,this.noHorizontalOverlap,be)}__shouldAlignStartVertically(e){const n=this.requiredVerticalSpace||Math.max(this.__oldContentHeight||0,this.$.overlay.offsetHeight);this.__oldContentHeight=this.$.overlay.offsetHeight;const s=Math.min(window.innerHeight,document.documentElement.clientHeight),o=this.verticalAlign==="top";return this.__shouldAlignStart(e,n,s,this.__margins,o,this.noVerticalOverlap,me)}__shouldAlignStart(e,n,s,o,r,a,l){const d=s-e[a?l.end:l.start]-o[l.end],v=e[a?l.start:l.end]-o[l.start],w=r?d:v,F=w>(r?v:d)||w>n;return r===F}__adjustBottomProperty(e,n,s){let o;if(e===n.end){if(n.end===me.end){const r=Math.min(window.innerHeight,document.documentElement.clientHeight);if(s>r&&this.__oldViewportHeight){const a=this.__oldViewportHeight-r;o=s-a}this.__oldViewportHeight=r}if(n.end===be.end){const r=Math.min(window.innerWidth,document.documentElement.clientWidth);if(s>r&&this.__oldViewportWidth){const a=this.__oldViewportWidth-r;o=s-a}this.__oldViewportWidth=r}}return o}__calculatePositionInOneDimension(e,n,s,o,r,a){const l=a?o.start:o.end,d=a?o.end:o.start,v=parseFloat(r.style[l]||getComputedStyle(r)[l]),w=this.__adjustBottomProperty(l,o,v),T=n[a?o.start:o.end]-e[s===a?o.end:o.start],F=w?`${w}px`:`${v+T*(a?-1:1)}px`;return{[l]:F,[d]:""}}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Vn=i=>class extends Bn(Wt(i)){static get properties(){return{position:{type:String,reflectToAttribute:!0}}}_updatePosition(){if(super._updatePosition(),!this.positionTarget||!this.opened)return;this.removeAttribute("arrow-centered");const e=this.positionTarget.getBoundingClientRect(),n=this.$.overlay.getBoundingClientRect(),s=Math.min(window.innerWidth,document.documentElement.clientWidth);let o=!1;if(n.left<0?(this.style.left="0px",this.style.right="",o=!0):n.right>s&&(this.style.right="0px",this.style.left="",o=!0),!o&&(this.position==="bottom"||this.position==="top")){const r=e.width/2-n.width/2;if(this.style.left){const a=n.left+r;a>0&&(this.style.left=`${a}px`,this.setAttribute("arrow-centered",""))}if(this.style.right){const a=parseFloat(this.style.right)+r;a>0&&(this.style.right=`${a}px`,this.setAttribute("arrow-centered",""))}}if(this.position==="start"||this.position==="end"){const r=e.height/2-n.height/2;this.style.top=`${n.top+r}px`}}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Hn=c`
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
 */class jn extends Vn(ie(b(g(y(_))))){static get is(){return"vaadin-tooltip-overlay"}static get styles(){return[Ut,Hn]}render(){return p`
      <div part="overlay" id="overlay">
        <div part="content" id="content"><slot></slot></div>
      </div>
    `}}f(jn);/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Un=i=>class extends i{static get properties(){return{position:{type:String},_position:{type:String,value:"bottom"},__effectivePosition:{type:String,computed:"__computePosition(position, _position)"}}}__computeHorizontalAlign(e){return["top-end","bottom-end","start-top","start","start-bottom"].includes(e)?"end":"start"}__computeNoHorizontalOverlap(e){return["start-top","start","start-bottom","end-top","end","end-bottom"].includes(e)}__computeNoVerticalOverlap(e){return["top-start","top-end","top","bottom-start","bottom","bottom-end"].includes(e)}__computeVerticalAlign(e){return["top-start","top-end","top","start-bottom","end-bottom"].includes(e)?"bottom":"top"}__computePosition(e,n){return e||n}};/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const qn=i=>class extends i{static get properties(){return{for:{type:String,observer:"__forChanged"},target:{type:Object},__isConnected:{type:Boolean,sync:!0}}}static get observers(){return["__targetOrConnectedChanged(target, __isConnected)"]}connectedCallback(){super.connectedCallback(),this.__isConnected=!0}disconnectedCallback(){super.disconnectedCallback(),this.__isConnected=!1}__forChanged(e){e&&(this.__setTargetByIdDebouncer=L.debounce(this.__setTargetByIdDebouncer,mt,()=>this.__setTargetById(e)))}__setTargetById(e){if(!this.isConnected)return;const n=this.getRootNode().getElementById(e);n?this.target=n:console.warn(`No element with id="${e}" set via "for" property found on the page.`)}__targetOrConnectedChanged(e,n){this.__previousTarget&&(this.__previousTarget!==e||!n)&&this._removeTargetListeners(this.__previousTarget),e&&n&&this._addTargetListeners(e),this.__previousTarget=e}_addTargetListeners(e){}_removeTargetListeners(e){}},$=500;let Kt=$,Gt=$,Yt=$;const I=new Set;let B=!1,N=null,V=null;class Wn{constructor(t){this.host=t}get focusDelay(){const t=this.host;return t.focusDelay!=null&&t.focusDelay>=0?t.focusDelay:Kt}get hoverDelay(){const t=this.host;return t.hoverDelay!=null&&t.hoverDelay>=0?t.hoverDelay:Gt}get hideDelay(){const t=this.host;return t.hideDelay!=null&&t.hideDelay>=0?t.hideDelay:Yt}get isClosing(){return I.has(this.host)}open(t={immediate:!1}){const{immediate:e,hover:n,focus:s}=t,o=n&&this.hoverDelay>0,r=s&&this.focusDelay>0;!e&&(o||r)&&!this.__closeTimeout?this.__warmupTooltip(r):this.__showTooltip()}close(t){!t&&this.hideDelay>0?this.__scheduleClose():(this.__abortClose(),this._setOpened(!1)),this.__abortWarmUp(),B&&(this.__abortCooldown(),this.__scheduleCooldown())}_isOpened(){return this.host.opened}_setOpened(t){this.host.opened=t}__flushClosingTooltips(){I.forEach(t=>{t._stateController.close(!0),I.delete(t)})}__showTooltip(){this.__abortClose(),this.__flushClosingTooltips(),this._setOpened(!0),B=!0,this.__abortWarmUp(),this.__abortCooldown()}__warmupTooltip(t){this._isOpened()||(B?this.__showTooltip():N==null&&this.__scheduleWarmUp(t))}__abortClose(){this.__closeTimeout&&(clearTimeout(this.__closeTimeout),this.__closeTimeout=null),this.isClosing&&I.delete(this.host)}__abortCooldown(){V&&(clearTimeout(V),V=null)}__abortWarmUp(){N&&(clearTimeout(N),N=null)}__scheduleClose(){this._isOpened()&&!this.isClosing&&(I.add(this.host),this.__closeTimeout=setTimeout(()=>{I.delete(this.host),this.__closeTimeout=null,this._setOpened(!1)},this.hideDelay))}__scheduleCooldown(){V=setTimeout(()=>{V=null,B=!1},this.hideDelay)}__scheduleWarmUp(t){const e=t?this.focusDelay:this.hoverDelay;N=setTimeout(()=>{N=null,B=!0,this.__showTooltip()},e)}}const Kn=i=>class extends Un(qn(i)){static get properties(){return{ariaTarget:{type:Object},context:{type:Object,value:()=>({})},focusDelay:{type:Number},generator:{type:Object},hideDelay:{type:Number},hoverDelay:{type:Number},manual:{type:Boolean,value:!1,sync:!0},opened:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"__openedChanged",sync:!0},shouldShow:{type:Object,value:()=>(e,n)=>!0},text:{type:String},markdown:{type:Boolean,value:!1,reflectToAttribute:!0},_effectiveAriaTarget:{type:Object,computed:"__computeAriaTarget(ariaTarget, target)",observer:"__effectiveAriaTargetChanged"},__isTargetHidden:{type:Boolean,value:!1},_isConnected:{type:Boolean,sync:!0}}}static setDefaultFocusDelay(e){Kt=e!=null&&e>=0?e:$}static setDefaultHideDelay(e){Yt=e!=null&&e>=0?e:$}static setDefaultHoverDelay(e){Gt=e!=null&&e>=0?e:$}constructor(){super(),this._uniqueId=`vaadin-tooltip-${St()}`,this.__onFocusin=this.__onFocusin.bind(this),this.__onFocusout=this.__onFocusout.bind(this),this.__onMouseDown=this.__onMouseDown.bind(this),this.__onMouseEnter=this.__onMouseEnter.bind(this),this.__onMouseLeave=this.__onMouseLeave.bind(this),this.__onKeyDown=this.__onKeyDown.bind(this),this.__onOverlayOpen=this.__onOverlayOpen.bind(this),this.__targetVisibilityObserver=new IntersectionObserver(e=>{e.forEach(n=>this.__onTargetVisibilityChange(n.isIntersecting))},{threshold:0}),this._stateController=new Wn(this)}connectedCallback(){super.connectedCallback(),this._isConnected=!0,document.body.addEventListener("vaadin-overlay-open",this.__onOverlayOpen)}disconnectedCallback(){super.disconnectedCallback(),this.opened&&!this.manual&&this._stateController.close(!0),this._isConnected=!1,document.body.removeEventListener("vaadin-overlay-open",this.__onOverlayOpen)}ready(){super.ready(),this._overlayElement=this.$.overlay,this.__contentController=new U(this,"overlay","div",{initializer:e=>{e.id=this._uniqueId,e.setAttribute("role","tooltip"),this.__contentNode=e}}),this.addController(this.__contentController)}updated(e){super.updated(e),(e.has("text")||e.has("generator")||e.has("context")||e.has("markdown"))&&this.__updateContent()}__openedChanged(e,n){e?document.addEventListener("keydown",this.__onKeyDown,!0):n&&document.removeEventListener("keydown",this.__onKeyDown,!0)}_addTargetListeners(e){e.addEventListener("mouseenter",this.__onMouseEnter),e.addEventListener("mouseleave",this.__onMouseLeave),e.addEventListener("focusin",this.__onFocusin),e.addEventListener("focusout",this.__onFocusout),e.addEventListener("mousedown",this.__onMouseDown),requestAnimationFrame(()=>{this.__targetVisibilityObserver.observe(e)})}_removeTargetListeners(e){e.removeEventListener("mouseenter",this.__onMouseEnter),e.removeEventListener("mouseleave",this.__onMouseLeave),e.removeEventListener("focusin",this.__onFocusin),e.removeEventListener("focusout",this.__onFocusout),e.removeEventListener("mousedown",this.__onMouseDown),this.__targetVisibilityObserver.unobserve(e)}__onFocusin(e){this.manual||oe()&&(this.target.contains(e.relatedTarget)||this.__isShouldShow()&&(this._overlayElement.hasAttribute("hidden")||(this.__focusInside=!0,!this.__isTargetHidden&&(!this.__hoverInside||!this.opened)&&this._stateController.open({focus:!0}))))}__onFocusout(e){this.manual||this.target.contains(e.relatedTarget)||(this.__focusInside=!1,this.__hoverInside||this._stateController.close(!0))}__onKeyDown(e){this.manual||e.key==="Escape"&&(e.stopPropagation(),this._stateController.close(!0))}__onMouseDown(){this.manual||this._stateController.close(!0)}__onMouseEnter(){this.manual||this.__isShouldShow()&&(this._overlayElement.hasAttribute("hidden")||this.__hoverInside||(this.__hoverInside=!0,!this.__isTargetHidden&&(!this.__focusInside||!this.opened)&&this._stateController.open({hover:!0})))}__onMouseLeave(e){e.relatedTarget!==this._overlayElement&&this.__handleMouseLeave()}__onOverlayMouseEnter(){this.manual||this._stateController.isClosing&&this._stateController.open({immediate:!0})}__onOverlayMouseLeave(e){e.relatedTarget!==this.target&&this.__handleMouseLeave()}__onOverlayMouseDown(e){e.stopPropagation()}__onOverlayClick(e){e.stopPropagation()}__handleMouseLeave(){this.manual||(this.__hoverInside=!1,this.__focusInside||this._stateController.close())}__onOverlayOpen(){this.manual||this._overlayElement.opened&&!this._overlayElement._last&&this._stateController.close(!0)}__onTargetVisibilityChange(e){if(this.manual)return;const n=this.__isTargetHidden;if(this.__isTargetHidden=!e,n&&e&&(this.__focusInside||this.__hoverInside)){this._stateController.open({immediate:!0});return}!e&&this.opened&&this._stateController.close(!0)}__isShouldShow(){return!(typeof this.shouldShow=="function"&&this.shouldShow(this.target,this.context)!==!0)}async __updateContent(){const e=typeof this.generator=="function"?this.generator(this.context):this.text;this.markdown&&e?(await this.constructor.__importMarkdownHelpers()).renderMarkdownToElement(this.__contentNode,e):this.__contentNode.textContent=e||"",this.$.overlay.toggleAttribute("hidden",this.__contentNode.textContent.trim()===""),this.dispatchEvent(new CustomEvent("content-changed",{detail:{content:this.__contentNode.textContent}}))}__computeAriaTarget(e,n){const s=r=>r&&r.nodeType===Node.ELEMENT_NODE,o=Array.isArray(e)?e.some(s):e;return e===null||o?e:n}__effectiveAriaTargetChanged(e,n){n&&[n].flat().forEach(s=>{At(s,"aria-describedby",this._uniqueId)}),e&&[e].flat().forEach(s=>{Ne(s,"aria-describedby",this._uniqueId)})}static __importMarkdownHelpers(){return this.__markdownHelpers||(this.__markdownHelpers=pi(()=>import("./markdown-helpers-RM02npbm.js"),[],import.meta.url)),this.__markdownHelpers}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Gn extends Kn(ne(C(g(_)))){static get is(){return"vaadin-tooltip"}static get styles(){return c`
      :host {
        display: contents;
      }
    `}render(){const t=this.__effectivePosition;return p`
      <vaadin-tooltip-overlay
        id="overlay"
        .owner="${this}"
        theme="${z(this._theme)}"
        .opened="${this._isConnected&&this.opened}"
        .positionTarget="${this.target}"
        .position="${t}"
        ?no-horizontal-overlap="${this.__computeNoHorizontalOverlap(t)}"
        ?no-vertical-overlap="${this.__computeNoVerticalOverlap(t)}"
        .horizontalAlign="${this.__computeHorizontalAlign(t)}"
        .verticalAlign="${this.__computeVerticalAlign(t)}"
        @click="${this.__onOverlayClick}"
        @mousedown="${this.__onOverlayMouseDown}"
        @mouseenter="${this.__onOverlayMouseEnter}"
        @mouseleave="${this.__onOverlayMouseLeave}"
        modeless
        ?markdown="${this.markdown}"
        exportparts="overlay, content"
        ><slot name="overlay"></slot
      ></vaadin-tooltip-overlay>
    `}}f(Gn);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Yn=c`
  [part='input-field'] {
    overflow: auto;
    scroll-padding: var(
      --vaadin-input-field-padding,
      var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container)
    );
  }

  ::slotted(textarea) {
    resize: none;
    white-space: pre-wrap;
  }

  [part='input-field'] ::slotted(:not(textarea)),
  [part~='clear-button'] {
    align-self: flex-start;
    position: sticky;
    top: 0;
  }

  [part~='clear-button'] {
    top: min(0px, (24px - 1lh) / -2);
  }

  /* Workaround https://bugzilla.mozilla.org/show_bug.cgi?id=1739079 */
  :host([disabled]) ::slotted(textarea) {
    user-select: none;
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const K=new ResizeObserver(i=>{setTimeout(()=>{i.forEach(t=>{t.target.isConnected&&(t.target.resizables?t.target.resizables.forEach(e=>{e._onResize(t.contentRect)}):t.target._onResize(t.contentRect))})})}),Xn=m(i=>class extends i{get _observeParent(){return!1}connectedCallback(){if(super.connectedCallback(),K.observe(this),this._observeParent){const e=this.parentNode instanceof ShadowRoot?this.parentNode.host:this.parentNode;e.resizables||(e.resizables=new Set,K.observe(e)),e.resizables.add(this),this.__parent=e}}disconnectedCallback(){super.disconnectedCallback(),K.unobserve(this);const e=this.__parent;if(this._observeParent&&e){const n=e.resizables;n&&(n.delete(this),n.size===0&&K.unobserve(e)),this.__parent=null}}_onResize(e){}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Zn extends U{constructor(t,e){super(t,"textarea","textarea",{initializer:(n,s)=>{const o=s.getAttribute("value");o&&(n.value=o);const r=s.getAttribute("name");r&&n.setAttribute("name",r),n.id=this.defaultId,typeof e=="function"&&e(n)},useUniqueId:!0})}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Jn=i=>class extends Xn(He(i)){static get properties(){return{maxlength:{type:Number},minlength:{type:Number},pattern:{type:String},minRows:{type:Number,value:2,observer:"__minRowsChanged"},maxRows:{type:Number}}}static get delegateAttrs(){return[...super.delegateAttrs,"maxlength","minlength","pattern"]}static get constraints(){return[...super.constraints,"maxlength","minlength","pattern"]}static get observers(){return["__updateMinHeight(minRows, inputElement)","__updateMaxHeight(maxRows, inputElement, _inputField)"]}get clearElement(){return this.$.clearButton}_onResize(){this._updateHeight(),this.__scrollPositionUpdated()}_onScroll(){this.__scrollPositionUpdated()}ready(){super.ready(),this.__textAreaController=new Zn(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e}),this.addController(this.__textAreaController),this.addController(new ae(this.inputElement,this._labelController)),this._inputField=this.shadowRoot.querySelector("[part=input-field]"),this._inputField.addEventListener("wheel",e=>{const n=this._inputField.scrollTop;this._inputField.scrollTop+=e.deltaY,n!==this._inputField.scrollTop&&(e.preventDefault(),this.__scrollPositionUpdated())}),this._updateHeight(),this.__scrollPositionUpdated()}__scrollPositionUpdated(){this._inputField.style.setProperty("--_text-area-vertical-scroll-position","0px"),this._inputField.style.setProperty("--_text-area-vertical-scroll-position",`${this._inputField.scrollTop}px`)}_valueChanged(e,n){super._valueChanged(e,n),this._updateHeight()}_updateHeight(){const e=this.inputElement,n=this._inputField;if(!e||!n)return;const s=n.scrollTop,o=this.value?this.value.length:0;if(this._oldValueLength>=o){const a=getComputedStyle(n).height,l=getComputedStyle(e).width;n.style.height=a,e.style.maxWidth=l,e.style.alignSelf="flex-start",e.style.height="auto"}this._oldValueLength=o;const r=e.scrollHeight;r>e.clientHeight&&(e.style.height=`${r}px`),e.style.removeProperty("max-width"),e.style.removeProperty("align-self"),n.style.removeProperty("height"),n.scrollTop=s,this.__updateMaxHeight(this.maxRows)}__updateMinHeight(e){this.inputElement&&this.inputElement===this.__textAreaController.defaultNode&&(this.inputElement.rows=Math.max(e,1))}__updateMaxHeight(e){if(!(!this._inputField||!this.inputElement))if(e){const n=getComputedStyle(this.inputElement),s=getComputedStyle(this._inputField),r=parseFloat(n.lineHeight)*e,a=parseFloat(n.paddingTop)+parseFloat(n.paddingBottom)+parseFloat(n.marginTop)+parseFloat(n.marginBottom)+parseFloat(s.borderTopWidth)+parseFloat(s.borderBottomWidth)+parseFloat(s.paddingTop)+parseFloat(s.paddingBottom),l=Math.ceil(r+a);this._inputField.style.setProperty("max-height",`${l}px`)}else this._inputField.style.removeProperty("max-height")}__minRowsChanged(e){e<1&&console.warn("<vaadin-text-area> minRows must be at least 1.")}scrollToStart(){this._inputField.scrollTop=0}scrollToEnd(){this._inputField.scrollTop=this._inputField.scrollHeight}checkValidity(){if(!super.checkValidity())return!1;if(!this.pattern||!this.inputElement.value)return!0;try{const e=this.inputElement.value.match(this.pattern);return e?e[0]===e.input:!1}catch{return!0}}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Qn extends Jn(b(C(g(y(_))))){static get is(){return"vaadin-text-area"}static get styles(){return[De,Yn]}render(){return p`
      <div class="vaadin-text-area-container">
        <div part="label">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true" @click="${this.focus}"></span>
        </div>

        <vaadin-input-container
          part="input-field"
          .readonly="${this.readonly}"
          .disabled="${this.disabled}"
          .invalid="${this.invalid}"
          theme="${z(this._theme)}"
          @scroll="${this._onScroll}"
        >
          <slot name="prefix" slot="prefix"></slot>
          <slot name="textarea"></slot>
          <slot name="suffix" slot="suffix"></slot>
          <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
        </vaadin-input-container>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>

        <slot name="tooltip"></slot>
      </div>
    `}ready(){super.ready(),this._tooltipController=new q(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}}f(Qn);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const es=c`
  :host([step-buttons-visible]) ::slotted(input) {
    text-align: center;
  }

  [part~='decrease-button']::before {
    mask-image: var(--_vaadin-icon-minus);
  }

  [part~='increase-button']::before {
    mask-image: var(--_vaadin-icon-plus);
  }

  :host([dir='rtl']) [part='input-field'] {
    direction: ltr;
  }

  :host([readonly]) [part$='button'] {
    pointer-events: none;
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const at="NaN",ts=i=>class extends He(i){static get properties(){return{min:{type:Number},max:{type:Number},step:{type:Number},stepButtonsVisible:{type:Boolean,value:!1,reflectToAttribute:!0}}}static get observers(){return["_stepChanged(step, inputElement)"]}static get delegateProps(){return[...super.delegateProps,"min","max"]}static get constraints(){return[...super.constraints,"min","max","step"]}constructor(){super(),this._setType("number"),this.__onWheel=this.__onWheel.bind(this)}get slotStyles(){const e=this.localName;return[`
          ${e} input[type="number"]::-webkit-outer-spin-button,
          ${e} input[type="number"]::-webkit-inner-spin-button {
            appearance: none;
            margin: 0;
          }

          ${e} input[type="number"] {
            appearance: textfield;
          }

          ${e}[dir='rtl'] input[type="number"]::placeholder {
            direction: rtl;
          }

          ${e}[dir='rtl']:not([step-buttons-visible]) input[type="number"]::placeholder {
            text-align: left;
          }
        `]}get clearElement(){return this.$.clearButton}get __hasUnparsableValue(){return this._inputElementValue===at}ready(){super.ready(),this.addController(new $e(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new ae(this.inputElement,this._labelController)),this._tooltipController=new q(this),this.addController(this._tooltipController),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement)}checkValidity(){return this.inputElement?this.inputElement.checkValidity():!this.invalid}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("wheel",this.__onWheel)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("wheel",this.__onWheel)}__onWheel(e){this.hasAttribute("focused")&&e.preventDefault()}_onDecreaseButtonTouchend(e){e.cancelable&&(e.preventDefault(),this.__blurActiveElement(),this._decreaseValue())}_onIncreaseButtonTouchend(e){e.cancelable&&(e.preventDefault(),this.__blurActiveElement(),this._increaseValue())}__blurActiveElement(){const e=Z();e&&e!==this.inputElement&&e.blur()}_onDecreaseButtonClick(){this._decreaseValue()}_onIncreaseButtonClick(){this._increaseValue()}_decreaseValue(){this._incrementValue(-1)}_increaseValue(){this._incrementValue(1)}_incrementValue(e){if(this.disabled||this.readonly)return;const n=this.step||1;let s=parseFloat(this.value);this.value?s<this.min?(e=0,s=this.min):s>this.max&&(e=0,s=this.max):this.min===0&&e<0||this.max===0&&e>0||this.max===0&&this.min===0?(e=0,s=0):(this.max==null||this.max>=0)&&(this.min==null||this.min<=0)?s=0:this.min>0?(s=this.min,this.max<0&&e<0&&(s=this.max),e=0):this.max<0&&(s=this.max,e<0?e=0:this._getIncrement(1,s-n)>this.max?s-=2*n:s-=n);const o=this._getIncrement(e,s);(!this.value||e===0||this._incrementIsInsideTheLimits(e,s))&&(this.inputElement.value=String(parseFloat(o)),this.inputElement.dispatchEvent(new Event("input",{bubbles:!0,composed:!0})),this.__commitValueChange())}_getIncrement(e,n){let s=this.step||1,o=this.min||0;const r=Math.max(this._getMultiplier(n),this._getMultiplier(s),this._getMultiplier(o));s*=r,n=Math.round(n*r),o*=r;const a=(n-o)%s;return e>0?(n-a+s)/r:e<0?(n-(a||s))/r:n/r}_getDecimalCount(e){const n=String(e),s=n.indexOf(".");return s===-1?1:n.length-s-1}_getMultiplier(e){if(!isNaN(e))return 10**this._getDecimalCount(e)}_incrementIsInsideTheLimits(e,n){return e<0?this.min==null||this._getIncrement(e,n)>=this.min:e>0?this.max==null||this._getIncrement(e,n)<=this.max:this._getIncrement(e,n)<=this.max&&this._getIncrement(e,n)>=this.min}_isButtonEnabled(e){const n=e*(this.step||1),s=parseFloat(this.value);return!this.value||!this.disabled&&this._incrementIsInsideTheLimits(n,s)}_stepChanged(e,n){n&&(n.step=e||"any")}_valueChanged(e,n){e&&isNaN(parseFloat(e))?this.value="":typeof this.value!="string"&&(this.value=String(this.value)),super._valueChanged(this.value,n),this.__keepCommittedValue||(this.__committedValue=this.value,this.__committedUnparsableValueStatus=!1)}_onKeyDown(e){e.key==="ArrowUp"?(e.preventDefault(),this._increaseValue()):e.key==="ArrowDown"&&(e.preventDefault(),this._decreaseValue()),super._onKeyDown(e)}_onInput(e){this.__keepCommittedValue=!0,super._onInput(e),this.__keepCommittedValue=!1}_onChange(e){e.stopPropagation()}_onClearAction(e){super._onClearAction(e),this.__commitValueChange()}_setFocused(e){super._setFocused(e),e||this.__commitValueChange()}_onEnter(e){super._onEnter(e),this.__commitValueChange()}__commitValueChange(){this.__committedValue!==this.value?(this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{bubbles:!0}))):this.__committedUnparsableValueStatus!==this.__hasUnparsableValue&&(this._requestValidation(),this.dispatchEvent(new CustomEvent("unparsable-change"))),this.__committedValue=this.value,this.__committedUnparsableValueStatus=this.__hasUnparsableValue}get _inputElementValue(){return this.inputElement&&this.inputElement.validity.badInput?at:super._inputElementValue}set _inputElementValue(e){super._inputElementValue=e}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Xt extends ts(b(C(g(y(_))))){static get is(){return"vaadin-number-field"}static get styles(){return[De,es]}render(){return p`
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
          theme="${z(this._theme)}"
        >
          <div
            part="field-button decrease-button"
            ?disabled="${!this._isButtonEnabled(-1,this.value,this.min,this.max,this.step)}"
            ?hidden="${!this.stepButtonsVisible}"
            @click="${this._onDecreaseButtonClick}"
            @touchend="${this._onDecreaseButtonTouchend}"
            aria-hidden="true"
            slot="prefix"
          ></div>
          <slot name="prefix" slot="prefix"></slot>
          <slot name="input"></slot>
          <slot name="suffix" slot="suffix"></slot>
          <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
          <div
            part="field-button increase-button"
            ?disabled="${!this._isButtonEnabled(1,this.value,this.min,this.max,this.step)}"
            ?hidden="${!this.stepButtonsVisible}"
            @click="${this._onIncreaseButtonClick}"
            @touchend="${this._onIncreaseButtonTouchend}"
            aria-hidden="true"
            slot="suffix"
          ></div>
        </vaadin-input-container>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>

        <slot name="tooltip"></slot>
      </div>
    `}}f(Xt);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class is extends Xt{static get is(){return"vaadin-integer-field"}constructor(){super(),this.allowedCharPattern="[-+\\d]"}_valueChanged(t,e){if(t!==""&&!this.__isInteger(t)){console.warn(`Trying to set non-integer value "${t}" to <vaadin-integer-field>. Clearing the value.`),this.value="";return}super._valueChanged(t,e)}_stepChanged(t,e){if(t!=null&&!this.__hasOnlyDigits(t)){console.warn(`<vaadin-integer-field> The \`step\` property must be a positive integer but \`${t}\` was provided, so the property was reset to \`null\`.`),this.step=null;return}super._stepChanged(t,e)}__isInteger(t){return/^(-\d)?\d*$/u.test(String(t))}__hasOnlyDigits(t){return/^\d+$/u.test(String(t))}}f(is);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ns=(i,t=i)=>c`
  :host {
    align-items: baseline;
    column-gap: var(--vaadin-${h(t)}-gap, var(--vaadin-gap-s));
    grid-template: none;
    grid-template-columns: auto 1fr;
    grid-template-rows: repeat(auto-fill, minmax(0, max-content));
    -webkit-tap-highlight-color: transparent;
    --_cursor: var(--vaadin-clickable-cursor);
  }

  :host([disabled]) {
    --_cursor: var(--vaadin-disabled-cursor);
  }

  :host(:not([has-label])) {
    column-gap: 0;
  }

  [part='${h(i)}'],
  ::slotted(input),
  [part='label'],
  ::slotted(label) {
    grid-row: 1;
  }

  [part='label'],
  ::slotted(label) {
    font-size: var(--vaadin-${h(t)}-label-font-size, var(--vaadin-input-field-label-font-size, inherit));
    line-height: var(--vaadin-${h(t)}-label-line-height, var(--vaadin-input-field-label-line-height, inherit));
    font-weight: var(--vaadin-${h(t)}-font-weight, var(--vaadin-input-field-label-font-weight, 500));
    color: var(--vaadin-${h(t)}-label-color, var(--vaadin-input-field-label-color, var(--vaadin-text-color)));
    word-break: break-word;
    cursor: var(--_cursor);
    /* TODO clicking the label part doesn't toggle the checked state, even though it triggers the active state */
  }

  [part='${h(i)}'],
  ::slotted(input) {
    grid-column: 1;
  }

  [part='label'],
  [part='helper-text'],
  [part='error-message'] {
    margin-bottom: 0;
    grid-column: 2;
    width: auto;
    min-width: auto;
  }

  [part='helper-text'],
  [part='error-message'] {
    margin-top: var(--_gap-s);
    grid-row: auto;
  }

  /* Baseline vertical alignment */
  :host::before {
    grid-row: 1;
    margin: 0;
    padding: 0;
    border: 0;
  }

  /* visually hidden */
  ::slotted(input) {
    cursor: inherit;
    align-self: stretch;
    appearance: none;
    cursor: var(--_cursor);
    /* Ensure minimum click target (WCAG) */
    width: 2px;
    height: 2px;
    scale: 12;
    margin: auto !important;
  }

  /* Control container (checkbox, radio button) */
  [part='${h(i)}'] {
    background: var(--vaadin-${h(t)}-background, var(--vaadin-background-color));
    border-color: var(--vaadin-${h(t)}-border-color, var(--vaadin-input-field-border-color, var(--vaadin-border-color)));
    border-radius: var(--vaadin-${h(t)}-border-radius, var(--vaadin-radius-s));
    border-style: var(--_border-style, solid);
    --_border-width: var(--vaadin-${h(t)}-border-width, var(--vaadin-input-field-border-width, 1px));
    border-width: var(--_border-width);
    box-sizing: border-box;
    --_color: var(--vaadin-${h(t)}-marker-color, var(--vaadin-${h(t)}-background, var(--vaadin-background-color)));
    color: var(--_color);
    height: var(--vaadin-${h(t)}-size, 1lh);
    width: var(--vaadin-${h(t)}-size, 1lh);
    position: relative;
    cursor: var(--_cursor);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  :host(:is([checked], [indeterminate])) {
    --vaadin-${h(t)}-background: var(--vaadin-text-color);
    --vaadin-${h(t)}-border-color: transparent;
  }

  :host([disabled]) {
    --vaadin-${h(t)}-background: var(--vaadin-input-field-disabled-background, var(--vaadin-background-container-strong));
    --vaadin-${h(t)}-border-color: transparent;
    --vaadin-${h(t)}-marker-color: var(--vaadin-text-color-disabled);
  }

  /* Focus ring */
  :host([focus-ring]) [part='${h(i)}'] {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--_border-width) * -1);
  }

  :host([focus-ring]:is([checked], [indeterminate])) [part='${h(i)}'] {
    outline-offset: 1px;
  }

  :host([readonly][focus-ring]) [part='${h(i)}'] {
    --vaadin-${h(t)}-border-color: transparent;
    outline-offset: calc(var(--_border-width) * -1);
    outline-style: dashed;
  }

  /* Checked indicator (checkmark, dot) */
  [part='${h(i)}']::after {
    content: '\\2003' / '';
    background: currentColor;
    border-radius: inherit;
    display: flex;
    align-items: center;
    --_filter: var(--vaadin-${h(t)}-marker-color, saturate(0) invert(1) hue-rotate(180deg) contrast(100) brightness(100));
    filter: var(--_filter);
  }

  :host(:not([checked], [indeterminate])) [part='${h(i)}']::after {
    opacity: 0;
  }

  @media (forced-colors: active) {
    :host(:is([checked], [indeterminate])) {
      --vaadin-${h(t)}-border-color: CanvasText !important;
    }

    :host(:is([checked], [indeterminate])) [part='${h(i)}'] {
      background: SelectedItem !important;
    }

    :host(:is([checked], [indeterminate])) [part='${h(i)}']::after {
      background: SelectedItemText !important;
    }

    :host([readonly]) [part='${h(i)}']::after {
      background: CanvasText !important;
    }

    :host([disabled]) {
      --vaadin-${h(t)}-border-color: GrayText !important;
    }

    :host([disabled]) [part='${h(i)}']::after {
      background: GrayText !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ss=c`
  [part='checkbox'] {
    color: var(--vaadin-checkbox-checkmark-color, var(--_color));
  }

  [part='checkbox']::after {
    inset: 0;
    mask: var(--_vaadin-icon-checkmark) 50% /
      var(--vaadin-checkbox-checkmark-size, var(--vaadin-checkbox-marker-size, 100%)) no-repeat;
    filter: var(--vaadin-checkbox-checkmark-color, var(--_filter));
  }

  :host([readonly]) {
    --vaadin-checkbox-background: transparent;
    --vaadin-checkbox-border-color: var(--vaadin-border-color);
    --vaadin-checkbox-marker-color: var(--vaadin-text-color);
    --_border-style: dashed;
  }

  :host([indeterminate]) [part='checkbox']::after {
    mask-image: var(--_vaadin-icon-minus);
  }
`,os=[Mt,ns("checkbox"),ss];/**
@license
Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/const rs=i=>i,Zt=typeof document.head.style.touchAction=="string",Me="__polymerGestures",ye="__polymerGesturesHandled",Oe="__polymerGesturesTouchAction",lt=25,dt=5,as=2,ls=["mousedown","mousemove","mouseup","click"],ds=[0,1,4,2],hs=(function(){try{return new MouseEvent("test",{buttons:1}).buttons===1}catch{return!1}})();function je(i){return ls.indexOf(i)>-1}let cs=!1;(function(){try{const i=Object.defineProperty({},"passive",{get(){cs=!0}});window.addEventListener("test",null,i),window.removeEventListener("test",null,i)}catch{}})();function us(i){je(i)}const ps=navigator.userAgent.match(/iP(?:[oa]d|hone)|Android/u),vs={button:!0,command:!0,fieldset:!0,input:!0,keygen:!0,optgroup:!0,option:!0,select:!0,textarea:!0};function O(i){const t=i.type;if(!je(t))return!1;if(t==="mousemove"){let n=i.buttons===void 0?1:i.buttons;return i instanceof window.MouseEvent&&!hs&&(n=ds[i.which]||0),!!(n&1)}return(i.button===void 0?0:i.button)===0}function fs(i){if(i.type==="click"){if(i.detail===0)return!0;const t=S(i);if(!t.nodeType||t.nodeType!==Node.ELEMENT_NODE)return!0;const e=t.getBoundingClientRect(),n=i.pageX,s=i.pageY;return!(n>=e.left&&n<=e.right&&s>=e.top&&s<=e.bottom)}return!1}const A={touch:{x:0,y:0,id:-1,scrollDecided:!1}};function _s(i){let t="auto";const e=Qt(i);for(let n=0,s;n<e.length;n++)if(s=e[n],s[Oe]){t=s[Oe];break}return t}function Jt(i,t,e){i.movefn=t,i.upfn=e,document.addEventListener("mousemove",t),document.addEventListener("mouseup",e)}function P(i){document.removeEventListener("mousemove",i.movefn),document.removeEventListener("mouseup",i.upfn),i.movefn=null,i.upfn=null}const Qt=window.ShadyDOM&&window.ShadyDOM.noPatch?window.ShadyDOM.composedPath:i=>i.composedPath&&i.composedPath()||[],Ue={},M=[];function gs(i,t){let e=document.elementFromPoint(i,t),n=e;for(;n&&n.shadowRoot&&!window.ShadyDOM;){const s=n;if(n=n.shadowRoot.elementFromPoint(i,t),s===n)break;n&&(e=n)}return e}function S(i){const t=Qt(i);return t.length>0?t[0]:i.target}function ms(i){const t=i.type,n=i.currentTarget[Me];if(!n)return;const s=n[t];if(!s)return;if(!i[ye]&&(i[ye]={},t.startsWith("touch"))){const r=i.changedTouches[0];if(t==="touchstart"&&i.touches.length===1&&(A.touch.id=r.identifier),A.touch.id!==r.identifier)return;Zt||(t==="touchstart"||t==="touchmove")&&bs(i)}const o=i[ye];if(!o.skip){for(let r=0,a;r<M.length;r++)a=M[r],s[a.name]&&!o[a.name]&&a.flow&&a.flow.start.indexOf(i.type)>-1&&a.reset&&a.reset();for(let r=0,a;r<M.length;r++)a=M[r],s[a.name]&&!o[a.name]&&(o[a.name]=!0,a[t](i))}}function bs(i){const t=i.changedTouches[0],e=i.type;if(e==="touchstart")A.touch.x=t.clientX,A.touch.y=t.clientY,A.touch.scrollDecided=!1;else if(e==="touchmove"){if(A.touch.scrollDecided)return;A.touch.scrollDecided=!0;const n=_s(i);let s=!1;const o=Math.abs(A.touch.x-t.clientX),r=Math.abs(A.touch.y-t.clientY);i.cancelable&&(n==="none"?s=!0:n==="pan-x"?s=r>o:n==="pan-y"&&(s=o>r)),s?i.preventDefault():Q("track")}}function ht(i,t,e){return Ue[t]?(ys(i,t,e),!0):!1}function ys(i,t,e){const n=Ue[t],s=n.deps,o=n.name;let r=i[Me];r||(i[Me]=r={});for(let a=0,l,d;a<s.length;a++)l=s[a],!(ps&&je(l)&&l!=="click")&&(d=r[l],d||(r[l]=d={_count:0}),d._count===0&&i.addEventListener(l,ms,us(l)),d[o]=(d[o]||0)+1,d._count=(d._count||0)+1);i.addEventListener(t,e),n.touchAction&&xs(i,n.touchAction)}function qe(i){M.push(i),i.emits.forEach(t=>{Ue[t]=i})}function ws(i){for(let t=0,e;t<M.length;t++){e=M[t];for(let n=0,s;n<e.emits.length;n++)if(s=e.emits[n],s===i)return e}return null}function xs(i,t){Zt&&i instanceof HTMLElement&&mt.run(()=>{i.style.touchAction=t}),i[Oe]=t}function We(i,t,e){const n=new Event(t,{bubbles:!0,cancelable:!0,composed:!0});if(n.detail=e,rs(i).dispatchEvent(n),n.defaultPrevented){const s=e.preventer||e.sourceEvent;s&&s.preventDefault&&s.preventDefault()}}function Q(i){const t=ws(i);t.info&&(t.info.prevent=!0)}qe({name:"downup",deps:["mousedown","touchstart","touchend"],flow:{start:["mousedown","touchstart"],end:["mouseup","touchend"]},emits:["down","up"],info:{movefn:null,upfn:null},reset(){P(this.info)},mousedown(i){if(!O(i))return;const t=S(i),e=this,n=o=>{O(o)||(H("up",t,o),P(e.info))},s=o=>{O(o)&&H("up",t,o),P(e.info)};Jt(this.info,n,s),H("down",t,i)},touchstart(i){H("down",S(i),i.changedTouches[0],i)},touchend(i){H("up",S(i),i.changedTouches[0],i)}});function H(i,t,e,n){t&&We(t,i,{x:e.clientX,y:e.clientY,sourceEvent:e,preventer:n,prevent(s){return Q(s)}})}qe({name:"track",touchAction:"none",deps:["mousedown","touchstart","touchmove","touchend"],flow:{start:["mousedown","touchstart"],end:["mouseup","touchend"]},emits:["track"],info:{x:0,y:0,state:"start",started:!1,moves:[],addMove(i){this.moves.length>as&&this.moves.shift(),this.moves.push(i)},movefn:null,upfn:null,prevent:!1},reset(){this.info.state="start",this.info.started=!1,this.info.moves=[],this.info.x=0,this.info.y=0,this.info.prevent=!1,P(this.info)},mousedown(i){if(!O(i))return;const t=S(i),e=this,n=o=>{const r=o.clientX,a=o.clientY;ct(e.info,r,a)&&(e.info.state=e.info.started?o.type==="mouseup"?"end":"track":"start",e.info.state==="start"&&Q("tap"),e.info.addMove({x:r,y:a}),O(o)||(e.info.state="end",P(e.info)),t&&we(e.info,t,o),e.info.started=!0)},s=o=>{e.info.started&&n(o),P(e.info)};Jt(this.info,n,s),this.info.x=i.clientX,this.info.y=i.clientY},touchstart(i){const t=i.changedTouches[0];this.info.x=t.clientX,this.info.y=t.clientY},touchmove(i){const t=S(i),e=i.changedTouches[0],n=e.clientX,s=e.clientY;ct(this.info,n,s)&&(this.info.state==="start"&&Q("tap"),this.info.addMove({x:n,y:s}),we(this.info,t,e),this.info.state="track",this.info.started=!0)},touchend(i){const t=S(i),e=i.changedTouches[0];this.info.started&&(this.info.state="end",this.info.addMove({x:e.clientX,y:e.clientY}),we(this.info,t,e))}});function ct(i,t,e){if(i.prevent)return!1;if(i.started)return!0;const n=Math.abs(i.x-t),s=Math.abs(i.y-e);return n>=dt||s>=dt}function we(i,t,e){if(!t)return;const n=i.moves[i.moves.length-2],s=i.moves[i.moves.length-1],o=s.x-i.x,r=s.y-i.y;let a,l=0;n&&(a=s.x-n.x,l=s.y-n.y),We(t,"track",{state:i.state,x:e.clientX,y:e.clientY,dx:o,dy:r,ddx:a,ddy:l,sourceEvent:e,hover(){return gs(e.clientX,e.clientY)}})}qe({name:"tap",deps:["mousedown","click","touchstart","touchend"],flow:{start:["mousedown","touchstart"],end:["click","touchend"]},emits:["tap"],info:{x:NaN,y:NaN,prevent:!1},reset(){this.info.x=NaN,this.info.y=NaN,this.info.prevent=!1},mousedown(i){O(i)&&(this.info.x=i.clientX,this.info.y=i.clientY)},click(i){O(i)&&ut(this.info,i)},touchstart(i){const t=i.changedTouches[0];this.info.x=t.clientX,this.info.y=t.clientY},touchend(i){ut(this.info,i.changedTouches[0],i)}});function ut(i,t,e){const n=Math.abs(t.clientX-i.x),s=Math.abs(t.clientY-i.y),o=S(e||t);!o||vs[o.localName]&&o.hasAttribute("disabled")||(isNaN(n)||isNaN(s)||n<=lt&&s<=lt||fs(t))&&(i.prevent||We(o,"tap",{x:t.clientX,y:t.clientY,sourceEvent:t,preventer:e}))}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ei=i=>class extends ze(Fe(i)){get _activeKeys(){return[" "]}ready(){super.ready(),ht(this,"down",e=>{this._shouldSetActive(e)&&this._setActive(!0)}),ht(this,"up",()=>{this._setActive(!1)})}disconnectedCallback(){super.disconnectedCallback(),this._setActive(!1)}_shouldSetActive(e){return!this.disabled}_onKeyDown(e){super._onKeyDown(e),this._shouldSetActive(e)&&this._activeKeys.includes(e.key)&&(this._setActive(!0),document.addEventListener("keyup",n=>{this._activeKeys.includes(n.key)&&this._setActive(!1)},{once:!0}))}_setActive(e){this.toggleAttribute("active",e)}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Cs=m(i=>class extends jt(ze(Re(i))){static get properties(){return{checked:{type:Boolean,value:!1,notify:!0,reflectToAttribute:!0,sync:!0}}}static get delegateProps(){return[...super.delegateProps,"checked"]}_onChange(e){const n=e.target;this._toggleChecked(n.checked)}_toggleChecked(e){this.checked=e}});/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Es=i=>class extends Pt(Ht(Cs($t(ei(i))))){static get properties(){return{indeterminate:{type:Boolean,notify:!0,value:!1,reflectToAttribute:!0},name:{type:String,value:""},readonly:{type:Boolean,value:!1,reflectToAttribute:!0}}}static get observers(){return["__readonlyChanged(readonly, inputElement)"]}static get delegateProps(){return[...super.delegateProps,"indeterminate"]}static get delegateAttrs(){return[...super.delegateAttrs,"name","invalid","required"]}constructor(){super(),this._setType("checkbox"),this._boundOnInputClick=this._onInputClick.bind(this),this.value="on",this.tabindex=0}get slotStyles(){return[`
          ${this.localName} > input[slot='input'] {
            opacity: 0;
          }
        `]}ready(){super.ready(),this.addController(new $e(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new ae(this.inputElement,this._labelController)),this._createMethodObserver("_checkedChanged(checked)")}_shouldSetActive(e){return this.readonly||e.target.localName==="a"||e.target===this._helperNode||e.target===this._errorNode?!1:super._shouldSetActive(e)}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("click",this._boundOnInputClick)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("click",this._boundOnInputClick)}_onInputClick(e){this.readonly&&e.preventDefault()}__readonlyChanged(e,n){n&&(e?n.setAttribute("aria-readonly","true"):n.removeAttribute("aria-readonly"))}_toggleChecked(e){this.indeterminate&&(this.indeterminate=!1),super._toggleChecked(e)}checkValidity(){return!this.required||!!this.checked}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}_checkedChanged(e){(e||this.__oldChecked)&&this._requestValidation(),this.__oldChecked=e}_requiredChanged(e){super._requiredChanged(e),e===!1&&this._requestValidation()}_onRequiredIndicatorClick(){this._labelNode.click()}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ks extends Es(C(b(g(y(_))))){static get is(){return"vaadin-checkbox"}static get styles(){return os}render(){return p`
      <div class="vaadin-checkbox-container">
        <div part="checkbox" aria-hidden="true"></div>
        <slot name="input"></slot>
        <div part="label">
          <slot name="label"></slot>
          <div part="required-indicator" @click="${this._onRequiredIndicatorClick}"></div>
        </div>
        <div part="helper-text">
          <slot name="helper"></slot>
        </div>
        <div part="error-message">
          <slot name="error-message"></slot>
        </div>
      </div>
      <slot name="tooltip"></slot>
    `}ready(){super.ready(),this._tooltipController=new q(this),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}}f(ks);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const As=c`
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
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ts=["mousedown","mouseup","click","dblclick","keypress","keydown","keyup"],Ss=i=>class extends ei(Dt(Nt(i))){constructor(){super(),this.__onInteractionEvent=this.__onInteractionEvent.bind(this),Ts.forEach(e=>{this.addEventListener(e,this.__onInteractionEvent,!0)}),this.tabindex=0}get _activeKeys(){return["Enter"," "]}ready(){super.ready(),this.hasAttribute("role")||this.setAttribute("role","button"),this.__shouldAllowFocusWhenDisabled()&&this.style.setProperty("--_vaadin-button-disabled-pointer-events","auto")}_onKeyDown(e){super._onKeyDown(e),!(e.altKey||e.shiftKey||e.ctrlKey||e.metaKey)&&this._activeKeys.includes(e.key)&&(e.preventDefault(),this.click())}__onInteractionEvent(e){this.__shouldSuppressInteractionEvent(e)&&e.stopImmediatePropagation()}__shouldSuppressInteractionEvent(e){return this.disabled}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ms extends Ss(C(b(g(y(_))))){static get is(){return"vaadin-button"}static get styles(){return As}static get properties(){return{disabled:{type:Boolean,value:!1,observer:"_disabledChanged",reflectToAttribute:!0,sync:!0}}}render(){return p`
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
    `}ready(){super.ready(),this._tooltipController=new q(this),this.addController(this._tooltipController)}__shouldAllowFocusWhenDisabled(){return window.Vaadin.featureFlags.accessibleDisabledButtons}}f(Ms);document.addEventListener("click",i=>{const t=i.composedPath().find(e=>e.hasAttribute&&e.hasAttribute("disableonclick"));t&&(t.disabled=!0)});/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const pt=c`
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
`,Os=window.Vaadin.featureFlags.layoutComponentImprovements,Ls=c`
  ::slotted([data-width-full]) {
    flex: 1;
  }

  ::slotted(vaadin-horizontal-layout[data-width-full]),
  ::slotted(vaadin-vertical-layout[data-width-full]) {
    min-width: 0;
  }
`,Is=Os?[pt,Ls]:[pt];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ns=i=>class extends i{ready(){super.ready();const t=this.shadowRoot.querySelector("slot:not([name])");this.__startSlotObserver=new Y(t,({currentNodes:s,removedNodes:o})=>{o.length&&this.__clearAttribute(o,"last-start-child");const r=s.filter(l=>l.nodeType===Node.ELEMENT_NODE);this.__updateAttributes(r,"start",!1,!0);const a=s.filter(l=>!Tt(l));this.toggleAttribute("has-start",a.length>0)});const e=this.shadowRoot.querySelector('[name="end"]');this.__endSlotObserver=new Y(e,({currentNodes:s,removedNodes:o})=>{o.length&&this.__clearAttribute(o,"first-end-child"),this.__updateAttributes(s,"end",!0,!1),this.toggleAttribute("has-end",s.length>0)});const n=this.shadowRoot.querySelector('[name="middle"]');this.__middleSlotObserver=new Y(n,({currentNodes:s,removedNodes:o})=>{o.length&&(this.__clearAttribute(o,"first-middle-child"),this.__clearAttribute(o,"last-middle-child")),this.__updateAttributes(s,"middle",!0,!0),this.toggleAttribute("has-middle",s.length>0)})}__clearAttribute(t,e){const n=t.find(s=>s.nodeType===Node.ELEMENT_NODE&&s.hasAttribute(e));n&&n.removeAttribute(e)}__updateAttributes(t,e,n,s){t.forEach((o,r)=>{if(n){const a=`first-${e}-child`;r===0?o.setAttribute(a,""):o.hasAttribute(a)&&o.removeAttribute(a)}if(s){const a=`last-${e}-child`;r===t.length-1?o.setAttribute(a,""):o.hasAttribute(a)&&o.removeAttribute(a)}})}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ds extends Ns(b(C(g(y(_))))){static get is(){return"vaadin-horizontal-layout"}static get styles(){return Is}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return p`
      <slot></slot>
      <slot name="middle"></slot>
      <slot name="end"></slot>
    `}}f(Ds);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const $s=c`
  /* Optical centering */
  :host::before,
  :host::after {
    content: '';
    flex-basis: 0;
    flex-grow: 1;
  }

  :host::after {
    flex-grow: 1.1;
  }

  :host {
    cursor: default;
  }

  [part='overlay']:focus-visible {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
  }

  [part='overlay'] {
    background: var(--vaadin-dialog-background, var(--vaadin-overlay-background, var(--vaadin-background-color)));
    background-origin: border-box;
    border: var(--vaadin-dialog-border-width, var(--vaadin-overlay-border-width, 1px)) solid
      var(--vaadin-dialog-border-color, var(--vaadin-overlay-border-color, var(--vaadin-border-color-secondary)));
    box-shadow: var(--vaadin-dialog-shadow, var(--vaadin-overlay-shadow, 0 8px 24px -4px rgba(0, 0, 0, 0.3)));
    border-radius: var(--vaadin-dialog-border-radius, var(--vaadin-radius-l));
    width: max-content;
    min-width: min(var(--vaadin-dialog-min-width, 4em), 100%);
    max-width: min(var(--vaadin-dialog-max-width, 100%), 100%);
    max-height: 100%;
  }

  [part='header'],
  [part='header-content'],
  [part='footer'] {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    flex: none;
    pointer-events: none;
    z-index: 1;
    gap: var(--vaadin-dialog-toolbar-gap, var(--vaadin-gap-s));
  }

  ::slotted(*) {
    pointer-events: auto;
  }

  [part='header'],
  [part='content'],
  [part='footer'] {
    padding: var(--vaadin-dialog-padding, var(--vaadin-padding-l));
  }

  :host([theme~='no-padding']) [part='content'] {
    padding: 0 !important;
  }

  :host(:is([has-header], [has-title])) [part='content'] {
    padding-top: 0;
  }

  :host([has-footer]) [part='content'] {
    padding-bottom: 0;
  }

  [part='header'] {
    flex-wrap: nowrap;
  }

  ::slotted([slot='header-content']),
  ::slotted([slot='title']),
  ::slotted([slot='footer']) {
    display: contents;
  }

  ::slotted([slot='title']) {
    font: inherit !important;
    color: inherit !important;
    overflow-wrap: anywhere;
  }

  [part='title'] {
    color: var(--vaadin-dialog-title-color, var(--vaadin-text-color));
    font-weight: var(--vaadin-dialog-title-font-weight, 600);
    font-size: var(--vaadin-dialog-title-font-size, 1em);
    line-height: var(--vaadin-dialog-title-line-height, inherit);
  }

  [part='header-content'] {
    flex: 1;
  }

  :host([has-title]) [part='header-content'],
  [part='footer'] {
    justify-content: flex-end;
  }

  :host(:not([has-title]):not([has-header])) [part='header'],
  :host(:not([has-header])) [part='header-content'],
  :host(:not([has-title])) [part='title'],
  :host(:not([has-footer])) [part='footer'] {
    display: none !important;
  }
`,Ps=c`
  [part='overlay'] {
    position: relative;
    overflow: visible;
    display: flex;
  }

  :host([has-bounds-set]) [part='overlay'] {
    min-width: 0;
    max-width: none;
    max-height: none;
  }

  /* Content part scrolls by default */
  [part='content'] {
    flex: 1;
    min-height: 0;
    overflow: auto;
    overscroll-behavior: contain;
    clip-path: border-box;
  }

  [part='header'],
  :host(:not([has-header])) [part='content'] {
    border-top-left-radius: inherit;
    border-top-right-radius: inherit;
  }

  [part='footer'],
  :host(:not([has-footer])) [part='content'] {
    border-bottom-left-radius: inherit;
    border-bottom-right-radius: inherit;
  }

  .resizer-container {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    max-width: 100%;
    border-radius: calc(
      var(--vaadin-dialog-border-radius, var(--vaadin-radius-l)) - var(
          --vaadin-dialog-border-width,
          var(--vaadin-overlay-border-width, 1px)
        )
    );
  }

  :host(:not([resizable])) .resizer {
    display: none;
  }

  .resizer {
    position: absolute;
    height: 16px;
    width: 16px;
  }

  .resizer.edge {
    height: 8px;
    width: 8px;
    inset: -4px;
  }

  .resizer.edge.n {
    width: auto;
    bottom: auto;
    cursor: ns-resize;
  }

  .resizer.ne {
    top: -4px;
    right: -4px;
    cursor: nesw-resize;
  }

  .resizer.edge.e {
    height: auto;
    left: auto;
    cursor: ew-resize;
  }

  .resizer.se {
    bottom: -4px;
    right: -4px;
    cursor: nwse-resize;
  }

  .resizer.edge.s {
    width: auto;
    top: auto;
    cursor: ns-resize;
  }

  .resizer.sw {
    bottom: -4px;
    left: -4px;
    cursor: nesw-resize;
  }

  .resizer.edge.w {
    height: auto;
    right: auto;
    cursor: ew-resize;
  }

  .resizer.nw {
    top: -4px;
    left: -4px;
    cursor: nwse-resize;
  }
`,zs=[Ut,$s,Ps];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Fs=i=>class extends Wt(i){static get properties(){return{headerTitle:{type:String},headerRenderer:{type:Object},footerRenderer:{type:Object}}}static get observers(){return["_headerFooterRendererChange(headerRenderer, footerRenderer, opened)","_headerTitleChanged(headerTitle, opened)"]}get _contentRoot(){return this.owner}get _rendererRoot(){if(!this.__savedRoot){const e=document.createElement("vaadin-dialog-content");e.style.display="contents",this.owner.appendChild(e),this.__savedRoot=e}return this.__savedRoot}ready(){super.ready(),this.__resizeObserver=new ResizeObserver(()=>{requestAnimationFrame(()=>{this.__updateOverflow()})}),this.__resizeObserver.observe(this.$.resizerContainer),this.$.content.addEventListener("scroll",()=>{this.__updateOverflow()}),this.shadowRoot.addEventListener("slotchange",()=>{this.__updateOverflow()})}__createContainer(e){const n=document.createElement("vaadin-dialog-content");return n.setAttribute("slot",e),n}__clearContainer(e){e.innerHTML="",delete e._$litPart$}__initContainer(e,n){return e?this.__clearContainer(e):(e=this.__createContainer(n),this.owner.appendChild(e)),e}_headerFooterRendererChange(e,n,s){const o=this.__oldHeaderRenderer!==e;this.__oldHeaderRenderer=e;const r=this.__oldFooterRenderer!==n;this.__oldFooterRenderer=n;const a=this._oldOpenedFooterHeader!==s;this._oldOpenedFooterHeader=s,u(this,"has-header",!!e),u(this,"has-footer",!!n),o&&(e?this.headerContainer=this.__initContainer(this.headerContainer,"header-content"):this.headerContainer&&(this.headerContainer.remove(),this.headerContainer=null,this.__updateOverflow())),r&&(n?this.footerContainer=this.__initContainer(this.footerContainer,"footer"):this.footerContainer&&(this.footerContainer.remove(),this.footerContainer=null,this.__updateOverflow())),(e&&(o||a)||n&&(r||a))&&s&&this.requestContentUpdate()}_headerTitleChanged(e,n){u(this,"has-title",!!e),n&&(e||this._oldHeaderTitle)&&this.requestContentUpdate(),this._oldHeaderTitle=e}_headerTitleRenderer(){this.headerTitle?(this.headerTitleElement||(this.headerTitleElement=document.createElement("h2"),this.headerTitleElement.setAttribute("slot","title"),this.headerTitleElement.classList.add("draggable")),this.owner.appendChild(this.headerTitleElement),this.headerTitleElement.textContent=this.headerTitle):this.headerTitleElement&&(this.headerTitleElement.remove(),this.headerTitleElement=null)}requestContentUpdate(){super.requestContentUpdate(),this.headerContainer&&this.headerRenderer&&this.headerRenderer.call(this.owner,this.headerContainer,this.owner),this.footerContainer&&this.footerRenderer&&this.footerRenderer.call(this.owner,this.footerContainer,this.owner),this._headerTitleRenderer(),this.__updateOverflow()}getBounds(){const e=this.$.overlay.getBoundingClientRect(),n=this.getBoundingClientRect(),s=e.top-n.top,o=e.left-n.left,r=e.width,a=e.height;return{top:s,left:o,width:r,height:a}}__updateOverflow(){let e="";const n=this.$.content;n.scrollTop>0&&(e+=" top"),n.scrollTop<n.scrollHeight-n.clientHeight&&(e+=" bottom");const s=e.trim();s.length>0&&this.getAttribute("overflow")!==s?u(this,"overflow",s):s.length===0&&this.hasAttribute("overflow")&&u(this,"overflow",null)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Rs extends Fs(ie(b(g(y(_))))){static get is(){return"vaadin-dialog-overlay"}static get styles(){return zs}get _focusTrapRoot(){return this.owner}render(){return p`
      <div id="backdrop" part="backdrop" ?hidden="${!this.withBackdrop}"></div>
      <div part="overlay" id="overlay">
        <section id="resizerContainer" class="resizer-container">
          <header part="header">
            <div part="title"><slot name="title"></slot></div>
            <div part="header-content"><slot name="header-content"></slot></div>
          </header>
          <div part="content" id="content"><slot></slot></div>
          <footer part="footer"><slot name="footer"></slot></footer>
        </section>
      </div>
    `}}f(Rs);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Bs=i=>class extends i{static get properties(){return{opened:{type:Boolean,reflectToAttribute:!0,value:!1,notify:!0,sync:!0},noCloseOnOutsideClick:{type:Boolean,value:!1},noCloseOnEsc:{type:Boolean,value:!1},modeless:{type:Boolean,value:!1},top:{type:String},left:{type:String},overlayRole:{type:String}}}static get observers(){return["__positionChanged(top, left)"]}ready(){super.ready();const e=this.$.overlay;e.addEventListener("vaadin-overlay-outside-click",this._handleOutsideClick.bind(this)),e.addEventListener("vaadin-overlay-escape-press",this._handleEscPress.bind(this)),e.addEventListener("vaadin-overlay-closed",this.__handleOverlayClosed.bind(this)),this._overlayElement=e,this.hasAttribute("role")||(this.role="dialog"),this.setAttribute("tabindex","0")}updated(e){super.updated(e),e.has("overlayRole")&&(this.role=this.overlayRole||"dialog"),e.has("modeless")&&(this.modeless?this.removeAttribute("aria-modal"):this.setAttribute("aria-modal","true"))}__handleOverlayClosed(){this.dispatchEvent(new CustomEvent("closed"))}connectedCallback(){super.connectedCallback(),this.__restoreOpened&&(this.opened=!0)}disconnectedCallback(){super.disconnectedCallback(),setTimeout(()=>{this.isConnected||(this.__restoreOpened=this.opened,this.opened=!1)})}_onOverlayOpened(e){e.detail.value===!1&&(this.opened=!1)}_handleOutsideClick(e){this.noCloseOnOutsideClick&&e.preventDefault()}_handleEscPress(e){this.noCloseOnEsc&&e.preventDefault()}_bringOverlayToFront(){this.modeless&&this._overlayElement.bringToFront()}__positionChanged(e,n){requestAnimationFrame(()=>this.$.overlay.setBounds({top:e,left:n}))}__sizeChanged(e,n){requestAnimationFrame(()=>this.$.overlay.setBounds({width:e,height:n},!1))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function ee(i){return i.touches?i.touches[0]:i}function ti(i){return i.clientX>=0&&i.clientX<=window.innerWidth&&i.clientY>=0&&i.clientY<=window.innerHeight}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Vs=i=>class extends i{static get properties(){return{draggable:{type:Boolean,value:!1,reflectToAttribute:!0},_touchDevice:{type:Boolean,value:Ft},__dragHandleClassName:{type:String}}}ready(){super.ready(),this._originalBounds={},this._originalMouseCoords={},this._startDrag=this._startDrag.bind(this),this._drag=this._drag.bind(this),this._stopDrag=this._stopDrag.bind(this),this.$.overlay.$.overlay.addEventListener("mousedown",this._startDrag),this.$.overlay.$.overlay.addEventListener("touchstart",this._startDrag)}_startDrag(e){if(!(e.type==="touchstart"&&e.touches.length>1)&&this.draggable&&(e.button===0||e.touches)){const n=this.$.overlay.$.resizerContainer,s=e.target===n,o=e.offsetX>n.clientWidth||e.offsetY>n.clientHeight,r=e.target===this.$.overlay.$.content,a=e.composedPath().some((l,d)=>{if(!l.classList)return!1;const v=l.classList.contains(this.__dragHandleClassName||"draggable"),w=l.classList.contains("draggable-leaf-only"),T=d===0;return w&&T||v&&(!w||T)});if(s&&!o||r||a){a||e.preventDefault(),this._originalBounds=this.$.overlay.getBounds();const l=ee(e);if(this._originalMouseCoords={top:l.pageY,left:l.pageX},window.addEventListener("mouseup",this._stopDrag),window.addEventListener("touchend",this._stopDrag),window.addEventListener("mousemove",this._drag),window.addEventListener("touchmove",this._drag),this.$.overlay.$.overlay.style.position!=="absolute"){const{top:d,left:v}=this._originalBounds;this.top=d,this.left=v}}}}_drag(e){const n=ee(e);if(ti(n)){const s=this._originalBounds.top+(n.pageY-this._originalMouseCoords.top),o=this._originalBounds.left+(n.pageX-this._originalMouseCoords.left);this.top=s,this.left=o}}_stopDrag(){this.dispatchEvent(new CustomEvent("dragged",{bubbles:!0,composed:!0,detail:{top:this.top,left:this.left}})),window.removeEventListener("mouseup",this._stopDrag),window.removeEventListener("touchend",this._stopDrag),window.removeEventListener("mousemove",this._drag),window.removeEventListener("touchmove",this._drag)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Hs=i=>class extends i{static get properties(){return{renderer:{type:Object},headerTitle:String,headerRenderer:{type:Object},footerRenderer:{type:Object}}}requestContentUpdate(){this._overlayElement&&this._overlayElement.requestContentUpdate()}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const js=i=>class extends i{static get properties(){return{resizable:{type:Boolean,value:!1,reflectToAttribute:!0}}}ready(){super.ready(),this._originalBounds={},this._originalMouseCoords={},this._resizeListeners={start:{},resize:{},stop:{}},this._addResizeListeners()}_addResizeListeners(){["n","e","s","w","nw","ne","se","sw"].forEach(e=>{const n=document.createElement("div");this._resizeListeners.start[e]=s=>this._startResize(s,e),this._resizeListeners.resize[e]=s=>this._resize(s,e),this._resizeListeners.stop[e]=()=>this._stopResize(e),e.length===1&&n.classList.add("edge"),n.classList.add("resizer"),n.classList.add(e),n.addEventListener("mousedown",this._resizeListeners.start[e]),n.addEventListener("touchstart",this._resizeListeners.start[e]),this.$.overlay.$.resizerContainer.appendChild(n)})}_startResize(e,n){if(!(e.type==="touchstart"&&e.touches.length>1)&&(e.button===0||e.touches)){e.preventDefault(),this._originalBounds=this.$.overlay.getBounds();const s=ee(e);this._originalMouseCoords={top:s.pageY,left:s.pageX},window.addEventListener("mousemove",this._resizeListeners.resize[n]),window.addEventListener("touchmove",this._resizeListeners.resize[n]),window.addEventListener("mouseup",this._resizeListeners.stop[n]),window.addEventListener("touchend",this._resizeListeners.stop[n]),this.$.overlay.setBounds(this._originalBounds),this.$.overlay.setAttribute("has-bounds-set","")}}_resize(e,n){const s=ee(e);ti(s)&&n.split("").forEach(r=>{switch(r){case"n":{const a=this._originalBounds.height-(s.pageY-this._originalMouseCoords.top),l=this._originalBounds.top+(s.pageY-this._originalMouseCoords.top);a>40&&(this.top=l,this.height=a);break}case"e":{const a=this._originalBounds.width+(s.pageX-this._originalMouseCoords.left);a>40&&(this.width=a);break}case"s":{const a=this._originalBounds.height+(s.pageY-this._originalMouseCoords.top);a>40&&(this.height=a);break}case"w":{const a=this._originalBounds.width-(s.pageX-this._originalMouseCoords.left),l=this._originalBounds.left+(s.pageX-this._originalMouseCoords.left);a>40&&(this.left=l,this.width=a);break}}})}_stopResize(e){window.removeEventListener("mousemove",this._resizeListeners.resize[e]),window.removeEventListener("touchmove",this._resizeListeners.resize[e]),window.removeEventListener("mouseup",this._resizeListeners.stop[e]),window.removeEventListener("touchend",this._resizeListeners.stop[e]),this.dispatchEvent(new CustomEvent("resize",{detail:this._getResizeDimensions()}))}_getResizeDimensions(){const{width:e,height:n,top:s,left:o}=getComputedStyle(this.$.overlay.$.overlay);return{width:e,height:n,top:s,left:o}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Us=i=>class extends i{static get properties(){return{width:{type:String},height:{type:String}}}static get observers(){return["__sizeChanged(width, height)"]}__sizeChanged(e,n){requestAnimationFrame(()=>this.$.overlay.setBounds({width:e,height:n},!1))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class qs extends Us(Vs(js(Hs(Bs(ne(C(g(_)))))))){static get is(){return"vaadin-dialog"}static get styles(){return c`
      :host([opened]),
      :host([opening]),
      :host([closing]) {
        display: block !important;
        position: fixed;
        outline: none;
      }

      :host,
      :host([hidden]) {
        display: none !important;
      }

      :host(:focus-visible) ::part(overlay) {
        outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
      }
    `}render(){return p`
      <vaadin-dialog-overlay
        id="overlay"
        .owner="${this}"
        .opened="${this.opened}"
        .headerTitle="${this.headerTitle}"
        .renderer="${this.renderer}"
        .headerRenderer="${this.headerRenderer}"
        .footerRenderer="${this.footerRenderer}"
        @opened-changed="${this._onOverlayOpened}"
        @mousedown="${this._bringOverlayToFront}"
        @touchstart="${this._bringOverlayToFront}"
        theme="${z(this._theme)}"
        .modeless="${this.modeless}"
        .withBackdrop="${!this.modeless}"
        ?resizable="${this.resizable}"
        restore-focus-on-close
        focus-trap
        exportparts="backdrop, overlay, header, title, header-content, content, footer"
      >
        <slot name="title" slot="title"></slot>
        <slot name="header-content" slot="header-content"></slot>
        <slot name="footer" slot="footer"></slot>
        <slot></slot>
      </vaadin-dialog-overlay>
    `}updated(t){super.updated(t),t.has("headerTitle")&&(this.ariaLabel=this.headerTitle)}}f(qs);/**
 * @license
 * Copyright 2020 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Ws=(i,t)=>i?._$litType$!==void 0,Ks=i=>i.strings===void 0;/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const j=(i,t)=>{const e=i._$AN;if(e===void 0)return!1;for(const n of e)n._$AO?.(t,!1),j(n,t);return!0},te=i=>{let t,e;do{if((t=i._$AM)===void 0)break;e=t._$AN,e.delete(i),i=t}while(e?.size===0)},ii=i=>{for(let t;t=i._$AM;i=t){let e=t._$AN;if(e===void 0)t._$AN=e=new Set;else if(e.has(i))break;e.add(i),Xs(t)}};function Gs(i){this._$AN!==void 0?(te(this),this._$AM=i,ii(this)):this._$AM=i}function Ys(i,t=!1,e=0){const n=this._$AH,s=this._$AN;if(s!==void 0&&s.size!==0)if(t)if(Array.isArray(n))for(let o=e;o<n.length;o++)j(n[o],!1),te(n[o]);else n!=null&&(j(n,!1),te(n));else j(this,i)}const Xs=i=>{i.type==vt.CHILD&&(i._$AP??=Ys,i._$AQ??=Gs)};class Zs extends vi{constructor(){super(...arguments),this._$AN=void 0}_$AT(t,e,n){super._$AT(t,e,n),ii(this),this.isConnected=t._$AU}_$AO(t,e=!0){t!==this.isConnected&&(this.isConnected=t,t?this.reconnected?.():this.disconnected?.()),e&&(j(this,t),te(this))}setValue(t){if(Ks(this._$Ct))this._$Ct._$AI(t,this);else{const e=[...this._$Ct._$AH];e[this._$Ci]=t,this._$Ct._$AI(e,this,0)}}disconnected(){}reconnected(){}}class Js extends Zs{constructor(t){if(super(t),t.type!==vt.CHILD)throw new Error(`${this.constructor.directiveName}() can only be used in child bindings`)}update(t,[e,n]){return this.updateContent(t,e,n),_i}updateContent(t,e,n){const{parentNode:s,startNode:o}=t;this.__parentNode=s;const r=n!=null,a=r?this.getNewNode(e,n):null,l=this.getOldNode(t);if(clearTimeout(this.__parentNode.__nodeRetryTimeout),r&&!a)this.__parentNode.__nodeRetryTimeout=setTimeout(()=>this.updateContent(t,e,n));else{if(l===a)return;l&&a?s.replaceChild(a,l):l?s.removeChild(l):a&&o.after(a)}}getNewNode(t,e){return window.Vaadin.Flow.clients[t].getByNodeId(e)}getOldNode(t){const{startNode:e,endNode:n}=t;if(e.nextSibling!==n)return e.nextSibling}disconnected(){clearTimeout(this.__parentNode.__nodeRetryTimeout)}}const ni=fi(Js);function Qs(i,t){return ni(i,t)}function eo(i,t,e){ft(p`${t.map(n=>ni(i,n))}`,e)}function to(i){const t=i.insertBefore;i.insertBefore=function(e,n){return n&&n.parentNode===this?t.call(this,e,n):t.call(this,e,null)}}window.Vaadin||={};window.Vaadin.FlowComponentHost||={patchVirtualContainer:to,getNode:Qs,setChildNodes:eo};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const io=c`
  :host {
    display: block;
  }

  [part='overlay'] {
    pointer-events: auto;
    box-sizing: border-box;
    width: var(--vaadin-notification-width, 40ch);
    max-width: 100%;
    padding: var(--vaadin-notification-padding, var(--vaadin-padding-s));
    background: var(--vaadin-notification-background, var(--vaadin-background-container));
    border: var(--vaadin-notification-border-width, 1px) solid
      var(--vaadin-notification-border-color, var(--vaadin-border-color-secondary));
    box-shadow: var(--vaadin-notification-shadow, 0 8px 24px -4px rgba(0, 0, 0, 0.3));
    border-radius: var(--vaadin-notification-border-radius, var(--vaadin-radius-l));
    cursor: default;
  }

  @media (forced-colors: active) {
    [part='overlay'] {
      border: 3px solid !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const no=c`
  :host {
    /* How much space to reserve for overlay box shadow, to prevent clipping it with overflow:auto */
    --_paint-area: 2em;
    /* Space between notifications and the viewport */
    --_padding: var(--vaadin-notification-viewport-inset, var(--vaadin-padding-s));
    /* Space between notifications */
    --_gap: var(--vaadin-notification-container-gap, var(--vaadin-gap-s));
    display: grid;
    /* top-stretch, top and bottom regions, bottom-stretch */
    grid-template-rows: auto 1fr auto;
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    overflow: hidden;
    padding: max(env(safe-area-inset-top, 0px), var(--_padding)) max(env(safe-area-inset-right, 0px), var(--_padding))
      max(env(safe-area-inset-bottom, 0px), var(--_padding)) max(env(safe-area-inset-left, 0px), var(--_padding));
    border: 0;
    background: transparent;
    pointer-events: none;
    interpolate-size: allow-keywords;
  }

  :host > * {
    grid-column: 1;
  }

  [region-group] {
    position: relative;
    grid-row: 2 / 3;
  }

  [region] {
    max-width: 100%;
    max-height: 100%;
    pointer-events: auto;
    scrollbar-width: none;
  }

  /* scrollbar-width is supported since Safari 18.2, use the following for earlier */
  [region]::-webkit-scrollbar {
    display: none;
  }

  [region='top-stretch'] {
    grid-row: 1;
    z-index: 2;
    --vaadin-notification-width: 100%;
  }

  [region='bottom-stretch'] {
    grid-row: 3;
    z-index: 2;
    --vaadin-notification-width: 100%;
  }

  [region='middle'],
  [region-group] > [region] {
    position: absolute;
  }

  [region='middle'] {
    position: fixed;
    top: 50%;
    left: 50%;
    translate: -50% -50%;
    max-width: calc(100% - var(--_padding) * 2);
  }

  [region]:where(:hover, :focus-within) {
    z-index: 1;
    overflow: auto;
    overscroll-behavior: contain;
    padding: var(--_paint-area);
  }

  [region]:not([region='middle'], [region$='center']):where(:hover, :focus-within) {
    margin-inline: calc(var(--_paint-area) * -1);
  }

  [region]:not([region='middle']):where(:hover, :focus-within) {
    margin-block: calc(var(--_paint-area) * -1);
  }

  [region-group='top'] > [region] {
    top: 0;
  }

  [region-group='bottom'] > [region] {
    bottom: 0;
  }

  [region-group] > [region$='start'] {
    inset-inline-start: 0;
  }

  [region-group] > [region$='center'] {
    left: 50%;
    translate: -50%;
  }

  [region-group] > [region$='end'] {
    inset-inline-end: 0;
  }

  ::slotted(*) {
    margin-bottom: var(--_gap);
  }

  :is([region^='bottom'], [region='middle']) ::slotted(*) {
    margin-top: var(--_gap);
    margin-bottom: 0;
  }
`;/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const so=i=>class extends i{static get properties(){return{overlayClass:{type:String},_overlayElement:{type:Object}}}static get observers(){return["__updateOverlayClassNames(overlayClass, _overlayElement)"]}__updateOverlayClassNames(e,n){if(!n||e===void 0)return;const{classList:s}=n;if(this.__initialClasses||(this.__initialClasses=new Set(s)),Array.isArray(this.__previousClasses)){const r=this.__previousClasses.filter(a=>!this.__initialClasses.has(a));r.length>0&&s.remove(...r)}const o=typeof e=="string"?e.split(" ").filter(Boolean):[];o.length>0&&s.add(...o),this.__previousClasses=o}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const oo=i=>class extends i{static get properties(){return{opened:{type:Boolean,value:!1,sync:!0,observer:"_openedChanged"}}}constructor(){super(),this._boundVaadinOverlayClose=this._onVaadinOverlayClose.bind(this),zt&&(this._boundIosResizeListener=()=>this._detectIosNavbar())}firstUpdated(t){super.firstUpdated(t),this.popover="manual"}bringToFront(){this.matches(":popover-open")&&(this.hidePopover(),this.showPopover())}_openedChanged(t){t?(document.body.appendChild(this),this.showPopover(),document.addEventListener("vaadin-overlay-close",this._boundVaadinOverlayClose),this._boundIosResizeListener&&(this._detectIosNavbar(),window.addEventListener("resize",this._boundIosResizeListener))):(document.body.removeChild(this),this.hidePopover(),document.removeEventListener("vaadin-overlay-close",this._boundVaadinOverlayClose),this._boundIosResizeListener&&window.removeEventListener("resize",this._boundIosResizeListener))}_detectIosNavbar(){const t=window.innerHeight,n=window.innerWidth>t,s=document.documentElement.clientHeight;n&&s>t?this.style.bottom=`${s-t}px`:this.style.bottom="0"}_onVaadinOverlayClose(t){const e=t.detail.sourceEvent;e&&e.composedPath().indexOf(this)>=0&&t.preventDefault()}},ro=i=>class extends ne(so(i)){static get properties(){return{assertive:{type:Boolean,value:!1,sync:!0},duration:{type:Number,value:5e3,sync:!0},opened:{type:Boolean,value:!1,notify:!0,sync:!0,observer:"_openedChanged"},position:{type:String,value:"bottom-start",observer:"_positionChanged",sync:!0},renderer:{type:Function,sync:!0}}}static get observers(){return["_durationChanged(duration, opened)","_rendererChanged(renderer, opened, _overlayElement)"]}static show(t,e){const n=customElements.get("vaadin-notification");return Ws(t)?n._createAndShowNotification(s=>{ft(t,s)},e):n._createAndShowNotification(s=>{s.innerText=t},e)}static _createAndShowNotification(t,e){const n=document.createElement("vaadin-notification");return e&&Number.isFinite(e.duration)&&(n.duration=e.duration),e&&e.position&&(n.position=e.position),e&&e.assertive&&(n.assertive=e.assertive),e&&e.theme&&n.setAttribute("theme",e.theme),n.renderer=t,document.body.appendChild(n),n.opened=!0,n.addEventListener("opened-changed",s=>{s.detail.value||n.remove()}),n}get _container(){const t=customElements.get("vaadin-notification");return t._container||(t._container=document.createElement("vaadin-notification-container"),document.body.appendChild(t._container)),t._container}get _card(){return this._overlayElement}ready(){super.ready(),this._overlayElement=this.shadowRoot.querySelector("vaadin-notification-card")}disconnectedCallback(){super.disconnectedCallback(),queueMicrotask(()=>{this.isConnected||(this.opened=!1)})}requestContentUpdate(){!this.renderer||!this._card||this.renderer(this._card,this)}__computeAriaLive(t){return t?"assertive":"polite"}_rendererChanged(t,e,n){if(!n)return;const s=this._oldRenderer!==t;this._oldRenderer=t,s&&(n.innerHTML="",delete n._$litPart$),e&&(this._didAnimateNotificationAppend||this._animatedAppendNotificationCard(),this.requestContentUpdate())}open(){this.opened=!0}close(){this.opened=!1}_openedChanged(t){t?(this._container.opened=!0,this._animatedAppendNotificationCard()):this._card&&this._closeNotificationCard()}__cleanUpOpeningClosingState(){this._card.removeAttribute("opening"),this._card.removeAttribute("closing"),this._card.removeEventListener("animationend",this.__animationEndListener)}_animatedAppendNotificationCard(){this._card?(this.__cleanUpOpeningClosingState(),this._card.setAttribute("opening",""),this._appendNotificationCard(),this.__animationEndListener=()=>this.__cleanUpOpeningClosingState(),this._card.addEventListener("animationend",this.__animationEndListener),this._didAnimateNotificationAppend=!0):this._didAnimateNotificationAppend=!1}_appendNotificationCard(){if(this._card){if(!this._container.shadowRoot.querySelector(`slot[name="${this.position}"]`)){console.warn(`Invalid alignment parameter provided: position=${this.position}`);return}this._container.firstElementChild&&this._container.bringToFront(),this._card.slot=this.position,this._container.firstElementChild&&/top/u.test(this.position)?this._container.insertBefore(this._card,this._container.firstElementChild):this._container.appendChild(this._card)}}_removeNotificationCard(){this._card&&(this._card.parentNode&&this._card.parentNode.removeChild(this._card),this._card.removeAttribute("closing"),this._container.opened=!!this._container.firstElementChild,this.dispatchEvent(new CustomEvent("closed")))}_closeNotificationCard(){this._durationTimeoutId&&clearTimeout(this._durationTimeoutId),this._animatedRemoveNotificationCard()}_animatedRemoveNotificationCard(){this.__cleanUpOpeningClosingState(),this._card.setAttribute("closing","");const t=getComputedStyle(this._card).getPropertyValue("animation-name");t&&t!=="none"?(this.__animationEndListener=()=>{this._removeNotificationCard(),this.__cleanUpOpeningClosingState()},this._card.addEventListener("animationend",this.__animationEndListener)):this._removeNotificationCard()}_positionChanged(){this.opened&&this._animatedAppendNotificationCard()}_durationChanged(t,e){e&&(clearTimeout(this._durationTimeoutId),t>0&&(this._durationTimeoutId=setTimeout(()=>this.close(),t)))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ao extends oo(b(C(g(y(_))))){static get is(){return"vaadin-notification-container"}static get styles(){return no}render(){return p`
      <div region="top-stretch"><slot name="top-stretch"></slot></div>
      <div region-group="top">
        <div region="top-start"><slot name="top-start"></slot></div>
        <div region="top-center"><slot name="top-center"></slot></div>
        <div region="top-end"><slot name="top-end"></slot></div>
      </div>
      <div region="middle"><slot name="middle"></slot></div>
      <div region-group="bottom">
        <div region="bottom-start"><slot name="bottom-start"></slot></div>
        <div region="bottom-center"><slot name="bottom-center"></slot></div>
        <div region="bottom-end"><slot name="bottom-end"></slot></div>
      </div>
      <div region="bottom-stretch"><slot name="bottom-stretch"></slot></div>
    `}}class lo extends b(g(y(_))){static get is(){return"vaadin-notification-card"}static get styles(){return io}render(){return p`
      <div part="overlay">
        <div part="content">
          <slot></slot>
        </div>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","alert")}}class ho extends ro(C(b(g(_)))){static get is(){return"vaadin-notification"}static get styles(){return c`
      :host {
        display: none !important;
      }
    `}render(){return p`
      <vaadin-notification-card
        theme="${z(this._theme)}"
        aria-live="${this.__computeAriaLive(this.assertive)}"
      ></vaadin-notification-card>
    `}}f(ao);f(lo);f(ho);function co(i,t){if(t.type==="stateKeyChanged"){const{value:e}=t;return{...i,key:e}}else return i}const uo=()=>{};class po extends HTMLElement{#e=void 0;#n=!1;#i=void 0;#t=Object.create(null);#o=new Map;#s=new Map;#r=uo;#d=new Map;#h;#a;#l;constructor(){super(),this.#h={useState:this.useState.bind(this),useCustomEvent:this.useCustomEvent.bind(this),useContent:this.useContent.bind(this)},this.#a=this.#u.bind(this),this.#p()}async connectedCallback(){this.#i=R.createElement(this.#a),!(!this.dispatchEvent(new CustomEvent("flow-portal-add",{bubbles:!0,cancelable:!0,composed:!0,detail:{children:this.#i,domNode:this}}))||this.#e)&&(await this.#l,this.#e=gi.createRoot(this),this.#c(),this.#e.render(this.#i))}addReadyCallback(t,e){this.#d.set(t,e)}async disconnectedCallback(){this.#e?(this.#l=Promise.resolve(),await this.#l,this.#e.unmount(),this.#e=void 0):this.dispatchEvent(new CustomEvent("flow-portal-remove",{bubbles:!0,cancelable:!0,composed:!0,detail:{children:this.#i,domNode:this}})),this.#n=!1,this.#i=void 0}useState(t,e){if(this.#o.has(t))return[this.#t[t],this.#o.get(t)];const n=this[t]??e;this.#t[t]=n,Object.defineProperty(this,t,{enumerable:!0,get(){return this.#t[t]},set(r){this.#t[t]=r,this.#r({type:"stateKeyChanged",key:t,value:n})}});const s=this.useCustomEvent(`${t}-changed`,{detail:{value:n}}),o=r=>{this.#t[t]=r,s({value:r}),this.#r({type:"stateKeyChanged",key:t,value:r})};return this.#o.set(t,o),[n,o]}useCustomEvent(t,e={}){if(!this.#s.has(t)){const n=(s=>{const o=s===void 0?e:{...e,detail:s},r=new CustomEvent(t,o);return this.dispatchEvent(r)});return this.#s.set(t,n),n}return this.#s.get(t)}useContent(t){return R.useEffect(()=>{this.#d.get(t)?.()},[]),R.createElement("flow-content-container",{name:t,style:{display:"contents"}})}#c(){this.#n||!this.#e||(this.#e.render(R.createElement(this.#a)),this.#n=!0)}#u(){const[t,e]=R.useReducer(co,this.#t);return this.#t=t,this.#r=e,this.render(this.#h)}#p(){let t=window.Vaadin||{};t.developmentMode&&(t.registrations=t.registrations||[],t.registrations.push({is:"ReactAdapterElement",version:"25.0.5"}))}}class vo extends po{async connectedCallback(){await super.connectedCallback(),this.style.display="contents"}render(){return mi.jsx(bi,{})}}customElements.define("react-router-outlet",vo);const fo=i=>Promise.resolve(0);window.Vaadin=window.Vaadin||{};window.Vaadin.Flow=window.Vaadin.Flow||{};window.Vaadin.Flow.loadOnDemand=fo;window.Vaadin.Flow.resetFocus=()=>{let i=document.activeElement;for(;i&&i.shadowRoot;)i=i.shadowRoot.activeElement;return!i||i.blur()||i.focus()||!0};
