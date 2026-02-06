import{f as Bs,S as Vs,i as v,b as C,a as w,A as Li,c as Pi,t as ee,e as zi,E as ke,D as $t,_ as Hs,r as E,d as Ee,g as Ws,j as qs,O as Us}from"./indexhtml-BTVs5fJa.js";import"./commonjsHelpers-CqkleIqs.js";/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */window.Vaadin||={};window.Vaadin.featureFlags||={};function js(s){return s.replace(/-[a-z]/gu,i=>i[1].toUpperCase())}const G={};function y(s,i="25.0.3"){if(Object.defineProperty(s,"version",{get(){return i}}),s.experimental){const t=typeof s.experimental=="string"?s.experimental:`${js(s.is.split("-").slice(1).join("-"))}Component`;if(!window.Vaadin.featureFlags[t]&&!G[t]){G[t]=new Set,G[t].add(s),Object.defineProperty(window.Vaadin.featureFlags,t,{get(){return G[t].size===0},set(n){n&&G[t].size>0&&(G[t].forEach(r=>{customElements.define(r.is,r)}),G[t].clear())}});return}else if(G[t]){G[t].add(s);return}}const e=customElements.get(s.is);if(!e)customElements.define(s.is,s);else{const t=e.version;t&&s.version&&t===s.version?console.warn(`The component ${s.is} has been loaded twice`):console.error(`Tried to define ${s.is} version ${s.version} when version ${e.version} is already in use. Something will probably break.`)}}const Gs=/\/\*[\*!]\s+vaadin-dev-mode:start([\s\S]*)vaadin-dev-mode:end\s+\*\*\//i,Ue=window.Vaadin&&window.Vaadin.Flow&&window.Vaadin.Flow.clients;function Ks(){function s(){return!0}return Mi(s)}function Ys(){try{return Xs()?!0:Zs()?Ue?!Qs():!Ks():!1}catch{return!1}}function Xs(){return localStorage.getItem("vaadin.developmentmode.force")}function Zs(){return["localhost","127.0.0.1"].indexOf(window.location.hostname)>=0}function Qs(){return!!(Ue&&Object.keys(Ue).map(i=>Ue[i]).filter(i=>i.productionMode).length>0)}function Mi(s,i){if(typeof s!="function")return;const e=Gs.exec(s.toString());if(e)try{s=new Function(e[1])}catch(t){console.log("vaadin-development-mode-detector: uncommentAndRun() failed",t)}return s(i)}window.Vaadin=window.Vaadin||{};const ni=function(s,i){if(window.Vaadin.developmentMode)return Mi(s,i)};window.Vaadin.developmentMode===void 0&&(window.Vaadin.developmentMode=Ys());function Js(){/*! vaadin-dev-mode:start
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

  vaadin-dev-mode:end **/}const en=function(){if(typeof ni=="function")return ni(Js)};/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
 */let ri=0,Fi=0;const fe=[];let Tt=!1;function tn(){Tt=!1;const s=fe.length;for(let i=0;i<s;i++){const e=fe[i];if(e)try{e()}catch(t){setTimeout(()=>{throw t})}}fe.splice(0,s),Fi+=s}const H={after(s){return{run(i){return window.setTimeout(i,s)},cancel(i){window.clearTimeout(i)}}},run(s,i){return window.setTimeout(s,i)},cancel(s){window.clearTimeout(s)}},X={run(s){return window.requestAnimationFrame(s)},cancel(s){window.cancelAnimationFrame(s)}},$i={run(s){return window.requestIdleCallback?window.requestIdleCallback(s):window.setTimeout(s,16)},cancel(s){window.cancelIdleCallback?window.cancelIdleCallback(s):window.clearTimeout(s)}},W={run(s){Tt||(Tt=!0,queueMicrotask(()=>tn())),fe.push(s);const i=ri;return ri+=1,i},cancel(s){const i=s-Fi;if(i>=0){if(!fe[i])throw new Error(`invalid async handle: ${s}`);fe[i]=null}}};/**
@license
Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/const Le=new Set;class I{static debounce(i,e,t){return i instanceof I?i._cancelAsync():i=new I,i.setConfig(e,t),i}constructor(){this._asyncModule=null,this._callback=null,this._timer=null}setConfig(i,e){this._asyncModule=i,this._callback=e,this._timer=this._asyncModule.run(()=>{this._timer=null,Le.delete(this),this._callback()})}cancel(){this.isActive()&&(this._cancelAsync(),Le.delete(this))}_cancelAsync(){this.isActive()&&(this._asyncModule.cancel(this._timer),this._timer=null)}flush(){this.isActive()&&(this.cancel(),this._callback())}isActive(){return this._timer!=null}}function Di(s){Le.add(s)}function sn(){const s=!!Le.size;return Le.forEach(i=>{try{i.flush()}catch(e){setTimeout(()=>{throw e})}}),s}const Re=()=>{let s;do s=sn();while(s)};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const K=[];function kt(s,i,e=s.getAttribute("dir")){i?s.setAttribute("dir",i):e!=null&&s.removeAttribute("dir")}function Rt(){return document.documentElement.getAttribute("dir")}function nn(){const s=Rt();K.forEach(i=>{kt(i,s)})}const rn=new MutationObserver(nn);rn.observe(document.documentElement,{attributes:!0,attributeFilter:["dir"]});const N=s=>class extends s{static get properties(){return{dir:{type:String,value:"",reflectToAttribute:!0,converter:{fromAttribute:e=>e||"",toAttribute:e=>e===""?null:e}}}}get __isRTL(){return this.getAttribute("dir")==="rtl"}connectedCallback(){super.connectedCallback(),(!this.hasAttribute("dir")||this.__restoreSubscription)&&(this.__subscribe(),kt(this,Rt(),null))}attributeChangedCallback(e,t,n){if(super.attributeChangedCallback(e,t,n),e!=="dir")return;const r=Rt(),o=n===r&&K.indexOf(this)===-1,a=!n&&t&&K.indexOf(this)===-1;o||a?(this.__subscribe(),kt(this,r,n)):n!==r&&t===r&&this.__unsubscribe()}disconnectedCallback(){super.disconnectedCallback(),this.__restoreSubscription=K.includes(this),this.__unsubscribe()}_valueToNodeAttribute(e,t,n){n==="dir"&&t===""&&!e.hasAttribute("dir")||super._valueToNodeAttribute(e,t,n)}_attributeToProperty(e,t,n){e==="dir"&&!t?this.dir="":super._attributeToProperty(e,t,n)}__subscribe(){K.includes(this)||K.push(this)}__unsubscribe(){K.includes(this)&&K.splice(K.indexOf(this),1)}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */window.Vaadin||(window.Vaadin={});window.Vaadin.registrations||(window.Vaadin.registrations=[]);window.Vaadin.developmentModeCallback||(window.Vaadin.developmentModeCallback={});window.Vaadin.developmentModeCallback["vaadin-usage-statistics"]=function(){en()};let ft;const oi=new Set,z=s=>class extends N(s){static finalize(){super.finalize();const{is:e}=this;if(e&&!oi.has(e)){window.Vaadin.registrations.push(this),oi.add(e);const t=window.Vaadin.developmentModeCallback;t&&(ft=I.debounce(ft,$i,()=>{t["vaadin-usage-statistics"]()}),Di(ft))}}constructor(){super(),document.doctype===null&&console.warn('Vaadin components require the "standards mode" declaration. Please add <!DOCTYPE html> to the HTML document.')}},Ni=new WeakMap;function on(s,i){let e=i;for(;e;){if(Ni.get(e)===s)return!0;e=Object.getPrototypeOf(e)}return!1}function B(s){return i=>{if(on(s,i))return i;const e=s(i);return Ni.set(e,s),e}}/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Ke(s,i){return s.split(".").reduce((e,t)=>e?e[t]:void 0,i)}function an(s,i,e){const t=s.split("."),n=t.pop(),r=t.reduce((o,a)=>o[a],e);r[n]=i}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const gt={},ln=/([A-Z])/gu;function ai(s){return gt[s]||(gt[s]=s.replace(ln,"-$1").toLowerCase()),gt[s]}function li(s){return s[0].toUpperCase()+s.substring(1)}function mt(s){const[i,e]=s.split("("),t=e.replace(")","").split(",").map(n=>n.trim());return{method:i,observerProps:t}}function vt(s,i){return Object.prototype.hasOwnProperty.call(s,i)||(s[i]=new Map(s[i])),s[i]}const dn=s=>{class i extends s{static enabledWarnings=[];static createProperty(t,n){[String,Boolean,Number,Array].includes(n)&&(n={type:n}),n&&n.reflectToAttribute&&(n.reflect=!0),super.createProperty(t,n)}static getOrCreateMap(t){return vt(this,t)}static finalize(){if(window.litIssuedWarnings&&(window.litIssuedWarnings.add("no-override-create-property"),window.litIssuedWarnings.add("no-override-get-property-descriptor")),super.finalize(),Array.isArray(this.observers)){const t=this.getOrCreateMap("__complexObservers");this.observers.forEach(n=>{const{method:r,observerProps:o}=mt(n);t.set(r,o)})}}static addCheckedInitializer(t){super.addInitializer(n=>{n instanceof this&&t(n)})}static getPropertyDescriptor(t,n,r){const o=super.getPropertyDescriptor(t,n,r);let a=o;if(this.getOrCreateMap("__propKeys").set(t,n),r.sync&&(a={get:o.get,set(l){const d=this[t];Bs(l,d)&&(this[n]=l,this.requestUpdate(t,d,r),this.hasUpdated&&this.performUpdate())},configurable:!0,enumerable:!0}),r.readOnly){const l=a.set;this.addCheckedInitializer(d=>{d[`_set${li(t)}`]=function(_){l.call(d,_)}}),a={get:a.get,set(){},configurable:!0,enumerable:!0}}if("value"in r&&this.addCheckedInitializer(l=>{const d=typeof r.value=="function"?r.value.call(l):r.value;r.readOnly?l[`_set${li(t)}`](d):l[t]=d}),r.observer){const l=r.observer;this.getOrCreateMap("__observers").set(t,l),this.addCheckedInitializer(d=>{d[l]||console.warn(`observer method ${l} not defined`)})}if(r.notify){if(!this.__notifyProps)this.__notifyProps=new Set;else if(!this.hasOwnProperty("__notifyProps")){const l=this.__notifyProps;this.__notifyProps=new Set(l)}this.__notifyProps.add(t)}if(r.computed){const l=`__assignComputed${t}`,d=mt(r.computed);this.prototype[l]=function(..._){this[t]=this[d.method](..._)},this.getOrCreateMap("__computedObservers").set(l,d.observerProps)}return r.attribute||(r.attribute=ai(t)),a}static get polylitConfig(){return{asyncFirstRender:!1}}connectedCallback(){super.connectedCallback();const{polylitConfig:t}=this.constructor;!this.hasUpdated&&!t.asyncFirstRender&&this.performUpdate()}firstUpdated(){super.firstUpdated(),this.$||(this.$={}),this.renderRoot.querySelectorAll("[id]").forEach(t=>{this.$[t.id]=t})}ready(){}willUpdate(t){this.constructor.__computedObservers&&this.__runComplexObservers(t,this.constructor.__computedObservers)}updated(t){const n=this.__isReadyInvoked;this.__isReadyInvoked=!0,this.constructor.__observers&&this.__runObservers(t,this.constructor.__observers),this.constructor.__complexObservers&&this.__runComplexObservers(t,this.constructor.__complexObservers),this.__dynamicPropertyObservers&&this.__runDynamicObservers(t,this.__dynamicPropertyObservers),this.__dynamicMethodObservers&&this.__runComplexObservers(t,this.__dynamicMethodObservers),this.constructor.__notifyProps&&this.__runNotifyProps(t,this.constructor.__notifyProps),n||this.ready()}setProperties(t){Object.entries(t).forEach(([n,r])=>{const o=this.constructor.__propKeys.get(n),a=this[o];this[o]=r,this.requestUpdate(n,a)}),this.hasUpdated&&this.performUpdate()}_createMethodObserver(t){const n=vt(this,"__dynamicMethodObservers"),{method:r,observerProps:o}=mt(t);n.set(r,o)}_createPropertyObserver(t,n){vt(this,"__dynamicPropertyObservers").set(n,t)}__runComplexObservers(t,n){n.forEach((r,o)=>{r.some(a=>t.has(a))&&(this[o]?this[o](...r.map(a=>this[a])):console.warn(`observer method ${o} not defined`))})}__runDynamicObservers(t,n){n.forEach((r,o)=>{t.has(r)&&this[o]&&this[o](this[r],t.get(r))})}__runObservers(t,n){t.forEach((r,o)=>{const a=n.get(o);a!==void 0&&this[a]&&this[a](this[o],r)})}__runNotifyProps(t,n){t.forEach((r,o)=>{n.has(o)&&this.dispatchEvent(new CustomEvent(`${ai(o)}-changed`,{detail:{value:this[o]}}))})}_get(t,n){return Ke(t,n)}_set(t,n,r){an(t,n,r)}}return i},x=B(dn);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Dt extends EventTarget{#e;#i=new Set;#t;#s=!1;constructor(i){super(),this.#e=i,this.#t=new CSSStyleSheet}#r(i){const{propertyName:e}=i;this.#i.has(e)&&this.dispatchEvent(new CustomEvent("property-changed",{detail:{propertyName:e}}))}observe(i){this.connect(),!this.#i.has(i)&&(this.#i.add(i),this.#t.replaceSync(`
      :root::before, :host::before {
        content: '' !important;
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
        visibility: hidden !important;
        transition: 1ms allow-discrete step-end !important;
        transition-property: ${[...this.#i].join(", ")} !important;
      }
    `))}connect(){this.#s||(this.#e.adoptedStyleSheets.unshift(this.#t),this.#n.addEventListener("transitionstart",i=>this.#r(i)),this.#n.addEventListener("transitionend",i=>this.#r(i)),this.#s=!0)}disconnect(){this.#i.clear(),this.#e.adoptedStyleSheets=this.#e.adoptedStyleSheets.filter(i=>i!==this.#t),this.#n.removeEventListener("transitionstart",this.#r),this.#n.removeEventListener("transitionend",this.#r),this.#s=!1}get#n(){return this.#e.documentElement??this.#e.host}static for(i){return i.__cssPropertyObserver||=new Dt(i),i.__cssPropertyObserver}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function hn(s){const{baseStyles:i,themeStyles:e,elementStyles:t,lumoInjector:n}=s.constructor,r=s.__lumoStyleSheet;return r&&(i||e)?[...n.includeBaseStyles?i:[],r,...e]:[r,...t].filter(Boolean)}function Bi(s){Vs(s.shadowRoot,hn(s))}function di(s,i){s.__lumoStyleSheet=i,Bi(s)}function bt(s){s.__lumoStyleSheet=void 0,Bi(s)}/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const hi=new Set;function Nt(s){hi.has(s)||(hi.add(s),console.warn(s))}/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ci=new WeakMap;function ui(s){try{return s.media.mediaText}catch{return Nt('[LumoInjector] Browser denied to access property "mediaText" for some CSS rules, so they were skipped.'),""}}function cn(s){try{return s.cssRules}catch{return Nt('[LumoInjector] Browser denied to access property "cssRules" for some CSS stylesheets, so they were skipped.'),[]}}function Vi(s,i={tags:new Map,modules:new Map}){for(const e of cn(s)){if(e instanceof CSSImportRule){const t=ui(e);t.startsWith("lumo_")?i.modules.set(t,[...e.styleSheet.cssRules]):Vi(e.styleSheet,i);continue}if(e instanceof CSSMediaRule){const t=ui(e);t.startsWith("lumo_")&&i.modules.set(t,[...e.cssRules]);continue}if(e instanceof CSSStyleRule&&e.cssText.includes("-inject")){for(const t of e.style){const n=t.match(/^--_lumo-(.*)-inject-modules$/u)?.[1];if(!n)continue;const r=e.style.getPropertyValue(t);i.tags.set(n,r.split(",").map(o=>o.trim().replace(/'|"/gu,"")))}continue}}return i}function un(s){let i=new Map,e=new Map;for(const t of s){let n=ci.get(t);n||(n=Vi(t),ci.set(t,n)),i=new Map([...i,...n.tags]),e=new Map([...e,...n.modules])}return{tags:i,modules:e}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Hi(s){return`--_lumo-${s.is}-inject`}class _n{#e;#i;#t=new Map;#s=new Map;constructor(i=document){this.#e=i,this.handlePropertyChange=this.handlePropertyChange.bind(this),this.#i=Dt.for(i),this.#i.addEventListener("property-changed",this.handlePropertyChange)}disconnect(){this.#i.removeEventListener("property-changed",this.handlePropertyChange),this.#t.clear(),this.#s.values().forEach(i=>i.forEach(bt))}forceUpdate(){for(const i of this.#t.keys())this.#n(i)}componentConnected(i){const{lumoInjector:e}=i.constructor,{is:t}=e;this.#s.set(t,this.#s.get(t)??new Set),this.#s.get(t).add(i);const n=this.#t.get(t);if(n){n.cssRules.length>0&&di(i,n);return}this.#r(t);const r=Hi(e);this.#i.observe(r)}componentDisconnected(i){const{is:e}=i.constructor.lumoInjector;this.#s.get(e)?.delete(i),bt(i)}handlePropertyChange(i){const{propertyName:e}=i.detail,t=e.match(/^--_lumo-(.*)-inject$/u)?.[1];t&&this.#n(t)}#r(i){this.#t.set(i,new CSSStyleSheet),this.#n(i)}#n(i){const{tags:e,modules:t}=un(this.#o),n=(e.get(i)??[]).flatMap(o=>t.get(o)??[]).map(o=>o.cssText).join(`
`),r=this.#t.get(i);r.replaceSync(n),this.#s.get(i)?.forEach(o=>{n?di(o,r):bt(o)})}get#o(){let i=new Set;for(const e of[this.#e,document])i=i.union(new Set(e.styleSheets)),i=i.union(new Set(e.adoptedStyleSheets));return[...i]}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const _i=new Set;function Wi(s){const i=s.getRootNode();return i.host&&i.host.constructor.version?Wi(i.host):i}const k=s=>class extends s{static finalize(){super.finalize();const e=Hi(this.lumoInjector);this.is&&!_i.has(e)&&(_i.add(e),CSS.registerProperty({name:e,syntax:"<number>",inherits:!0,initialValue:"0"}))}static get lumoInjector(){return{is:this.is,includeBaseStyles:!1}}connectedCallback(){super.connectedCallback();const e=Wi(this);e.__lumoInjectorDisabled||this.isConnected&&(e.__lumoInjector||=new _n(e),this.__lumoInjector=e.__lumoInjector,this.__lumoInjector.componentConnected(this))}disconnectedCallback(){super.disconnectedCallback(),this.__lumoInjector&&(this.__lumoInjector.componentDisconnected(this),this.__lumoInjector=void 0)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ze=s=>class extends s{static get properties(){return{_theme:{type:String,readOnly:!0}}}static get observedAttributes(){return[...super.observedAttributes,"theme"]}attributeChangedCallback(e,t,n){super.attributeChangedCallback(e,t,n),e==="theme"&&this._set_theme(n)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ot=[],pn=new Set,fn=new Set;function gn(s){return s&&Object.prototype.hasOwnProperty.call(s,"__themes")}function mn(s,i){return(s||"").split(" ").some(e=>new RegExp(`^${e.split("*").join(".*")}$`,"u").test(i))}function vn(s){return s.map(i=>i.cssText).join(`
`)}const bn="vaadin-themable-mixin-style";function yn(s,i){const e=document.createElement("style");e.id=bn,e.textContent=vn(s),i.content.appendChild(e)}function Cn(s=""){let i=0;return s.startsWith("lumo-")||s.startsWith("material-")?i=1:s.startsWith("vaadin-")&&(i=2),i}function qi(s){const i=[];return s.include&&[].concat(s.include).forEach(e=>{const t=Ot.find(n=>n.moduleId===e);t?i.push(...qi(t),...t.styles):console.warn(`Included moduleId ${e} not found in style registry`)},s.styles),i}function wn(s){const i=`${s}-default-theme`,e=Ot.filter(t=>t.moduleId!==i&&mn(t.themeFor,s)).map(t=>({...t,styles:[...qi(t),...t.styles],includePriority:Cn(t.moduleId)})).sort((t,n)=>n.includePriority-t.includePriority);return e.length>0?e:Ot.filter(t=>t.moduleId===i)}const S=s=>class extends ze(s){constructor(){super(),pn.add(new WeakRef(this))}static finalize(){if(super.finalize(),this.is&&fn.add(this.is),this.elementStyles)return;const e=this.prototype._template;!e||gn(this)||yn(this.getStylesForThis(),e)}static finalizeStyles(e){return this.baseStyles=e?[e].flat(1/0):[],this.themeStyles=this.getStylesForThis(),[...this.baseStyles,...this.themeStyles]}static getStylesForThis(){const e=s.__themes||[],t=Object.getPrototypeOf(this.prototype),n=(t?t.constructor.__themes:[])||[];this.__themes=[...e,...n,...wn(this.is)];const r=this.__themes.flatMap(o=>o.styles);return r.filter((o,a)=>a===r.lastIndexOf(o))}};/**
 * @license
 * Copyright (c) 2026 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ui=(s,...i)=>{const e=document.createElement("style");e.id=s,e.textContent=i.map(t=>t.toString()).join(`
`),document.head.insertAdjacentElement("afterbegin",e)};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */["--vaadin-text-color","--vaadin-text-color-disabled","--vaadin-text-color-secondary","--vaadin-border-color","--vaadin-border-color-secondary","--vaadin-background-color"].forEach(s=>{CSS.registerProperty({name:s,syntax:"<color>",inherits:!0,initialValue:"light-dark(black, white)"})});Ui("vaadin-base",v`
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
 */const pi=v`
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
`,xn=window.Vaadin.featureFlags.layoutComponentImprovements,En=v`
  ::slotted([data-height-full]) {
    flex: 1;
  }

  ::slotted(vaadin-horizontal-layout[data-height-full]),
  ::slotted(vaadin-vertical-layout[data-height-full]) {
    min-height: 0;
  }
`,Sn=xn?[pi,En]:[pi];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class In extends S(z(x(k(w)))){static get is(){return"vaadin-vertical-layout"}static get styles(){return Sn}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return C`<slot></slot>`}}y(In);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const st=v`
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
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const An=v`
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
`,Tn=v`
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
`,kn=[st,An,Tn];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const nt=s=>s.test(navigator.userAgent),Lt=s=>s.test(navigator.platform),Rn=s=>s.test(navigator.vendor),Pt=nt(/Android/u),ji=nt(/Chrome/u)&&Rn(/Google Inc/u),Gi=nt(/Firefox/u),On=Lt(/^iPad/u)||Lt(/^Mac/u)&&navigator.maxTouchPoints>1,Ln=Lt(/^iPhone/u),ve=Ln||On,Bt=nt(/^((?!chrome|android).)*safari/iu),Me=(()=>{try{return document.createEvent("TouchEvent"),!0}catch{return!1}})();/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let Vt=!1;window.addEventListener("keydown",()=>{Vt=!0},{capture:!0});window.addEventListener("mousedown",()=>{Vt=!1},{capture:!0});function Ye(){let s=document.activeElement||document.body;for(;s.shadowRoot&&s.shadowRoot.activeElement;)s=s.shadowRoot.activeElement;return s}function ne(){return Vt}function Ki(s){const i=s.style;if(i.visibility==="hidden"||i.display==="none")return!0;const e=window.getComputedStyle(s);return e.visibility==="hidden"||e.display==="none"}function Pn(s,i){const e=Math.max(s.tabIndex,0),t=Math.max(i.tabIndex,0);return e===0||t===0?t>e:e>t}function zn(s,i){const e=[];for(;s.length>0&&i.length>0;)Pn(s[0],i[0])?e.push(i.shift()):e.push(s.shift());return e.concat(s,i)}function zt(s){const i=s.length;if(i<2)return s;const e=Math.ceil(i/2),t=zt(s.slice(0,e)),n=zt(s.slice(e));return zn(t,n)}function q(s){return s.checkVisibility?!s.checkVisibility({visibilityProperty:!0}):s.offsetParent===null&&s.clientWidth===0&&s.clientHeight===0?!0:Ki(s)}function Ht(s){return s.matches('[tabindex="-1"]')?!1:s.matches("input, select, textarea, button, object")?s.matches(":not([disabled])"):s.matches("a[href], area[href], iframe, [tabindex], [contentEditable]")}function Wt(s){return s.getRootNode().activeElement===s}function Mn(s){if(!Ht(s))return-1;const i=s.getAttribute("tabindex")||0;return Number(i)}function Yi(s,i){if(s.nodeType!==Node.ELEMENT_NODE||Ki(s))return!1;const e=s,t=Mn(e);let n=t>0;t>=0&&i.push(e);let r=[];return e.localName==="slot"?r=e.assignedNodes({flatten:!0}):r=(e.shadowRoot||e).children,[...r].forEach(o=>{n=Yi(o,i)||n}),n}function Fn(s){const i=[];return Yi(s,i)?zt(i):i}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class $n{saveFocus(i){this.focusNode=i||Ye()}restoreFocus(i){const e=this.focusNode;if(!e)return;const t={preventScroll:i?i.preventScroll:!1,focusVisible:i?i.focusVisible:!1};Ye()===document.body?setTimeout(()=>e.focus(t)):e.focus(t),this.focusNode=null}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const yt=[];class Dn{constructor(i){this.host=i,this.__trapNode=null,this.__onKeyDown=this.__onKeyDown.bind(this)}get __focusableElements(){return Fn(this.__trapNode)}get __focusedElementIndex(){const i=this.__focusableElements;return i.indexOf(i.filter(Wt).pop())}hostConnected(){document.addEventListener("keydown",this.__onKeyDown)}hostDisconnected(){document.removeEventListener("keydown",this.__onKeyDown)}trapFocus(i){if(this.__trapNode=i,this.__focusableElements.length===0)throw this.__trapNode=null,new Error("The trap node should have at least one focusable descendant or be focusable itself.");yt.push(this),this.__focusedElementIndex===-1&&this.__focusableElements[0].focus({focusVisible:ne()})}releaseFocus(){this.__trapNode=null,yt.pop()}__onKeyDown(i){if(this.__trapNode&&this===Array.from(yt).pop()&&i.key==="Tab"){i.preventDefault();const e=i.shiftKey;this.__focusNextElement(e)}}__focusNextElement(i=!1){const e=this.__focusableElements,t=i?-1:1,n=this.__focusedElementIndex,r=(e.length+n+t)%e.length,o=e[r];o.focus({focusVisible:!0}),o.localName==="input"&&o.select()}}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Xi=s=>class extends s{static get properties(){return{focusTrap:{type:Boolean,value:!1},restoreFocusOnClose:{type:Boolean,value:!1},restoreFocusNode:{type:HTMLElement}}}constructor(){super(),this.__focusTrapController=new Dn(this),this.__focusRestorationController=new $n}get _contentRoot(){return this}ready(){super.ready(),this.addController(this.__focusTrapController),this.addController(this.__focusRestorationController)}get _focusTrapRoot(){return this.$.overlay}_resetFocus(){if(this.focusTrap&&this.__focusTrapController.releaseFocus(),this.restoreFocusOnClose&&this._shouldRestoreFocus()){const e=ne(),t=!e;this.__focusRestorationController.restoreFocus({preventScroll:t,focusVisible:e})}}_saveFocus(){this.restoreFocusOnClose&&this.__focusRestorationController.saveFocus(this.restoreFocusNode)}_trapFocus(){this.focusTrap&&!q(this._focusTrapRoot)&&this.__focusTrapController.trapFocus(this._focusTrapRoot)}_shouldRestoreFocus(){const e=Ye();return e===document.body||this._deepContains(e)}_deepContains(e){if(this._contentRoot.contains(e))return!0;let t=e;const n=e.ownerDocument;for(;t&&t!==n&&t!==this._contentRoot;)t=t.parentNode||t.host;return t===this._contentRoot}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const je=new Set,Xe=()=>[...je].filter(s=>!s.hasAttribute("closing")),Zi=s=>{const i=Xe(),e=i[i.indexOf(s)+1];return e?s._deepContains(e)?Zi(e):!1:!0},fi=(s,i=e=>!0)=>{const e=Xe().filter(i);return s===e.pop()},Nn=s=>class extends s{get _last(){return fi(this)}get _isAttached(){return je.has(this)}bringToFront(){fi(this)||Zi(this)||(this.matches(":popover-open")&&(this.hidePopover(),this.showPopover()),this._removeAttachedInstance(),this._appendAttachedInstance())}_enterModalState(){document.body.style.pointerEvents!=="none"&&(this._previousDocumentPointerEvents=document.body.style.pointerEvents,document.body.style.pointerEvents="none"),Xe().forEach(e=>{e!==this&&(e.$.overlay.style.pointerEvents="none")})}_exitModalState(){this._previousDocumentPointerEvents!==void 0&&(document.body.style.pointerEvents=this._previousDocumentPointerEvents,delete this._previousDocumentPointerEvents);const e=Xe();let t;for(;(t=e.pop())&&!(t!==this&&(t.$.overlay.style.removeProperty("pointer-events"),!t.modeless)););}_appendAttachedInstance(){je.add(this)}_removeAttachedInstance(){this._isAttached&&je.delete(this)}};/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Bn(s,i){let e=null,t;const n=document.documentElement;function r(){t&&clearTimeout(t),e&&e.disconnect(),e=null}function o(a=!1,l=1){r();const{left:d,top:_,width:f,height:g}=s.getBoundingClientRect();if(a||i(),!f||!g)return;const b=Math.floor(_),L=Math.floor(n.clientWidth-(d+f)),A=Math.floor(n.clientHeight-(_+g)),M=Math.floor(d),h={rootMargin:`${-b}px ${-L}px ${-A}px ${-M}px`,threshold:Math.max(0,Math.min(1,l))||1};let c=!0;function u(p){const m=p[0].intersectionRatio;if(m!==l){if(!c)return o();m?o(!1,m):t=setTimeout(()=>{o(!1,1e-7)},1e3)}c=!1}e=new IntersectionObserver(u,h),e.observe(s)}return o(!0),r}function P(s,i,e){const t=[s];s.owner&&t.push(s.owner),typeof e=="string"?t.forEach(n=>{n.setAttribute(i,e)}):e?t.forEach(n=>{n.setAttribute(i,"")}):t.forEach(n=>{n.removeAttribute(i)})}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const rt=s=>class extends Xi(Nn(s)){static get properties(){return{opened:{type:Boolean,notify:!0,observer:"_openedChanged",reflectToAttribute:!0,sync:!0},owner:{type:Object,sync:!0},model:{type:Object,sync:!0},renderer:{type:Object,sync:!0},modeless:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_modelessChanged",sync:!0},hidden:{type:Boolean,reflectToAttribute:!0,observer:"_hiddenChanged",sync:!0},withBackdrop:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_withBackdropChanged",sync:!0}}}static get observers(){return["_rendererOrDataChanged(renderer, owner, model, opened)"]}get _rendererRoot(){return this}constructor(){super(),this._boundMouseDownListener=this._mouseDownListener.bind(this),this._boundMouseUpListener=this._mouseUpListener.bind(this),this._boundOutsideClickListener=this._outsideClickListener.bind(this),this._boundKeydownListener=this._keydownListener.bind(this),ve&&(this._boundIosResizeListener=()=>this._detectIosNavbar())}firstUpdated(){super.firstUpdated(),this.popover="manual",this.addEventListener("click",()=>{}),this.$.backdrop&&this.$.backdrop.addEventListener("click",()=>{}),this.addEventListener("mouseup",()=>{document.activeElement===document.body&&this.$.overlay.getAttribute("tabindex")==="0"&&this.$.overlay.focus()}),this.addEventListener("animationcancel",()=>{this._flushAnimation("opening"),this._flushAnimation("closing")})}connectedCallback(){super.connectedCallback(),this._boundIosResizeListener&&(this._detectIosNavbar(),window.addEventListener("resize",this._boundIosResizeListener))}disconnectedCallback(){super.disconnectedCallback(),this.__scheduledOpen&&(cancelAnimationFrame(this.__scheduledOpen),this.__scheduledOpen=null),this._boundIosResizeListener&&window.removeEventListener("resize",this._boundIosResizeListener)}requestContentUpdate(){this.renderer&&this.renderer.call(this.owner,this._rendererRoot,this.owner,this.model)}close(e){const t=new CustomEvent("vaadin-overlay-close",{bubbles:!0,cancelable:!0,detail:{overlay:this,sourceEvent:e}});this.dispatchEvent(t),document.body.dispatchEvent(t),t.defaultPrevented||(this.opened=!1)}setBounds(e,t=!0){const n=this.$.overlay,r={...e};t&&n.style.position!=="absolute"&&(n.style.position="absolute"),Object.keys(r).forEach(o=>{r[o]!==null&&!isNaN(r[o])&&(r[o]=`${r[o]}px`)}),Object.assign(n.style,r)}_detectIosNavbar(){if(!this.opened)return;const e=window.innerHeight,n=window.innerWidth>e,r=document.documentElement.clientHeight;n&&r>e?this.style.setProperty("--vaadin-overlay-viewport-bottom",`${r-e}px`):this.style.setProperty("--vaadin-overlay-viewport-bottom","0")}_shouldAddGlobalListeners(){return!this.modeless}_addGlobalListeners(){this.__hasGlobalListeners||(this.__hasGlobalListeners=!0,document.addEventListener("mousedown",this._boundMouseDownListener),document.addEventListener("mouseup",this._boundMouseUpListener),document.documentElement.addEventListener("click",this._boundOutsideClickListener,!0))}_removeGlobalListeners(){this.__hasGlobalListeners&&(this.__hasGlobalListeners=!1,document.removeEventListener("mousedown",this._boundMouseDownListener),document.removeEventListener("mouseup",this._boundMouseUpListener),document.documentElement.removeEventListener("click",this._boundOutsideClickListener,!0))}_rendererOrDataChanged(e,t,n,r){const o=this._oldOwner!==t||this._oldModel!==n;this._oldModel=n,this._oldOwner=t;const a=this._oldRenderer!==e,l=this._oldRenderer!==void 0;this._oldRenderer=e;const d=this._oldOpened!==r;this._oldOpened=r,a&&l&&(this._rendererRoot.innerHTML="",delete this._rendererRoot._$litPart$),r&&e&&(a||d||o)&&this.requestContentUpdate()}_modelessChanged(e){this.opened&&(this._shouldAddGlobalListeners()?this._addGlobalListeners():this._removeGlobalListeners()),e?this._exitModalState():this.opened&&this._enterModalState(),P(this,"modeless",e)}_withBackdropChanged(e){P(this,"with-backdrop",e)}_openedChanged(e,t){if(e){if(!this.isConnected){this.opened=!1;return}this._saveFocus(),this._animatedOpening(),this.__scheduledOpen=requestAnimationFrame(()=>{setTimeout(()=>{this._trapFocus();const n=new CustomEvent("vaadin-overlay-open",{detail:{overlay:this},bubbles:!0});this.dispatchEvent(n),document.body.dispatchEvent(n)})}),document.addEventListener("keydown",this._boundKeydownListener),this._shouldAddGlobalListeners()&&this._addGlobalListeners()}else t&&(this.__scheduledOpen&&(cancelAnimationFrame(this.__scheduledOpen),this.__scheduledOpen=null),this._resetFocus(),this._animatedClosing(),document.removeEventListener("keydown",this._boundKeydownListener),this._shouldAddGlobalListeners()&&this._removeGlobalListeners())}_hiddenChanged(e){e&&this.hasAttribute("closing")&&this._flushAnimation("closing")}_shouldAnimate(){const e=getComputedStyle(this),t=e.getPropertyValue("animation-name");return!(e.getPropertyValue("display")==="none")&&t&&t!=="none"}_enqueueAnimation(e,t){const n=`__${e}Handler`,r=o=>{o&&o.target!==this||(t(),this.removeEventListener("animationend",r),delete this[n])};this[n]=r,this.addEventListener("animationend",r)}_flushAnimation(e){const t=`__${e}Handler`;typeof this[t]=="function"&&this[t]()}_animatedOpening(){this._isAttached&&this.hasAttribute("closing")&&this._flushAnimation("closing"),this._attachOverlay(),this._appendAttachedInstance(),this.bringToFront(),this.modeless||this._enterModalState(),P(this,"opening",!0),this._shouldAnimate()?this._enqueueAnimation("opening",()=>{this._finishOpening()}):this._finishOpening()}_attachOverlay(){this.showPopover()}_finishOpening(){P(this,"opening",!1)}_finishClosing(){this._detachOverlay(),this._removeAttachedInstance(),this.$.overlay.style.removeProperty("pointer-events"),P(this,"closing",!1),this.dispatchEvent(new CustomEvent("vaadin-overlay-closed"))}_animatedClosing(){this.hasAttribute("opening")&&this._flushAnimation("opening"),this._isAttached&&(this._exitModalState(),P(this,"closing",!0),this.dispatchEvent(new CustomEvent("vaadin-overlay-closing")),this._shouldAnimate()?this._enqueueAnimation("closing",()=>{this._finishClosing()}):this._finishClosing())}_detachOverlay(){this.hidePopover()}_mouseDownListener(e){this._mouseDownInside=e.composedPath().indexOf(this.$.overlay)>=0}_mouseUpListener(e){this._mouseUpInside=e.composedPath().indexOf(this.$.overlay)>=0}_shouldCloseOnOutsideClick(e){return this._last}_outsideClickListener(e){if(e.composedPath().includes(this.$.overlay)||this._mouseDownInside||this._mouseUpInside){this._mouseDownInside=!1,this._mouseUpInside=!1;return}if(!this._shouldCloseOnOutsideClick(e))return;const t=new CustomEvent("vaadin-overlay-outside-click",{cancelable:!0,detail:{sourceEvent:e}});this.dispatchEvent(t),this.opened&&!t.defaultPrevented&&this.close(e)}_keydownListener(e){if(!(!this._last||e.defaultPrevented)&&!(!this._shouldAddGlobalListeners()&&!e.composedPath().includes(this._focusTrapRoot))&&e.key==="Escape"){const t=new CustomEvent("vaadin-overlay-escape-press",{cancelable:!0,detail:{sourceEvent:e}});this.dispatchEvent(t),this.opened&&!t.defaultPrevented&&this.close(e)}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Vn=s=>class extends rt(s){static get properties(){return{headerTitle:{type:String},headerRenderer:{type:Object},footerRenderer:{type:Object}}}static get observers(){return["_headerFooterRendererChange(headerRenderer, footerRenderer, opened)","_headerTitleChanged(headerTitle, opened)"]}get _contentRoot(){return this.owner}get _rendererRoot(){if(!this.__savedRoot){const e=document.createElement("vaadin-dialog-content");e.style.display="contents",this.owner.appendChild(e),this.__savedRoot=e}return this.__savedRoot}ready(){super.ready(),this.__resizeObserver=new ResizeObserver(()=>{requestAnimationFrame(()=>{this.__updateOverflow()})}),this.__resizeObserver.observe(this.$.resizerContainer),this.$.content.addEventListener("scroll",()=>{this.__updateOverflow()}),this.shadowRoot.addEventListener("slotchange",()=>{this.__updateOverflow()})}__createContainer(e){const t=document.createElement("vaadin-dialog-content");return t.setAttribute("slot",e),t}__clearContainer(e){e.innerHTML="",delete e._$litPart$}__initContainer(e,t){return e?this.__clearContainer(e):(e=this.__createContainer(t),this.owner.appendChild(e)),e}_headerFooterRendererChange(e,t,n){const r=this.__oldHeaderRenderer!==e;this.__oldHeaderRenderer=e;const o=this.__oldFooterRenderer!==t;this.__oldFooterRenderer=t;const a=this._oldOpenedFooterHeader!==n;this._oldOpenedFooterHeader=n,P(this,"has-header",!!e),P(this,"has-footer",!!t),r&&(e?this.headerContainer=this.__initContainer(this.headerContainer,"header-content"):this.headerContainer&&(this.headerContainer.remove(),this.headerContainer=null,this.__updateOverflow())),o&&(t?this.footerContainer=this.__initContainer(this.footerContainer,"footer"):this.footerContainer&&(this.footerContainer.remove(),this.footerContainer=null,this.__updateOverflow())),(e&&(r||a)||t&&(o||a))&&n&&this.requestContentUpdate()}_headerTitleChanged(e,t){P(this,"has-title",!!e),t&&(e||this._oldHeaderTitle)&&this.requestContentUpdate(),this._oldHeaderTitle=e}_headerTitleRenderer(){this.headerTitle?(this.headerTitleElement||(this.headerTitleElement=document.createElement("h2"),this.headerTitleElement.setAttribute("slot","title"),this.headerTitleElement.classList.add("draggable")),this.owner.appendChild(this.headerTitleElement),this.headerTitleElement.textContent=this.headerTitle):this.headerTitleElement&&(this.headerTitleElement.remove(),this.headerTitleElement=null)}requestContentUpdate(){super.requestContentUpdate(),this.headerContainer&&this.headerRenderer&&this.headerRenderer.call(this.owner,this.headerContainer,this.owner),this.footerContainer&&this.footerRenderer&&this.footerRenderer.call(this.owner,this.footerContainer,this.owner),this._headerTitleRenderer(),this.__updateOverflow()}getBounds(){const e=this.$.overlay.getBoundingClientRect(),t=this.getBoundingClientRect(),n=e.top-t.top,r=e.left-t.left,o=e.width,a=e.height;return{top:n,left:r,width:o,height:a}}__updateOverflow(){let e="";const t=this.$.content;t.scrollTop>0&&(e+=" top"),t.scrollTop<t.scrollHeight-t.clientHeight&&(e+=" bottom");const n=e.trim();n.length>0&&this.getAttribute("overflow")!==n?P(this,"overflow",n):n.length===0&&this.hasAttribute("overflow")&&P(this,"overflow",null)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Hn extends Vn(N(S(x(k(w))))){static get is(){return"vaadin-dialog-overlay"}static get styles(){return kn}get _focusTrapRoot(){return this.owner}render(){return C`
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
    `}}y(Hn);/**
 * @license
 * Copyright 2018 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const U=s=>s??Li;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Wn=s=>class extends s{static get properties(){return{opened:{type:Boolean,reflectToAttribute:!0,value:!1,notify:!0,sync:!0},noCloseOnOutsideClick:{type:Boolean,value:!1},noCloseOnEsc:{type:Boolean,value:!1},modeless:{type:Boolean,value:!1},top:{type:String},left:{type:String},overlayRole:{type:String}}}static get observers(){return["__positionChanged(top, left)"]}ready(){super.ready();const e=this.$.overlay;e.addEventListener("vaadin-overlay-outside-click",this._handleOutsideClick.bind(this)),e.addEventListener("vaadin-overlay-escape-press",this._handleEscPress.bind(this)),e.addEventListener("vaadin-overlay-closed",this.__handleOverlayClosed.bind(this)),this._overlayElement=e,this.hasAttribute("role")||(this.role="dialog"),this.setAttribute("tabindex","0")}updated(e){super.updated(e),e.has("overlayRole")&&(this.role=this.overlayRole||"dialog"),e.has("modeless")&&(this.modeless?this.removeAttribute("aria-modal"):this.setAttribute("aria-modal","true"))}__handleOverlayClosed(){this.dispatchEvent(new CustomEvent("closed"))}connectedCallback(){super.connectedCallback(),this.__restoreOpened&&(this.opened=!0)}disconnectedCallback(){super.disconnectedCallback(),setTimeout(()=>{this.isConnected||(this.__restoreOpened=this.opened,this.opened=!1)})}_onOverlayOpened(e){e.detail.value===!1&&(this.opened=!1)}_handleOutsideClick(e){this.noCloseOnOutsideClick&&e.preventDefault()}_handleEscPress(e){this.noCloseOnEsc&&e.preventDefault()}_bringOverlayToFront(){this.modeless&&this._overlayElement.bringToFront()}__positionChanged(e,t){requestAnimationFrame(()=>this.$.overlay.setBounds({top:e,left:t}))}__sizeChanged(e,t){requestAnimationFrame(()=>this.$.overlay.setBounds({width:e,height:t},!1))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Ze(s){return s.touches?s.touches[0]:s}function Qi(s){return s.clientX>=0&&s.clientX<=window.innerWidth&&s.clientY>=0&&s.clientY<=window.innerHeight}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const qn=s=>class extends s{static get properties(){return{draggable:{type:Boolean,value:!1,reflectToAttribute:!0},_touchDevice:{type:Boolean,value:Me},__dragHandleClassName:{type:String}}}ready(){super.ready(),this._originalBounds={},this._originalMouseCoords={},this._startDrag=this._startDrag.bind(this),this._drag=this._drag.bind(this),this._stopDrag=this._stopDrag.bind(this),this.$.overlay.$.overlay.addEventListener("mousedown",this._startDrag),this.$.overlay.$.overlay.addEventListener("touchstart",this._startDrag)}_startDrag(e){if(!(e.type==="touchstart"&&e.touches.length>1)&&this.draggable&&(e.button===0||e.touches)){const t=this.$.overlay.$.resizerContainer,n=e.target===t,r=e.offsetX>t.clientWidth||e.offsetY>t.clientHeight,o=e.target===this.$.overlay.$.content,a=e.composedPath().some((l,d)=>{if(!l.classList)return!1;const _=l.classList.contains(this.__dragHandleClassName||"draggable"),f=l.classList.contains("draggable-leaf-only"),g=d===0;return f&&g||_&&(!f||g)});if(n&&!r||o||a){a||e.preventDefault(),this._originalBounds=this.$.overlay.getBounds();const l=Ze(e);if(this._originalMouseCoords={top:l.pageY,left:l.pageX},window.addEventListener("mouseup",this._stopDrag),window.addEventListener("touchend",this._stopDrag),window.addEventListener("mousemove",this._drag),window.addEventListener("touchmove",this._drag),this.$.overlay.$.overlay.style.position!=="absolute"){const{top:d,left:_}=this._originalBounds;this.top=d,this.left=_}}}}_drag(e){const t=Ze(e);if(Qi(t)){const n=this._originalBounds.top+(t.pageY-this._originalMouseCoords.top),r=this._originalBounds.left+(t.pageX-this._originalMouseCoords.left);this.top=n,this.left=r}}_stopDrag(){this.dispatchEvent(new CustomEvent("dragged",{bubbles:!0,composed:!0,detail:{top:this.top,left:this.left}})),window.removeEventListener("mouseup",this._stopDrag),window.removeEventListener("touchend",this._stopDrag),window.removeEventListener("mousemove",this._drag),window.removeEventListener("touchmove",this._drag)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Un=s=>class extends s{static get properties(){return{renderer:{type:Object},headerTitle:String,headerRenderer:{type:Object},footerRenderer:{type:Object}}}requestContentUpdate(){this._overlayElement&&this._overlayElement.requestContentUpdate()}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const jn=s=>class extends s{static get properties(){return{resizable:{type:Boolean,value:!1,reflectToAttribute:!0}}}ready(){super.ready(),this._originalBounds={},this._originalMouseCoords={},this._resizeListeners={start:{},resize:{},stop:{}},this._addResizeListeners()}_addResizeListeners(){["n","e","s","w","nw","ne","se","sw"].forEach(e=>{const t=document.createElement("div");this._resizeListeners.start[e]=n=>this._startResize(n,e),this._resizeListeners.resize[e]=n=>this._resize(n,e),this._resizeListeners.stop[e]=()=>this._stopResize(e),e.length===1&&t.classList.add("edge"),t.classList.add("resizer"),t.classList.add(e),t.addEventListener("mousedown",this._resizeListeners.start[e]),t.addEventListener("touchstart",this._resizeListeners.start[e]),this.$.overlay.$.resizerContainer.appendChild(t)})}_startResize(e,t){if(!(e.type==="touchstart"&&e.touches.length>1)&&(e.button===0||e.touches)){e.preventDefault(),this._originalBounds=this.$.overlay.getBounds();const n=Ze(e);this._originalMouseCoords={top:n.pageY,left:n.pageX},window.addEventListener("mousemove",this._resizeListeners.resize[t]),window.addEventListener("touchmove",this._resizeListeners.resize[t]),window.addEventListener("mouseup",this._resizeListeners.stop[t]),window.addEventListener("touchend",this._resizeListeners.stop[t]),this.$.overlay.setBounds(this._originalBounds),this.$.overlay.setAttribute("has-bounds-set","")}}_resize(e,t){const n=Ze(e);Qi(n)&&t.split("").forEach(o=>{switch(o){case"n":{const a=this._originalBounds.height-(n.pageY-this._originalMouseCoords.top),l=this._originalBounds.top+(n.pageY-this._originalMouseCoords.top);a>40&&(this.top=l,this.height=a);break}case"e":{const a=this._originalBounds.width+(n.pageX-this._originalMouseCoords.left);a>40&&(this.width=a);break}case"s":{const a=this._originalBounds.height+(n.pageY-this._originalMouseCoords.top);a>40&&(this.height=a);break}case"w":{const a=this._originalBounds.width-(n.pageX-this._originalMouseCoords.left),l=this._originalBounds.left+(n.pageX-this._originalMouseCoords.left);a>40&&(this.left=l,this.width=a);break}}})}_stopResize(e){window.removeEventListener("mousemove",this._resizeListeners.resize[e]),window.removeEventListener("touchmove",this._resizeListeners.resize[e]),window.removeEventListener("mouseup",this._resizeListeners.stop[e]),window.removeEventListener("touchend",this._resizeListeners.stop[e]),this.dispatchEvent(new CustomEvent("resize",{detail:this._getResizeDimensions()}))}_getResizeDimensions(){const{width:e,height:t,top:n,left:r}=getComputedStyle(this.$.overlay.$.overlay);return{width:e,height:t,top:n,left:r}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Gn=s=>class extends s{static get properties(){return{width:{type:String},height:{type:String}}}static get observers(){return["__sizeChanged(width, height)"]}__sizeChanged(e,t){requestAnimationFrame(()=>this.$.overlay.setBounds({width:e,height:t},!1))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Kn extends Gn(qn(jn(Un(Wn(ze(z(x(w)))))))){static get is(){return"vaadin-dialog"}static get styles(){return v`
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
    `}render(){return C`
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
        theme="${U(this._theme)}"
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
    `}updated(i){super.updated(i),i.has("headerTitle")&&(this.ariaLabel=this.headerTitle)}}y(Kn);/**
 * @license
 * Copyright 2020 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Yn=(s,i)=>s?._$litType$!==void 0,Ji=s=>s.strings===void 0,Xn={},Zn=(s,i=Xn)=>s._$AH=i;/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Oe=(s,i)=>{const e=s._$AN;if(e===void 0)return!1;for(const t of e)t._$AO?.(i,!1),Oe(t,i);return!0},Qe=s=>{let i,e;do{if((i=s._$AM)===void 0)break;e=i._$AN,e.delete(s),s=i}while(e?.size===0)},es=s=>{for(let i;i=s._$AM;s=i){let e=i._$AN;if(e===void 0)i._$AN=e=new Set;else if(e.has(s))break;e.add(s),er(i)}};function Qn(s){this._$AN!==void 0?(Qe(this),this._$AM=s,es(this)):this._$AM=s}function Jn(s,i=!1,e=0){const t=this._$AH,n=this._$AN;if(n!==void 0&&n.size!==0)if(i)if(Array.isArray(t))for(let r=e;r<t.length;r++)Oe(t[r],!1),Qe(t[r]);else t!=null&&(Oe(t,!1),Qe(t));else Oe(this,s)}const er=s=>{s.type==ee.CHILD&&(s._$AP??=Jn,s._$AQ??=Qn)};class tr extends Pi{constructor(){super(...arguments),this._$AN=void 0}_$AT(i,e,t){super._$AT(i,e,t),es(this),this.isConnected=i._$AU}_$AO(i,e=!0){i!==this.isConnected&&(this.isConnected=i,i?this.reconnected?.():this.disconnected?.()),e&&(Oe(this,i),Qe(this))}setValue(i){if(Ji(this._$Ct))this._$Ct._$AI(i,this);else{const e=[...this._$Ct._$AH];e[this._$Ci]=i,this._$Ct._$AI(e,this,0)}}disconnected(){}reconnected(){}}class ir extends tr{constructor(i){if(super(i),i.type!==ee.CHILD)throw new Error(`${this.constructor.directiveName}() can only be used in child bindings`)}update(i,[e,t]){return this.updateContent(i,e,t),ke}updateContent(i,e,t){const{parentNode:n,startNode:r}=i;this.__parentNode=n;const o=t!=null,a=o?this.getNewNode(e,t):null,l=this.getOldNode(i);if(clearTimeout(this.__parentNode.__nodeRetryTimeout),o&&!a)this.__parentNode.__nodeRetryTimeout=setTimeout(()=>this.updateContent(i,e,t));else{if(l===a)return;l&&a?n.replaceChild(a,l):l?n.removeChild(l):a&&r.after(a)}}getNewNode(i,e){return window.Vaadin.Flow.clients[i].getByNodeId(e)}getOldNode(i){const{startNode:e,endNode:t}=i;if(e.nextSibling!==t)return e.nextSibling}disconnected(){clearTimeout(this.__parentNode.__nodeRetryTimeout)}}const ts=zi(ir);function sr(s,i){return ts(s,i)}function nr(s,i,e){$t(C`${i.map(t=>ts(s,t))}`,e)}function rr(s){const i=s.insertBefore;s.insertBefore=function(e,t){return t&&t.parentNode===this?i.call(this,e,t):i.call(this,e,null)}}window.Vaadin||={};window.Vaadin.FlowComponentHost||={patchVirtualContainer:rr,getNode:sr,setChildNodes:nr};/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */CSS.registerProperty({name:"--_min-width-labels-aside",syntax:"<length>",inherits:!1,initialValue:"0px"});Ui("vaadin-form-layout-base",v`
    @layer vaadin.base {
      html {
        --vaadin-form-layout-label-spacing: var(--vaadin-gap-s);
        --vaadin-form-layout-label-width: 8em;
        --vaadin-form-layout-column-spacing: var(--vaadin-gap-l);
        --vaadin-form-layout-row-spacing: var(--vaadin-gap-l);
      }
    }
  `);const or=v`
  :host {
    /* Default values */
    --_label-spacing: var(--vaadin-form-layout-label-spacing);
    --_label-width: var(--vaadin-form-layout-label-width);
    --_column-spacing: var(--vaadin-form-layout-column-spacing);
    --_row-spacing: var(--vaadin-form-layout-row-spacing);

    align-self: stretch;
    display: block;
    max-width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  :host(:not([auto-responsive])) {
    contain: layout;
  }

  :host(:not([auto-responsive])) #layout {
    align-items: baseline; /* default \`stretch\` is not appropriate */
    display: flex;
    flex-wrap: wrap; /* the items should wrap */
    /* Compensate for row spacing */
    margin-block: calc(-0.5 * var(--_row-spacing));
  }

  :host(:not([auto-responsive])) #layout ::slotted(*) {
    /* Items should neither grow nor shrink. */
    flex-grow: 0;
    flex-shrink: 0;

    /* Margins make spacing between the columns and rows */
    margin-inline: calc(0.5 * var(--_column-spacing));
    margin-block: calc(0.5 * var(--_row-spacing));
  }

  #layout ::slotted(br) {
    display: none;
  }

  :host([auto-responsive]) {
    /* Column width */
    --_column-width: var(--vaadin-field-default-width, 12em);
    --_column-width-labels-above: var(--_column-width);
    --_column-width-labels-aside: calc(var(--_column-width) + var(--_label-width) + var(--_label-spacing));

    /* Column gap */
    --_min-total-gap: calc((var(--_min-columns) - 1) * var(--_column-spacing));
    --_max-total-gap: calc((var(--_max-columns) - 1) * var(--_column-spacing));

    /* Minimum form layout width */
    --_min-width-labels-above: calc(var(--_min-columns) * var(--_column-width-labels-above) + var(--_min-total-gap));
    --_min-width-labels-aside: calc(var(--_min-columns) * var(--_column-width-labels-aside) + var(--_min-total-gap));
    --_min-width: var(--_min-width-labels-above);

    /* Maximum form layout width */
    --_max-width-labels-above: calc(var(--_max-columns) * var(--_column-width-labels-above) + var(--_max-total-gap));
    --_max-width-labels-aside: calc(var(--_max-columns) * var(--_column-width-labels-aside) + var(--_max-total-gap));
    --_max-width: var(--_max-width-labels-above);

    display: flex;
    min-width: var(--_min-width);
  }

  :host([auto-responsive]) #layout {
    /* By default, labels should be displayed above the fields */
    --_form-item-labels-above: initial; /* true */
    --_form-item-labels-aside: ' '; /* false */

    /* CSS grid related properties */
    --_grid-column-width: var(--_column-width-labels-above);
    --_grid-repeat: var(--_grid-column-width);

    display: grid;
    gap: var(--_row-spacing) var(--_column-spacing);

    /*
      Auto-columns can be created when an item's colspan exceeds the rendered column count.
      By setting auto-columns to 0, we exclude these columns from --_grid-rendered-column-count,
      which is then used to cap the colspan.
    */
    grid-auto-columns: 0;

    align-self: start;
    grid-template-columns: repeat(auto-fill, var(--_grid-repeat));
    place-items: baseline start;

    /*
      Firefox requires min-width on both :host and #layout to allow the layout
      to shrink below the value specified in the CSS width property above.
    */
    min-width: var(--_min-width);

    /*
      To prevent the layout from exceeding the column limit defined by --_max-columns,
      its width needs to be constrained:

      1. "width" is used instead of "max-width" because, together with the default "flex: 0 1 auto",
      it allows the layout to shrink to its minimum width inside <vaadin-horizontal-layout>, which
      wouldn't work otherwise.

      2. "width" is used instead of "flex-basis" to make the layout expand to the maximum
      number of columns inside <vaadin-overlay>, which creates a new stacking context
      without a predefined width.
    */
    width: var(--_max-width);
  }

  :host([auto-responsive]) #layout ::slotted(*) {
    /* Make form items inherit label position from the layout */
    --_form-item-labels-above: inherit;
    --_form-item-labels-aside: inherit;

    /* By default, place each child on a new row */
    grid-column: 1 / span min(var(--_grid-colspan, 1), var(--_grid-rendered-column-count));

    /* Form items do not need margins in auto-responsive mode */
    margin: 0;
  }

  :host([auto-responsive][auto-rows]) #layout ::slotted(*) {
    grid-column-start: var(--_grid-colstart, auto);
  }

  :host([auto-responsive][labels-aside]) {
    --_max-width: var(--_max-width-labels-aside);
  }

  :host([auto-responsive][labels-aside]) #layout[fits-labels-aside] {
    --_form-item-labels-above: ' '; /* false */
    --_form-item-labels-aside: initial; /* true */
    --_grid-column-width: var(--_column-width-labels-aside);
  }

  :host([auto-responsive][expand-columns]) #layout {
    /*
      The "min" value in minmax ensures that once "maxColumns" is reached, the grid stops adding
      new columns and instead expands the existing ones evenly to fill the available space.

      The "max" value in minmax allows CSS grid columns to grow and evenly distribute any space
      that remains when there isn't room for an additional column and "maxColumns" hasn't been
      reached yet.
    */
    --_grid-repeat: minmax(
      max(var(--_grid-column-width), calc((100% - var(--_max-total-gap)) / var(--_max-columns))),
      1fr
    );

    /* Allow the layout to take up full available width of the parent element. */
    flex-grow: 1;
  }
`,ar=v`
  /* Using :where to ensure user styles always take precedence */
  :where(
    vaadin-form-layout[auto-responsive] > *,
    vaadin-form-layout[auto-responsive] vaadin-form-row > *,
    vaadin-form-layout[auto-responsive] vaadin-form-item > *
  ) {
    box-sizing: border-box;
    max-width: 100%;
  }

  :where(
    vaadin-form-layout[auto-responsive][expand-fields] > *,
    vaadin-form-layout[auto-responsive][expand-fields] vaadin-form-row > *,
    vaadin-form-layout[auto-responsive][expand-fields] vaadin-form-item > *
  ) {
    min-width: 100%;
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ct=new WeakMap;function lr(s){return Ct.has(s)||Ct.set(s,new Set),Ct.get(s)}function dr(s,i){const e=document.createElement("style");e.textContent=s,i===document?document.head.appendChild(e):i.insertBefore(e,i.firstChild)}const Fe=B(s=>class extends s{get slotStyles(){return[]}connectedCallback(){super.connectedCallback(),this.__applySlotStyles()}__applySlotStyles(){const e=this.getRootNode(),t=lr(e);this.slotStyles.forEach(n=>{t.has(n)||(dr(n,e),t.add(n))})}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class is{constructor(i,e){this.host=i,this.props={},this.config=e,this.isConnected=!1,this.__resizeObserver=new ResizeObserver(t=>setTimeout(()=>this._onResize(t))),this.__mutationObserver=new MutationObserver(t=>this._onMutation(t))}connect(){this.isConnected||(this.isConnected=!0,this.__resizeObserver.observe(this.host),this.__mutationObserver.observe(this.host,this.config.mutationObserverOptions))}disconnect(){this.isConnected&&(this.isConnected=!1,this.__resizeObserver.disconnect(),this.__mutationObserver.disconnect())}setProps(i){this.props=i}updateLayout(){}_onResize(i){}_onMutation(i){}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function gi(s){return s.localName==="br"}class hr extends is{constructor(i){super(i,{mutationObserverOptions:{subtree:!0,childList:!0,attributes:!0,attributeFilter:["colspan","data-colspan","hidden"]}})}connect(){this.isConnected||(super.connect(),this.updateLayout())}disconnect(){if(!this.isConnected)return;super.disconnect();const{host:i}=this;i.style.removeProperty("--_column-width"),i.style.removeProperty("--_max-columns"),i.$.layout.removeAttribute("fits-labels-aside"),i.$.layout.style.removeProperty("--_grid-rendered-column-count"),this.__children.forEach(e=>{e.style.removeProperty("--_grid-colstart"),e.style.removeProperty("--_grid-colspan")})}setProps(i){super.setProps(i),this.isConnected&&this.updateLayout()}updateLayout(){const{host:i,props:e}=this;if(!this.isConnected||q(i))return;let t=0,n=0;const r=this.__children;r.filter(o=>gi(o)||!q(o)).forEach((o,a,l)=>{const d=l[a-1];if(gi(o)){t=0;return}(d&&d.parentElement!==o.parentElement||!e.autoRows&&o.parentElement===i)&&(t=0),e.autoRows&&t===0?o.style.setProperty("--_grid-colstart",1):o.style.removeProperty("--_grid-colstart");const _=o.getAttribute("colspan")||o.getAttribute("data-colspan");_?(t+=parseInt(_),o.style.setProperty("--_grid-colspan",_)):(t+=1,o.style.removeProperty("--_grid-colspan")),n=Math.max(n,t)}),r.filter(q).forEach(o=>{o.style.removeProperty("--_grid-colstart")}),e.columnWidth?i.style.setProperty("--_column-width",e.columnWidth):i.style.removeProperty("--_column-width"),i.style.setProperty("--_min-columns",e.minColumns),i.style.setProperty("--_max-columns",Math.min(Math.max(e.minColumns,e.maxColumns),n)),i.$.layout.toggleAttribute("fits-labels-aside",this.props.labelsAside&&this.__fitsLabelsAside),i.$.layout.style.setProperty("--_grid-rendered-column-count",this.__renderedColumnCount)}_onResize(){this.updateLayout()}_onMutation(i){i.some(({target:t})=>t===this.host||t.parentElement===this.host||t.parentElement.localName==="vaadin-form-row")&&this.updateLayout()}get __children(){return[...this.host.children].flatMap(i=>i.localName==="vaadin-form-row"?[...i.children]:i)}get __renderedColumnCount(){const{gridTemplateColumns:i}=getComputedStyle(this.host.$.layout);return i.split(" ").filter(e=>e!=="0px").length}get __minWidthLabelsAside(){return parseFloat(getComputedStyle(this.host).getPropertyValue("--_min-width-labels-aside"))}get __fitsLabelsAside(){return this.host.offsetWidth>=this.__minWidthLabelsAside}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function cr(s){return CSS.supports("word-spacing",s)&&!["inherit","normal"].includes(s)}function mi(s){return typeof s=="number"&&s>=1&&s<1/0?Math.floor(s):1}class ur extends is{constructor(i){super(i,{mutationObserverOptions:{subtree:!0,childList:!0,attributes:!0,attributeFilter:["colspan","data-colspan","hidden"]}})}connect(){this.isConnected||(super.connect(),this.__selectResponsiveStep(),this.updateLayout(),requestAnimationFrame(()=>this.__selectResponsiveStep()),requestAnimationFrame(()=>this.updateLayout()))}disconnect(){if(!this.isConnected)return;super.disconnect();const{host:i}=this;i.$.layout.style.removeProperty("opacity"),[...i.children].forEach(e=>{e.style.removeProperty("width"),e.style.removeProperty("margin-left"),e.style.removeProperty("margin-right"),e.removeAttribute("label-position")})}setProps(i){const{responsiveSteps:e}=i;if(!Array.isArray(e))throw new Error('Invalid "responsiveSteps" type, an Array is required.');if(e.length<1)throw new Error('Invalid empty "responsiveSteps" array, at least one item is required.');e.forEach(t=>{if(mi(t.columns)!==t.columns)throw new Error(`Invalid 'columns' value of ${t.columns}, a natural number is required.`);if(t.minWidth!==void 0&&!cr(t.minWidth))throw new Error(`Invalid 'minWidth' value of ${t.minWidth}, a valid CSS length required.`);if(t.labelsPosition!==void 0&&["aside","top"].indexOf(t.labelsPosition)===-1)throw new Error(`Invalid 'labelsPosition' value of ${t.labelsPosition}, 'aside' or 'top' string is required.`)}),super.setProps(i),this.isConnected&&(this.__selectResponsiveStep(),this.updateLayout())}updateLayout(){const{host:i}=this;if(!this.isConnected||q(i))return;const e=getComputedStyle(i),t=e.getPropertyValue("--_column-spacing"),n=e.direction,r=`margin-${n==="ltr"?"left":"right"}`,o=`margin-${n==="ltr"?"right":"left"}`,a=i.offsetWidth;let l=0;Array.from(i.children).filter(d=>d.localName==="br"||getComputedStyle(d).display!=="none").forEach((d,_,f)=>{if(d.localName==="br"){l=0;return}const g=d.getAttribute("colspan")||d.getAttribute("data-colspan");let b;b=mi(parseFloat(g)),b=Math.min(b,this.__columnCount);const L=b/this.__columnCount;d.style.width=`calc(${L*100}% - ${1-L} * ${t})`,l+b>this.__columnCount&&(l=0),l===0?d.style.setProperty(r,"0px"):d.style.removeProperty(r);const A=_+1,M=A<f.length&&f[A].localName==="br";if(l+b===this.__columnCount)d.style.setProperty(o,"0px");else if(M){const $=(this.__columnCount-l-b)/this.__columnCount;d.style.setProperty(o,`calc(${$*a}px + ${$} * ${t})`)}else d.style.removeProperty(o);l=(l+b)%this.__columnCount,d.localName==="vaadin-form-item"&&(this.__labelsOnTop?d.getAttribute("label-position")!=="top"&&(d.__useLayoutLabelPosition=!0,d.setAttribute("label-position","top")):d.__useLayoutLabelPosition&&(delete d.__useLayoutLabelPosition,d.removeAttribute("label-position")))})}_onResize(){const{host:i}=this;if(q(i)){i.$.layout.style.opacity="0";return}this.__selectResponsiveStep(),this.updateLayout(),i.$.layout.style.opacity=""}_onMutation(i){i.some(({target:t})=>t===this.host||t.parentElement===this.host)&&this.updateLayout()}__selectResponsiveStep(){if(!this.isConnected)return;const{host:i,props:e}=this;let t;const n="background-position";e.responsiveSteps.forEach(r=>{i.$.layout.style.setProperty(n,r.minWidth),parseFloat(getComputedStyle(i.$.layout).getPropertyValue(n))<=i.offsetWidth&&(t=r)}),i.$.layout.style.removeProperty(n),t&&(this.__columnCount=t.columns,this.__labelsOnTop=t.labelsPosition==="top")}}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const _r=s=>class extends Fe(s){static get properties(){return{responsiveSteps:{type:Array,value(){return[{minWidth:0,columns:1,labelsPosition:"top"},{minWidth:"20em",columns:1},{minWidth:"40em",columns:2}]},observer:"__responsiveStepsChanged",sync:!0},autoResponsive:{type:Boolean,sync:!0,value:()=>!!(window.Vaadin&&window.Vaadin.featureFlags&&window.Vaadin.featureFlags.defaultAutoResponsiveFormLayout),reflectToAttribute:!0},columnWidth:{type:String,sync:!0},maxColumns:{type:Number,sync:!0,value:10},minColumns:{type:Number,sync:!0,value:1},autoRows:{type:Boolean,sync:!0,value:!1,reflectToAttribute:!0},labelsAside:{type:Boolean,sync:!0,value:!1,reflectToAttribute:!0},expandColumns:{type:Boolean,sync:!0,value:!1,reflectToAttribute:!0},expandFields:{type:Boolean,sync:!0,value:!1,reflectToAttribute:!0}}}static get observers(){return["__autoResponsiveLayoutPropsChanged(columnWidth, maxColumns, minColumns, autoRows, labelsAside, expandColumns, expandFields)","__autoResponsiveChanged(autoResponsive)"]}constructor(){super(),this.__currentLayout,this.__autoResponsiveLayout=new hr(this),this.__responsiveStepsLayout=new ur(this)}connectedCallback(){super.connectedCallback(),this.__currentLayout.connect()}disconnectedCallback(){super.disconnectedCallback(),this.__currentLayout.disconnect()}get slotStyles(){return[`${ar}`.replace("vaadin-form-layout",this.localName)]}_updateLayout(){this.__currentLayout.updateLayout()}__responsiveStepsChanged(i,e){try{this.__responsiveStepsLayout.setProps({responsiveSteps:i})}catch(t){e&&e!==i?(console.warn(`${t.message} Using previously set 'responsiveSteps' instead.`),this.responsiveSteps=e):(console.warn(`${t.message} Using default 'responsiveSteps' instead.`),this.responsiveSteps=[{minWidth:0,columns:1,labelsPosition:"top"},{minWidth:"20em",columns:1},{minWidth:"40em",columns:2}])}}__autoResponsiveLayoutPropsChanged(i,e,t,n,r,o,a){this.__autoResponsiveLayout.setProps({columnWidth:i,maxColumns:e,minColumns:t,autoRows:n,labelsAside:r,expandColumns:o,expandFields:a})}__autoResponsiveChanged(i){this.__currentLayout&&this.__currentLayout.disconnect(),i?this.__currentLayout=this.__autoResponsiveLayout:this.__currentLayout=this.__responsiveStepsLayout,this.__currentLayout.connect()}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class pr extends _r(S(z(x(w)))){static get is(){return"vaadin-form-layout"}static get styles(){return or}render(){return C`
      <div id="layout">
        <slot id="slot"></slot>
      </div>
    `}}y(pr);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const fr=v`
  :host {
    /* By default, when auto-responsive mode is disabled, labels should be displayed beside the fields. */
    --_form-item-labels-above: ' '; /* false */
    --_form-item-labels-aside: initial; /* true */

    align-items: var(--_form-item-labels-aside, baseline);
    display: inline-flex;
    flex-flow: var(--_form-item-labels-above, column) nowrap;
    justify-self: stretch;
  }

  :host([label-position='top']) {
    --_form-item-labels-above: initial; /* true */
    --_form-item-labels-aside: ' '; /* false */
  }

  :host([hidden]) {
    display: none !important;
  }

  [part='label'] {
    color: var(--vaadin-form-item-label-color, var(--vaadin-text-color));
    flex: 0 0 auto;
    font-size: var(--vaadin-form-item-label-font-size, inherit);
    font-weight: var(--vaadin-form-item-label-font-weight, 500);
    line-height: var(--vaadin-form-item-label-line-height, inherit);
    width: var(--_form-item-labels-aside, var(--_label-width, 8em));
    word-break: break-word;
  }

  #spacing {
    flex: 0 0 auto;
    width: var(--_label-spacing, 1em);
  }

  #content {
    flex: 1 1 auto;
    min-width: 0;
  }

  #content ::slotted(.full-width) {
    box-sizing: border-box;
    min-width: 0;
    width: 100%;
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function gr(s){const i=[];for(;s;){if(s.nodeType===Node.DOCUMENT_NODE){i.push(s);break}if(s.nodeType===Node.DOCUMENT_FRAGMENT_NODE){i.push(s),s=s.host;continue}if(s.assignedSlot){s=s.assignedSlot;continue}s=s.parentNode}return i}function ss(s,i){return i?i.closest(s)||ss(s,i.getRootNode().host):null}function qt(s){return s?new Set(s.split(" ")):new Set}function ot(s){return s?[...s].join(" "):""}function at(s,i,e){const t=qt(s.getAttribute(i));t.add(e),s.setAttribute(i,ot(t))}function Ut(s,i,e){const t=qt(s.getAttribute(i));if(t.delete(e),t.size===0){s.removeAttribute(i);return}s.setAttribute(i,ot(t))}function ns(s){return s.nodeType===Node.TEXT_NODE&&s.textContent.trim()===""}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let mr=0;function $e(){return mr++}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const vr=s=>class extends s{constructor(){super(),this.__onFieldInteraction=this.__onFieldInteraction.bind(this),this.__fieldNodeObserver=new MutationObserver(()=>this.__synchronizeAttributes()),this.__labelNode=null,this.__fieldNode=null,this.__isFieldDirty=!1}ready(){super.ready()}_getFieldAriaTarget(i){return i.ariaTarget||i}__linkLabelToField(i){at(this._getFieldAriaTarget(i),"aria-labelledby",this.__labelId)}__unlinkLabelFromField(i){Ut(this._getFieldAriaTarget(i),"aria-labelledby",this.__labelId)}__onLabelClick(){const i=this.__fieldNode;i&&(i.focus({focusVisible:!1}),i.click())}__onLabelSlotChange(){this.__labelNode&&(this.__labelNode=null,this.__fieldNode&&this.__unlinkLabelFromField(this.__fieldNode));const i=this.$.labelSlot.assignedElements()[0];i&&(this.__labelNode=i,this.__labelNode.id?this.__labelId=this.__labelNode.id:(this.__labelId=`label-${this.localName}-${$e()}`,this.__labelNode.id=this.__labelId),this.__fieldNode&&this.__linkLabelToField(this.__fieldNode))}__onContentSlotChange(){this.__fieldNode&&(this.__unlinkLabelFromField(this.__fieldNode),this.__fieldNodeObserver.disconnect(),this.__fieldNode.removeEventListener("blur",this.__onFieldInteraction),this.__fieldNode.removeEventListener("change",this.__onFieldInteraction),this.__fieldNode=null,this.__isFieldDirty=!1);const i=this.$.contentSlot.assignedElements();i.length>1&&Nt(`WARNING: Since Vaadin 23, placing multiple fields directly to a <vaadin-form-item> is deprecated.
Please wrap fields with a <vaadin-custom-field> instead.`);const e=i.find(t=>t.validate||t.checkValidity);e&&(this.__fieldNode=e,this.__fieldNode.addEventListener("blur",this.__onFieldInteraction),this.__fieldNode.addEventListener("change",this.__onFieldInteraction),this.__fieldNodeObserver.observe(this.__fieldNode,{attributes:!0,attributeFilter:["required","invalid"]}),this.__labelNode&&this.__linkLabelToField(this.__fieldNode)),this.__synchronizeAttributes()}__onFieldInteraction(){this.__isFieldDirty=!0,this.__synchronizeAttributes()}__synchronizeAttributes(){const i=this.__fieldNode;if(!i){this.removeAttribute("required"),this.removeAttribute("invalid");return}this.toggleAttribute("required",i.hasAttribute("required")),this.toggleAttribute("invalid",i.hasAttribute("invalid")||i.matches(":invalid")&&this.__isFieldDirty)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class br extends vr(S(x(k(w)))){static get is(){return"vaadin-form-item"}static get styles(){return fr}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return C`
      <div id="label" part="label" @click="${this.__onLabelClick}">
        <slot name="label" id="labelSlot" @slotchange="${this.__onLabelSlotChange}"></slot>
        <span part="required-indicator" aria-hidden="true"></span>
      </div>
      <div id="spacing"></div>
      <div id="content">
        <slot id="contentSlot" @slotchange="${this.__onContentSlotChange}"></slot>
      </div>
    `}}y(br);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const yr=v`
  :host {
    display: contents;
  }

  :host([hidden]) {
    display: none !important;
  }

  ::slotted(*) {
    /* Make form items inherit label position from the layout */
    --_form-item-labels-above: inherit;
    --_form-item-labels-aside: inherit;

    grid-column: auto / span min(var(--_grid-colspan, 1), var(--_grid-rendered-column-count));
  }

  ::slotted(:first-child) {
    grid-column-start: 1;
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Cr extends S(x(w)){static get is(){return"vaadin-form-row"}static get styles(){return yr}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return C`<slot></slot>`}}y(Cr);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const wr=v`
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
 */class xr extends S(N(x(k(w)))){static get is(){return"vaadin-input-container"}static get styles(){return wr}static get properties(){return{disabled:{type:Boolean,reflectToAttribute:!0},readonly:{type:Boolean,reflectToAttribute:!0},invalid:{type:Boolean,reflectToAttribute:!0}}}render(){return C`
      <slot name="prefix"></slot>
      <slot></slot>
      <slot name="suffix"></slot>
    `}ready(){super.ready(),this.addEventListener("pointerdown",i=>{i.target===this&&i.preventDefault()}),this.addEventListener("click",i=>{i.target===this&&this.shadowRoot.querySelector("slot:not([name])").assignedNodes({flatten:!0}).forEach(e=>e.focus&&e.focus())})}}y(xr);/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class te{constructor(i,e){this.slot=i,this.callback=e,this._storedNodes=[],this._connected=!1,this._scheduled=!1,this._boundSchedule=()=>{this._schedule()},this.connect(),this._schedule()}connect(){this.slot.addEventListener("slotchange",this._boundSchedule),this._connected=!0}disconnect(){this.slot.removeEventListener("slotchange",this._boundSchedule),this._connected=!1}_schedule(){this._scheduled||(this._scheduled=!0,queueMicrotask(()=>{this.flush()}))}flush(){this._connected&&(this._scheduled=!1,this._processNodes())}_processNodes(){const i=this.slot.assignedNodes({flatten:!0});let e=[];const t=[],n=[];i.length&&(e=i.filter(r=>!this._storedNodes.includes(r))),this._storedNodes.length&&this._storedNodes.forEach((r,o)=>{const a=i.indexOf(r);a===-1?t.push(r):a!==o&&n.push(r)}),(e.length||t.length||n.length)&&this.callback({addedNodes:e,currentNodes:i,movedNodes:n,removedNodes:t}),this._storedNodes=i}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class he extends EventTarget{static generateId(i,e="default"){return`${e}-${i.localName}-${$e()}`}constructor(i,e,t,n={}){super();const{initializer:r,multiple:o,observe:a,useUniqueId:l,uniqueIdPrefix:d}=n;this.host=i,this.slotName=e,this.tagName=t,this.observe=typeof a=="boolean"?a:!0,this.multiple=typeof o=="boolean"?o:!1,this.slotInitializer=r,o&&(this.nodes=[]),l&&(this.defaultId=this.constructor.generateId(i,d||e))}hostConnected(){this.initialized||(this.multiple?this.initMultiple():this.initSingle(),this.observe&&this.observeSlot(),this.initialized=!0)}initSingle(){let i=this.getSlotChild();i?(this.node=i,this.initAddedNode(i)):(i=this.attachDefaultNode(),this.initNode(i))}initMultiple(){const i=this.getSlotChildren();if(i.length===0){const e=this.attachDefaultNode();e&&(this.nodes=[e],this.initNode(e))}else this.nodes=i,i.forEach(e=>{this.initAddedNode(e)})}attachDefaultNode(){const{host:i,slotName:e,tagName:t}=this;let n=this.defaultNode;return!n&&t&&(n=document.createElement(t),n instanceof Element&&(e!==""&&n.setAttribute("slot",e),this.defaultNode=n)),n&&(this.node=n,i.appendChild(n)),n}getSlotChildren(){const{slotName:i}=this;return Array.from(this.host.childNodes).filter(e=>e.nodeType===Node.ELEMENT_NODE&&e.hasAttribute("data-slot-ignore")?!1:e.nodeType===Node.ELEMENT_NODE&&e.slot===i||e.nodeType===Node.TEXT_NODE&&e.textContent.trim()&&i==="")}getSlotChild(){return this.getSlotChildren()[0]}initNode(i){const{slotInitializer:e}=this;e&&e(i,this.host)}initCustomNode(i){}teardownNode(i){}initAddedNode(i){i!==this.defaultNode&&(this.initCustomNode(i),this.initNode(i))}observeSlot(){const{slotName:i}=this,e=i===""?"slot:not([name])":`slot[name=${i}]`,t=this.host.shadowRoot.querySelector(e);this.__slotObserver=new te(t,({addedNodes:n,removedNodes:r})=>{const o=this.multiple?this.nodes:[this.node],a=n.filter(l=>!ns(l)&&!o.includes(l)&&!(l.nodeType===Node.ELEMENT_NODE&&l.hasAttribute("data-slot-ignore")));r.length&&(this.nodes=o.filter(l=>!r.includes(l)),r.forEach(l=>{this.teardownNode(l)})),a&&a.length>0&&(this.multiple?(this.defaultNode&&this.defaultNode.remove(),this.nodes=[...o,...a].filter(l=>l!==this.defaultNode),a.forEach(l=>{this.initAddedNode(l)})):(this.node&&this.node.remove(),this.node=a[0],this.initAddedNode(this.node)))})}}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Q extends he{constructor(i){super(i,"tooltip"),this.setTarget(i),this.__onContentChange=this.__onContentChange.bind(this)}initCustomNode(i){i.target=this.target,this.ariaTarget!==void 0&&(i.ariaTarget=this.ariaTarget),this.context!==void 0&&(i.context=this.context),this.manual!==void 0&&(i.manual=this.manual),this.opened!==void 0&&(i.opened=this.opened),this.position!==void 0&&(i._position=this.position),this.shouldShow!==void 0&&(i.shouldShow=this.shouldShow),this.manual||this.host.setAttribute("has-tooltip",""),this.__notifyChange(i),i.addEventListener("content-changed",this.__onContentChange)}teardownNode(i){this.manual||this.host.removeAttribute("has-tooltip"),i.removeEventListener("content-changed",this.__onContentChange),this.__notifyChange(null)}setAriaTarget(i){this.ariaTarget=i;const e=this.node;e&&(e.ariaTarget=i)}setContext(i){this.context=i;const e=this.node;e&&(e.context=i)}setManual(i){this.manual=i;const e=this.node;e&&(e.manual=i)}setOpened(i){this.opened=i;const e=this.node;e&&(e.opened=i)}setPosition(i){this.position=i;const e=this.node;e&&(e._position=i)}setShouldShow(i){this.shouldShow=i;const e=this.node;e&&(e.shouldShow=i)}setTarget(i){this.target=i;const e=this.node;e&&(e.target=i)}__onContentChange(i){this.__notifyChange(i.target)}__notifyChange(i){this.dispatchEvent(new CustomEvent("tooltip-changed",{detail:{node:i}}))}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Er=v`
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
 */const De=v`
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
 */const lt=[De,Er];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class dt extends he{constructor(i,e,t={}){const{uniqueIdPrefix:n}=t;super(i,"input","input",{initializer:(r,o)=>{o.value&&(r.value=o.value),o.type&&r.setAttribute("type",o.type),r.id=this.defaultId,typeof e=="function"&&e(r)},useUniqueId:!0,uniqueIdPrefix:n})}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ce=B(s=>class extends s{get _keyboardActive(){return ne()}ready(){this.addEventListener("focusin",e=>{this._shouldSetFocus(e)&&this._setFocused(!0)}),this.addEventListener("focusout",e=>{this._shouldRemoveFocus(e)&&this._setFocused(!1)}),super.ready()}disconnectedCallback(){super.disconnectedCallback(),this.hasAttribute("focused")&&this._setFocused(!1)}focus(e){super.focus(e),e&&e.focusVisible===!1||this.setAttribute("focus-ring","")}_setFocused(e){this.toggleAttribute("focused",e),this.toggleAttribute("focus-ring",e&&this._keyboardActive)}_shouldSetFocus(e){return!0}_shouldRemoveFocus(e){return!0}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const we=B(s=>class extends s{static get properties(){return{disabled:{type:Boolean,value:!1,observer:"_disabledChanged",reflectToAttribute:!0,sync:!0}}}_disabledChanged(e){this._setAriaDisabled(e)}_setAriaDisabled(e){e?this.setAttribute("aria-disabled","true"):this.removeAttribute("aria-disabled")}click(){this.disabled||super.click()}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const jt=s=>class extends we(s){static get properties(){return{tabindex:{type:Number,reflectToAttribute:!0,observer:"_tabindexChanged",sync:!0},_lastTabIndex:{type:Number}}}_disabledChanged(e,t){super._disabledChanged(e,t),!this.__shouldAllowFocusWhenDisabled()&&(e?(this.tabindex!==void 0&&(this._lastTabIndex=this.tabindex),this.setAttribute("tabindex","-1")):t&&(this._lastTabIndex!==void 0?this.setAttribute("tabindex",this._lastTabIndex):this.tabindex=void 0))}_tabindexChanged(e){this.__shouldAllowFocusWhenDisabled()||this.disabled&&e!==-1&&(this._lastTabIndex=e,this.setAttribute("tabindex","-1"))}focus(e){(!this.disabled||this.__shouldAllowFocusWhenDisabled())&&super.focus(e)}__shouldAllowFocusWhenDisabled(){return!1}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ht=B(s=>class extends Ce(jt(s)){static get properties(){return{autofocus:{type:Boolean},focusElement:{type:Object,readOnly:!0,observer:"_focusElementChanged",sync:!0},_lastTabIndex:{value:0}}}constructor(){super(),this._boundOnBlur=this._onBlur.bind(this),this._boundOnFocus=this._onFocus.bind(this)}ready(){super.ready(),this.autofocus&&!this.disabled&&requestAnimationFrame(()=>{this.focus()})}focus(e){this.focusElement&&!this.disabled&&(this.focusElement.focus(),e&&e.focusVisible===!1||this.setAttribute("focus-ring",""))}blur(){this.focusElement&&this.focusElement.blur()}click(){this.focusElement&&!this.disabled&&this.focusElement.click()}_focusElementChanged(e,t){e?(e.disabled=this.disabled,this._addFocusListeners(e),this.__forwardTabIndex(this.tabindex)):t&&this._removeFocusListeners(t)}_addFocusListeners(e){e.addEventListener("blur",this._boundOnBlur),e.addEventListener("focus",this._boundOnFocus)}_removeFocusListeners(e){e.removeEventListener("blur",this._boundOnBlur),e.removeEventListener("focus",this._boundOnFocus)}_onFocus(e){e.stopPropagation(),this.dispatchEvent(new Event("focus"))}_onBlur(e){e.stopPropagation(),this.dispatchEvent(new Event("blur"))}_shouldSetFocus(e){return e.target===this.focusElement}_shouldRemoveFocus(e){return e.target===this.focusElement}_disabledChanged(e,t){super._disabledChanged(e,t),this.focusElement&&(this.focusElement.disabled=e),e&&this.blur()}_tabindexChanged(e){this.__forwardTabIndex(e)}__forwardTabIndex(e){e!==void 0&&this.focusElement&&(this.focusElement.tabIndex=e,e!==-1&&(this.tabindex=void 0)),this.disabled&&e&&(e!==-1&&(this._lastTabIndex=e),this.tabindex=void 0),e===void 0&&this.hasAttribute("tabindex")&&this.removeAttribute("tabindex")}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const xe=B(s=>class extends s{ready(){super.ready(),this.addEventListener("keydown",e=>{this._onKeyDown(e)}),this.addEventListener("keyup",e=>{this._onKeyUp(e)})}_onKeyDown(e){switch(e.key){case"Enter":this._onEnter(e);break;case"Escape":this._onEscape(e);break}}_onKeyUp(e){}_onEnter(e){}_onEscape(e){}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ct=B(s=>class extends s{static get properties(){return{inputElement:{type:Object,readOnly:!0,observer:"_inputElementChanged",sync:!0},type:{type:String,readOnly:!0},value:{type:String,value:"",observer:"_valueChanged",notify:!0,sync:!0}}}constructor(){super(),this._boundOnInput=this._onInput.bind(this),this._boundOnChange=this._onChange.bind(this)}get _hasValue(){return this.value!=null&&this.value!==""}get _inputElementValueProperty(){return"value"}get _inputElementValue(){return this.inputElement?this.inputElement[this._inputElementValueProperty]:void 0}set _inputElementValue(e){this.inputElement&&(this.inputElement[this._inputElementValueProperty]=e)}clear(){this.value="",this._inputElementValue=""}_addInputListeners(e){e.addEventListener("input",this._boundOnInput),e.addEventListener("change",this._boundOnChange)}_removeInputListeners(e){e.removeEventListener("input",this._boundOnInput),e.removeEventListener("change",this._boundOnChange)}_forwardInputValue(e){this.inputElement&&(this._inputElementValue=e??"")}_inputElementChanged(e,t){e?this._addInputListeners(e):t&&this._removeInputListeners(t)}_onInput(e){const t=e.composedPath()[0];this.__userInput=e.isTrusted,this.value=t.value,this.__userInput=!1}_onChange(e){}_toggleHasValue(e){this.toggleAttribute("has-value",e)}_valueChanged(e,t){this._toggleHasValue(this._hasValue),!(e===""&&t===void 0)&&(this.__userInput||this._forwardInputValue(e))}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Sr=s=>class extends ct(xe(s)){static get properties(){return{clearButtonVisible:{type:Boolean,reflectToAttribute:!0,value:!1}}}get clearElement(){return console.warn(`Please implement the 'clearElement' property in <${this.localName}>`),null}ready(){super.ready(),this.clearElement&&(this.clearElement.addEventListener("mousedown",e=>this._onClearButtonMouseDown(e)),this.clearElement.addEventListener("click",e=>this._onClearButtonClick(e)))}_onClearButtonClick(e){e.preventDefault(),this._onClearAction()}_onClearButtonMouseDown(e){this._shouldKeepFocusOnClearMousedown()&&e.preventDefault(),Me||this.inputElement.focus()}_onEscape(e){super._onEscape(e),this.clearButtonVisible&&this.value&&!this.readonly&&(e.stopPropagation(),this._onClearAction())}_onClearAction(){this._inputElementValue="",this.inputElement.dispatchEvent(new Event("input",{bubbles:!0,composed:!0})),this.inputElement.dispatchEvent(new Event("change",{bubbles:!0}))}_shouldKeepFocusOnClearMousedown(){return Wt(this.inputElement)}};/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const wt=new Map;function Gt(s){return wt.has(s)||wt.set(s,new WeakMap),wt.get(s)}function rs(s,i){s&&s.removeAttribute(i)}function os(s,i){if(!s||!i)return;const e=Gt(i);if(e.has(s))return;const t=qt(s.getAttribute(i));e.set(s,new Set(t))}function Ir(s,i){if(!s||!i)return;const e=Gt(i),t=e.get(s);!t||t.size===0?s.removeAttribute(i):at(s,i,ot(t)),e.delete(s)}function Ge(s,i,e={newId:null,oldId:null,fromUser:!1}){if(!s||!i)return;const{newId:t,oldId:n,fromUser:r}=e,o=Gt(i),a=o.get(s);if(!r&&a){n&&a.delete(n),t&&a.add(t);return}r&&(a?t||o.delete(s):os(s,i),rs(s,i)),Ut(s,i,n);const l=t||ot(a);l&&at(s,i,l)}function Ar(s,i){os(s,i),rs(s,i)}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Tr{constructor(i){this.host=i,this.__required=!1}setTarget(i){this.__target=i,this.__setAriaRequiredAttribute(this.__required),this.__setLabelIdToAriaAttribute(this.__labelId,this.__labelId),this.__labelIdFromUser!=null&&this.__setLabelIdToAriaAttribute(this.__labelIdFromUser,this.__labelIdFromUser,!0),this.__setErrorIdToAriaAttribute(this.__errorId),this.__setHelperIdToAriaAttribute(this.__helperId),this.setAriaLabel(this.__label)}setRequired(i){this.__setAriaRequiredAttribute(i),this.__required=i}setAriaLabel(i){this.__setAriaLabelToAttribute(i),this.__label=i}setLabelId(i,e=!1){const t=e?this.__labelIdFromUser:this.__labelId;this.__setLabelIdToAriaAttribute(i,t,e),e?this.__labelIdFromUser=i:this.__labelId=i}setErrorId(i){this.__setErrorIdToAriaAttribute(i,this.__errorId),this.__errorId=i}setHelperId(i){this.__setHelperIdToAriaAttribute(i,this.__helperId),this.__helperId=i}__setAriaLabelToAttribute(i){this.__target&&(i?(Ar(this.__target,"aria-labelledby"),this.__target.setAttribute("aria-label",i)):this.__label&&(Ir(this.__target,"aria-labelledby"),this.__target.removeAttribute("aria-label")))}__setLabelIdToAriaAttribute(i,e,t){Ge(this.__target,"aria-labelledby",{newId:i,oldId:e,fromUser:t})}__setErrorIdToAriaAttribute(i,e){Ge(this.__target,"aria-describedby",{newId:i,oldId:e,fromUser:!1})}__setHelperIdToAriaAttribute(i,e){Ge(this.__target,"aria-describedby",{newId:i,oldId:e,fromUser:!1})}__setAriaRequiredAttribute(i){this.__target&&(["input","textarea"].includes(this.__target.localName)||(i?this.__target.setAttribute("aria-required","true"):this.__target.removeAttribute("aria-required")))}}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const V=document.createElement("div");V.style.position="fixed";V.style.clip="rect(0px, 0px, 0px, 0px)";V.setAttribute("aria-live","polite");document.body.appendChild(V);let Ve;function kr(s,i={}){const e=i.mode||"polite",t=i.timeout===void 0?150:i.timeout;e==="alert"?(V.removeAttribute("aria-live"),V.removeAttribute("role"),Ve=I.debounce(Ve,X,()=>{V.setAttribute("role","alert")})):(Ve&&Ve.cancel(),V.removeAttribute("role"),V.setAttribute("aria-live",e)),V.textContent="",setTimeout(()=>{V.textContent=s},t)}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Kt extends he{constructor(i,e,t,n={}){super(i,e,t,{...n,useUniqueId:!0})}initCustomNode(i){this.__updateNodeId(i),this.__notifyChange(i)}teardownNode(i){const e=this.getSlotChild();e&&e!==this.defaultNode?this.__notifyChange(e):(this.restoreDefaultNode(),this.updateDefaultNode(this.node))}attachDefaultNode(){const i=super.attachDefaultNode();return i&&this.__updateNodeId(i),i}restoreDefaultNode(){}updateDefaultNode(i){this.__notifyChange(i)}observeNode(i){this.__nodeObserver&&this.__nodeObserver.disconnect(),this.__nodeObserver=new MutationObserver(e=>{e.forEach(t=>{const n=t.target,r=n===this.node;t.type==="attributes"?r&&this.__updateNodeId(n):(r||n.parentElement===this.node)&&this.__notifyChange(this.node)})}),this.__nodeObserver.observe(i,{attributes:!0,attributeFilter:["id"],childList:!0,subtree:!0,characterData:!0})}__hasContent(i){return i?i.nodeType===Node.ELEMENT_NODE&&(customElements.get(i.localName)||i.children.length>0)||i.textContent&&i.textContent.trim()!=="":!1}__notifyChange(i){this.dispatchEvent(new CustomEvent("slot-content-changed",{detail:{hasContent:this.__hasContent(i),node:i}}))}__updateNodeId(i){const e=!this.nodes||i===this.nodes[0];i.nodeType===Node.ELEMENT_NODE&&(!this.multiple||e)&&!i.id&&(i.id=this.defaultId)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Rr extends Kt{constructor(i){super(i,"error-message","div")}setErrorMessage(i){this.errorMessage=i,this.updateDefaultNode(this.node)}setInvalid(i){this.invalid=i,this.updateDefaultNode(this.node)}initAddedNode(i){i!==this.defaultNode&&this.initCustomNode(i)}initNode(i){this.updateDefaultNode(i)}initCustomNode(i){i.textContent&&!this.errorMessage&&(this.errorMessage=i.textContent.trim()),super.initCustomNode(i)}restoreDefaultNode(){this.attachDefaultNode()}updateDefaultNode(i){const{errorMessage:e,invalid:t}=this,n=!!(t&&e&&e.trim()!=="");i&&(i.textContent=n?e:"",i.hidden=!n,n&&kr(e,{mode:"assertive"})),super.updateDefaultNode(i)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Or extends Kt{constructor(i){super(i,"helper",null)}setHelperText(i){this.helperText=i,this.getSlotChild()||this.restoreDefaultNode(),this.node===this.defaultNode&&this.updateDefaultNode(this.node)}restoreDefaultNode(){const{helperText:i}=this;if(i&&i.trim()!==""){this.tagName="div";const e=this.attachDefaultNode();this.observeNode(e)}}updateDefaultNode(i){i&&(i.textContent=this.helperText),super.updateDefaultNode(i)}initCustomNode(i){super.initCustomNode(i),this.observeNode(i)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class as extends Kt{constructor(i){super(i,"label","label")}setLabel(i){this.label=i,this.getSlotChild()||this.restoreDefaultNode(),this.node===this.defaultNode&&this.updateDefaultNode(this.node)}restoreDefaultNode(){const{label:i}=this;if(i&&i.trim()!==""){const e=this.attachDefaultNode();this.observeNode(e)}}updateDefaultNode(i){i&&(i.textContent=this.label),super.updateDefaultNode(i)}initCustomNode(i){super.initCustomNode(i),this.observeNode(i)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ls=B(s=>class extends s{static get properties(){return{label:{type:String,observer:"_labelChanged"}}}constructor(){super(),this._labelController=new as(this),this._labelController.addEventListener("slot-content-changed",e=>{this.toggleAttribute("has-label",e.detail.hasContent)})}get _labelId(){const e=this._labelNode;return e&&e.id}get _labelNode(){return this._labelController.node}ready(){super.ready(),this.addController(this._labelController)}_labelChanged(e){this._labelController.setLabel(e)}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ds=B(s=>class extends s{static get properties(){return{invalid:{type:Boolean,reflectToAttribute:!0,notify:!0,value:!1,sync:!0},manualValidation:{type:Boolean,value:!1},required:{type:Boolean,reflectToAttribute:!0,sync:!0}}}validate(){const e=this.checkValidity();return this._setInvalid(!e),this.dispatchEvent(new CustomEvent("validated",{detail:{valid:e}})),e}checkValidity(){return!this.required||!!this.value}_setInvalid(e){this._shouldSetInvalid(e)&&(this.invalid=e)}_shouldSetInvalid(e){return!0}_requestValidation(){this.manualValidation||this.validate()}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ne=s=>class extends ds(ls(s)){static get properties(){return{ariaTarget:{type:Object,observer:"_ariaTargetChanged"},errorMessage:{type:String,observer:"_errorMessageChanged"},helperText:{type:String,observer:"_helperTextChanged"},accessibleName:{type:String,observer:"_accessibleNameChanged"},accessibleNameRef:{type:String,observer:"_accessibleNameRefChanged"}}}static get observers(){return["_invalidChanged(invalid)","_requiredChanged(required)"]}constructor(){super(),this._fieldAriaController=new Tr(this),this._helperController=new Or(this),this._errorController=new Rr(this),this._errorController.addEventListener("slot-content-changed",e=>{this.toggleAttribute("has-error-message",e.detail.hasContent)}),this._labelController.addEventListener("slot-content-changed",e=>{const{hasContent:t,node:n}=e.detail;this.__labelChanged(t,n)}),this._helperController.addEventListener("slot-content-changed",e=>{const{hasContent:t,node:n}=e.detail;this.toggleAttribute("has-helper",t),this.__helperChanged(t,n)})}get _errorNode(){return this._errorController.node}get _helperNode(){return this._helperController.node}ready(){super.ready(),this.addController(this._fieldAriaController),this.addController(this._helperController),this.addController(this._errorController)}__helperChanged(e,t){e?this._fieldAriaController.setHelperId(t.id):this._fieldAriaController.setHelperId(null)}_accessibleNameChanged(e){this._fieldAriaController.setAriaLabel(e)}_accessibleNameRefChanged(e){this._fieldAriaController.setLabelId(e,!0)}__labelChanged(e,t){e?this._fieldAriaController.setLabelId(t.id):this._fieldAriaController.setLabelId(null)}_errorMessageChanged(e){this._errorController.setErrorMessage(e)}_helperTextChanged(e){this._helperController.setHelperText(e)}_ariaTargetChanged(e){e&&this._fieldAriaController.setTarget(e)}_requiredChanged(e){this._fieldAriaController.setRequired(e)}_invalidChanged(e){this._errorController.setInvalid(e),setTimeout(()=>{if(e){const t=this._errorNode;this._fieldAriaController.setErrorId(t&&t.id)}else this._fieldAriaController.setErrorId(null)})}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Yt=B(s=>class extends s{static get properties(){return{stateTarget:{type:Object,observer:"_stateTargetChanged"}}}static get delegateAttrs(){return[]}static get delegateProps(){return[]}ready(){super.ready(),this._createDelegateAttrsObserver(),this._createDelegatePropsObserver()}_stateTargetChanged(e){e&&(this._ensureAttrsDelegated(),this._ensurePropsDelegated())}_createDelegateAttrsObserver(){this._createMethodObserver(`_delegateAttrsChanged(${this.constructor.delegateAttrs.join(", ")})`)}_createDelegatePropsObserver(){this._createMethodObserver(`_delegatePropsChanged(${this.constructor.delegateProps.join(", ")})`)}_ensureAttrsDelegated(){this.constructor.delegateAttrs.forEach(e=>{this._delegateAttribute(e,this[e])})}_ensurePropsDelegated(){this.constructor.delegateProps.forEach(e=>{this._delegateProperty(e,this[e])})}_delegateAttrsChanged(...e){this.constructor.delegateAttrs.forEach((t,n)=>{this._delegateAttribute(t,e[n])})}_delegatePropsChanged(...e){this.constructor.delegateProps.forEach((t,n)=>{this._delegateProperty(t,e[n])})}_delegateAttribute(e,t){this.stateTarget&&(e==="invalid"&&this._delegateAttribute("aria-invalid",t?"true":!1),typeof t=="boolean"?this.stateTarget.toggleAttribute(e,t):t?this.stateTarget.setAttribute(e,t):this.stateTarget.removeAttribute(e))}_delegateProperty(e,t){this.stateTarget&&(this.stateTarget[e]=t)}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Lr=B(s=>class extends Yt(ds(ct(s))){static get constraints(){return["required"]}static get delegateAttrs(){return[...super.delegateAttrs,"required"]}ready(){super.ready(),this._createConstraintsObserver()}checkValidity(){return this.inputElement&&this._hasValidConstraints(this.constructor.constraints.map(e=>this[e]))?this.inputElement.checkValidity():!this.invalid}_hasValidConstraints(e){return e.some(t=>this.__isValidConstraint(t))}_createConstraintsObserver(){this._createMethodObserver(`_constraintsChanged(stateTarget, ${this.constructor.constraints.join(", ")})`)}_constraintsChanged(e,...t){if(!e)return;const n=this._hasValidConstraints(t),r=this.__previousHasConstraints&&!n;(this._hasValue||this.invalid)&&n?this._requestValidation():r&&!this.manualValidation&&this._setInvalid(!1),this.__previousHasConstraints=n}_onChange(e){e.stopPropagation(),this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{detail:{sourceEvent:e},bubbles:e.bubbles,cancelable:e.cancelable}))}__isValidConstraint(e){return!!e||e===0}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Pr=s=>class extends Fe(ht(Lr(Ne(Sr(xe(s)))))){static get properties(){return{allowedCharPattern:{type:String,observer:"_allowedCharPatternChanged"},autoselect:{type:Boolean,value:!1},name:{type:String,reflectToAttribute:!0},placeholder:{type:String,reflectToAttribute:!0},readonly:{type:Boolean,value:!1,reflectToAttribute:!0},title:{type:String,reflectToAttribute:!0}}}static get delegateAttrs(){return[...super.delegateAttrs,"name","type","placeholder","readonly","invalid","title"]}constructor(){super(),this._boundOnPaste=this._onPaste.bind(this),this._boundOnDrop=this._onDrop.bind(this),this._boundOnBeforeInput=this._onBeforeInput.bind(this)}get slotStyles(){const e=this.localName;return[`
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
        `]}_onFocus(e){super._onFocus(e),this.autoselect&&this.inputElement&&this.inputElement.select()}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("paste",this._boundOnPaste),e.addEventListener("drop",this._boundOnDrop),e.addEventListener("beforeinput",this._boundOnBeforeInput)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("paste",this._boundOnPaste),e.removeEventListener("drop",this._boundOnDrop),e.removeEventListener("beforeinput",this._boundOnBeforeInput)}_onKeyDown(e){super._onKeyDown(e),this.allowedCharPattern&&!this.__shouldAcceptKey(e)&&e.target===this.inputElement&&(e.preventDefault(),this._markInputPrevented())}_markInputPrevented(){this.setAttribute("input-prevented",""),this._preventInputDebouncer=I.debounce(this._preventInputDebouncer,H.after(200),()=>{this.removeAttribute("input-prevented")})}__shouldAcceptKey(e){return e.metaKey||e.ctrlKey||!e.key||e.key.length!==1||this.__allowedCharRegExp.test(e.key)}_onPaste(e){if(this.allowedCharPattern){const t=e.clipboardData.getData("text");this.__allowedTextRegExp.test(t)||(e.preventDefault(),this._markInputPrevented())}}_onDrop(e){if(this.allowedCharPattern){const t=e.dataTransfer.getData("text");this.__allowedTextRegExp.test(t)||(e.preventDefault(),this._markInputPrevented())}}_onBeforeInput(e){this.allowedCharPattern&&e.data&&!this.__allowedTextRegExp.test(e.data)&&(e.preventDefault(),this._markInputPrevented())}_allowedCharPatternChanged(e){if(e)try{this.__allowedCharRegExp=new RegExp(`^${e}$`,"u"),this.__allowedTextRegExp=new RegExp(`^${e}*$`,"u")}catch(t){console.error(t)}}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Xt=s=>class extends Pr(s){static get properties(){return{autocomplete:{type:String},autocorrect:{type:String,reflectToAttribute:!0},autocapitalize:{type:String,reflectToAttribute:!0}}}static get delegateAttrs(){return[...super.delegateAttrs,"autocapitalize","autocomplete","autocorrect"]}_inputElementChanged(e){super._inputElementChanged(e),e&&(e.value&&e.value!==this.value&&(console.warn(`Please define value on the <${this.localName}> component!`),e.value=""),this.value&&(e.value=this.value))}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}_onInput(e){super._onInput(e),this.invalid&&this._requestValidation()}_valueChanged(e,t){super._valueChanged(e,t),t!==void 0&&this.invalid&&this._requestValidation()}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Be{constructor(i,e){this.input=i,this.__preventDuplicateLabelClick=this.__preventDuplicateLabelClick.bind(this),e.addEventListener("slot-content-changed",t=>{this.__initLabel(t.detail.node)}),this.__initLabel(e.node)}__initLabel(i){i&&(i.addEventListener("click",this.__preventDuplicateLabelClick),this.input&&i.setAttribute("for",this.input.id))}__preventDuplicateLabelClick(){const i=e=>{e.stopImmediatePropagation(),this.input.removeEventListener("click",i)};this.input.addEventListener("click",i)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const zr=s=>class extends Xt(s){static get properties(){return{maxlength:{type:Number},minlength:{type:Number},pattern:{type:String}}}static get delegateAttrs(){return[...super.delegateAttrs,"maxlength","minlength","pattern"]}static get constraints(){return[...super.constraints,"maxlength","minlength","pattern"]}constructor(){super(),this._setType("text")}get clearElement(){return this.$.clearButton}ready(){super.ready(),this.addController(new dt(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new Be(this.inputElement,this._labelController))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Zt extends zr(S(z(x(k(w))))){static get is(){return"vaadin-text-field"}static get styles(){return[lt]}render(){return C`
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
          theme="${U(this._theme)}"
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
    `}ready(){super.ready(),this._tooltipController=new Q(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}_renderSuffix(){return C`
      <slot name="suffix" slot="suffix"></slot>
      <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
    `}}y(Zt);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const xt={start:"top",end:"bottom"},Et={start:"left",end:"right"},vi=new ResizeObserver(s=>{setTimeout(()=>{s.forEach(i=>{i.target.__overlay&&i.target.__overlay._updatePosition()})})}),Qt=s=>class extends s{static get properties(){return{positionTarget:{type:Object,value:null,sync:!0},horizontalAlign:{type:String,value:"start",sync:!0},verticalAlign:{type:String,value:"top",sync:!0},noHorizontalOverlap:{type:Boolean,value:!1,sync:!0},noVerticalOverlap:{type:Boolean,value:!1,sync:!0},requiredVerticalSpace:{type:Number,value:0,sync:!0}}}constructor(){super(),this.__onScroll=this.__onScroll.bind(this),this._updatePosition=this._updatePosition.bind(this)}connectedCallback(){super.connectedCallback(),this.opened&&this.__addUpdatePositionEventListeners()}disconnectedCallback(){super.disconnectedCallback(),this.__removeUpdatePositionEventListeners()}updated(e){if(super.updated(e),e.has("positionTarget")){const n=e.get("positionTarget");(!this.positionTarget&&n||this.positionTarget&&!n&&this.__margins)&&this.__resetPosition()}(e.has("opened")||e.has("positionTarget"))&&this.__updatePositionSettings(this.opened,this.positionTarget),["horizontalAlign","verticalAlign","noHorizontalOverlap","noVerticalOverlap","requiredVerticalSpace"].some(n=>e.has(n))&&this._updatePosition()}__addUpdatePositionEventListeners(){window.visualViewport.addEventListener("resize",this._updatePosition),window.visualViewport.addEventListener("scroll",this.__onScroll,!0),this.__positionTargetAncestorRootNodes=gr(this.positionTarget),this.__positionTargetAncestorRootNodes.forEach(e=>{e.addEventListener("scroll",this.__onScroll,!0)}),this.positionTarget&&(this.__observePositionTargetMove=Bn(this.positionTarget,()=>{this._updatePosition()}))}__removeUpdatePositionEventListeners(){window.visualViewport.removeEventListener("resize",this._updatePosition),window.visualViewport.removeEventListener("scroll",this.__onScroll,!0),this.__positionTargetAncestorRootNodes&&(this.__positionTargetAncestorRootNodes.forEach(e=>{e.removeEventListener("scroll",this.__onScroll,!0)}),this.__positionTargetAncestorRootNodes=null),this.__observePositionTargetMove&&(this.__observePositionTargetMove(),this.__observePositionTargetMove=null)}__updatePositionSettings(e,t){if(this.__removeUpdatePositionEventListeners(),t&&(t.__overlay=null,vi.unobserve(t),e&&(this.__addUpdatePositionEventListeners(),t.__overlay=this,vi.observe(t))),e){const n=getComputedStyle(this);this.__margins||(this.__margins={},["top","bottom","left","right"].forEach(r=>{this.__margins[r]=parseInt(n[r],10)})),this._updatePosition(),requestAnimationFrame(()=>this._updatePosition())}}__onScroll(e){e.target instanceof Node&&this._deepContains(e.target)||this._updatePosition()}__resetPosition(){this.__margins=null,Object.assign(this.style,{justifyContent:"",alignItems:"",top:"",bottom:"",left:"",right:""}),P(this,"bottom-aligned",!1),P(this,"top-aligned",!1),P(this,"end-aligned",!1),P(this,"start-aligned",!1)}_updatePosition(){if(!this.positionTarget||!this.opened||!this.__margins)return;const e=this.positionTarget.getBoundingClientRect();if(e.width===0&&e.height===0&&this.opened){this.opened=!1;return}const t=this.__shouldAlignStartVertically(e);this.style.justifyContent=t?"flex-start":"flex-end";const n=this.__isRTL,r=this.__shouldAlignStartHorizontally(e,n),o=!n&&r||n&&!r;this.style.alignItems=o?"flex-start":"flex-end";const a=this.getBoundingClientRect(),l=this.__calculatePositionInOneDimension(e,a,this.noVerticalOverlap,xt,this,t),d=this.__calculatePositionInOneDimension(e,a,this.noHorizontalOverlap,Et,this,r);Object.assign(this.style,l,d),P(this,"bottom-aligned",!t),P(this,"top-aligned",t),P(this,"end-aligned",!o),P(this,"start-aligned",o)}__shouldAlignStartHorizontally(e,t){const n=Math.max(this.__oldContentWidth||0,this.$.overlay.offsetWidth);this.__oldContentWidth=this.$.overlay.offsetWidth;const r=Math.min(window.innerWidth,document.documentElement.clientWidth),o=!t&&this.horizontalAlign==="start"||t&&this.horizontalAlign==="end";return this.__shouldAlignStart(e,n,r,this.__margins,o,this.noHorizontalOverlap,Et)}__shouldAlignStartVertically(e){const t=this.requiredVerticalSpace||Math.max(this.__oldContentHeight||0,this.$.overlay.offsetHeight);this.__oldContentHeight=this.$.overlay.offsetHeight;const n=Math.min(window.innerHeight,document.documentElement.clientHeight),r=this.verticalAlign==="top";return this.__shouldAlignStart(e,t,n,this.__margins,r,this.noVerticalOverlap,xt)}__shouldAlignStart(e,t,n,r,o,a,l){const d=n-e[a?l.end:l.start]-r[l.end],_=e[a?l.start:l.end]-r[l.start],f=o?d:_,b=f>(o?_:d)||f>t;return o===b}__adjustBottomProperty(e,t,n){let r;if(e===t.end){if(t.end===xt.end){const o=Math.min(window.innerHeight,document.documentElement.clientHeight);if(n>o&&this.__oldViewportHeight){const a=this.__oldViewportHeight-o;r=n-a}this.__oldViewportHeight=o}if(t.end===Et.end){const o=Math.min(window.innerWidth,document.documentElement.clientWidth);if(n>o&&this.__oldViewportWidth){const a=this.__oldViewportWidth-o;r=n-a}this.__oldViewportWidth=o}}return r}__calculatePositionInOneDimension(e,t,n,r,o,a){const l=a?r.start:r.end,d=a?r.end:r.start,_=parseFloat(o.style[l]||getComputedStyle(o)[l]),f=this.__adjustBottomProperty(l,r,_),g=t[a?r.start:r.end]-e[n===a?r.end:r.start],b=f?`${f}px`:`${_+g*(a?-1:1)}px`;return{[l]:b,[d]:""}}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Mr=s=>class extends Qt(rt(s)){static get properties(){return{position:{type:String,reflectToAttribute:!0}}}_updatePosition(){if(super._updatePosition(),!this.positionTarget||!this.opened)return;this.removeAttribute("arrow-centered");const e=this.positionTarget.getBoundingClientRect(),t=this.$.overlay.getBoundingClientRect(),n=Math.min(window.innerWidth,document.documentElement.clientWidth);let r=!1;if(t.left<0?(this.style.left="0px",this.style.right="",r=!0):t.right>n&&(this.style.right="0px",this.style.left="",r=!0),!r&&(this.position==="bottom"||this.position==="top")){const o=e.width/2-t.width/2;if(this.style.left){const a=t.left+o;a>0&&(this.style.left=`${a}px`,this.setAttribute("arrow-centered",""))}if(this.style.right){const a=parseFloat(this.style.right)+o;a>0&&(this.style.right=`${a}px`,this.setAttribute("arrow-centered",""))}}if(this.position==="start"||this.position==="end"){const o=e.height/2-t.height/2;this.style.top=`${t.top+o}px`}}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Fr=v`
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
 */class $r extends Mr(N(S(x(k(w))))){static get is(){return"vaadin-tooltip-overlay"}static get styles(){return[st,Fr]}render(){return C`
      <div part="overlay" id="overlay">
        <div part="content" id="content"><slot></slot></div>
      </div>
    `}}y($r);/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Dr=s=>class extends s{static get properties(){return{position:{type:String},_position:{type:String,value:"bottom"},__effectivePosition:{type:String,computed:"__computePosition(position, _position)"}}}__computeHorizontalAlign(e){return["top-end","bottom-end","start-top","start","start-bottom"].includes(e)?"end":"start"}__computeNoHorizontalOverlap(e){return["start-top","start","start-bottom","end-top","end","end-bottom"].includes(e)}__computeNoVerticalOverlap(e){return["top-start","top-end","top","bottom-start","bottom","bottom-end"].includes(e)}__computeVerticalAlign(e){return["top-start","top-end","top","start-bottom","end-bottom"].includes(e)?"bottom":"top"}__computePosition(e,t){return e||t}};/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Nr=s=>class extends s{static get properties(){return{for:{type:String,observer:"__forChanged"},target:{type:Object},__isConnected:{type:Boolean,sync:!0}}}static get observers(){return["__targetOrConnectedChanged(target, __isConnected)"]}connectedCallback(){super.connectedCallback(),this.__isConnected=!0}disconnectedCallback(){super.disconnectedCallback(),this.__isConnected=!1}__forChanged(e){e&&(this.__setTargetByIdDebouncer=I.debounce(this.__setTargetByIdDebouncer,W,()=>this.__setTargetById(e)))}__setTargetById(e){if(!this.isConnected)return;const t=this.getRootNode().getElementById(e);t?this.target=t:console.warn(`No element with id="${e}" set via "for" property found on the page.`)}__targetOrConnectedChanged(e,t){this.__previousTarget&&(this.__previousTarget!==e||!t)&&this._removeTargetListeners(this.__previousTarget),e&&t&&this._addTargetListeners(e),this.__previousTarget=e}_addTargetListeners(e){}_removeTargetListeners(e){}},ge=500;let hs=ge,cs=ge,us=ge;const ce=new Set;let Se=!1,ue=null,Ie=null;class Br{constructor(i){this.host=i}get focusDelay(){const i=this.host;return i.focusDelay!=null&&i.focusDelay>=0?i.focusDelay:hs}get hoverDelay(){const i=this.host;return i.hoverDelay!=null&&i.hoverDelay>=0?i.hoverDelay:cs}get hideDelay(){const i=this.host;return i.hideDelay!=null&&i.hideDelay>=0?i.hideDelay:us}get isClosing(){return ce.has(this.host)}open(i={immediate:!1}){const{immediate:e,hover:t,focus:n}=i,r=t&&this.hoverDelay>0,o=n&&this.focusDelay>0;!e&&(r||o)&&!this.__closeTimeout?this.__warmupTooltip(o):this.__showTooltip()}close(i){!i&&this.hideDelay>0?this.__scheduleClose():(this.__abortClose(),this._setOpened(!1)),this.__abortWarmUp(),Se&&(this.__abortCooldown(),this.__scheduleCooldown())}_isOpened(){return this.host.opened}_setOpened(i){this.host.opened=i}__flushClosingTooltips(){ce.forEach(i=>{i._stateController.close(!0),ce.delete(i)})}__showTooltip(){this.__abortClose(),this.__flushClosingTooltips(),this._setOpened(!0),Se=!0,this.__abortWarmUp(),this.__abortCooldown()}__warmupTooltip(i){this._isOpened()||(Se?this.__showTooltip():ue==null&&this.__scheduleWarmUp(i))}__abortClose(){this.__closeTimeout&&(clearTimeout(this.__closeTimeout),this.__closeTimeout=null),this.isClosing&&ce.delete(this.host)}__abortCooldown(){Ie&&(clearTimeout(Ie),Ie=null)}__abortWarmUp(){ue&&(clearTimeout(ue),ue=null)}__scheduleClose(){this._isOpened()&&!this.isClosing&&(ce.add(this.host),this.__closeTimeout=setTimeout(()=>{ce.delete(this.host),this.__closeTimeout=null,this._setOpened(!1)},this.hideDelay))}__scheduleCooldown(){Ie=setTimeout(()=>{Ie=null,Se=!1},this.hideDelay)}__scheduleWarmUp(i){const e=i?this.focusDelay:this.hoverDelay;ue=setTimeout(()=>{ue=null,Se=!0,this.__showTooltip()},e)}}const Vr=s=>class extends Dr(Nr(s)){static get properties(){return{ariaTarget:{type:Object},context:{type:Object,value:()=>({})},focusDelay:{type:Number},generator:{type:Object},hideDelay:{type:Number},hoverDelay:{type:Number},manual:{type:Boolean,value:!1,sync:!0},opened:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"__openedChanged",sync:!0},shouldShow:{type:Object,value:()=>(e,t)=>!0},text:{type:String},markdown:{type:Boolean,value:!1,reflectToAttribute:!0},_effectiveAriaTarget:{type:Object,computed:"__computeAriaTarget(ariaTarget, target)",observer:"__effectiveAriaTargetChanged"},__isTargetHidden:{type:Boolean,value:!1},_isConnected:{type:Boolean,sync:!0}}}static setDefaultFocusDelay(e){hs=e!=null&&e>=0?e:ge}static setDefaultHideDelay(e){us=e!=null&&e>=0?e:ge}static setDefaultHoverDelay(e){cs=e!=null&&e>=0?e:ge}constructor(){super(),this._uniqueId=`vaadin-tooltip-${$e()}`,this.__onFocusin=this.__onFocusin.bind(this),this.__onFocusout=this.__onFocusout.bind(this),this.__onMouseDown=this.__onMouseDown.bind(this),this.__onMouseEnter=this.__onMouseEnter.bind(this),this.__onMouseLeave=this.__onMouseLeave.bind(this),this.__onKeyDown=this.__onKeyDown.bind(this),this.__onOverlayOpen=this.__onOverlayOpen.bind(this),this.__targetVisibilityObserver=new IntersectionObserver(e=>{e.forEach(t=>this.__onTargetVisibilityChange(t.isIntersecting))},{threshold:0}),this._stateController=new Br(this)}connectedCallback(){super.connectedCallback(),this._isConnected=!0,document.body.addEventListener("vaadin-overlay-open",this.__onOverlayOpen)}disconnectedCallback(){super.disconnectedCallback(),this.opened&&!this.manual&&this._stateController.close(!0),this._isConnected=!1,document.body.removeEventListener("vaadin-overlay-open",this.__onOverlayOpen)}ready(){super.ready(),this._overlayElement=this.$.overlay,this.__contentController=new he(this,"overlay","div",{initializer:e=>{e.id=this._uniqueId,e.setAttribute("role","tooltip"),this.__contentNode=e}}),this.addController(this.__contentController)}updated(e){super.updated(e),(e.has("text")||e.has("generator")||e.has("context")||e.has("markdown"))&&this.__updateContent()}__openedChanged(e,t){e?document.addEventListener("keydown",this.__onKeyDown,!0):t&&document.removeEventListener("keydown",this.__onKeyDown,!0)}_addTargetListeners(e){e.addEventListener("mouseenter",this.__onMouseEnter),e.addEventListener("mouseleave",this.__onMouseLeave),e.addEventListener("focusin",this.__onFocusin),e.addEventListener("focusout",this.__onFocusout),e.addEventListener("mousedown",this.__onMouseDown),requestAnimationFrame(()=>{this.__targetVisibilityObserver.observe(e)})}_removeTargetListeners(e){e.removeEventListener("mouseenter",this.__onMouseEnter),e.removeEventListener("mouseleave",this.__onMouseLeave),e.removeEventListener("focusin",this.__onFocusin),e.removeEventListener("focusout",this.__onFocusout),e.removeEventListener("mousedown",this.__onMouseDown),this.__targetVisibilityObserver.unobserve(e)}__onFocusin(e){this.manual||ne()&&(this.target.contains(e.relatedTarget)||this.__isShouldShow()&&(this._overlayElement.hasAttribute("hidden")||(this.__focusInside=!0,!this.__isTargetHidden&&(!this.__hoverInside||!this.opened)&&this._stateController.open({focus:!0}))))}__onFocusout(e){this.manual||this.target.contains(e.relatedTarget)||(this.__focusInside=!1,this.__hoverInside||this._stateController.close(!0))}__onKeyDown(e){this.manual||e.key==="Escape"&&(e.stopPropagation(),this._stateController.close(!0))}__onMouseDown(){this.manual||this._stateController.close(!0)}__onMouseEnter(){this.manual||this.__isShouldShow()&&(this._overlayElement.hasAttribute("hidden")||this.__hoverInside||(this.__hoverInside=!0,!this.__isTargetHidden&&(!this.__focusInside||!this.opened)&&this._stateController.open({hover:!0})))}__onMouseLeave(e){e.relatedTarget!==this._overlayElement&&this.__handleMouseLeave()}__onOverlayMouseEnter(){this.manual||this._stateController.isClosing&&this._stateController.open({immediate:!0})}__onOverlayMouseLeave(e){e.relatedTarget!==this.target&&this.__handleMouseLeave()}__onOverlayMouseDown(e){e.stopPropagation()}__onOverlayClick(e){e.stopPropagation()}__handleMouseLeave(){this.manual||(this.__hoverInside=!1,this.__focusInside||this._stateController.close())}__onOverlayOpen(){this.manual||this._overlayElement.opened&&!this._overlayElement._last&&this._stateController.close(!0)}__onTargetVisibilityChange(e){if(this.manual)return;const t=this.__isTargetHidden;if(this.__isTargetHidden=!e,t&&e&&(this.__focusInside||this.__hoverInside)){this._stateController.open({immediate:!0});return}!e&&this.opened&&this._stateController.close(!0)}__isShouldShow(){return!(typeof this.shouldShow=="function"&&this.shouldShow(this.target,this.context)!==!0)}async __updateContent(){const e=typeof this.generator=="function"?this.generator(this.context):this.text;this.markdown&&e?(await this.constructor.__importMarkdownHelpers()).renderMarkdownToElement(this.__contentNode,e):this.__contentNode.textContent=e||"",this.$.overlay.toggleAttribute("hidden",this.__contentNode.textContent.trim()===""),this.dispatchEvent(new CustomEvent("content-changed",{detail:{content:this.__contentNode.textContent}}))}__computeAriaTarget(e,t){const n=o=>o&&o.nodeType===Node.ELEMENT_NODE,r=Array.isArray(e)?e.some(n):e;return e===null||r?e:t}__effectiveAriaTargetChanged(e,t){t&&[t].flat().forEach(n=>{Ut(n,"aria-describedby",this._uniqueId)}),e&&[e].flat().forEach(n=>{at(n,"aria-describedby",this._uniqueId)})}static __importMarkdownHelpers(){return this.__markdownHelpers||(this.__markdownHelpers=Hs(()=>import("./markdown-helpers-RM02npbm.js"),[],import.meta.url)),this.__markdownHelpers}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Hr extends Vr(ze(z(x(w)))){static get is(){return"vaadin-tooltip"}static get styles(){return v`
      :host {
        display: contents;
      }
    `}render(){const i=this.__effectivePosition;return C`
      <vaadin-tooltip-overlay
        id="overlay"
        .owner="${this}"
        theme="${U(this._theme)}"
        .opened="${this._isConnected&&this.opened}"
        .positionTarget="${this.target}"
        .position="${i}"
        ?no-horizontal-overlap="${this.__computeNoHorizontalOverlap(i)}"
        ?no-vertical-overlap="${this.__computeNoVerticalOverlap(i)}"
        .horizontalAlign="${this.__computeHorizontalAlign(i)}"
        .verticalAlign="${this.__computeVerticalAlign(i)}"
        @click="${this.__onOverlayClick}"
        @mousedown="${this.__onOverlayMouseDown}"
        @mouseenter="${this.__onOverlayMouseEnter}"
        @mouseleave="${this.__onOverlayMouseLeave}"
        modeless
        ?markdown="${this.markdown}"
        exportparts="overlay, content"
        ><slot name="overlay"></slot
      ></vaadin-tooltip-overlay>
    `}}y(Hr);/**
@license
Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/const Wr=s=>s,_s=typeof document.head.style.touchAction=="string",Je="__polymerGestures",St="__polymerGesturesHandled",Mt="__polymerGesturesTouchAction",bi=25,yi=5,qr=2,Ur=["mousedown","mousemove","mouseup","click"],jr=[0,1,4,2],Gr=(function(){try{return new MouseEvent("test",{buttons:1}).buttons===1}catch{return!1}})();function Jt(s){return Ur.indexOf(s)>-1}let Kr=!1;(function(){try{const s=Object.defineProperty({},"passive",{get(){Kr=!0}});window.addEventListener("test",null,s),window.removeEventListener("test",null,s)}catch{}})();function ps(s){Jt(s)}const Yr=navigator.userAgent.match(/iP(?:[oa]d|hone)|Android/u),Xr={button:!0,command:!0,fieldset:!0,input:!0,keygen:!0,optgroup:!0,option:!0,select:!0,textarea:!0};function le(s){const i=s.type;if(!Jt(i))return!1;if(i==="mousemove"){let t=s.buttons===void 0?1:s.buttons;return s instanceof window.MouseEvent&&!Gr&&(t=jr[s.which]||0),!!(t&1)}return(s.button===void 0?0:s.button)===0}function Zr(s){if(s.type==="click"){if(s.detail===0)return!0;const i=ie(s);if(!i.nodeType||i.nodeType!==Node.ELEMENT_NODE)return!0;const e=i.getBoundingClientRect(),t=s.pageX,n=s.pageY;return!(t>=e.left&&t<=e.right&&n>=e.top&&n<=e.bottom)}return!1}const Y={touch:{x:0,y:0,id:-1,scrollDecided:!1}};function Qr(s){let i="auto";const e=gs(s);for(let t=0,n;t<e.length;t++)if(n=e[t],n[Mt]){i=n[Mt];break}return i}function fs(s,i,e){s.movefn=i,s.upfn=e,document.addEventListener("mousemove",i),document.addEventListener("mouseup",e)}function me(s){document.removeEventListener("mousemove",s.movefn),document.removeEventListener("mouseup",s.upfn),s.movefn=null,s.upfn=null}const gs=window.ShadyDOM&&window.ShadyDOM.noPatch?window.ShadyDOM.composedPath:s=>s.composedPath&&s.composedPath()||[],Z={},ae=[];function ms(s,i){let e=document.elementFromPoint(s,i),t=e;for(;t&&t.shadowRoot&&!window.ShadyDOM;){const n=t;if(t=t.shadowRoot.elementFromPoint(s,i),n===t)break;t&&(e=t)}return e}function ie(s){const i=gs(s);return i.length>0?i[0]:s.target}function vs(s){const i=s.type,t=s.currentTarget[Je];if(!t)return;const n=t[i];if(!n)return;if(!s[St]&&(s[St]={},i.startsWith("touch"))){const o=s.changedTouches[0];if(i==="touchstart"&&s.touches.length===1&&(Y.touch.id=o.identifier),Y.touch.id!==o.identifier)return;_s||(i==="touchstart"||i==="touchmove")&&Jr(s)}const r=s[St];if(!r.skip){for(let o=0,a;o<ae.length;o++)a=ae[o],n[a.name]&&!r[a.name]&&a.flow&&a.flow.start.indexOf(s.type)>-1&&a.reset&&a.reset();for(let o=0,a;o<ae.length;o++)a=ae[o],n[a.name]&&!r[a.name]&&(r[a.name]=!0,a[i](s))}}function Jr(s){const i=s.changedTouches[0],e=s.type;if(e==="touchstart")Y.touch.x=i.clientX,Y.touch.y=i.clientY,Y.touch.scrollDecided=!1;else if(e==="touchmove"){if(Y.touch.scrollDecided)return;Y.touch.scrollDecided=!0;const t=Qr(s);let n=!1;const r=Math.abs(Y.touch.x-i.clientX),o=Math.abs(Y.touch.y-i.clientY);s.cancelable&&(t==="none"?n=!0:t==="pan-x"?n=o>r:t==="pan-y"&&(n=r>o)),n?s.preventDefault():be("track")}}function de(s,i,e){return Z[i]?(eo(s,i,e),!0):!1}function bs(s,i,e){return Z[i]?(to(s,i,e),!0):!1}function eo(s,i,e){const t=Z[i],n=t.deps,r=t.name;let o=s[Je];o||(s[Je]=o={});for(let a=0,l,d;a<n.length;a++)l=n[a],!(Yr&&Jt(l)&&l!=="click")&&(d=o[l],d||(o[l]=d={_count:0}),d._count===0&&s.addEventListener(l,vs,ps(l)),d[r]=(d[r]||0)+1,d._count=(d._count||0)+1);s.addEventListener(i,e),t.touchAction&&so(s,t.touchAction)}function to(s,i,e){const t=Z[i],n=t.deps,r=t.name,o=s[Je];if(o)for(let a=0,l,d;a<n.length;a++)l=n[a],d=o[l],d&&d[r]&&(d[r]=(d[r]||1)-1,d._count=(d._count||1)-1,d._count===0&&s.removeEventListener(l,vs,ps(l)));s.removeEventListener(i,e)}function ut(s){ae.push(s),s.emits.forEach(i=>{Z[i]=s})}function io(s){for(let i=0,e;i<ae.length;i++){e=ae[i];for(let t=0,n;t<e.emits.length;t++)if(n=e.emits[t],n===s)return e}return null}function so(s,i){_s&&s instanceof HTMLElement&&W.run(()=>{s.style.touchAction=i}),s[Mt]=i}function ei(s,i,e){const t=new Event(i,{bubbles:!0,cancelable:!0,composed:!0});if(t.detail=e,Wr(s).dispatchEvent(t),t.defaultPrevented){const n=e.preventer||e.sourceEvent;n&&n.preventDefault&&n.preventDefault()}}function be(s){const i=io(s);i.info&&(i.info.prevent=!0)}ut({name:"downup",deps:["mousedown","touchstart","touchend"],flow:{start:["mousedown","touchstart"],end:["mouseup","touchend"]},emits:["down","up"],info:{movefn:null,upfn:null},reset(){me(this.info)},mousedown(s){if(!le(s))return;const i=ie(s),e=this,t=r=>{le(r)||(Ae("up",i,r),me(e.info))},n=r=>{le(r)&&Ae("up",i,r),me(e.info)};fs(this.info,t,n),Ae("down",i,s)},touchstart(s){Ae("down",ie(s),s.changedTouches[0],s)},touchend(s){Ae("up",ie(s),s.changedTouches[0],s)}});function Ae(s,i,e,t){i&&ei(i,s,{x:e.clientX,y:e.clientY,sourceEvent:e,preventer:t,prevent(n){return be(n)}})}ut({name:"track",touchAction:"none",deps:["mousedown","touchstart","touchmove","touchend"],flow:{start:["mousedown","touchstart"],end:["mouseup","touchend"]},emits:["track"],info:{x:0,y:0,state:"start",started:!1,moves:[],addMove(s){this.moves.length>qr&&this.moves.shift(),this.moves.push(s)},movefn:null,upfn:null,prevent:!1},reset(){this.info.state="start",this.info.started=!1,this.info.moves=[],this.info.x=0,this.info.y=0,this.info.prevent=!1,me(this.info)},mousedown(s){if(!le(s))return;const i=ie(s),e=this,t=r=>{const o=r.clientX,a=r.clientY;Ci(e.info,o,a)&&(e.info.state=e.info.started?r.type==="mouseup"?"end":"track":"start",e.info.state==="start"&&be("tap"),e.info.addMove({x:o,y:a}),le(r)||(e.info.state="end",me(e.info)),i&&It(e.info,i,r),e.info.started=!0)},n=r=>{e.info.started&&t(r),me(e.info)};fs(this.info,t,n),this.info.x=s.clientX,this.info.y=s.clientY},touchstart(s){const i=s.changedTouches[0];this.info.x=i.clientX,this.info.y=i.clientY},touchmove(s){const i=ie(s),e=s.changedTouches[0],t=e.clientX,n=e.clientY;Ci(this.info,t,n)&&(this.info.state==="start"&&be("tap"),this.info.addMove({x:t,y:n}),It(this.info,i,e),this.info.state="track",this.info.started=!0)},touchend(s){const i=ie(s),e=s.changedTouches[0];this.info.started&&(this.info.state="end",this.info.addMove({x:e.clientX,y:e.clientY}),It(this.info,i,e))}});function Ci(s,i,e){if(s.prevent)return!1;if(s.started)return!0;const t=Math.abs(s.x-i),n=Math.abs(s.y-e);return t>=yi||n>=yi}function It(s,i,e){if(!i)return;const t=s.moves[s.moves.length-2],n=s.moves[s.moves.length-1],r=n.x-s.x,o=n.y-s.y;let a,l=0;t&&(a=n.x-t.x,l=n.y-t.y),ei(i,"track",{state:s.state,x:e.clientX,y:e.clientY,dx:r,dy:o,ddx:a,ddy:l,sourceEvent:e,hover(){return ms(e.clientX,e.clientY)}})}ut({name:"tap",deps:["mousedown","click","touchstart","touchend"],flow:{start:["mousedown","touchstart"],end:["click","touchend"]},emits:["tap"],info:{x:NaN,y:NaN,prevent:!1},reset(){this.info.x=NaN,this.info.y=NaN,this.info.prevent=!1},mousedown(s){le(s)&&(this.info.x=s.clientX,this.info.y=s.clientY)},click(s){le(s)&&wi(this.info,s)},touchstart(s){const i=s.changedTouches[0];this.info.x=i.clientX,this.info.y=i.clientY},touchend(s){wi(this.info,s.changedTouches[0],s)}});function wi(s,i,e){const t=Math.abs(i.clientX-s.x),n=Math.abs(i.clientY-s.y),r=ie(e||i);!r||Xr[r.localName]&&r.hasAttribute("disabled")||(isNaN(t)||isNaN(n)||t<=bi&&n<=bi||Zr(i))&&(s.prevent||ei(r,"tap",{x:i.clientX,y:i.clientY,sourceEvent:i,preventer:e}))}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const _t=s=>class extends we(xe(s)){get _activeKeys(){return[" "]}ready(){super.ready(),de(this,"down",e=>{this._shouldSetActive(e)&&this._setActive(!0)}),de(this,"up",()=>{this._setActive(!1)})}disconnectedCallback(){super.disconnectedCallback(),this._setActive(!1)}_shouldSetActive(e){return!this.disabled}_onKeyDown(e){super._onKeyDown(e),this._shouldSetActive(e)&&this._activeKeys.includes(e.key)&&(this._setActive(!0),document.addEventListener("keyup",t=>{this._activeKeys.includes(t.key)&&this._setActive(!1)},{once:!0}))}_setActive(e){this.toggleAttribute("active",e)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const no=["mousedown","mouseup","click","dblclick","keypress","keydown","keyup"],ti=s=>class extends _t(jt(Ce(s))){constructor(){super(),this.__onInteractionEvent=this.__onInteractionEvent.bind(this),no.forEach(e=>{this.addEventListener(e,this.__onInteractionEvent,!0)}),this.tabindex=0}get _activeKeys(){return["Enter"," "]}ready(){super.ready(),this.hasAttribute("role")||this.setAttribute("role","button"),this.__shouldAllowFocusWhenDisabled()&&this.style.setProperty("--_vaadin-button-disabled-pointer-events","auto")}_onKeyDown(e){super._onKeyDown(e),!(e.altKey||e.shiftKey||e.ctrlKey||e.metaKey)&&this._activeKeys.includes(e.key)&&(e.preventDefault(),this.click())}__onInteractionEvent(e){this.__shouldSuppressInteractionEvent(e)&&e.stopImmediatePropagation()}__shouldSuppressInteractionEvent(e){return this.disabled}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ys=v`
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
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ro=v`
  :host {
    --vaadin-button-background: transparent;
    --vaadin-button-padding: 0;
    color: var(--vaadin-input-field-button-text-color, inherit);
    display: block;
    border: none;
    cursor: var(--vaadin-clickable-cursor);
  }

  :host::before {
    background: currentColor;
    content: '';
    display: block;
    height: var(--vaadin-icon-size, 1lh);
    mask: var(--_vaadin-icon-eye) 50% / var(--vaadin-icon-visual-size, 100%) no-repeat;
    width: var(--vaadin-icon-size, 1lh);
  }

  :host([aria-pressed='true'])::before {
    mask-image: var(--_vaadin-icon-eye-slash);
  }

  @media (forced-colors: active) {
    :host::before {
      background: CanvasText;
    }

    :host([disabled])::before {
      background: GrayText;
    }
  }
`,oo=[ys,ro];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ao extends ti(N(S(x(k(w))))){static get is(){return"vaadin-password-field-button"}static get styles(){return oo}render(){return C``}}y(ao);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const lo=v`
  [part~='reveal-button']::before {
    display: none;
  }

  [part='input-field']:has([part~='reveal-button']:focus-within) {
    outline: none;
    --vaadin-input-field-border-color: inherit;
  }

  :host([readonly]) [part~='reveal-button'] {
    color: var(--vaadin-input-field-button-text-color, var(--vaadin-text-color-secondary));
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ho=s=>class extends Fe(we(Ce(ct(s)))){static get properties(){return{revealButtonHidden:{type:Boolean,value:!1},passwordVisible:{type:Boolean,value:!1,reflectToAttribute:!0,readOnly:!0},i18n:{type:Object,value:()=>({reveal:"Show password"})}}}static get delegateAttrs(){return super.delegateAttrs.filter(e=>e!=="autocapitalize")}constructor(){super(),this._setType("password"),this.__boundRevealButtonClick=this._onRevealButtonClick.bind(this),this.__boundRevealButtonMouseDown=this._onRevealButtonMouseDown.bind(this),this.__lastChange=""}get slotStyles(){const e=this.localName;return[...super.slotStyles,`
          ${e} [slot="input"]::-ms-reveal {
            display: none;
          }
        `]}ready(){super.ready(),this._revealPart=this.shadowRoot.querySelector('[part~="reveal-button"]'),this._revealButtonController=new he(this,"reveal","vaadin-password-field-button",{initializer:e=>{this._revealNode=e,e.addEventListener("click",this.__boundRevealButtonClick),e.addEventListener("mousedown",this.__boundRevealButtonMouseDown)}}),this.addController(this._revealButtonController),this.inputElement&&(this.inputElement.autocapitalize="off")}updated(e){super.updated(e),e.has("disabled")&&(this._revealNode.disabled=this.disabled),e.has("revealButtonHidden")&&this._toggleRevealHidden(this.revealButtonHidden),e.has("passwordVisible")&&(this._setType(this.passwordVisible?"text":"password"),this._revealNode.setAttribute("aria-pressed",this.passwordVisible?"true":"false")),e.has("i18n")&&this.i18n&&this.i18n.reveal&&this._revealNode.setAttribute("aria-label",this.i18n.reveal)}_onChange(e){super._onChange(e),this.__lastChange=this.inputElement.value}_shouldSetFocus(e){return e.target===this.inputElement||e.target===this._revealNode}_shouldRemoveFocus(e){return!(e.relatedTarget===this._revealNode||e.relatedTarget===this.inputElement&&e.target===this._revealNode)}_setFocused(e){if(super._setFocused(e),!e)this._setPasswordVisible(!1),this.__lastChange!==this.inputElement.value&&(this.__lastChange=this.inputElement.value,this.dispatchEvent(new CustomEvent("change",{bubbles:!0})));else{const t=this.getRootNode().activeElement===this._revealNode;this.toggleAttribute("focus-ring",this._keyboardActive&&!t)}}_onRevealButtonClick(){this._setPasswordVisible(!this.passwordVisible)}_onRevealButtonMouseDown(e){e.preventDefault(),this.inputElement.focus()}_toggleRevealHidden(e){this._revealNode&&(e?(this._revealPart.setAttribute("hidden",""),this._revealNode.setAttribute("tabindex","-1"),this._revealNode.setAttribute("aria-hidden","true")):(this._revealPart.removeAttribute("hidden"),this._revealNode.setAttribute("tabindex","0"),this._revealNode.removeAttribute("aria-hidden")))}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class co extends ho(Zt){static get is(){return"vaadin-password-field"}static get styles(){return[...super.styles,lo]}_renderSuffix(){return C`
      ${super._renderSuffix()}
      <div part="field-button reveal-button" slot="suffix">
        <slot name="reveal"></slot>
      </div>
    `}}y(co);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const uo=v`
  :host([dir='rtl']) [part='input-field'] {
    direction: ltr;
  }

  :host([dir='rtl']) [part='input-field'] ::slotted(input)::placeholder {
    direction: rtl;
    text-align: left;
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class _o extends Zt{static get is(){return"vaadin-email-field"}static get styles(){return[...super.styles,uo]}static get delegateAttrs(){return super.delegateAttrs.filter(i=>i!=="autocapitalize")}constructor(){super(),this._setType("email"),this.pattern="^[a-zA-Z0-9_\\-+]+(?:\\.[a-zA-Z0-9_\\-+]+)*@[a-zA-Z0-9\\-.]+\\.[a-zA-Z0-9\\-]{2,}$"}ready(){super.ready(),this.inputElement&&(this.inputElement.autocapitalize="off")}}y(_o);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const po=v`
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
 */const He=new ResizeObserver(s=>{setTimeout(()=>{s.forEach(i=>{i.target.isConnected&&(i.target.resizables?i.target.resizables.forEach(e=>{e._onResize(i.contentRect)}):i.target._onResize(i.contentRect))})})}),fo=B(s=>class extends s{get _observeParent(){return!1}connectedCallback(){if(super.connectedCallback(),He.observe(this),this._observeParent){const e=this.parentNode instanceof ShadowRoot?this.parentNode.host:this.parentNode;e.resizables||(e.resizables=new Set,He.observe(e)),e.resizables.add(this),this.__parent=e}}disconnectedCallback(){super.disconnectedCallback(),He.unobserve(this);const e=this.__parent;if(this._observeParent&&e){const t=e.resizables;t&&(t.delete(this),t.size===0&&He.unobserve(e)),this.__parent=null}}_onResize(e){}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class go extends he{constructor(i,e){super(i,"textarea","textarea",{initializer:(t,n)=>{const r=n.getAttribute("value");r&&(t.value=r);const o=n.getAttribute("name");o&&t.setAttribute("name",o),t.id=this.defaultId,typeof e=="function"&&e(t)},useUniqueId:!0})}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const mo=s=>class extends fo(Xt(s)){static get properties(){return{maxlength:{type:Number},minlength:{type:Number},pattern:{type:String},minRows:{type:Number,value:2,observer:"__minRowsChanged"},maxRows:{type:Number}}}static get delegateAttrs(){return[...super.delegateAttrs,"maxlength","minlength","pattern"]}static get constraints(){return[...super.constraints,"maxlength","minlength","pattern"]}static get observers(){return["__updateMinHeight(minRows, inputElement)","__updateMaxHeight(maxRows, inputElement, _inputField)"]}get clearElement(){return this.$.clearButton}_onResize(){this._updateHeight(),this.__scrollPositionUpdated()}_onScroll(){this.__scrollPositionUpdated()}ready(){super.ready(),this.__textAreaController=new go(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e}),this.addController(this.__textAreaController),this.addController(new Be(this.inputElement,this._labelController)),this._inputField=this.shadowRoot.querySelector("[part=input-field]"),this._inputField.addEventListener("wheel",e=>{const t=this._inputField.scrollTop;this._inputField.scrollTop+=e.deltaY,t!==this._inputField.scrollTop&&(e.preventDefault(),this.__scrollPositionUpdated())}),this._updateHeight(),this.__scrollPositionUpdated()}__scrollPositionUpdated(){this._inputField.style.setProperty("--_text-area-vertical-scroll-position","0px"),this._inputField.style.setProperty("--_text-area-vertical-scroll-position",`${this._inputField.scrollTop}px`)}_valueChanged(e,t){super._valueChanged(e,t),this._updateHeight()}_updateHeight(){const e=this.inputElement,t=this._inputField;if(!e||!t)return;const n=t.scrollTop,r=this.value?this.value.length:0;if(this._oldValueLength>=r){const a=getComputedStyle(t).height,l=getComputedStyle(e).width;t.style.height=a,e.style.maxWidth=l,e.style.alignSelf="flex-start",e.style.height="auto"}this._oldValueLength=r;const o=e.scrollHeight;o>e.clientHeight&&(e.style.height=`${o}px`),e.style.removeProperty("max-width"),e.style.removeProperty("align-self"),t.style.removeProperty("height"),t.scrollTop=n,this.__updateMaxHeight(this.maxRows)}__updateMinHeight(e){this.inputElement&&this.inputElement===this.__textAreaController.defaultNode&&(this.inputElement.rows=Math.max(e,1))}__updateMaxHeight(e){if(!(!this._inputField||!this.inputElement))if(e){const t=getComputedStyle(this.inputElement),n=getComputedStyle(this._inputField),o=parseFloat(t.lineHeight)*e,a=parseFloat(t.paddingTop)+parseFloat(t.paddingBottom)+parseFloat(t.marginTop)+parseFloat(t.marginBottom)+parseFloat(n.borderTopWidth)+parseFloat(n.borderBottomWidth)+parseFloat(n.paddingTop)+parseFloat(n.paddingBottom),l=Math.ceil(o+a);this._inputField.style.setProperty("max-height",`${l}px`)}else this._inputField.style.removeProperty("max-height")}__minRowsChanged(e){e<1&&console.warn("<vaadin-text-area> minRows must be at least 1.")}scrollToStart(){this._inputField.scrollTop=0}scrollToEnd(){this._inputField.scrollTop=this._inputField.scrollHeight}checkValidity(){if(!super.checkValidity())return!1;if(!this.pattern||!this.inputElement.value)return!0;try{const e=this.inputElement.value.match(this.pattern);return e?e[0]===e.input:!1}catch{return!0}}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class vo extends mo(S(z(x(k(w))))){static get is(){return"vaadin-text-area"}static get styles(){return[lt,po]}render(){return C`
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
          theme="${U(this._theme)}"
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
    `}ready(){super.ready(),this._tooltipController=new Q(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}}y(vo);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const bo=v`
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
 */const xi="NaN",yo=s=>class extends Xt(s){static get properties(){return{min:{type:Number},max:{type:Number},step:{type:Number},stepButtonsVisible:{type:Boolean,value:!1,reflectToAttribute:!0}}}static get observers(){return["_stepChanged(step, inputElement)"]}static get delegateProps(){return[...super.delegateProps,"min","max"]}static get constraints(){return[...super.constraints,"min","max","step"]}constructor(){super(),this._setType("number"),this.__onWheel=this.__onWheel.bind(this)}get slotStyles(){const e=this.localName;return[`
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
        `]}get clearElement(){return this.$.clearButton}get __hasUnparsableValue(){return this._inputElementValue===xi}ready(){super.ready(),this.addController(new dt(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new Be(this.inputElement,this._labelController)),this._tooltipController=new Q(this),this.addController(this._tooltipController),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement)}checkValidity(){return this.inputElement?this.inputElement.checkValidity():!this.invalid}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("wheel",this.__onWheel)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("wheel",this.__onWheel)}__onWheel(e){this.hasAttribute("focused")&&e.preventDefault()}_onDecreaseButtonTouchend(e){e.cancelable&&(e.preventDefault(),this.__blurActiveElement(),this._decreaseValue())}_onIncreaseButtonTouchend(e){e.cancelable&&(e.preventDefault(),this.__blurActiveElement(),this._increaseValue())}__blurActiveElement(){const e=Ye();e&&e!==this.inputElement&&e.blur()}_onDecreaseButtonClick(){this._decreaseValue()}_onIncreaseButtonClick(){this._increaseValue()}_decreaseValue(){this._incrementValue(-1)}_increaseValue(){this._incrementValue(1)}_incrementValue(e){if(this.disabled||this.readonly)return;const t=this.step||1;let n=parseFloat(this.value);this.value?n<this.min?(e=0,n=this.min):n>this.max&&(e=0,n=this.max):this.min===0&&e<0||this.max===0&&e>0||this.max===0&&this.min===0?(e=0,n=0):(this.max==null||this.max>=0)&&(this.min==null||this.min<=0)?n=0:this.min>0?(n=this.min,this.max<0&&e<0&&(n=this.max),e=0):this.max<0&&(n=this.max,e<0?e=0:this._getIncrement(1,n-t)>this.max?n-=2*t:n-=t);const r=this._getIncrement(e,n);(!this.value||e===0||this._incrementIsInsideTheLimits(e,n))&&(this.inputElement.value=String(parseFloat(r)),this.inputElement.dispatchEvent(new Event("input",{bubbles:!0,composed:!0})),this.__commitValueChange())}_getIncrement(e,t){let n=this.step||1,r=this.min||0;const o=Math.max(this._getMultiplier(t),this._getMultiplier(n),this._getMultiplier(r));n*=o,t=Math.round(t*o),r*=o;const a=(t-r)%n;return e>0?(t-a+n)/o:e<0?(t-(a||n))/o:t/o}_getDecimalCount(e){const t=String(e),n=t.indexOf(".");return n===-1?1:t.length-n-1}_getMultiplier(e){if(!isNaN(e))return 10**this._getDecimalCount(e)}_incrementIsInsideTheLimits(e,t){return e<0?this.min==null||this._getIncrement(e,t)>=this.min:e>0?this.max==null||this._getIncrement(e,t)<=this.max:this._getIncrement(e,t)<=this.max&&this._getIncrement(e,t)>=this.min}_isButtonEnabled(e){const t=e*(this.step||1),n=parseFloat(this.value);return!this.value||!this.disabled&&this._incrementIsInsideTheLimits(t,n)}_stepChanged(e,t){t&&(t.step=e||"any")}_valueChanged(e,t){e&&isNaN(parseFloat(e))?this.value="":typeof this.value!="string"&&(this.value=String(this.value)),super._valueChanged(this.value,t),this.__keepCommittedValue||(this.__committedValue=this.value,this.__committedUnparsableValueStatus=!1)}_onKeyDown(e){e.key==="ArrowUp"?(e.preventDefault(),this._increaseValue()):e.key==="ArrowDown"&&(e.preventDefault(),this._decreaseValue()),super._onKeyDown(e)}_onInput(e){this.__keepCommittedValue=!0,super._onInput(e),this.__keepCommittedValue=!1}_onChange(e){e.stopPropagation()}_onClearAction(e){super._onClearAction(e),this.__commitValueChange()}_setFocused(e){super._setFocused(e),e||this.__commitValueChange()}_onEnter(e){super._onEnter(e),this.__commitValueChange()}__commitValueChange(){this.__committedValue!==this.value?(this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{bubbles:!0}))):this.__committedUnparsableValueStatus!==this.__hasUnparsableValue&&(this._requestValidation(),this.dispatchEvent(new CustomEvent("unparsable-change"))),this.__committedValue=this.value,this.__committedUnparsableValueStatus=this.__hasUnparsableValue}get _inputElementValue(){return this.inputElement&&this.inputElement.validity.badInput?xi:super._inputElementValue}set _inputElementValue(e){super._inputElementValue=e}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Cs extends yo(S(z(x(k(w))))){static get is(){return"vaadin-number-field"}static get styles(){return[lt,bo]}render(){return C`
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
          theme="${U(this._theme)}"
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
    `}}y(Cs);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Co extends Cs{static get is(){return"vaadin-integer-field"}constructor(){super(),this.allowedCharPattern="[-+\\d]"}_valueChanged(i,e){if(i!==""&&!this.__isInteger(i)){console.warn(`Trying to set non-integer value "${i}" to <vaadin-integer-field>. Clearing the value.`),this.value="";return}super._valueChanged(i,e)}_stepChanged(i,e){if(i!=null&&!this.__hasOnlyDigits(i)){console.warn(`<vaadin-integer-field> The \`step\` property must be a positive integer but \`${i}\` was provided, so the property was reset to \`null\`.`),this.step=null;return}super._stepChanged(i,e)}__isInteger(i){return/^(-\d)?\d*$/u.test(String(i))}__hasOnlyDigits(i){return/^\d+$/u.test(String(i))}}y(Co);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ws=(s,i=s)=>v`
  :host {
    align-items: baseline;
    column-gap: var(--vaadin-${E(i)}-gap, var(--vaadin-gap-s));
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

  [part='${E(s)}'],
  ::slotted(input),
  [part='label'],
  ::slotted(label) {
    grid-row: 1;
  }

  [part='label'],
  ::slotted(label) {
    font-size: var(--vaadin-${E(i)}-label-font-size, var(--vaadin-input-field-label-font-size, inherit));
    line-height: var(--vaadin-${E(i)}-label-line-height, var(--vaadin-input-field-label-line-height, inherit));
    font-weight: var(--vaadin-${E(i)}-font-weight, var(--vaadin-input-field-label-font-weight, 500));
    color: var(--vaadin-${E(i)}-label-color, var(--vaadin-input-field-label-color, var(--vaadin-text-color)));
    word-break: break-word;
    cursor: var(--_cursor);
    /* TODO clicking the label part doesn't toggle the checked state, even though it triggers the active state */
  }

  [part='${E(s)}'],
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
  [part='${E(s)}'] {
    background: var(--vaadin-${E(i)}-background, var(--vaadin-background-color));
    border-color: var(--vaadin-${E(i)}-border-color, var(--vaadin-input-field-border-color, var(--vaadin-border-color)));
    border-radius: var(--vaadin-${E(i)}-border-radius, var(--vaadin-radius-s));
    border-style: var(--_border-style, solid);
    --_border-width: var(--vaadin-${E(i)}-border-width, var(--vaadin-input-field-border-width, 1px));
    border-width: var(--_border-width);
    box-sizing: border-box;
    --_color: var(--vaadin-${E(i)}-marker-color, var(--vaadin-${E(i)}-background, var(--vaadin-background-color)));
    color: var(--_color);
    height: var(--vaadin-${E(i)}-size, 1lh);
    width: var(--vaadin-${E(i)}-size, 1lh);
    position: relative;
    cursor: var(--_cursor);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  :host(:is([checked], [indeterminate])) {
    --vaadin-${E(i)}-background: var(--vaadin-text-color);
    --vaadin-${E(i)}-border-color: transparent;
  }

  :host([disabled]) {
    --vaadin-${E(i)}-background: var(--vaadin-input-field-disabled-background, var(--vaadin-background-container-strong));
    --vaadin-${E(i)}-border-color: transparent;
    --vaadin-${E(i)}-marker-color: var(--vaadin-text-color-disabled);
  }

  /* Focus ring */
  :host([focus-ring]) [part='${E(s)}'] {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--_border-width) * -1);
  }

  :host([focus-ring]:is([checked], [indeterminate])) [part='${E(s)}'] {
    outline-offset: 1px;
  }

  :host([readonly][focus-ring]) [part='${E(s)}'] {
    --vaadin-${E(i)}-border-color: transparent;
    outline-offset: calc(var(--_border-width) * -1);
    outline-style: dashed;
  }

  /* Checked indicator (checkmark, dot) */
  [part='${E(s)}']::after {
    content: '\\2003' / '';
    background: currentColor;
    border-radius: inherit;
    display: flex;
    align-items: center;
    --_filter: var(--vaadin-${E(i)}-marker-color, saturate(0) invert(1) hue-rotate(180deg) contrast(100) brightness(100));
    filter: var(--_filter);
  }

  :host(:not([checked], [indeterminate])) [part='${E(s)}']::after {
    opacity: 0;
  }

  @media (forced-colors: active) {
    :host(:is([checked], [indeterminate])) {
      --vaadin-${E(i)}-border-color: CanvasText !important;
    }

    :host(:is([checked], [indeterminate])) [part='${E(s)}'] {
      background: SelectedItem !important;
    }

    :host(:is([checked], [indeterminate])) [part='${E(s)}']::after {
      background: SelectedItemText !important;
    }

    :host([readonly]) [part='${E(s)}']::after {
      background: CanvasText !important;
    }

    :host([disabled]) {
      --vaadin-${E(i)}-border-color: GrayText !important;
    }

    :host([disabled]) [part='${E(s)}']::after {
      background: GrayText !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const wo=v`
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
`,xo=[De,ws("checkbox"),wo];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const xs=B(s=>class extends Yt(we(ct(s))){static get properties(){return{checked:{type:Boolean,value:!1,notify:!0,reflectToAttribute:!0,sync:!0}}}static get delegateProps(){return[...super.delegateProps,"checked"]}_onChange(e){const t=e.target;this._toggleChecked(t.checked)}_toggleChecked(e){this.checked=e}});/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Eo=s=>class extends Fe(Ne(xs(ht(_t(s))))){static get properties(){return{indeterminate:{type:Boolean,notify:!0,value:!1,reflectToAttribute:!0},name:{type:String,value:""},readonly:{type:Boolean,value:!1,reflectToAttribute:!0}}}static get observers(){return["__readonlyChanged(readonly, inputElement)"]}static get delegateProps(){return[...super.delegateProps,"indeterminate"]}static get delegateAttrs(){return[...super.delegateAttrs,"name","invalid","required"]}constructor(){super(),this._setType("checkbox"),this._boundOnInputClick=this._onInputClick.bind(this),this.value="on",this.tabindex=0}get slotStyles(){return[`
          ${this.localName} > input[slot='input'] {
            opacity: 0;
          }
        `]}ready(){super.ready(),this.addController(new dt(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new Be(this.inputElement,this._labelController)),this._createMethodObserver("_checkedChanged(checked)")}_shouldSetActive(e){return this.readonly||e.target.localName==="a"||e.target===this._helperNode||e.target===this._errorNode?!1:super._shouldSetActive(e)}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("click",this._boundOnInputClick)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("click",this._boundOnInputClick)}_onInputClick(e){this.readonly&&e.preventDefault()}__readonlyChanged(e,t){t&&(e?t.setAttribute("aria-readonly","true"):t.removeAttribute("aria-readonly"))}_toggleChecked(e){this.indeterminate&&(this.indeterminate=!1),super._toggleChecked(e)}checkValidity(){return!this.required||!!this.checked}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}_checkedChanged(e){(e||this.__oldChecked)&&this._requestValidation(),this.__oldChecked=e}_requiredChanged(e){super._requiredChanged(e),e===!1&&this._requestValidation()}_onRequiredIndicatorClick(){this._labelNode.click()}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class So extends Eo(z(S(x(k(w))))){static get is(){return"vaadin-checkbox"}static get styles(){return xo}render(){return C`
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
    `}ready(){super.ready(),this._tooltipController=new Q(this),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}}y(So);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Es=v`
  :host {
    align-items: center;
    border-radius: var(--vaadin-item-border-radius, var(--vaadin-radius-m));
    box-sizing: border-box;
    cursor: var(--vaadin-clickable-cursor);
    display: flex;
    column-gap: var(--vaadin-item-gap, var(--vaadin-gap-s));
    height: var(--vaadin-item-height, auto);
    padding: var(--vaadin-item-padding, var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container));
    -webkit-tap-highlight-color: transparent;
  }

  :host([focused]) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--vaadin-focus-ring-width) / -1);
  }

  :host([disabled]) {
    cursor: var(--vaadin-disabled-cursor);
    opacity: 0.5;
    pointer-events: none;
  }

  :host([hidden]) {
    display: none !important;
  }

  [part='checkmark'] {
    color: var(--vaadin-item-checkmark-color, inherit);
    display: var(--vaadin-item-checkmark-display, none);
    visibility: hidden;
  }

  [part='checkmark']::before {
    content: '';
    display: block;
    background: currentColor;
    height: var(--vaadin-icon-size, 1lh);
    mask: var(--_vaadin-icon-checkmark) 50% / var(--vaadin-icon-visual-size, 100%) no-repeat;
    width: var(--vaadin-icon-size, 1lh);
  }

  :host([selected]) [part='checkmark'] {
    visibility: visible;
  }

  [part='content'] {
    flex: 1;
    display: flex;
    align-items: center;
    column-gap: inherit;
    justify-content: var(--vaadin-item-text-align, start);
  }

  @media (forced-colors: active) {
    [part='checkmark']::before {
      background: CanvasText;
    }
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ss=s=>class extends _t(Ce(s)){static get properties(){return{_hasVaadinItemMixin:{value:!0},selected:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_selectedChanged",sync:!0},_value:String}}get _activeKeys(){return["Enter"," "]}get value(){return this._value!==void 0?this._value:this.textContent.trim()}set value(e){this._value=e}ready(){super.ready();const e=this.getAttribute("value");e!==null&&(this.value=e)}focus(e){this.disabled||super.focus(e)}_shouldSetActive(e){return!this.disabled&&!(e.type==="keydown"&&e.defaultPrevented)}_selectedChanged(e){this.setAttribute("aria-selected",e)}_disabledChanged(e){super._disabledChanged(e),e&&(this.selected=!1,this.blur())}_onKeyDown(e){super._onKeyDown(e),this._activeKeys.includes(e.key)&&!e.defaultPrevented&&(e.preventDefault(),this.click())}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Io extends Ss(S(N(x(k(w))))){static get is(){return"vaadin-select-item"}static get styles(){return Es}static get properties(){return{role:{type:String,value:"option",reflectToAttribute:!0}}}render(){return C`
      <span part="checkmark" aria-hidden="true"></span>
      <div part="content">
        <slot></slot>
      </div>
    `}}y(Io);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Is(s,i){const{scrollLeft:e}=s;return i!=="rtl"?e:s.scrollWidth-s.clientWidth+e}function Ao(s,i,e){i!=="rtl"?s.scrollLeft=e:s.scrollLeft=s.clientWidth-s.scrollWidth+e}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const To=s=>class extends xe(s){get focused(){return(this._getItems()||[]).find(Wt)}get _vertical(){return!0}get _tabNavigation(){return!1}focus(e){const t=this._getFocusableIndex();t>=0&&this._focus(t,e)}_getFocusableIndex(){const e=this._getItems();return Array.isArray(e)?this._getAvailableIndex(e,0,null,t=>!q(t)):-1}_getItems(){return Array.from(this.children)}_onKeyDown(e){if(super._onKeyDown(e),e.metaKey||e.ctrlKey)return;const{key:t,shiftKey:n}=e,r=this._getItems()||[],o=r.indexOf(this.focused);let a,l;const _=!this._vertical&&this.getAttribute("dir")==="rtl"?-1:1;this.__isPrevKeyPressed(t,n)?(l=-_,a=o-_):this.__isNextKeyPressed(t,n)?(l=_,a=o+_):t==="Home"?(l=1,a=0):t==="End"&&(l=-1,a=r.length-1),a=this._getAvailableIndex(r,a,l,f=>!q(f)),!(this._tabNavigation&&t==="Tab"&&(a>o&&e.shiftKey||a<o&&!e.shiftKey||a===o))&&a>=0&&(e.preventDefault(),this._focus(a,{focusVisible:!0},!0))}__isPrevKeyPressed(e,t){return this._vertical?e==="ArrowUp":e==="ArrowLeft"||this._tabNavigation&&e==="Tab"&&t}__isNextKeyPressed(e,t){return this._vertical?e==="ArrowDown":e==="ArrowRight"||this._tabNavigation&&e==="Tab"&&!t}_focus(e,t,n=!1){const r=this._getItems();this._focusItem(r[e],t,n)}_focusItem(e,t){e&&e.focus(t)}_getAvailableIndex(e,t,n,r){const o=e.length;let a=t;for(let l=0;typeof a=="number"&&l<o;l+=1,a+=n||1){a<0?a=o-1:a>=o&&(a=0);const d=e[a];if(this._isItemFocusable(d)&&this.__isMatchingItem(d,r))return a}return-1}__isMatchingItem(e,t){return typeof t=="function"?t(e):!0}_isItemFocusable(e){return!e.hasAttribute("disabled")}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const As=s=>class extends To(s){static get properties(){return{disabled:{type:Boolean,value:!1,reflectToAttribute:!0},selected:{type:Number,reflectToAttribute:!0,notify:!0,sync:!0},orientation:{type:String,reflectToAttribute:!0,value:""},items:{type:Array,readOnly:!0,notify:!0},_searchBuf:{type:String,value:""}}}static get observers(){return["_enhanceItems(items, orientation, selected, disabled)"]}get _isRTL(){return!this._vertical&&this.getAttribute("dir")==="rtl"}get _scrollerElement(){return console.warn(`Please implement the '_scrollerElement' property in <${this.localName}>`),this}get _vertical(){return this.orientation!=="horizontal"}focus(e){this._observer&&this._observer.flush();const t=Array.isArray(this.items)?this.items:[],n=this._getAvailableIndex(t,0,null,r=>r.tabIndex===0&&!q(r));n>=0?this._focus(n,e):super.focus(e)}ready(){super.ready(),this.addEventListener("click",t=>this._onClick(t));const e=this.shadowRoot.querySelector("slot:not([name])");this._observer=new te(e,()=>{this._setItems(this._filterItems([...this.children]))})}_getItems(){return this.items}_enhanceItems(e,t,n,r){if(!r&&e){this.setAttribute("aria-orientation",t||"vertical"),e.forEach(a=>{t?a.setAttribute("orientation",t):a.removeAttribute("orientation")}),this._setFocusable(n<0||!n?0:n);const o=e[n];e.forEach(a=>{a.selected=a===o}),o&&!o.disabled&&this._scrollToItem(n)}}_filterItems(e){return e.filter(t=>t._hasVaadinItemMixin)}_onClick(e){if(e.metaKey||e.shiftKey||e.ctrlKey||e.defaultPrevented)return;const t=this._filterItems(e.composedPath())[0];let n;t&&!t.disabled&&(n=this.items.indexOf(t))>=0&&(this.selected=n)}_searchKey(e,t){this._searchReset=I.debounce(this._searchReset,H.after(500),()=>{this._searchBuf=""}),this._searchBuf+=t.toLowerCase(),this.items.some(r=>this.__isMatchingKey(r))||(this._searchBuf=t.toLowerCase());const n=this._searchBuf.length===1?e+1:e;return this._getAvailableIndex(this.items,n,1,r=>this.__isMatchingKey(r)&&getComputedStyle(r).display!=="none")}__isMatchingKey(e){return e.textContent.replace(/[^\p{L}\p{Nd}]/gu,"").toLowerCase().startsWith(this._searchBuf)}_onKeyDown(e){if(e.metaKey||e.ctrlKey)return;const t=e.key,n=this.items.indexOf(this.focused);if(/[\p{L}\p{Nd}]/u.test(t)&&t.length===1){const r=this._searchKey(n,t);r>=0&&this._focus(r);return}super._onKeyDown(e)}_setFocusable(e){e=this._getAvailableIndex(this.items,e,1);const t=this.items[e];this.items.forEach(n=>{n.tabIndex=n===t?0:-1})}_focus(e,t){this.items.forEach((n,r)=>{n.focused=r===e}),this._setFocusable(e),this._scrollToItem(e),super._focus(e,t)}_scrollToItem(e){const t=this.items[e];if(!t)return;const n=this._vertical?["top","bottom"]:this._isRTL?["right","left"]:["left","right"],r=this._scrollerElement.getBoundingClientRect(),o=(this.items[e+1]||t).getBoundingClientRect(),a=(this.items[e-1]||t).getBoundingClientRect();let l=0;!this._isRTL&&o[n[1]]>=r[n[1]]||this._isRTL&&o[n[1]]<=r[n[1]]?l=o[n[1]]-r[n[1]]:(!this._isRTL&&a[n[0]]<=r[n[0]]||this._isRTL&&a[n[0]]>=r[n[0]])&&(l=a[n[0]]-r[n[0]]),this._scroll(l)}_scroll(e){if(this._vertical)this._scrollerElement.scrollTop+=e;else{const t=this.getAttribute("dir")||"ltr",n=Is(this._scrollerElement,t)+e;Ao(this._scrollerElement,t,n)}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ts=v`
  :host {
    --vaadin-item-checkmark-display: block;
    display: flex;
  }

  :host([hidden]) {
    display: none !important;
  }

  [part='items'] {
    height: 100%;
    overflow-y: auto;
    width: 100%;
  }

  [part='items'] ::slotted(hr) {
    border-color: var(--vaadin-divider-color, var(--vaadin-border-color-secondary));
    border-width: 0 0 1px;
    margin: 4px 8px;
    margin-inline-start: calc(var(--vaadin-icon-size, 1lh) + var(--vaadin-item-gap, var(--vaadin-gap-s)) + 8px);
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ko extends As(S(N(x(k(w))))){static get is(){return"vaadin-select-list-box"}static get styles(){return Ts}static get properties(){return{orientation:{readOnly:!0}}}get _scrollerElement(){return this.shadowRoot.querySelector('[part="items"]')}render(){return C`
      <div part="items">
        <slot></slot>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","listbox")}}y(ko);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ro=v`
  :host {
    align-items: flex-start;
    justify-content: flex-start;
  }

  [part='overlay'] {
    min-width: var(--vaadin-select-overlay-width, var(--_vaadin-select-overlay-default-width));
  }

  [part='content'] {
    padding: var(--vaadin-item-overlay-padding, 4px);
  }

  [part='backdrop'] {
    background: transparent;
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Oo=s=>class extends Qt(rt(N(s))){static get observers(){return["_updateOverlayWidth(opened, positionTarget)"]}ready(){super.ready(),this.restoreFocusOnClose=!0}get _contentRoot(){return this._rendererRoot}get _rendererRoot(){if(!this.__savedRoot){const e=document.createElement("div");e.setAttribute("slot","overlay"),this.owner.appendChild(e),this.__savedRoot=e}return this.__savedRoot}_shouldCloseOnOutsideClick(e){return!0}_mouseDownListener(e){super._mouseDownListener(e),e.preventDefault()}_getMenuElement(){return Array.from(this._rendererRoot.children).find(e=>e.localName!=="style")}_updateOverlayWidth(e,t){e&&t&&this.style.setProperty("--_vaadin-select-overlay-default-width",`${t.offsetWidth}px`)}requestContentUpdate(){if(super.requestContentUpdate(),this.owner){const e=this._getMenuElement();this.owner._assignMenuElement(e)}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Lo extends Oo(S(x(k(w)))){static get is(){return"vaadin-select-overlay"}static get styles(){return[st,Ro]}render(){return C`
      <div id="backdrop" part="backdrop" ?hidden="${!this.withBackdrop}"></div>
      <div part="overlay" id="overlay">
        <div part="content" id="content">
          <slot></slot>
        </div>
      </div>
    `}updated(i){super.updated(i),i.has("renderer")&&this.requestContentUpdate()}}y(Lo);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Po=v`
  :host {
    min-height: 1lh;
    outline: none;
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
    display: flex;
    align-items: center;
  }

  ::slotted(*) {
    padding: 0;
    cursor: inherit;
  }

  .vaadin-button-container,
  [part='label'] {
    display: contents;
  }

  :host([placeholder]) {
    color: var(--vaadin-input-field-placeholder-color, var(--vaadin-text-color-secondary));
  }

  :host([disabled]) {
    pointer-events: none;
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class zo extends ti(S(x(k(w)))){static get is(){return"vaadin-select-value-button"}static get styles(){return Po}render(){return C`
      <div class="vaadin-button-container">
        <span part="label">
          <slot></slot>
        </span>
      </div>
    `}}y(zo);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Mo=v`
  .sr-only {
    border: 0 !important;
    clip: rect(1px, 1px, 1px, 1px) !important;
    clip-path: inset(50%) !important;
    height: 1px !important;
    margin: -1px !important;
    overflow: hidden !important;
    padding: 0 !important;
    position: absolute !important;
    width: 1px !important;
    white-space: nowrap !important;
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Fo=v`
  :host {
    position: relative;
  }

  ::slotted([slot='value']) {
    flex: 1;
  }

  ::slotted(div[slot='overlay']) {
    display: contents;
  }

  :host(:not([focus-ring])) [part='input-field'] {
    outline: none;
  }

  :host([readonly]:not([focus-ring])) [part='input-field'] {
    --vaadin-input-field-border-color: inherit;
  }

  [part='input-field'],
  :host(:not([readonly])) ::slotted([slot='value']) {
    cursor: var(--vaadin-clickable-cursor);
  }

  [part~='toggle-button']::before {
    mask-image: var(--_vaadin-icon-chevron-down);
  }

  :host([readonly]) [part~='toggle-button'] {
    display: none;
  }

  :host([theme~='align-start']) {
    --vaadin-item-text-align: start;
  }

  :host([theme~='align-center']) {
    --vaadin-item-text-align: center;
  }

  :host([theme~='align-end']) {
    --vaadin-item-text-align: end;
  }

  :host([theme~='align-left']) {
    --vaadin-item-text-align: left;
  }

  :host([theme~='align-right']) {
    --vaadin-item-text-align: right;
  }

  :host([theme~='align-start']) ::slotted([slot='value']) {
    justify-content: start;
  }

  :host([theme~='align-center']) ::slotted([slot='value']) {
    justify-content: center;
  }

  :host([theme~='align-end']) ::slotted([slot='value']) {
    justify-content: end;
  }

  :host([theme~='align-left']) ::slotted([slot='value']) {
    justify-content: left;
  }

  :host([theme~='align-right']) ::slotted([slot='value']) {
    justify-content: right;
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ks{constructor(i,e){this.query=i,this.callback=e,this._boundQueryHandler=this._queryHandler.bind(this)}hostConnected(){this._removeListener(),this._mediaQuery=window.matchMedia(this.query),this._addListener(),this._queryHandler(this._mediaQuery)}hostDisconnected(){this._removeListener()}_addListener(){this._mediaQuery&&this._mediaQuery.addListener(this._boundQueryHandler)}_removeListener(){this._mediaQuery&&this._mediaQuery.removeListener(this._boundQueryHandler),this._mediaQuery=null}_queryHandler(i){typeof this.callback=="function"&&this.callback(i.matches)}}/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class $o extends he{constructor(i){super(i,"value","vaadin-select-value-button",{initializer:(e,t)=>{t._setFocusElement(e),t.ariaTarget=e,t.stateTarget=e,e.setAttribute("aria-haspopup","listbox")}})}}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Do=s=>class extends ht(Yt(xe(Ne(s)))){static get properties(){return{items:{type:Array,observer:"__itemsChanged"},opened:{type:Boolean,value:!1,notify:!0,observer:"_openedChanged",reflectToAttribute:!0,sync:!0},renderer:{type:Object},value:{type:String,value:"",notify:!0,observer:"_valueChanged",sync:!0},name:{type:String},placeholder:{type:String},readonly:{type:Boolean,value:!1,reflectToAttribute:!0},noVerticalOverlap:{type:Boolean,value:!1},_phone:Boolean,_phoneMediaQuery:{value:"(max-width: 450px), (max-height: 450px)"},_inputContainer:Object,_items:Object}}static get delegateAttrs(){return[...super.delegateAttrs,"invalid"]}static get observers(){return["_updateAriaExpanded(opened, focusElement)","_updateSelectedItem(value, _items, placeholder)"]}constructor(){super(),this._itemId=`value-${this.localName}-${$e()}`,this._srLabelController=new as(this),this._srLabelController.slotName="sr-label"}disconnectedCallback(){super.disconnectedCallback(),this.opened=!1}ready(){super.ready(),this._inputContainer=this.shadowRoot.querySelector('[part~="input-field"]'),this._overlayElement=this.$.overlay,this._valueButtonController=new $o(this),this.addController(this._valueButtonController),this.addController(this._srLabelController),this.addController(new ks(this._phoneMediaQuery,e=>{this._phone=e})),this._tooltipController=new Q(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.focusElement),this.addController(this._tooltipController)}updated(e){super.updated(e),e.has("_phone")&&this.toggleAttribute("phone",this._phone)}requestContentUpdate(){this._overlayElement&&this._overlayElement.requestContentUpdate()}_requiredChanged(e){super._requiredChanged(e),e===!1&&this._requestValidation()}__itemsChanged(e,t){(e||t)&&this.requestContentUpdate()}_assignMenuElement(e){e&&e!==this.__lastMenuElement&&(this._menuElement=e,this.__initMenuItems(e),e.addEventListener("items-changed",()=>{this.__initMenuItems(e)}),e.addEventListener("selected-changed",()=>this.__updateValueButton()),e.addEventListener("keydown",t=>this._onKeyDownInside(t),!0),e.addEventListener("click",t=>{const n=t.composedPath().find(r=>r._hasVaadinItemMixin);this.__dispatchChangePending=!!(n&&n.value!==void 0&&n.value!==this.value),this.opened=!1},!0),this.__lastMenuElement=e),this._menuElement&&this._menuElement.items&&this._updateSelectedItem(this.value,this._menuElement.items)}__initMenuItems(e){e.items&&(this._items=e.items)}_valueChanged(e,t){this.toggleAttribute("has-value",!!e),t!==void 0&&!this.__dispatchChangePending&&this._requestValidation()}_onClick(e){this.disabled||(e.preventDefault(),this.opened=!this.readonly)}_onEscape(e){this.opened&&(e.stopPropagation(),this.opened=!1)}_onToggleMouseDown(e){e.preventDefault(),this.opened||this.focusElement.focus()}_onKeyDown(e){if(super._onKeyDown(e),!(e.altKey||e.shiftKey||e.ctrlKey||e.metaKey)&&e.target===this.focusElement&&!this.readonly&&!this.disabled&&!this.opened){if(/^(Enter|SpaceBar|\s|ArrowDown|Down|ArrowUp|Up)$/u.test(e.key))e.preventDefault(),this.opened=!0;else if(/[\p{L}\p{Nd}]/u.test(e.key)&&e.key.length===1){const t=this._menuElement.selected,n=t!==void 0?t:-1,r=this._menuElement._searchKey(n,e.key);r>=0&&(this.__dispatchChangePending=!0,this._updateAriaLive(!0),this._menuElement.selected=r)}}}_onKeyDownInside(e){e.key==="Tab"&&(this.focusElement.setAttribute("tabindex","-1"),this._overlayElement.restoreFocusOnClose=!1,this.opened=!1,setTimeout(()=>{this.focusElement.setAttribute("tabindex","0"),this._overlayElement.restoreFocusOnClose=!0}))}_openedChanged(e,t){if(e){if(this.disabled||this.readonly){this.opened=!1;return}this._updateAriaLive(!1);const n=this.hasAttribute("focus-ring");this._openedWithFocusRing=n,n&&this.removeAttribute("focus-ring")}else t&&(this._openedWithFocusRing&&this.setAttribute("focus-ring",""),!this.__dispatchChangePending&&!this._keyboardActive&&this._requestValidation())}_updateAriaExpanded(e,t){t&&t.setAttribute("aria-expanded",e?"true":"false")}_updateAriaLive(e){this.focusElement&&(e?this.focusElement.setAttribute("aria-live","polite"):this.focusElement.removeAttribute("aria-live"))}__attachSelectedItem(e){let t;const n=e.getAttribute("label");n?t=this.__createItemElement({label:n}):t=e.cloneNode(!0),t._sourceItem=e,this.__appendValueItemElement(t,this.focusElement),t.selected=!0}__createItemElement(e){const t=document.createElement(e.component||"vaadin-select-item");return e.label&&(t.textContent=e.label),e.value&&(t.value=e.value),e.disabled&&(t.disabled=e.disabled),e.className&&(t.className=e.className),t}__appendValueItemElement(e,t){t.appendChild(e),e.removeAttribute("tabindex"),e.removeAttribute("aria-selected"),e.removeAttribute("role"),e.removeAttribute("focused"),e.removeAttribute("focus-ring"),e.removeAttribute("active"),e.setAttribute("id",this._itemId)}_accessibleNameChanged(e){this._srLabelController.setLabel(e),this._setCustomAriaLabelledBy(e?this._srLabelController.defaultId:null)}_accessibleNameRefChanged(e){this._setCustomAriaLabelledBy(e)}_setCustomAriaLabelledBy(e){const t=this._getLabelIdWithItemId(e);this._fieldAriaController.setLabelId(t,!0)}_getLabelIdWithItemId(e){const n=(this._items?this._items[this._menuElement.selected]:!1)||this.placeholder?this._itemId:"";return e?`${e} ${n}`.trim():null}__updateValueButton(){const e=this.focusElement;if(!e)return;e.innerHTML="";const t=this._items[this._menuElement.selected];if(e.removeAttribute("placeholder"),this._hasContent(t))this.__attachSelectedItem(t);else if(this.placeholder){const r=this.__createItemElement({label:this.placeholder});this.__appendValueItemElement(r,e),e.setAttribute("placeholder","")}!this._valueChanging&&t&&(this._selectedChanging=!0,this.value=t.value||"",this.__dispatchChangePending&&this.__dispatchChange(),delete this._selectedChanging);const n=t||this.placeholder?{newId:this._itemId}:{oldId:this._itemId};Ge(e,"aria-labelledby",n),(this.accessibleName||this.accessibleNameRef)&&this._setCustomAriaLabelledBy(this.accessibleNameRef||this._srLabelController.defaultId)}_hasContent(e){if(!e)return!1;const t=!!(e.hasAttribute("label")?e.getAttribute("label"):e.textContent.trim()),n=e.childElementCount>0;return t||n}_updateSelectedItem(e,t){if(t){const n=e==null?e:e.toString();this._menuElement.selected=t.reduce((r,o,a)=>r===void 0&&o.value===n?a:r,void 0),this._selectedChanging||(this._valueChanging=!0,this.__updateValueButton(),delete this._valueChanging)}}_shouldRemoveFocus(e){return!this.contains(e.relatedTarget)}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}checkValidity(){return!this.required||this.readonly||!!this.value}__defaultRenderer(e,t){if(!this.items||this.items.length===0){e.textContent="";return}let n=e.firstElementChild;n||(n=document.createElement("vaadin-select-list-box"),e.appendChild(n)),n.textContent="",this.items.forEach(r=>{n.appendChild(this.__createItemElement(r))})}__dispatchChange(){this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{bubbles:!0})),this.__dispatchChangePending=!1}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class No extends Do(z(S(x(k(w))))){static get is(){return"vaadin-select"}static get styles(){return[lt,Mo,Fo]}render(){return C`
      <div class="vaadin-select-container">
        <div part="label" @click="${this._onClick}">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true" @click="${this.focus}"></span>
        </div>

        <vaadin-input-container
          part="input-field"
          .readonly="${this.readonly}"
          .disabled="${this.disabled}"
          .invalid="${this.invalid}"
          theme="${U(this._theme)}"
          @click="${this._onClick}"
        >
          <slot name="prefix" slot="prefix"></slot>
          <slot name="value"></slot>
          <div
            part="field-button toggle-button"
            slot="suffix"
            aria-hidden="true"
            @mousedown="${this._onToggleMouseDown}"
          ></div>
        </vaadin-input-container>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>
      </div>

      <vaadin-select-overlay
        id="overlay"
        .owner="${this}"
        .positionTarget="${this._inputContainer}"
        .opened="${this.opened}"
        .withBackdrop="${this._phone}"
        .renderer="${this.renderer||this.__defaultRenderer}"
        ?phone="${this._phone}"
        theme="${U(this._theme)}"
        ?no-vertical-overlap="${this.noVerticalOverlap}"
        exportparts="backdrop, overlay, content"
        @opened-changed="${this._onOpenedChanged}"
        @vaadin-overlay-open="${this._onOverlayOpen}"
      >
        <slot name="overlay"></slot>
      </vaadin-select-overlay>

      <slot name="tooltip"></slot>
      <div class="sr-only">
        <slot name="sr-label"></slot>
      </div>
    `}_onOpenedChanged(i){this.opened=i.detail.value}_onOverlayOpen(){this._menuElement&&this._menuElement.focus({focusVisible:ne()})}}y(No);window.Vaadin.Flow.selectConnector={};window.Vaadin.Flow.selectConnector.initLazy=s=>{s.$connector||(s.$connector={},s.renderer=i=>{const e=s.querySelector("vaadin-select-list-box");e&&(i.firstChild&&i.removeChild(i.firstChild),i.appendChild(e))})};/**
 * @license
 * Copyright 2020 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Bo=zi(class extends Pi{constructor(s){if(super(s),s.type!==ee.PROPERTY&&s.type!==ee.ATTRIBUTE&&s.type!==ee.BOOLEAN_ATTRIBUTE)throw Error("The `live` directive is not allowed on child or event bindings");if(!Ji(s))throw Error("`live` bindings can only contain a single expression")}render(s){return s}update(s,[i]){if(i===ke||i===Li)return i;const e=s.element,t=s.name;if(s.type===ee.PROPERTY){if(i===e[t])return ke}else if(s.type===ee.BOOLEAN_ATTRIBUTE){if(!!i===e.hasAttribute(t))return ke}else if(s.type===ee.ATTRIBUTE&&e.getAttribute(t)===i+"")return ke;return Zn(s),i}}),et=window;et.Vaadin=et.Vaadin||{};et.Vaadin.setLitRenderer=(s,i,e,t,n,r,o)=>{const a=g=>n.map(b=>(...L)=>{g!==void 0&&t(b,g,L[0]instanceof Event?[]:[...L])}),l=["html","root","live","appId","itemKey","model","item","index",...n,`return html\`${e}\``],d=new Function(...l),_=(g,b,L)=>{const{item:A,index:M}=b;$t(d(C,g,Bo,o,L,b,A,M,...a(L)),g)},f=(g,b,L)=>{const{item:A}=L;g.__litRenderer!==f&&(g.innerHTML="",delete g._$litPart$,g.__litRenderer=f);const M={};for(const $ in A)$.startsWith(r)&&(M[$.replace(r,"")]=A[$]);_(g,{...L,item:M},A.key)};f.__rendererId=r,s[i]=f};et.Vaadin.unsetLitRenderer=(s,i,e)=>{s[i]?.__rendererId===e&&(s[i]=void 0)};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Vo=v`
  [part='radio'] {
    border-radius: 50%;
    color: var(--vaadin-radio-button-dot-color, var(--_color));
  }

  [part='radio']::after {
    width: var(--vaadin-radio-button-dot-size, var(--vaadin-radio-button-marker-size, 50%));
    height: var(--vaadin-radio-button-dot-size, var(--vaadin-radio-button-marker-size, 50%));
    border-radius: 50%;
    filter: var(--vaadin-radio-button-dot-color, var(--_filter));
  }
`,Ho=[De,ws("radio","radio-button"),Vo];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Wo=s=>class extends Fe(ls(xs(ht(_t(s))))){static get properties(){return{name:{type:String,value:""}}}static get delegateAttrs(){return[...super.delegateAttrs,"name"]}constructor(){super(),this._setType("radio"),this.value="on",this.tabindex=0}get slotStyles(){return[`
          ${this.localName} > input[slot='input'] {
            opacity: 0;
          }
        `]}ready(){super.ready(),this.addController(new dt(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new Be(this.inputElement,this._labelController))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class qo extends Wo(z(S(x(k(w))))){static get is(){return"vaadin-radio-button"}static get styles(){return Ho}render(){return C`
      <div class="vaadin-radio-button-container">
        <div part="radio" aria-hidden="true"></div>
        <slot name="input"></slot>
        <slot name="label"></slot>
      </div>
    `}}y(qo);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Rs=v`
  [part='label'],
  [part='helper-text'],
  [part='error-message'] {
    width: auto;
    min-width: auto;
  }

  [part='group-field'] {
    display: flex;
    flex-direction: column;
    gap: var(--vaadin-gap-xs) var(--vaadin-gap-xl);
  }

  :host([theme~='horizontal']) [part='group-field'] {
    flex-flow: row wrap;
    align-items: center;
  }

  :host([has-label][theme~='horizontal']) [part='group-field'] {
    padding: var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container);
    padding-inline: 0;
    border-block: var(--vaadin-input-field-border-width, 1px) solid transparent;
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Uo=[De,Rs,v`
    :host([readonly]) ::slotted(vaadin-radio-button) {
      --vaadin-radio-button-background: transparent;
      --vaadin-radio-button-border-color: var(--vaadin-border-color);
      --vaadin-radio-button-marker-color: var(--vaadin-text-color);
      --_border-style: dashed;
    }
  `];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const jo=s=>class extends Ne(Ce(we(xe(s)))){static get properties(){return{name:{type:String,observer:"__nameChanged",sync:!0},value:{type:String,notify:!0,value:"",sync:!0,observer:"__valueChanged"},readonly:{type:Boolean,value:!1,reflectToAttribute:!0,sync:!0,observer:"__readonlyChanged"},_fieldName:{type:String}}}constructor(){super(),this.__registerRadioButton=this.__registerRadioButton.bind(this),this.__unregisterRadioButton=this.__unregisterRadioButton.bind(this),this.__onRadioButtonCheckedChange=this.__onRadioButtonCheckedChange.bind(this),this._tooltipController=new Q(this),this._tooltipController.addEventListener("tooltip-changed",e=>{const t=e.detail.node;if(t&&t.isConnected){const n=this.__radioButtons.map(r=>r.inputElement);this._tooltipController.setAriaTarget(n)}else this._tooltipController.setAriaTarget([])})}get __radioButtons(){return this.__filterRadioButtons([...this.children])}get __selectedRadioButton(){return this.__radioButtons.find(e=>e.checked)}get isHorizontalRTL(){return this.__isRTL&&this._theme!=="vertical"}ready(){super.ready(),this.ariaTarget=this,this.setAttribute("role","radiogroup"),this._fieldName=`${this.localName}-${$e()}`;const e=this.shadowRoot.querySelector("slot:not([name])");this._observer=new te(e,({addedNodes:t,removedNodes:n})=>{this.__filterRadioButtons(t).reverse().forEach(this.__registerRadioButton),this.__filterRadioButtons(n).forEach(this.__unregisterRadioButton);const r=this.__radioButtons.map(o=>o.inputElement);this._tooltipController.setAriaTarget(r)}),this.addController(this._tooltipController)}__filterRadioButtons(e){return e.filter(t=>t.nodeType===Node.ELEMENT_NODE&&t.localName==="vaadin-radio-button")}_onKeyDown(e){super._onKeyDown(e);const t=e.composedPath().find(n=>n.nodeType===Node.ELEMENT_NODE&&n.localName==="vaadin-radio-button");["ArrowLeft","ArrowUp"].includes(e.key)&&(e.preventDefault(),this.__selectNextRadioButton(t)),["ArrowRight","ArrowDown"].includes(e.key)&&(e.preventDefault(),this.__selectPrevRadioButton(t))}_invalidChanged(e){super._invalidChanged(e),e?this.setAttribute("aria-invalid","true"):this.removeAttribute("aria-invalid")}__nameChanged(e){this.__radioButtons.forEach(t=>{t.name=e||this._fieldName})}__selectNextRadioButton(e){const t=this.__radioButtons.indexOf(e);this.__selectIncRadioButton(t,this.isHorizontalRTL?1:-1)}__selectPrevRadioButton(e){const t=this.__radioButtons.indexOf(e);this.__selectIncRadioButton(t,this.isHorizontalRTL?-1:1)}__selectIncRadioButton(e,t){const n=(this.__radioButtons.length+e+t)%this.__radioButtons.length,r=this.__radioButtons[n];r.disabled?this.__selectIncRadioButton(n,t):(r.focusElement.focus(),r.focusElement.click())}__registerRadioButton(e){e.name=this.name||this._fieldName,e.addEventListener("checked-changed",this.__onRadioButtonCheckedChange),(this.disabled||this.readonly)&&(e.disabled=!0),e.checked&&this.__selectRadioButton(e)}__unregisterRadioButton(e){e.removeEventListener("checked-changed",this.__onRadioButtonCheckedChange),e.value===this.value&&this.__selectRadioButton(null)}__onRadioButtonCheckedChange(e){e.target.checked&&this.__selectRadioButton(e.target)}__valueChanged(e,t){if(!(t===void 0&&e==="")){if(e){const n=this.__radioButtons.find(r=>r.value===e);n?(this.__selectRadioButton(n),this.toggleAttribute("has-value",!0)):console.warn(`The radio button with the value "${e}" was not found.`)}else this.__selectRadioButton(null),this.removeAttribute("has-value");t!==void 0&&this._requestValidation()}}__readonlyChanged(e,t){!e&&t===void 0||t!==e&&this.__updateRadioButtonsDisabledProperty()}_disabledChanged(e,t){super._disabledChanged(e,t),!(!e&&t===void 0)&&t!==e&&this.__updateRadioButtonsDisabledProperty()}_shouldRemoveFocus(e){return!this.contains(e.relatedTarget)}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}__selectRadioButton(e){e?this.value=e.value:this.value="",this.__radioButtons.forEach(t=>{t.checked=t===e}),this.readonly&&this.__updateRadioButtonsDisabledProperty()}__updateRadioButtonsDisabledProperty(){this.__radioButtons.forEach(e=>{this.readonly?e.disabled=e!==this.__selectedRadioButton:e.disabled=this.disabled})}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Go extends jo(z(S(x(k(w))))){static get is(){return"vaadin-radio-group"}static get styles(){return Uo}render(){return C`
      <div class="vaadin-group-field-container">
        <div part="label">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true"></span>
        </div>

        <div part="group-field">
          <slot></slot>
        </div>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>
      </div>

      <slot name="tooltip"></slot>
    `}}y(Go);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ko=[De,Rs];/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Yo=s=>class extends Ne(Ce(we(s))){static get properties(){return{value:{type:Array,value:()=>[],notify:!0,sync:!0,observer:"__valueChanged"},readonly:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"__readonlyChanged"}}}constructor(){super(),this.__registerCheckbox=this.__registerCheckbox.bind(this),this.__unregisterCheckbox=this.__unregisterCheckbox.bind(this),this.__onCheckboxCheckedChanged=this.__onCheckboxCheckedChanged.bind(this),this._tooltipController=new Q(this),this._tooltipController.addEventListener("tooltip-changed",e=>{const t=e.detail.node;if(t&&t.isConnected){const n=this.__checkboxes.map(r=>r.inputElement);this._tooltipController.setAriaTarget(n)}else this._tooltipController.setAriaTarget([])})}get __checkboxes(){return this.__filterCheckboxes([...this.children])}ready(){super.ready(),this.ariaTarget=this,this.setAttribute("role","group");const e=this.shadowRoot.querySelector("slot:not([name])");this._observer=new te(e,({addedNodes:t,removedNodes:n})=>{const r=this.__filterCheckboxes(t),o=this.__filterCheckboxes(n);r.forEach(this.__registerCheckbox),o.forEach(this.__unregisterCheckbox);const a=this.__checkboxes.map(l=>l.inputElement);this._tooltipController.setAriaTarget(a),this.__warnOfCheckboxesWithoutValue(r)}),this.addController(this._tooltipController)}checkValidity(){return!this.required||!!(this.value&&this.value.length>0)}__filterCheckboxes(e){return e.filter(t=>t.nodeType===Node.ELEMENT_NODE&&t.localName==="vaadin-checkbox")}__warnOfCheckboxesWithoutValue(e){e.some(n=>{const{value:r}=n;return!n.hasAttribute("value")&&(!r||r==="on")})&&console.warn("Please provide the value attribute to all the checkboxes inside the checkbox group.")}__registerCheckbox(e){e.addEventListener("checked-changed",this.__onCheckboxCheckedChanged),this.disabled&&(e.disabled=!0),this.readonly&&(e.readonly=!0),e.checked?this.__addCheckboxToValue(e.value):this.value&&this.value.includes(e.value)&&(e.checked=!0)}__unregisterCheckbox(e){e.removeEventListener("checked-changed",this.__onCheckboxCheckedChanged),e.checked&&this.__removeCheckboxFromValue(e.value)}_disabledChanged(e,t){super._disabledChanged(e,t),!(!e&&t===void 0)&&t!==e&&this.__checkboxes.forEach(n=>{n.disabled=e})}__addCheckboxToValue(e){this.value?this.value.includes(e)||(this.value=[...this.value,e]):this.value=[e]}__removeCheckboxFromValue(e){this.value&&this.value.includes(e)&&(this.value=this.value.filter(t=>t!==e))}__onCheckboxCheckedChanged(e){const t=e.target;t.checked?this.__addCheckboxToValue(t.value):this.__removeCheckboxFromValue(t.value)}__valueChanged(e,t){e&&e.length===0&&t===void 0||(this.toggleAttribute("has-value",e&&e.length>0),this.__checkboxes.forEach(n=>{n.checked=e&&e.includes(n.value)}),t!==void 0&&this._requestValidation())}__readonlyChanged(e,t){(e||t)&&this.__checkboxes.forEach(n=>{n.readonly=e})}_shouldRemoveFocus(e){return!this.contains(e.relatedTarget)}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}};/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Xo extends Yo(z(S(x(k(w))))){static get is(){return"vaadin-checkbox-group"}static get styles(){return Ko}render(){return C`
      <div class="vaadin-group-field-container">
        <div part="label">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true"></span>
        </div>

        <div part="group-field">
          <slot></slot>
        </div>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>
      </div>

      <slot name="tooltip"></slot>
    `}}y(Xo);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Zo=v`
  :host {
    display: block;
    width: 100%; /* prevent collapsing inside non-stretching column flex */
    height: var(--vaadin-progress-bar-height, 0.5lh);
    contain: layout size;
  }

  :host([hidden]) {
    display: none !important;
  }

  [part='bar'] {
    box-sizing: border-box;
    height: 100%;
    --_padding: var(--vaadin-progress-bar-padding, 0px);
    padding: var(--_padding);
    background: var(--vaadin-progress-bar-background, var(--vaadin-background-container));
    border-radius: var(--vaadin-progress-bar-border-radius, var(--vaadin-radius-m));
    border: var(--vaadin-progress-bar-border-width, 1px) solid
      var(--vaadin-progress-bar-border-color, var(--vaadin-border-color-secondary));
  }

  [part='value'] {
    box-sizing: border-box;
    height: 100%;
    width: calc(var(--vaadin-progress-value) * 100%);
    background: var(--vaadin-progress-bar-value-background, var(--vaadin-border-color));
    border-radius: calc(
      var(--vaadin-progress-bar-border-radius, var(--vaadin-radius-m)) - var(
          --vaadin-progress-bar-border-width,
          1px
        ) - var(--_padding)
    );
    transition: width 150ms;
  }

  /* Indeterminate progress */
  :host([indeterminate]) [part='value'] {
    --_w-min: clamp(8px, 5%, 16px);
    --_w-max: clamp(16px, 20%, 128px);
    animation: indeterminate var(--vaadin-progress-bar-animation-duration, 1s) linear infinite alternate;
    width: var(--_w-min);
  }

  :host([indeterminate][aria-valuenow]) [part='value'] {
    animation-delay: 150ms;
  }

  @keyframes indeterminate {
    0% {
      animation-timing-function: ease-in;
    }

    20% {
      margin-inline-start: 0%;
      width: var(--_w-max);
    }

    50% {
      margin-inline-start: calc(50% - var(--_w-max) / 2);
    }

    80% {
      width: var(--_w-max);
      margin-inline-start: calc(100% - var(--_w-max));
      animation-timing-function: ease-out;
    }

    100% {
      width: var(--_w-min);
      margin-inline-start: calc(100% - var(--_w-min));
    }
  }

  @keyframes indeterminate-reduced {
    100% {
      opacity: 0.2;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    [part='value'] {
      transition: none;
    }

    :host([indeterminate]) [part='value'] {
      width: 25%;
      animation: indeterminate-reduced 2s linear infinite alternate;
    }
  }

  @media (forced-colors: active) {
    [part='bar'] {
      border-width: max(1px, var(--vaadin-progress-bar-border-width));
    }

    [part='value'] {
      background: CanvasText !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Qo=s=>class extends s{static get properties(){return{value:{type:Number,observer:"_valueChanged"},min:{type:Number,value:0,observer:"_minChanged"},max:{type:Number,value:1,observer:"_maxChanged"},indeterminate:{type:Boolean,value:!1,reflectToAttribute:!0}}}static get observers(){return["_normalizedValueChanged(value, min, max)"]}ready(){super.ready(),this.setAttribute("role","progressbar")}_normalizedValueChanged(e,t,n){const r=this._normalizeValue(e,t,n);this.style.setProperty("--vaadin-progress-value",r)}_valueChanged(e){this.setAttribute("aria-valuenow",e)}_minChanged(e){this.setAttribute("aria-valuemin",e)}_maxChanged(e){this.setAttribute("aria-valuemax",e)}_normalizeValue(e,t,n){let r;return!e&&e!==0?r=0:t>=n?r=1:(r=(e-t)/(n-t),r=Math.min(Math.max(r,0),1)),r}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Jo extends Qo(z(S(x(k(w))))){static get is(){return"vaadin-progress-bar"}static get styles(){return Zo}render(){return C`
      <div part="bar">
        <div part="value"></div>
      </div>
    `}}y(Jo);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function ye(s){return s.__cells||Array.from(s.querySelectorAll('[part~="cell"]:not([part~="details-cell"])'))}function D(s,i){[...s.children].forEach(i)}function Pe(s,i){ye(s).forEach(i),s.__detailsCell&&i(s.__detailsCell)}function Os(s,i,e){let t=1;s.forEach(n=>{t%10===0&&(t+=1),n._order=e+t*i,t+=1})}function pt(s,i,e){switch(typeof e){case"boolean":s.toggleAttribute(i,e);break;case"string":s.setAttribute(i,e);break;default:s.removeAttribute(i);break}}function O(s,i,e){s.classList.toggle(i,e||e===""),s.part.toggle(i,e||e===""),s.part.length===0&&s.removeAttribute("part")}function tt(s,i,e){s.forEach(t=>{O(t,i,e)})}function _e(s,i){const e=ye(s);Object.entries(i).forEach(([t,n])=>{pt(s,t,n);const r=`${t}-row`;O(s,r,n),tt(e,`${r}-cell`,n)})}function Ei(s,i){const e=ye(s);Object.entries(i).forEach(([t,n])=>{const r=s.getAttribute(t);if(pt(s,t,n),r){const o=`${t}-${r}-row`;O(s,o,!1),tt(e,`${o}-cell`,!1)}if(n){const o=`${t}-${n}-row`;O(s,o,n),tt(e,`${o}-cell`,n)}})}function oe(s,i,e,t,n){pt(s,i,e),n&&O(s,n,!1),O(s,t||`${i}-cell`,e)}function ea(s){return ye(s).find(i=>i._content.querySelector("vaadin-grid-tree-toggle"))}class se{constructor(i,e){this.__host=i,this.__callback=e,this.__currentSlots=[],this.__onMutation=this.__onMutation.bind(this),this.__observer=new MutationObserver(this.__onMutation),this.__observer.observe(i,{childList:!0}),this.__initialCallDebouncer=I.debounce(this.__initialCallDebouncer,W,()=>this.__onMutation())}disconnect(){this.__observer.disconnect(),this.__initialCallDebouncer.cancel(),this.__toggleSlotChangeListeners(!1)}flush(){this.__onMutation()}__toggleSlotChangeListeners(i){this.__currentSlots.forEach(e=>{i?e.addEventListener("slotchange",this.__onMutation):e.removeEventListener("slotchange",this.__onMutation)})}__onMutation(){const i=!this.__currentColumns;this.__currentColumns=this.__currentColumns||[];const e=se.getColumns(this.__host),t=e.filter(a=>!this.__currentColumns.includes(a)),n=this.__currentColumns.filter(a=>!e.includes(a)),r=this.__currentColumns.some((a,l)=>a!==e[l]);this.__currentColumns=e,this.__toggleSlotChangeListeners(!1),this.__currentSlots=[...this.__host.children].filter(a=>a instanceof HTMLSlotElement),this.__toggleSlotChangeListeners(!0),(i||t.length||n.length||r)&&this.__callback(t,n)}static __isColumnElement(i){return i.nodeType===Node.ELEMENT_NODE&&/\bcolumn\b/u.test(i.localName)}static getColumns(i){const e=[],t=i._isColumnElement||se.__isColumnElement;return[...i.children].forEach(n=>{t(n)?e.push(n):n instanceof HTMLSlotElement&&[...n.assignedElements({flatten:!0})].filter(r=>t(r)).forEach(r=>e.push(r))}),e}}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ls=s=>class extends s{static get properties(){return{resizable:{type:Boolean,sync:!0,value(){if(this.localName==="vaadin-grid-column-group")return;const e=this.parentNode;return e&&e.localName==="vaadin-grid-column-group"&&e.resizable||!1}},frozen:{type:Boolean,value:!1,sync:!0},frozenToEnd:{type:Boolean,value:!1,sync:!0},rowHeader:{type:Boolean,value:!1,sync:!0},hidden:{type:Boolean,value:!1,sync:!0},header:{type:String,sync:!0},textAlign:{type:String,sync:!0},headerPartName:{type:String,sync:!0},footerPartName:{type:String,sync:!0},_lastFrozen:{type:Boolean,value:!1,sync:!0},_bodyContentHidden:{type:Boolean,value:!1,sync:!0},_firstFrozenToEnd:{type:Boolean,value:!1,sync:!0},_order:{type:Number,sync:!0},_reorderStatus:{type:Boolean,sync:!0},_emptyCells:Array,_headerCell:{type:Object,sync:!0},_footerCell:{type:Object,sync:!0},_grid:Object,__initialized:{type:Boolean,value:!0},headerRenderer:{type:Function,sync:!0},_headerRenderer:{type:Function,computed:"_computeHeaderRenderer(headerRenderer, header, __initialized)"},footerRenderer:{type:Function,sync:!0},_footerRenderer:{type:Function,computed:"_computeFooterRenderer(footerRenderer, __initialized)"},__gridColumnElement:{type:Boolean,value:!0}}}static get observers(){return["_widthChanged(width, _headerCell, _footerCell, _cells)","_frozenChanged(frozen, _headerCell, _footerCell, _cells)","_frozenToEndChanged(frozenToEnd, _headerCell, _footerCell, _cells)","_flexGrowChanged(flexGrow, _headerCell, _footerCell, _cells)","_textAlignChanged(textAlign, _cells, _headerCell, _footerCell)","_orderChanged(_order, _headerCell, _footerCell, _cells)","_lastFrozenChanged(_lastFrozen)","_firstFrozenToEndChanged(_firstFrozenToEnd)","_onRendererOrBindingChanged(_renderer, _cells, _bodyContentHidden, path)","_onHeaderRendererOrBindingChanged(_headerRenderer, _headerCell, path, header)","_onFooterRendererOrBindingChanged(_footerRenderer, _footerCell)","_resizableChanged(resizable, _headerCell)","_reorderStatusChanged(_reorderStatus, _headerCell, _footerCell, _cells)","_hiddenChanged(hidden, _headerCell, _footerCell, _cells)","_rowHeaderChanged(rowHeader, _cells)","__headerFooterPartNameChanged(_headerCell, _footerCell, headerPartName, footerPartName)"]}get _grid(){return this._gridValue||(this._gridValue=this._findHostGrid()),this._gridValue}get _allCells(){return[].concat(this._cells||[]).concat(this._emptyCells||[]).concat(this._headerCell).concat(this._footerCell).filter(e=>e)}connectedCallback(){super.connectedCallback(),requestAnimationFrame(()=>{this._grid&&this._allCells.forEach(e=>{e._content.parentNode||this._grid.appendChild(e._content)})})}disconnectedCallback(){super.disconnectedCallback(),requestAnimationFrame(()=>{this._grid||this._allCells.forEach(e=>{e._content.parentNode&&e._content.parentNode.removeChild(e._content)})}),this._gridValue=void 0}_findHostGrid(){let e=this;for(;e&&!/^vaadin.*grid(-pro)?$/u.test(e.localName);)e=e.assignedSlot?e.assignedSlot.parentNode:e.parentNode;return e||void 0}_renderHeaderAndFooter(){this._renderHeaderCellContent(this._headerRenderer,this._headerCell),this._renderFooterCellContent(this._footerRenderer,this._footerCell)}_flexGrowChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("flexGrow"),this._allCells.forEach(t=>{t.style.flexGrow=e})}_orderChanged(e){this._allCells.forEach(t=>{t.style.order=e})}_widthChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("width"),this._allCells.forEach(t=>{t.style.width=e})}_frozenChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("frozen",e),this._allCells.forEach(t=>{oe(t,"frozen",e)}),this._grid&&this._grid._frozenCellsChanged&&this._grid._frozenCellsChanged()}_frozenToEndChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("frozenToEnd",e),this._allCells.forEach(t=>{this._grid&&t.parentElement===this._grid.$.sizer||oe(t,"frozen-to-end",e)}),this._grid&&this._grid._frozenCellsChanged&&this._grid._frozenCellsChanged()}_lastFrozenChanged(e){this._allCells.forEach(t=>{oe(t,"last-frozen",e)}),this.parentElement&&this.parentElement._columnPropChanged&&(this.parentElement._lastFrozen=e)}_firstFrozenToEndChanged(e){this._allCells.forEach(t=>{this._grid&&t.parentElement===this._grid.$.sizer||oe(t,"first-frozen-to-end",e)}),this.parentElement&&this.parentElement._columnPropChanged&&(this.parentElement._firstFrozenToEnd=e)}_rowHeaderChanged(e,t){t&&t.forEach(n=>{n.setAttribute("role",e?"rowheader":"gridcell")})}_generateHeader(e){return e.substr(e.lastIndexOf(".")+1).replace(/([A-Z])/gu,"-$1").toLowerCase().replace(/-/gu," ").replace(/^./u,t=>t.toUpperCase())}_reorderStatusChanged(e){const t=this.__previousReorderStatus,n=t?`reorder-${t}-cell`:"",r=`reorder-${e}-cell`;this._allCells.forEach(o=>{oe(o,"reorder-status",e,r,n)}),this.__previousReorderStatus=e}_resizableChanged(e,t){e===void 0||t===void 0||t&&[t].concat(this._emptyCells).forEach(n=>{if(n){const r=n.querySelector('[part~="resize-handle"]');if(r&&n.removeChild(r),e){const o=document.createElement("div");O(o,"resize-handle",!0),n.appendChild(o)}}})}_textAlignChanged(e){if(!(e===void 0||this._grid===void 0)){if(["start","end","center"].indexOf(e)===-1){console.warn('textAlign can only be set as "start", "end" or "center"');return}this._allCells.forEach(t=>{t._content.style.textAlign=e})}}_hiddenChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("hidden",e),!!e!=!!this._previousHidden&&this._grid&&(e===!0&&this._allCells.forEach(t=>{t._content.parentNode&&t._content.parentNode.removeChild(t._content)}),this._grid._debouncerHiddenChanged=I.debounce(this._grid._debouncerHiddenChanged,X,()=>{this._grid&&this._grid._renderColumnTree&&this._grid._renderColumnTree(this._grid._columnTree)}),this._grid._debounceUpdateFrozenColumn&&this._grid._debounceUpdateFrozenColumn(),this._grid._resetKeyboardNavigation&&this._grid._resetKeyboardNavigation()),this._previousHidden=e}_runRenderer(e,t,n){const r=n&&n.item&&!t.parentElement.hidden;if(!(r||e===this._headerRenderer||e===this._footerRenderer))return;const a=[t._content,this];r&&a.push(n),e.apply(this,a)}__renderCellsContent(e,t){this.hidden||!this._grid||t.forEach(n=>{if(!n.parentElement)return;const r=this._grid.__getRowModel(n.parentElement);e&&(n._renderer!==e&&this._clearCellContent(n),n._renderer=e,this._runRenderer(e,n,r))})}_clearCellContent(e){e._content.innerHTML="",delete e._content._$litPart$}_renderHeaderCellContent(e,t){!t||!e||(this.__renderCellsContent(e,[t]),this._grid&&t.parentElement&&this._grid.__debounceUpdateHeaderFooterRowVisibility(t.parentElement))}_onHeaderRendererOrBindingChanged(e,t,...n){this._renderHeaderCellContent(e,t)}__headerFooterPartNameChanged(e,t,n,r){[{cell:e,partName:n},{cell:t,partName:r}].forEach(({cell:o,partName:a})=>{if(o){const l=o.__customParts||[];o.part.remove(...l),o.__customParts=a?a.trim().split(" "):[],o.part.add(...o.__customParts)}})}_renderBodyCellsContent(e,t){!t||!e||this.__renderCellsContent(e,t)}_onRendererOrBindingChanged(e,t,...n){this._renderBodyCellsContent(e,t)}_renderFooterCellContent(e,t){!t||!e||(this.__renderCellsContent(e,[t]),this._grid&&t.parentElement&&this._grid.__debounceUpdateHeaderFooterRowVisibility(t.parentElement))}_onFooterRendererOrBindingChanged(e,t){this._renderFooterCellContent(e,t)}__setTextContent(e,t){e.textContent!==t&&(e.textContent=t)}__textHeaderRenderer(){this.__setTextContent(this._headerCell._content,this.header)}_defaultHeaderRenderer(){this.path&&this.__setTextContent(this._headerCell._content,this._generateHeader(this.path))}_defaultRenderer(e,t,{item:n}){this.path&&this.__setTextContent(e,Ke(this.path,n))}_defaultFooterRenderer(){}_computeHeaderRenderer(e,t){return e||(t!=null?this.__textHeaderRenderer:this._defaultHeaderRenderer)}_computeRenderer(e){return e||this._defaultRenderer}_computeFooterRenderer(e){return e||this._defaultFooterRenderer}},ta=s=>class extends Ls(N(s)){static get properties(){return{width:{type:String,value:"100px",sync:!0},flexGrow:{type:Number,value:1,sync:!0},renderer:{type:Function,sync:!0},_renderer:{type:Function,computed:"_computeRenderer(renderer, __initialized)"},path:{type:String,sync:!0},autoWidth:{type:Boolean,value:!1},_focusButtonMode:{type:Boolean,value:!1},_cells:{type:Array,sync:!0}}}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ps extends ta(x(w)){static get is(){return"vaadin-grid-column"}}y(Ps);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ia=v`
  /* stylelint-disable no-duplicate-selectors */
  :host {
    display: flex;
    max-width: 100%;
    height: 400px;
    min-height: var(--_grid-min-height, 0);
    flex: 1 1 auto;
    align-self: stretch;
    position: relative;
    box-sizing: border-box;
    overflow: hidden;
    -webkit-tap-highlight-color: transparent;
    background: var(--vaadin-grid-background, var(--vaadin-background-color));
    border: var(--vaadin-grid-border-width, 1px) solid var(--_border-color);
    cursor: default;
    --_border-color: var(--vaadin-grid-border-color, var(--vaadin-border-color-secondary));
    --_row-border-width: var(--vaadin-grid-row-border-width, 1px);
    --_column-border-width: var(--vaadin-grid-column-border-width, 0px);
    --_default-cell-padding: var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container);
    border-radius: var(--vaadin-grid-border-radius, var(--vaadin-radius-m));
  }

  :host([hidden]),
  [hidden] {
    display: none !important;
  }

  :host([disabled]) {
    pointer-events: none;
    opacity: 0.7;
  }

  /* Variant: No outer border */
  :host([theme~='no-border']) {
    border-width: 0;
    border-radius: 0;
  }

  :host([all-rows-visible]) {
    height: auto;
    align-self: flex-start;
    min-height: auto;
    flex-grow: 0;
    flex-shrink: 0;
    width: 100%;
  }

  #scroller {
    contain: layout;
    position: relative;
    display: flex;
    width: 100%;
    min-width: 0;
    min-height: 0;
    align-self: stretch;
    overflow: hidden;
  }

  #items {
    flex-grow: 1;
    flex-shrink: 0;
    display: block;
    position: sticky;
    width: 100%;
    left: 0;
    min-height: 1px;
    z-index: 1;
  }

  #table {
    display: flex;
    flex-direction: column;
    width: 100%;
    overflow: auto;
    position: relative;
    border-radius: inherit;
    /* Workaround for a Chrome bug: new stacking context here prevents the scrollbar from getting hidden */
    z-index: 0;
  }

  [no-scrollbars]:is([safari], [firefox]) #table {
    overflow: hidden;
  }

  #header,
  #footer {
    display: block;
    position: sticky;
    left: 0;
    width: 100%;
    z-index: 2;
  }

  :host([dir='rtl']) #items,
  :host([dir='rtl']) #header,
  :host([dir='rtl']) #footer {
    left: auto;
  }

  #header {
    top: 0;
  }

  #footer {
    bottom: 0;
  }

  th {
    text-align: inherit;
  }

  #header th,
  .reorder-ghost {
    font-size: var(--vaadin-grid-header-font-size, 1em);
    font-weight: var(--vaadin-grid-header-font-weight, 500);
    color: var(--vaadin-grid-header-text-color, var(--vaadin-text-color));
  }

  .row {
    display: flex;
    width: 100%;
    box-sizing: border-box;
    margin: 0;
    position: relative;
  }

  .row:not(:focus-within) {
    --_non-focused-row-none: none;
  }

  .body-row[loading] .body-cell ::slotted(vaadin-grid-cell-content) {
    visibility: hidden;
  }

  [column-rendering='lazy'] .body-cell:not([frozen]):not([frozen-to-end]) {
    transform: translateX(var(--_grid-lazy-columns-start));
  }

  #items .row:empty {
    height: 100%;
  }

  .cell {
    padding: 0;
    box-sizing: border-box;
  }

  .cell:where(:not(.details-cell)) {
    flex-shrink: 0;
    flex-grow: 1;
    display: flex;
    width: 100%;
    position: relative;
    align-items: center;
    white-space: nowrap;
  }

  /*
    Block borders

    ::after - row and cell focus outline
    ::before - header bottom and footer top borders that only appear when scrolling
  */

  .row::after {
    top: 0;
    bottom: calc(var(--_row-border-width) * -1);
  }

  .body-row {
    scroll-margin-bottom: var(--_row-border-width);
  }

  .cell {
    border-block: var(--_row-border-width) var(--_border-color);
    border-top-style: solid;
  }

  .cell::after {
    top: calc(var(--_row-border-width) * -1);
    bottom: calc(var(--_row-border-width) * -1);
  }

  /* Block borders / Last header row and first footer row */

  .last-header-row::before,
  .first-footer-row::before {
    position: absolute;
    inset-inline: 0;
    border-block: var(--_row-border-width) var(--_border-color);
    transform: translateX(var(--_grid-horizontal-scroll-position));
  }

  /* Block borders / First header row */

  .first-header-row-cell {
    border-top-style: none;
  }

  .first-header-row-cell::after {
    top: 0;
  }

  /* Block borders / Last header row */

  :host([overflow~='top']) .last-header-row::before {
    content: '';
    bottom: calc(var(--_row-border-width) * -1);
    border-bottom-style: solid;
  }

  /* Block borders / First body row */

  #table:not([has-header]) .first-row-cell {
    border-top-style: none;
  }

  #table:not([has-header]) .first-row-cell::after {
    top: 0;
  }

  /* Block borders / Last body row */

  .last-row::after {
    bottom: 0;
  }

  .last-row .details-cell,
  .last-row-cell:not(.details-opened-row-cell) {
    border-bottom-style: solid;
  }

  /* Block borders / Last body row without footer */

  :host([all-rows-visible]),
  :host([overflow~='top']),
  :host([overflow~='bottom']) {
    #table:not([has-footer]) .last-row .details-cell,
    #table:not([has-footer]) .last-row-cell:not(.details-opened-row-cell) {
      border-bottom-style: none;

      &::after {
        bottom: 0;
      }
    }
  }

  /* Block borders / First footer row */

  .first-footer-row::after {
    top: calc(var(--_row-border-width) * -1);
  }

  .first-footer-row-cell {
    border-top-style: none;
  }

  :host([overflow~='bottom']),
  :host(:not([overflow~='top']):not([all-rows-visible])) #scroller:not([empty-state]) {
    .first-footer-row::before {
      content: '';
      top: calc(var(--_row-border-width) * -1);
      border-top-style: solid;
    }
  }

  /* Block borders / Last footer row */

  .last-footer-row::after,
  .last-footer-row-cell::after {
    bottom: 0;
  }

  /* Inline borders */

  .cell {
    border-inline: var(--_column-border-width) var(--_border-color);
  }

  .header-cell:not(.first-column-cell),
  .footer-cell:not(.first-column-cell),
  .body-cell:not(.first-column-cell) {
    border-inline-start-style: solid;
  }

  .last-frozen-cell:not(.last-column-cell) {
    border-inline-end-style: solid;

    & + .cell {
      border-inline-start-style: none;
    }
  }

  /* Row and cell background */

  .row {
    background-color: var(--vaadin-grid-row-background-color, var(--vaadin-background-color));
  }

  .cell {
    --_cell-background-image: linear-gradient(
      var(--vaadin-grid-cell-background-color, transparent),
      var(--vaadin-grid-cell-background-color, transparent)
    );

    background-color: inherit;
    background-repeat: no-repeat;
    background-origin: padding-box;
    background-image: var(--_cell-background-image);
  }

  .body-cell {
    --_cell-highlight-background-image: linear-gradient(
      var(--vaadin-grid-row-highlight-background-color, transparent),
      var(--vaadin-grid-row-highlight-background-color, transparent)
    );

    background-image:
      var(--_row-hover-background-image, none), var(--_row-selected-background-image, none),
      var(--_cell-highlight-background-image, none), var(--_row-odd-background-image, none),
      var(--_cell-background-image, none);
  }

  .selected-row {
    --_row-selected-background-color: var(
      --vaadin-grid-row-selected-background-color,
      color-mix(in srgb, currentColor 8%, transparent)
    );
    --_row-selected-background-image: linear-gradient(
      var(--_row-selected-background-color),
      var(--_row-selected-background-color)
    );
  }

  @media (any-hover: hover) {
    .body-row:hover {
      --_row-hover-background-color: var(--vaadin-grid-row-hover-background-color, transparent);
      --_row-hover-background-image: linear-gradient(
        var(--_row-hover-background-color),
        var(--_row-hover-background-color)
      );
    }
  }

  :host([theme~='row-stripes']) .odd-row {
    --_row-odd-background-color: var(
      --vaadin-grid-row-odd-background-color,
      color-mix(in srgb, var(--vaadin-text-color) 4%, transparent)
    );
    --_row-odd-background-image: linear-gradient(var(--_row-odd-background-color), var(--_row-odd-background-color));
  }

  /* Variant: wrap cell contents */

  :host([theme~='wrap-cell-content']) .cell:not(.details-cell) {
    white-space: normal;
  }

  /* Raise highlighted rows above others */
  .row,
  .frozen-cell,
  .frozen-to-end-cell {
    &:focus,
    &:focus-within {
      z-index: 3;
    }
  }

  .details-cell {
    position: absolute;
    bottom: 0;
    width: 100%;
  }

  .cell ::slotted(vaadin-grid-cell-content) {
    display: block;
    overflow: hidden;
    text-overflow: var(--vaadin-grid-cell-text-overflow, ellipsis);
    padding: var(--vaadin-grid-cell-padding, var(--_default-cell-padding));
    flex: 1;
    min-height: 1lh;
    min-width: 0;
  }

  [frozen],
  [frozen-to-end] {
    z-index: 2;
  }

  /* Empty state */
  #scroller:not([empty-state]) #emptystatebody,
  #scroller[empty-state] #items {
    display: none;
  }

  #emptystatebody {
    display: flex;
    position: sticky;
    inset: 0;
    flex: 1;
    overflow: hidden;
  }

  #emptystaterow {
    display: flex;
    flex: 1;
  }

  #emptystatecell {
    display: block;
    flex: 1;
    overflow: auto;
    padding: var(--vaadin-grid-cell-padding, var(--_default-cell-padding));
    outline: none;
    border-block: var(--_row-border-width) var(--_border-color);
  }

  #table[has-header] #emptystatecell {
    border-top-style: solid;
  }

  #table[has-footer] #emptystatecell {
    border-bottom-style: solid;
  }

  #emptystatecell:focus-visible {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--vaadin-focus-ring-width) * -1);
  }

  /* Reordering styles */
  :host([reordering]) .cell ::slotted(vaadin-grid-cell-content),
  :host([reordering]) .resize-handle,
  #scroller[no-content-pointer-events] .cell ::slotted(vaadin-grid-cell-content) {
    pointer-events: none;
  }

  .reorder-ghost {
    visibility: hidden;
    position: fixed;
    pointer-events: none;
    box-shadow:
      0 0 0 1px hsla(0deg, 0%, 0%, 0.2),
      0 8px 24px -2px hsla(0deg, 0%, 0%, 0.2);
    padding: var(--vaadin-grid-cell-padding, var(--_default-cell-padding)) !important;
    border-radius: 3px;

    /* Prevent overflowing the grid in Firefox */
    top: 0;
    inset-inline-start: 0;
  }

  :host([reordering]) {
    -webkit-user-select: none;
    user-select: none;
  }

  :host([reordering]) .cell {
    /* TODO expose a custom property to control this */
    --_reorder-curtain-filter: brightness(0.9) contrast(1.1);
  }

  :host([reordering]) .cell::after {
    content: '';
    position: absolute;
    inset: 0;
    z-index: 1;
    -webkit-backdrop-filter: var(--_reorder-curtain-filter);
    backdrop-filter: var(--_reorder-curtain-filter);
    outline: 0;
  }

  :host([reordering]) .cell[reorder-status='allowed'] {
    /* TODO expose a custom property to control this */
    --_reorder-curtain-filter: brightness(0.94) contrast(1.07);
  }

  :host([reordering]) .cell[reorder-status='dragging'] {
    --_reorder-curtain-filter: none;
  }

  /* Resizing styles */
  .resize-handle {
    position: absolute;
    top: 0;
    inset-inline-end: 0;
    height: 100%;
    cursor: col-resize;
    z-index: 1;
    opacity: 0;
    width: var(--vaadin-focus-ring-width);
    background: var(--vaadin-grid-column-resize-handle-color, var(--vaadin-focus-ring-color));
    transition: opacity 0.2s;
    translate: var(--_column-border-width);
  }

  .last-column-cell .resize-handle {
    translate: 0;
  }

  :host(:not([reordering])) *:not([column-resizing]) .resize-handle:hover,
  .resize-handle:active {
    opacity: 1;
    transition-delay: 0.15s;
  }

  .resize-handle::before {
    position: absolute;
    content: '';
    height: 100%;
    width: 16px;
    translate: calc(-50% + var(--vaadin-focus-ring-width) / 2);
  }

  :host([dir='rtl']) .resize-handle::before {
    translate: calc(50% - var(--vaadin-focus-ring-width) / 2);
  }

  [first-frozen-to-end] .resize-handle::before,
  :is([last-column], [last-frozen]) .resize-handle::before {
    width: 8px;
    translate: 0;
  }

  :is([last-column], [last-frozen]) .resize-handle::before {
    inset-inline-end: 0;
  }

  [frozen-to-end] :is(.resize-handle, .resize-handle::before) {
    inset-inline: 0 auto;
  }

  [frozen-to-end] .resize-handle {
    translate: calc(var(--_column-border-width) * -1);
  }

  [first-frozen-to-end] {
    margin-inline-start: auto;
  }

  #scroller:is([column-resizing], [range-selecting]) {
    -webkit-user-select: none;
    user-select: none;
  }

  /* Focus outline element, also used for d'n'd indication */
  :is(.row, .cell)::after {
    position: absolute;
    z-index: 3;
    inset-inline: 0;
    pointer-events: none;
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--vaadin-focus-ring-width) * -1);
  }

  .row::after {
    transform: translateX(var(--_grid-horizontal-scroll-position));
  }

  .cell:where(:not(.details-cell))::after {
    inset-inline: calc(var(--_column-border-width) * -1);
  }

  .first-column-cell::after {
    inset-inline-start: 0;
  }

  .last-column-cell::after {
    inset-inline-end: 0;
  }

  :host([navigating]) .row:focus,
  :host([navigating]) .cell:focus {
    outline: 0;
  }

  .row:focus-visible,
  .cell:focus-visible {
    outline: 0;
  }

  .row:focus-visible::after,
  .cell:focus-visible::after,
  :host([navigating]) .row:focus::after,
  :host([navigating]) .cell:focus::after {
    content: '';
  }

  /* Drag'n'drop styles */
  :host([dragover]) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--vaadin-grid-border-width, 1px) * -1);
  }

  .row[dragover] {
    z-index: 100 !important;
  }

  .row[dragover]::after {
    content: '';
  }

  .row[dragover='above']::after {
    outline: 0;
    border-top: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
  }

  .row:not(.first-row)[dragover='above']::after {
    top: calc(var(--vaadin-focus-ring-width) / -2);
  }

  .row[dragover='below']::after {
    outline: 0;
    border-bottom: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
  }

  .row:not(.last-row)[dragover='below']::after {
    bottom: calc(var(--vaadin-focus-ring-width) / -2);
  }

  .row[dragstart] .cell {
    border-block: none !important;
    padding-block: var(--_row-border-width) !important;
  }

  .row[dragstart] .cell[last-column] {
    border-radius: 0 3px 3px 0;
  }

  .row[dragstart] .cell[first-column] {
    border-radius: 3px 0 0 3px;
  }

  /* Indicates the number of dragged rows */
  /* TODO export custom properties to control styles */
  #scroller .row[dragstart]:not([dragstart=''])::before {
    position: absolute;
    left: var(--_grid-drag-start-x);
    top: var(--_grid-drag-start-y);
    z-index: 100;
    content: attr(dragstart);
    box-sizing: border-box;
    padding: 0.3em;
    color: white;
    background-color: red;
    border-radius: 1em;
    font-size: 0.75rem;
    line-height: 1;
    font-weight: 500;
    min-width: 1.6em;
    text-align: center;
  }

  /* Sizer styles */
  #sizer {
    display: flex;
    visibility: hidden;
  }

  #sizer .details-cell,
  #sizer .cell ::slotted(vaadin-grid-cell-content) {
    display: none !important;
  }

  #sizer .cell {
    display: block;
    flex-shrink: 0;
    line-height: 0;
    height: 0 !important;
    min-height: 0 !important;
    max-height: 0 !important;
    padding: 0 !important;
    border: none !important;
  }

  #sizer .cell::before {
    content: '-';
  }
`;/**
 * @license
 * Copyright (c) 2016 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
 */const Si=navigator.userAgent.match(/iP(?:hone|ad;(?: U;)? CPU) OS (\d+)/u),sa=Si&&Si[1]>=8,Ii=3,na={_ratio:.5,_scrollerPaddingTop:0,_scrollPosition:0,_physicalSize:0,_physicalAverage:0,_physicalAverageCount:0,_physicalTop:0,_virtualCount:0,_estScrollHeight:0,_scrollHeight:0,_viewportHeight:0,_viewportWidth:0,_physicalItems:null,_physicalSizes:null,_firstVisibleIndexVal:null,_lastVisibleIndexVal:null,_maxPages:2,_templateCost:0,get _physicalBottom(){return this._physicalTop+this._physicalSize},get _scrollBottom(){return this._scrollPosition+this._viewportHeight},get _virtualEnd(){return this._virtualStart+this._physicalCount-1},get _hiddenContentSize(){return this._physicalSize-this._viewportHeight},get _maxScrollTop(){return this._estScrollHeight-this._viewportHeight+this._scrollOffset},get _maxVirtualStart(){const s=this._virtualCount;return Math.max(0,s-this._physicalCount)},get _virtualStart(){return this._virtualStartVal||0},set _virtualStart(s){s=this._clamp(s,0,this._maxVirtualStart),this._virtualStartVal=s},get _physicalStart(){return this._physicalStartVal||0},set _physicalStart(s){s%=this._physicalCount,s<0&&(s=this._physicalCount+s),this._physicalStartVal=s},get _physicalEnd(){return(this._physicalStart+this._physicalCount-1)%this._physicalCount},get _physicalCount(){return this._physicalCountVal||0},set _physicalCount(s){this._physicalCountVal=s},get _optPhysicalSize(){return this._viewportHeight===0?1/0:this._viewportHeight*this._maxPages},get _isVisible(){return!!(this.offsetWidth||this.offsetHeight)},get firstVisibleIndex(){let s=this._firstVisibleIndexVal;if(s==null){let i=this._physicalTop+this._scrollOffset;s=this._iterateItems((e,t)=>{if(i+=this._getPhysicalSizeIncrement(e),i>this._scrollPosition)return t})||0,this._firstVisibleIndexVal=s}return s},get lastVisibleIndex(){let s=this._lastVisibleIndexVal;if(s==null){let i=this._physicalTop+this._scrollOffset;this._iterateItems((e,t)=>{i<this._scrollBottom&&(s=t),i+=this._getPhysicalSizeIncrement(e)}),this._lastVisibleIndexVal=s}return s},get _scrollOffset(){return this._scrollerPaddingTop+this.scrollOffset},_scrollHandler(){const s=Math.max(0,Math.min(this._maxScrollTop,this._scrollTop));let i=s-this._scrollPosition;const e=i>=0;if(this._scrollPosition=s,this._firstVisibleIndexVal=null,this._lastVisibleIndexVal=null,Math.abs(i)>this._physicalSize&&this._physicalSize>0){i-=this._scrollOffset;const t=Math.round(i/this._physicalAverage);this._virtualStart+=t,this._physicalStart+=t,this._physicalTop=Math.min(Math.floor(this._virtualStart)*this._physicalAverage,this._scrollPosition),this._update()}else if(this._physicalCount>0){const t=this._getReusables(e);e?(this._physicalTop=t.physicalTop,this._virtualStart+=t.indexes.length,this._physicalStart+=t.indexes.length):(this._virtualStart-=t.indexes.length,this._physicalStart-=t.indexes.length),this._update(t.indexes,e?null:t.indexes),this._debounce("_increasePoolIfNeeded",this._increasePoolIfNeeded.bind(this,0),W)}},_getReusables(s){let i,e,t;const n=[],r=this._hiddenContentSize*this._ratio,o=this._virtualStart,a=this._virtualEnd,l=this._physicalCount;let d=this._physicalTop+this._scrollOffset;const _=this._physicalBottom+this._scrollOffset,f=this._scrollPosition,g=this._scrollBottom;for(s?(i=this._physicalStart,e=f-d):(i=this._physicalEnd,e=_-g);t=this._getPhysicalSizeIncrement(i),e-=t,!(n.length>=l||e<=r);)if(s){if(a+n.length+1>=this._virtualCount||d+t>=f-this._scrollOffset)break;n.push(i),d+=t,i=(i+1)%l}else{if(o-n.length<=0||d+this._physicalSize-t<=g)break;n.push(i),d-=t,i=i===0?l-1:i-1}return{indexes:n,physicalTop:d-this._scrollOffset}},_update(s,i){if(!(s&&s.length===0||this._physicalCount===0)){if(this._assignModels(s),this._updateMetrics(s),i)for(;i.length;){const e=i.pop();this._physicalTop-=this._getPhysicalSizeIncrement(e)}this._positionItems(),this._updateScrollerSize()}},_isClientFull(){return this._scrollBottom!==0&&this._physicalBottom-1>=this._scrollBottom&&this._physicalTop<=this._scrollPosition},_increasePoolIfNeeded(s){const e=this._clamp(this._physicalCount+s,Ii,this._virtualCount-this._virtualStart)-this._physicalCount;let t=Math.round(this._physicalCount*.5);if(!(e<0)){if(e>0){const n=window.performance.now();[].push.apply(this._physicalItems,this._createPool(e));for(let r=0;r<e;r++)this._physicalSizes.push(0);this._physicalCount+=e,this._physicalStart>this._physicalEnd&&this._isIndexRendered(this._focusedVirtualIndex)&&this._getPhysicalIndex(this._focusedVirtualIndex)<this._physicalEnd&&(this._physicalStart+=e),this._update(),this._templateCost=(window.performance.now()-n)/e,t=Math.round(this._physicalCount*.5)}this._virtualEnd>=this._virtualCount-1||t===0||(this._isClientFull()?this._physicalSize<this._optPhysicalSize&&this._debounce("_increasePoolIfNeeded",this._increasePoolIfNeeded.bind(this,this._clamp(Math.round(50/this._templateCost),1,t)),$i):this._debounce("_increasePoolIfNeeded",this._increasePoolIfNeeded.bind(this,t),W))}},_render(){if(!(!this.isAttached||!this._isVisible))if(this._physicalCount!==0){const s=this._getReusables(!0);this._physicalTop=s.physicalTop,this._virtualStart+=s.indexes.length,this._physicalStart+=s.indexes.length,this._update(s.indexes),this._update(),this._increasePoolIfNeeded(0)}else this._virtualCount>0&&(this.updateViewportBoundaries(),this._increasePoolIfNeeded(Ii))},_itemsChanged(s){s.path==="items"&&(this._virtualStart=0,this._physicalTop=0,this._virtualCount=this.items?this.items.length:0,this._physicalIndexForKey={},this._firstVisibleIndexVal=null,this._lastVisibleIndexVal=null,this._physicalItems||(this._physicalItems=[]),this._physicalSizes||(this._physicalSizes=[]),this._physicalStart=0,this._scrollTop>this._scrollOffset&&this._resetScrollPosition(0),this._debounce("_render",this._render,X))},_iterateItems(s,i){let e,t,n,r;if(arguments.length===2&&i){for(r=0;r<i.length;r++)if(e=i[r],t=this._computeVidx(e),(n=s.call(this,e,t))!=null)return n}else{for(e=this._physicalStart,t=this._virtualStart;e<this._physicalCount;e++,t++)if((n=s.call(this,e,t))!=null)return n;for(e=0;e<this._physicalStart;e++,t++)if((n=s.call(this,e,t))!=null)return n}},_computeVidx(s){return s>=this._physicalStart?this._virtualStart+(s-this._physicalStart):this._virtualStart+(this._physicalCount-this._physicalStart)+s},_positionItems(){this._adjustScrollPosition();let s=this._physicalTop;this._iterateItems(i=>{this.translate3d(0,`${s}px`,0,this._physicalItems[i]),s+=this._physicalSizes[i]})},_getPhysicalSizeIncrement(s){return this._physicalSizes[s]},_adjustScrollPosition(){const s=this._virtualStart===0?this._physicalTop:Math.min(this._scrollPosition+this._physicalTop,0);if(s!==0){this._physicalTop-=s;const i=this._scrollPosition;!sa&&i>0&&this._resetScrollPosition(i-s)}},_resetScrollPosition(s){this.scrollTarget&&s>=0&&(this._scrollTop=s,this._scrollPosition=this._scrollTop)},_updateScrollerSize(s){const i=this._physicalBottom+Math.max(this._virtualCount-this._physicalCount-this._virtualStart,0)*this._physicalAverage;this._estScrollHeight=i,(s||this._scrollHeight===0||this._scrollPosition>=i-this._physicalSize||Math.abs(i-this._scrollHeight)>=this._viewportHeight)&&(this.$.items.style.height=`${i}px`,this._scrollHeight=i)},scrollToIndex(s){if(typeof s!="number"||s<0||s>this.items.length-1||(Re(),this._physicalCount===0))return;s=this._clamp(s,0,this._virtualCount-1),(!this._isIndexRendered(s)||s>=this._maxVirtualStart)&&(this._virtualStart=s-1),this._assignModels(),this._updateMetrics(),this._physicalTop=this._virtualStart*this._physicalAverage;let i=this._physicalStart,e=this._virtualStart,t=0;const n=this._hiddenContentSize;for(;e<s&&t<=n;)t+=this._getPhysicalSizeIncrement(i),i=(i+1)%this._physicalCount,e+=1;this._updateScrollerSize(!0),this._positionItems(),this._resetScrollPosition(this._physicalTop+this._scrollOffset+t),this._increasePoolIfNeeded(0),this._firstVisibleIndexVal=null,this._lastVisibleIndexVal=null},_resetAverage(){this._physicalAverage=0,this._physicalAverageCount=0},_resizeHandler(){this._debounce("_render",()=>{this._firstVisibleIndexVal=null,this._lastVisibleIndexVal=null,this._isVisible?(this.updateViewportBoundaries(),this.toggleScrollListener(!0),this._resetAverage(),this._render()):this.toggleScrollListener(!1)},X)},_isIndexRendered(s){return s>=this._virtualStart&&s<=this._virtualEnd},_getPhysicalIndex(s){return(this._physicalStart+(s-this._virtualStart))%this._physicalCount},_clamp(s,i,e){return Math.min(e,Math.max(i,s))},_debounce(s,i,e){this._debouncers||(this._debouncers={}),this._debouncers[s]=I.debounce(this._debouncers[s],e,i.bind(this)),Di(this._debouncers[s])}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ra=1e5,At=1e3;class zs{constructor({createElements:i,updateElement:e,scrollTarget:t,scrollContainer:n,reorderElements:r,elementsContainer:o,__disableHeightPlaceholder:a}){this.isAttached=!0,this._vidxOffset=0,this.createElements=i,this.updateElement=e,this.scrollTarget=t,this.scrollContainer=n,this.reorderElements=r,this.elementsContainer=o||n,this.__disableHeightPlaceholder=a??!1,this._maxPages=1.3,this.__placeholderHeight=200,this.__elementHeightQueue=Array(10),this.timeouts={SCROLL_REORDER:500,PREVENT_OVERSCROLL:500,FIX_INVALID_ITEM_POSITIONING:100},this.__resizeObserver=new ResizeObserver(()=>this._resizeHandler()),getComputedStyle(this.scrollTarget).overflow==="visible"&&(this.scrollTarget.style.overflow="auto"),getComputedStyle(this.scrollContainer).position==="static"&&(this.scrollContainer.style.position="relative"),this.__resizeObserver.observe(this.scrollTarget),this.scrollTarget.addEventListener("scroll",()=>this._scrollHandler()),new ResizeObserver(([{contentRect:d}])=>{const _=d.width===0&&d.height===0;!_&&this.__scrollTargetHidden&&this.scrollTarget.scrollTop!==this._scrollPosition&&(this.scrollTarget.scrollTop=this._scrollPosition),this.__scrollTargetHidden=_}).observe(this.scrollTarget),this._scrollLineHeight=this._getScrollLineHeight(),this.scrollTarget.addEventListener("virtualizer-element-focused",d=>this.__onElementFocused(d)),this.elementsContainer.addEventListener("focusin",()=>{this.scrollTarget.dispatchEvent(new CustomEvent("virtualizer-element-focused",{detail:{element:this.__getFocusedElement()}}))}),this.reorderElements&&(this.scrollTarget.addEventListener("mousedown",()=>{this.__mouseDown=!0}),this.scrollTarget.addEventListener("mouseup",()=>{this.__mouseDown=!1,this.__pendingReorder&&this.__reorderElements()}))}get scrollOffset(){return 0}get adjustedFirstVisibleIndex(){return this.firstVisibleIndex+this._vidxOffset}get adjustedLastVisibleIndex(){return this.lastVisibleIndex+this._vidxOffset}get _maxVirtualIndexOffset(){return this.size-this._virtualCount}__hasPlaceholders(){return this.__getVisibleElements().some(i=>i.__virtualizerPlaceholder)}scrollToIndex(i){if(typeof i!="number"||isNaN(i)||this.size===0||!this.scrollTarget.offsetHeight)return;delete this.__pendingScrollToIndex,this._physicalCount<=3&&this.flush(),i=this._clamp(i,0,this.size-1);const e=this.__getVisibleElements().length;let t=Math.floor(i/this.size*this._virtualCount);this._virtualCount-t<e?(t=this._virtualCount-(this.size-i),this._vidxOffset=this._maxVirtualIndexOffset):t<e?i<At?(t=i,this._vidxOffset=0):(t=At,this._vidxOffset=i-t):this._vidxOffset=i-t,this.__skipNextVirtualIndexAdjust=!0,super.scrollToIndex(t),this.adjustedFirstVisibleIndex!==i&&this._scrollTop<this._maxScrollTop&&!this.grid&&(this._scrollTop-=this.__getIndexScrollOffset(i)||0),this._scrollHandler(),this.__hasPlaceholders()&&(this.__pendingScrollToIndex=i)}flush(){this.scrollTarget.offsetHeight!==0&&(this._resizeHandler(),Re(),this._scrollHandler(),this.__fixInvalidItemPositioningDebouncer&&this.__fixInvalidItemPositioningDebouncer.flush(),this.__scrollReorderDebouncer&&this.__scrollReorderDebouncer.flush(),this.__debouncerWheelAnimationFrame&&this.__debouncerWheelAnimationFrame.flush())}hostConnected(){this.scrollTarget.offsetParent&&this.scrollTarget.scrollTop!==this._scrollPosition&&(this.scrollTarget.scrollTop=this._scrollPosition)}update(i=0,e=this.size-1){const t=[];this.__getVisibleElements().forEach(n=>{n.__virtualIndex>=i&&n.__virtualIndex<=e&&(this.__updateElement(n,n.__virtualIndex,!0),t.push(n))}),this.__afterElementsUpdated(t)}_updateMetrics(i){Re();let e=0,t=0;const n=this._physicalAverageCount,r=this._physicalAverage;this._iterateItems((o,a)=>{t+=this._physicalSizes[o];const l=this._physicalSizes[o];this._physicalSizes[o]=Math.ceil(this.__getBorderBoxHeight(this._physicalItems[o])),this._physicalSizes[o]!==l&&(this.__resizeObserver.unobserve(this._physicalItems[o]),this.__resizeObserver.observe(this._physicalItems[o],{box:"border-box"})),e+=this._physicalSizes[o],this._physicalAverageCount+=this._physicalSizes[o]?1:0},i),this._physicalSize=this._physicalSize+e-t,this._physicalAverageCount!==n&&(this._physicalAverage=Math.round((r*n+e)/this._physicalAverageCount))}__getBorderBoxHeight(i){const e=getComputedStyle(i),t=parseFloat(e.height)||0;if(e.boxSizing==="border-box")return t;const n=parseFloat(e.paddingBottom)||0,r=parseFloat(e.paddingTop)||0,o=parseFloat(e.borderBottomWidth)||0,a=parseFloat(e.borderTopWidth)||0;return t+n+r+o+a}__updateElement(i,e,t){i.__virtualizerPlaceholder&&(i.style.paddingTop="",i.style.opacity="",i.__virtualizerPlaceholder=!1),!this.__preventElementUpdates&&(i.__lastUpdatedIndex!==e||t)&&(this.updateElement(i,e),i.__lastUpdatedIndex=e)}__afterElementsUpdated(i){this.__disableHeightPlaceholder||i.forEach(e=>{const t=e.offsetHeight;if(t===0)e.style.paddingTop=`${this.__placeholderHeight}px`,e.style.opacity="0",e.__virtualizerPlaceholder=!0,this.__placeholderClearDebouncer=I.debounce(this.__placeholderClearDebouncer,X,()=>this._resizeHandler());else{this.__elementHeightQueue.push(t),this.__elementHeightQueue.shift();const n=this.__elementHeightQueue.filter(r=>r!==void 0);this.__placeholderHeight=Math.round(n.reduce((r,o)=>r+o,0)/n.length)}}),this.__pendingScrollToIndex!==void 0&&!this.__hasPlaceholders()&&this.scrollToIndex(this.__pendingScrollToIndex)}__getIndexScrollOffset(i){const e=this.__getVisibleElements().find(t=>t.__virtualIndex===i);return e?this.scrollTarget.getBoundingClientRect().top-e.getBoundingClientRect().top:void 0}get size(){return this.__size}set size(i){if(i===this.size)return;this.__fixInvalidItemPositioningDebouncer&&this.__fixInvalidItemPositioningDebouncer.cancel(),this._debouncers&&this._debouncers._increasePoolIfNeeded&&this._debouncers._increasePoolIfNeeded.cancel(),this.__preventElementUpdates=!0;let e,t;if(i>0&&(e=this.adjustedFirstVisibleIndex,t=this.__getIndexScrollOffset(e)),this.__size=i,this._itemsChanged({path:"items"}),Re(),i>0){e=Math.min(e,i-1),this.scrollToIndex(e);const n=this.__getIndexScrollOffset(e);t!==void 0&&n!==void 0&&(this._scrollTop+=t-n)}this.__preventElementUpdates=!1,this._isVisible||this._assignModels(),this.elementsContainer.children.length||requestAnimationFrame(()=>this._resizeHandler()),this._resizeHandler(),Re(),this._debounce("_update",this._update,W)}get _scrollTop(){return this.scrollTarget.scrollTop}set _scrollTop(i){this.scrollTarget.scrollTop=i}get items(){return{length:Math.min(this.size,ra)}}get offsetHeight(){return this.scrollTarget.offsetHeight}get $(){return{items:this.scrollContainer}}updateViewportBoundaries(){const i=window.getComputedStyle(this.scrollTarget);this._scrollerPaddingTop=this.scrollTarget===this?0:parseInt(i["padding-top"],10),this._isRTL=i.direction==="rtl",this._viewportWidth=this.elementsContainer.offsetWidth,this._viewportHeight=this.scrollTarget.offsetHeight,this._scrollPageHeight=this._viewportHeight-this._scrollLineHeight,this.grid&&this._updateGridMetrics()}setAttribute(){}_createPool(i){const e=this.createElements(i),t=document.createDocumentFragment();return e.forEach(n=>{n.style.position="absolute",t.appendChild(n),this.__resizeObserver.observe(n,{box:"border-box"})}),this.elementsContainer.appendChild(t),e}_assignModels(i){const e=[];this._iterateItems((t,n)=>{const r=this._physicalItems[t];r.hidden=n>=this.size,r.hidden?delete r.__lastUpdatedIndex:(r.__virtualIndex=n+(this._vidxOffset||0),this.__updateElement(r,r.__virtualIndex),e.push(r))},i),this.__afterElementsUpdated(e)}_isClientFull(){return setTimeout(()=>{this.__clientFull=!0}),this.__clientFull||super._isClientFull()}translate3d(i,e,t,n){n.style.transform=`translateY(${e})`}toggleScrollListener(){}__getFocusedElement(i=this.__getVisibleElements()){return i.find(e=>e.contains(this.elementsContainer.getRootNode().activeElement)||e.contains(this.scrollTarget.getRootNode().activeElement))}__nextFocusableSiblingMissing(i,e){return e.indexOf(i)===e.length-1&&this.size>i.__virtualIndex+1}__previousFocusableSiblingMissing(i,e){return e.indexOf(i)===0&&i.__virtualIndex>0}__onElementFocused(i){if(!this.reorderElements)return;const e=i.detail.element;if(!e)return;const t=this.__getVisibleElements();(this.__previousFocusableSiblingMissing(e,t)||this.__nextFocusableSiblingMissing(e,t))&&this.flush();const n=this.__getVisibleElements();this.__nextFocusableSiblingMissing(e,n)?(this._scrollTop+=Math.ceil(e.getBoundingClientRect().bottom)-Math.floor(this.scrollTarget.getBoundingClientRect().bottom-1),this.flush()):this.__previousFocusableSiblingMissing(e,n)&&(this._scrollTop-=Math.ceil(this.scrollTarget.getBoundingClientRect().top+1)-Math.floor(e.getBoundingClientRect().top),this.flush())}_scrollHandler(){if(this.scrollTarget.offsetHeight===0)return;this._adjustVirtualIndexOffset(this._scrollTop-this._scrollPosition);const i=this._scrollTop-this._scrollPosition;if(super._scrollHandler(),this._physicalCount!==0){const e=i>=0,t=this._getReusables(!e);t.indexes.length&&(this._physicalTop=t.physicalTop,e?(this._virtualStart-=t.indexes.length,this._physicalStart-=t.indexes.length):(this._virtualStart+=t.indexes.length,this._physicalStart+=t.indexes.length),this._resizeHandler())}i&&(this.__fixInvalidItemPositioningDebouncer=I.debounce(this.__fixInvalidItemPositioningDebouncer,H.after(this.timeouts.FIX_INVALID_ITEM_POSITIONING),()=>this.__fixInvalidItemPositioning()),this.__overscrollDebouncer?.isActive()||(this.scrollTarget.style.overscrollBehavior="none"),this.__overscrollDebouncer=I.debounce(this.__overscrollDebouncer,H.after(this.timeouts.PREVENT_OVERSCROLL),()=>{this.scrollTarget.style.overscrollBehavior=null})),this.reorderElements&&(this.__scrollReorderDebouncer=I.debounce(this.__scrollReorderDebouncer,H.after(this.timeouts.SCROLL_REORDER),()=>this.__reorderElements())),this._scrollPosition===0&&this.firstVisibleIndex!==0&&Math.abs(i)>0&&this.scrollToIndex(0)}_resizeHandler(){super._resizeHandler();const i=this.adjustedLastVisibleIndex===this.size-1,e=this._physicalTop-this._scrollPosition;if(i&&e>0){const t=Math.ceil(e/this._physicalAverage);this._virtualStart=Math.max(0,this._virtualStart-t),this._physicalStart=Math.max(0,this._physicalStart-t),super.scrollToIndex(this._virtualCount-1),this.scrollTarget.scrollTop=this.scrollTarget.scrollHeight-this.scrollTarget.clientHeight}}__fixInvalidItemPositioning(){if(!this.scrollTarget.isConnected)return;const i=this._physicalTop>this._scrollTop,e=this._physicalBottom<this._scrollBottom,t=this.adjustedFirstVisibleIndex===0,n=this.adjustedLastVisibleIndex===this.size-1;if(i&&!t||e&&!n){const r=e,o=this._ratio;this._ratio=0,this._scrollPosition=this._scrollTop+(r?-1:1),this._scrollHandler(),this._ratio=o}}_increasePoolIfNeeded(i){if(this._physicalCount>2&&this._physicalAverage>0&&i>0){const t=Math.ceil(this._optPhysicalSize/this._physicalAverage)-this._physicalCount;super._increasePoolIfNeeded(Math.max(i,Math.min(100,t)))}else super._increasePoolIfNeeded(i)}get _optPhysicalSize(){const i=super._optPhysicalSize;return i<=0||this.__hasPlaceholders()?i:i+this.__getItemHeightBuffer()}__getItemHeightBuffer(){if(this._physicalCount===0)return 0;const i=Math.ceil(this._viewportHeight*(this._maxPages-1)/2),e=Math.max(...this._physicalSizes);return e>Math.min(...this._physicalSizes)?Math.max(0,e-i):0}_getScrollLineHeight(){const i=document.createElement("div");i.style.fontSize="initial",i.style.display="none",document.body.appendChild(i);const e=window.getComputedStyle(i).fontSize;return document.body.removeChild(i),e?window.parseInt(e):void 0}__getVisibleElements(){return Array.from(this.elementsContainer.children).filter(i=>!i.hidden)}__reorderElements(){if(this.__mouseDown){this.__pendingReorder=!0;return}this.__pendingReorder=!1;const i=this._virtualStart+(this._vidxOffset||0),e=this.__getVisibleElements(),t=this.__getFocusedElement(e)||e[0];if(!t)return;const n=t.__virtualIndex-i,r=e.indexOf(t)-n;if(r>0)for(let o=0;o<r;o++)this.elementsContainer.appendChild(e[o]);else if(r<0)for(let o=e.length+r;o<e.length;o++)this.elementsContainer.insertBefore(e[o],e[0]);if(Bt){const{transform:o}=this.scrollTarget.style;this.scrollTarget.style.transform="translateZ(0)",setTimeout(()=>{this.scrollTarget.style.transform=o})}}_adjustVirtualIndexOffset(i){const e=this._maxVirtualIndexOffset;if(this._virtualCount>=this.size)this._vidxOffset=0;else if(this.__skipNextVirtualIndexAdjust)this.__skipNextVirtualIndexAdjust=!1;else if(Math.abs(i)>1e4){const t=this._scrollTop/(this.scrollTarget.scrollHeight-this.scrollTarget.clientHeight);this._vidxOffset=Math.round(t*e)}else{const t=this._vidxOffset,n=At,r=100;this._scrollTop===0?(this._vidxOffset=0,t!==this._vidxOffset&&super.scrollToIndex(0)):this.firstVisibleIndex<n&&this._vidxOffset>0&&(this._vidxOffset-=Math.min(this._vidxOffset,r),super.scrollToIndex(this.firstVisibleIndex+(t-this._vidxOffset))),this._scrollTop>=this._maxScrollTop&&this._maxScrollTop>0?(this._vidxOffset=e,t!==this._vidxOffset&&super.scrollToIndex(this._virtualCount-1)):this.firstVisibleIndex>this._virtualCount-n&&this._vidxOffset<e&&(this._vidxOffset+=Math.min(e-this._vidxOffset,r),super.scrollToIndex(this.firstVisibleIndex-(this._vidxOffset-t)))}}}Object.setPrototypeOf(zs.prototype,na);/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class oa{constructor(i){this.__adapter=new zs(i)}get firstVisibleIndex(){return this.__adapter.adjustedFirstVisibleIndex}get lastVisibleIndex(){return this.__adapter.adjustedLastVisibleIndex}get size(){return this.__adapter.size}set size(i){this.__adapter.size=i}scrollToIndex(i){this.__adapter.scrollToIndex(i)}update(i=0,e=this.size-1){this.__adapter.update(i,e)}flush(){this.__adapter.flush()}hostConnected(){this.__adapter.hostConnected()}}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const aa=s=>class extends s{static get properties(){return{accessibleName:{type:String}}}static get observers(){return["__a11yUpdateGridSize(size, _columnTree, __emptyState)"]}__a11yGetHeaderRowCount(e){return e.filter(t=>t.some(n=>n.headerRenderer||n.path&&n.header!==null||n.header)).length}__a11yGetFooterRowCount(e){return e.filter(t=>t.some(n=>n.footerRenderer)).length}__a11yUpdateGridSize(e,t,n){if(e===void 0||t===void 0)return;const r=this.__a11yGetHeaderRowCount(t),o=this.__a11yGetFooterRowCount(t),l=(n?1:e)+r+o;this.$.table.setAttribute("aria-rowcount",l);const d=t[t.length-1],_=n?1:l&&d&&d.length||0;this.$.table.setAttribute("aria-colcount",_),this.__a11yUpdateHeaderRows(),this.__a11yUpdateFooterRows()}__a11yUpdateHeaderRows(){D(this.$.header,(e,t)=>{e.setAttribute("aria-rowindex",t+1)})}__a11yUpdateFooterRows(){D(this.$.footer,(e,t)=>{e.setAttribute("aria-rowindex",this.__a11yGetHeaderRowCount(this._columnTree)+this.size+t+1)})}__a11yUpdateRowRowindex(e){e.setAttribute("aria-rowindex",e.index+this.__a11yGetHeaderRowCount(this._columnTree)+1)}__a11yUpdateRowSelected(e,t){e.setAttribute("aria-selected",!!t),Pe(e,n=>{n.setAttribute("aria-selected",!!t)})}__a11yUpdateRowExpanded(e){const t=ea(e);this.__isRowExpandable(e)?(e.setAttribute("aria-expanded","false"),t&&t.setAttribute("aria-expanded","false")):this.__isRowCollapsible(e)?(e.setAttribute("aria-expanded","true"),t&&t.setAttribute("aria-expanded","true")):(e.removeAttribute("aria-expanded"),t&&t.removeAttribute("aria-expanded"))}__a11yUpdateRowLevel(e,t){t>0||this.__isRowCollapsible(e)||this.__isRowExpandable(e)?e.setAttribute("aria-level",t+1):e.removeAttribute("aria-level")}__a11ySetRowDetailsCell(e,t){Pe(e,n=>{n!==t&&n.setAttribute("aria-controls",t.id)})}__a11yUpdateCellColspan(e,t){e.setAttribute("aria-colspan",Number(t))}__a11yUpdateSorters(){Array.from(this.querySelectorAll("vaadin-grid-sorter")).forEach(e=>{let t=e.parentNode;for(;t&&t.localName!=="vaadin-grid-cell-content";)t=t.parentNode;t&&t.assignedSlot&&t.assignedSlot.parentNode.setAttribute("aria-sort",{asc:"ascending",desc:"descending"}[String(e.direction)]||"none")})}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ms=s=>s.offsetParent&&!s.part.contains("body-cell")&&Ht(s)&&getComputedStyle(s).visibility!=="hidden",la=s=>class extends s{static get properties(){return{activeItem:{type:Object,notify:!0,value:null,sync:!0}}}ready(){super.ready(),this.$.scroller.addEventListener("click",this._onClick.bind(this)),this.addEventListener("cell-activate",this._activateItem.bind(this)),this.addEventListener("row-activate",this._activateItem.bind(this))}_activateItem(e){const t=e.detail.model,n=t?t.item:null;n&&(this.activeItem=this._itemsEqual(this.activeItem,n)?null:n)}_shouldPreventCellActivationOnClick(e){const{cell:t}=this._getGridEventLocation(e);return e.defaultPrevented||!t||t.part.contains("details-cell")||t===this.$.emptystatecell||t._content.contains(this.getRootNode().activeElement)||this._isFocusable(e.target)||e.target instanceof HTMLLabelElement}_onClick(e){if(this._shouldPreventCellActivationOnClick(e))return;const{cell:t}=this._getGridEventLocation(e);t&&this.dispatchEvent(new CustomEvent("cell-activate",{detail:{model:this.__getRowModel(t.parentElement)}}))}_isFocusable(e){return Ms(e)}};/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function pe(s,i){return s.split(".").reduce((e,t)=>e[t],i)}function Ai(s,i,e){if(e.length===0)return!1;let t=!0;return s.forEach(({path:n})=>{if(!n||n.indexOf(".")===-1)return;const r=n.replace(/\.[^.]*$/u,"");pe(r,e[0])===void 0&&(console.warn(`Path "${n}" used for ${i} does not exist in all of the items, ${i} is disabled.`),t=!1)}),t}function it(s){return[void 0,null].indexOf(s)>=0?"":isNaN(s)?s.toString():s}function Ti(s,i){return s=it(s),i=it(i),s<i?-1:s>i?1:0}function da(s,i){return s.sort((e,t)=>i.map(n=>n.direction==="asc"?Ti(pe(n.path,e),pe(n.path,t)):n.direction==="desc"?Ti(pe(n.path,t),pe(n.path,e)):0).reduce((n,r)=>n!==0?n:r,0))}function ha(s,i){return s.filter(e=>i.every(t=>{const n=it(pe(t.path,e)),r=it(t.value).toString().toLowerCase();return n.toString().toLowerCase().includes(r)}))}const ca=s=>(i,e)=>{let t=s?[...s]:[];i.filters&&Ai(i.filters,"filtering",t)&&(t=ha(t,i.filters)),Array.isArray(i.sortOrders)&&i.sortOrders.length&&Ai(i.sortOrders,"sorting",t)&&(t=da(t,i.sortOrders));const n=Math.min(t.length,i.pageSize),r=i.page*n,o=r+n,a=t.slice(r,o);e(a,t.length)};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ua=s=>class extends s{static get properties(){return{items:{type:Array,sync:!0}}}static get observers(){return["__dataProviderOrItemsChanged(dataProvider, items, isAttached, items.*)"]}__setArrayDataProvider(e){const t=ca(this.items);t.__items=e,this._arrayDataProvider=t,this.size=e.length,this.dataProvider=t}_onDataProviderPageReceived(){super._onDataProviderPageReceived(),this._arrayDataProvider&&(this.size=this._flatSize)}__dataProviderOrItemsChanged(e,t,n){n&&(this._arrayDataProvider?e!==this._arrayDataProvider?(this._arrayDataProvider=void 0,this.items=void 0):t?this._arrayDataProvider.__items===t?this.clearCache():this.__setArrayDataProvider(t):(this._arrayDataProvider=void 0,this.dataProvider=void 0,this.size=0,this.clearCache()):t&&this.__setArrayDataProvider(t))}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const _a=s=>class extends s{static get properties(){return{__pendingRecalculateColumnWidths:{type:Boolean,value:!0}}}static get observers(){return["__dataProviderChangedAutoWidth(dataProvider)","__columnTreeChangedAutoWidth(_columnTree)","__flatSizeChangedAutoWidth(_flatSize)"]}updated(i){super.updated(i),i.has("__hostVisible")&&!i.get("__hostVisible")&&this.__tryToRecalculateColumnWidthsIfPending()}__dataProviderChangedAutoWidth(i){this.__hasHadRenderedRowsForColumnWidthCalculation||this.recalculateColumnWidths()}__columnTreeChangedAutoWidth(i){queueMicrotask(()=>this.recalculateColumnWidths())}__flatSizeChangedAutoWidth(i){requestAnimationFrame(()=>{i&&!this.__hasHadRenderedRowsForColumnWidthCalculation?this.recalculateColumnWidths():this.__tryToRecalculateColumnWidthsIfPending()})}_onDataProviderPageLoaded(){super._onDataProviderPageLoaded(),this.__tryToRecalculateColumnWidthsIfPending()}_updateFrozenColumn(){super._updateFrozenColumn(),this.__tryToRecalculateColumnWidthsIfPending()}__getIntrinsicWidth(i){return this.__intrinsicWidthCache.has(i)||this.__calculateAndCacheIntrinsicWidths([i]),this.__intrinsicWidthCache.get(i)}__getDistributedWidth(i,e){if(i==null||i===this)return 0;const t=Math.max(this.__getIntrinsicWidth(i),this.__getDistributedWidth(this.__getParentColumnGroup(i),i));if(!e)return t;const n=i,r=t,o=n._visibleChildColumns.map(_=>this.__getIntrinsicWidth(_)).reduce((_,f)=>_+f,0),a=Math.max(0,r-o),d=this.__getIntrinsicWidth(e)/o*a;return this.__getIntrinsicWidth(e)+d}_recalculateColumnWidths(){this.__virtualizer.flush(),[...this.$.header.children,...this.$.footer.children].forEach(r=>{r.__debounceUpdateHeaderFooterRowVisibility&&r.__debounceUpdateHeaderFooterRowVisibility.flush()}),this.__hasHadRenderedRowsForColumnWidthCalculation=this.__hasHadRenderedRowsForColumnWidthCalculation||this._getRenderedRows().length>0,this.__intrinsicWidthCache=new Map;const i=this._firstVisibleIndex,e=this._lastVisibleIndex;this.__viewportRowsCache=this._getRenderedRows().filter(r=>r.index>=i&&r.index<=e);const t=this.__getAutoWidthColumns(),n=new Set;for(const r of t){let o=this.__getParentColumnGroup(r);for(;o&&!n.has(o);)n.add(o),o=this.__getParentColumnGroup(o)}this.__calculateAndCacheIntrinsicWidths([...t,...n]),t.forEach(r=>{r.width=`${this.__getDistributedWidth(r)}px`}),this.__intrinsicWidthCache.clear()}__getParentColumnGroup(i){const e=(i.assignedSlot||i).parentElement;return e&&e!==this?e:null}__setVisibleCellContentAutoWidth(i,e){i._allCells.filter(t=>this.$.items.contains(t)?this.__viewportRowsCache.includes(t.parentElement):!0).forEach(t=>{t.__measuringAutoWidth=e,t.__measuringAutoWidth?(t.__originalWidth=t.style.width,t.style.width="auto",t.style.position="absolute"):(t.style.width=t.__originalWidth,delete t.__originalWidth,t.style.position="")}),e?this.$.scroller.setAttribute("measuring-auto-width",""):this.$.scroller.removeAttribute("measuring-auto-width")}__getAutoWidthCellsMaxWidth(i){return i._allCells.reduce((e,t)=>t.__measuringAutoWidth?Math.max(e,t.offsetWidth+1):e,0)}__calculateAndCacheIntrinsicWidths(i){i.forEach(e=>this.__setVisibleCellContentAutoWidth(e,!0)),i.forEach(e=>{const t=this.__getAutoWidthCellsMaxWidth(e);this.__intrinsicWidthCache.set(e,t)}),i.forEach(e=>this.__setVisibleCellContentAutoWidth(e,!1))}recalculateColumnWidths(){if(!this.__isReadyForColumnWidthCalculation()){this.__pendingRecalculateColumnWidths=!0;return}this._recalculateColumnWidths()}__tryToRecalculateColumnWidthsIfPending(){this.__pendingRecalculateColumnWidths&&(this.__pendingRecalculateColumnWidths=!1,this.recalculateColumnWidths())}__getAutoWidthColumns(){return this._getColumns().filter(i=>!i.hidden&&i.autoWidth)}__isReadyForColumnWidthCalculation(){if(!this._columnTree)return!1;const i=this.__getAutoWidthColumns().filter(o=>!customElements.get(o.localName));if(i.length)return Promise.all(i.map(o=>customElements.whenDefined(o.localName))).then(()=>{this.__tryToRecalculateColumnWidthsIfPending()}),!1;const e=[...this.$.items.children].some(o=>o.index===void 0),t=this._debouncerHiddenChanged&&this._debouncerHiddenChanged.isActive(),n=this.__debounceUpdateFrozenColumn&&this.__debounceUpdateFrozenColumn.isActive(),r=this.clientHeight>0;return!this._dataProviderController.isLoading()&&!e&&!q(this)&&!t&&!n&&r}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const pa=s=>class extends s{static get properties(){return{columnReorderingAllowed:{type:Boolean,value:!1},_orderBaseScope:{type:Number,value:1e7}}}static get observers(){return["_updateOrders(_columnTree)"]}ready(){super.ready(),de(this,"track",this._onTrackEvent),this._reorderGhost=this.shadowRoot.querySelector('[part="reorder-ghost"]'),this.addEventListener("touchstart",this._onTouchStart.bind(this)),this.addEventListener("touchmove",this._onTouchMove.bind(this)),this.addEventListener("touchend",this._onTouchEnd.bind(this)),this.addEventListener("contextmenu",this._onContextMenu.bind(this))}_onContextMenu(e){this.hasAttribute("reordering")&&(e.preventDefault(),Me||this._onTrackEnd())}_onTouchStart(e){this._startTouchReorderTimeout=setTimeout(()=>{this._onTrackStart({detail:{x:e.touches[0].clientX,y:e.touches[0].clientY}})},100)}_onTouchMove(e){this._draggedColumn&&e.preventDefault(),clearTimeout(this._startTouchReorderTimeout)}_onTouchEnd(){clearTimeout(this._startTouchReorderTimeout),this._onTrackEnd()}_onTrackEvent(e){if(e.detail.state==="start"){const t=e.composedPath(),n=t[t.indexOf(this.$.header)-2];if(!n||!n._content||n._content.contains(this.getRootNode().activeElement)||this.$.scroller.hasAttribute("column-resizing"))return;this._touchDevice||this._onTrackStart(e)}else e.detail.state==="track"?this._onTrack(e):e.detail.state==="end"&&this._onTrackEnd(e)}_onTrackStart(e){if(!this.columnReorderingAllowed)return;const t=e.composedPath&&e.composedPath();if(t&&t.slice(0,Math.max(0,t.indexOf(this))).some(r=>r.draggable))return;const n=this._cellFromPoint(e.detail.x,e.detail.y);if(!(!n||!n.part.contains("header-cell"))){for(this.toggleAttribute("reordering",!0),this._draggedColumn=n._column;this._draggedColumn.parentElement.childElementCount===1;)this._draggedColumn=this._draggedColumn.parentElement;this._setSiblingsReorderStatus(this._draggedColumn,"allowed"),this._draggedColumn._reorderStatus="dragging",this._updateGhost(n),this._reorderGhost.style.visibility="visible",this._updateGhostPosition(e.detail.x,this._touchDevice?e.detail.y-50:e.detail.y),this._autoScroller()}}_onTrack(e){if(!this._draggedColumn)return;const t=this._cellFromPoint(e.detail.x,e.detail.y);if(!t)return;const n=this._getTargetColumn(t,this._draggedColumn);if(this._isSwapAllowed(this._draggedColumn,n)&&this._isSwappableByPosition(n,e.detail.x)){const r=this._columnTree.findIndex(_=>_.includes(n)),o=this._getColumnsInOrder(r),a=o.indexOf(this._draggedColumn),l=o.indexOf(n),d=a<l?1:-1;for(let _=a;_!==l;_+=d)this._swapColumnOrders(this._draggedColumn,o[_+d])}this._updateGhostPosition(e.detail.x,this._touchDevice?e.detail.y-50:e.detail.y),this._lastDragClientX=e.detail.x}_onTrackEnd(){this._draggedColumn&&(this.toggleAttribute("reordering",!1),this._draggedColumn._reorderStatus="",this._setSiblingsReorderStatus(this._draggedColumn,""),this._draggedColumn=null,this._lastDragClientX=null,this._reorderGhost.style.visibility="hidden",this.dispatchEvent(new CustomEvent("column-reorder",{detail:{columns:this._getColumnsInOrder()}})))}_getColumnsInOrder(e=this._columnTree.length-1){return this._columnTree[e].filter(t=>!t.hidden).sort((t,n)=>t._order-n._order)}_cellFromPoint(e=0,t=0){this._draggedColumn||this.$.scroller.toggleAttribute("no-content-pointer-events",!0);const n=this.shadowRoot.elementFromPoint(e,t);return this.$.scroller.toggleAttribute("no-content-pointer-events",!1),this._getCellFromElement(n)}_getCellFromElement(e){if(e){if(e._column)return e;const{parentElement:t}=e;if(t&&t._focusButton===e)return t}return null}_updateGhostPosition(e,t){const n=this._reorderGhost.getBoundingClientRect(),r=e-n.width/2,o=t-n.height/2,a=parseInt(this._reorderGhost._left||0),l=parseInt(this._reorderGhost._top||0);this._reorderGhost._left=a-(n.left-r),this._reorderGhost._top=l-(n.top-o),this._reorderGhost.style.transform=`translate(${this._reorderGhost._left}px, ${this._reorderGhost._top}px)`}_updateGhost(e){const t=this._reorderGhost;t.textContent=e._content.innerText;const n=window.getComputedStyle(e);return["boxSizing","display","width","height","background","alignItems","padding","border","flex-direction","overflow"].forEach(r=>{t.style[r]=n[r]}),t}_updateOrders(e){e!==void 0&&(e[0].forEach(t=>{t._order=0}),Os(e[0],this._orderBaseScope,0))}_setSiblingsReorderStatus(e,t){D(e.parentNode,n=>{/column/u.test(n.localName)&&this._isSwapAllowed(n,e)&&(n._reorderStatus=t)})}_autoScroller(){if(this._lastDragClientX){const e=this._lastDragClientX-this.getBoundingClientRect().right+50,t=this.getBoundingClientRect().left-this._lastDragClientX+50;e>0?this.$.table.scrollLeft+=e/10:t>0&&(this.$.table.scrollLeft-=t/10)}this._draggedColumn&&setTimeout(()=>this._autoScroller(),10)}_isSwapAllowed(e,t){if(e&&t){const n=e!==t,r=e.parentElement===t.parentElement,o=e.frozen&&t.frozen||e.frozenToEnd&&t.frozenToEnd||!e.frozen&&!e.frozenToEnd&&!t.frozen&&!t.frozenToEnd;return n&&r&&o}}_isSwappableByPosition(e,t){const n=Array.from(this.$.header.querySelectorAll('tr:not([hidden]) [part~="cell"]')).find(a=>e.contains(a._column)),r=this.$.header.querySelector("tr:not([hidden]) [reorder-status=dragging]").getBoundingClientRect(),o=n.getBoundingClientRect();return o.left>r.left?t>o.right-r.width:t<o.left+r.width}_swapColumnOrders(e,t){[e._order,t._order]=[t._order,e._order],this._debounceUpdateFrozenColumn(),this._updateFirstAndLastColumn()}_getTargetColumn(e,t){if(e&&t){let n=e._column;for(;n.parentElement!==t.parentElement&&n!==this;)n=n.parentElement;return n.parentElement===t.parentElement?n:e._column}}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const fa=s=>class extends s{ready(){super.ready();const e=this.$.scroller;de(e,"track",this._onHeaderTrack.bind(this)),e.addEventListener("touchmove",t=>e.hasAttribute("column-resizing")&&t.preventDefault()),e.addEventListener("contextmenu",t=>t.target.part.contains("resize-handle")&&t.preventDefault()),e.addEventListener("mousedown",t=>t.target.part.contains("resize-handle")&&t.preventDefault())}_onHeaderTrack(e){const t=e.target;if(t.part.contains("resize-handle")){let r=t.parentElement._column;for(this.$.scroller.toggleAttribute("column-resizing",!0);r.localName==="vaadin-grid-column-group";)r=r._childColumns.slice(0).sort((f,g)=>f._order-g._order).filter(f=>!f.hidden).pop();const o=this.__isRTL,a=e.detail.x,l=Array.from(this.$.header.querySelectorAll('[part~="row"]:last-child [part~="cell"]')),d=l.find(f=>f._column===r);if(d.offsetWidth){const f=getComputedStyle(d._content),g=10+parseInt(f.paddingLeft)+parseInt(f.paddingRight)+parseInt(f.borderLeftWidth)+parseInt(f.borderRightWidth)+parseInt(f.marginLeft)+parseInt(f.marginRight);let b;const L=d.offsetWidth,A=d.getBoundingClientRect();d.hasAttribute("frozen-to-end")?b=L+(o?a-A.right:A.left-a):b=L+(o?A.left-a:a-A.right),r.width=`${Math.max(g,b)}px`,r.flexGrow=0}l.sort((f,g)=>f._column._order-g._column._order).forEach((f,g,b)=>{g<b.indexOf(d)&&(f._column.width=`${f.offsetWidth}px`,f._column.flexGrow=0)});const _=this._frozenToEndCells[0];if(_&&this.$.table.scrollWidth>this.$.table.offsetWidth){const f=_.getBoundingClientRect(),g=a-(o?f.right:f.left);(o&&g<=0||!o&&g>=0)&&(this.$.table.scrollLeft+=g)}e.detail.state==="end"&&(this.$.scroller.toggleAttribute("column-resizing",!1),this.dispatchEvent(new CustomEvent("column-resize",{detail:{resizedColumn:r}}))),this._resizeHandler()}}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ii{context;pageSize;items=[];pendingRequests={};#e={};#i=0;#t=0;constructor(i,e,t,n,r){this.context=i,this.pageSize=e,this.size=t,this.parentCache=n,this.parentCacheIndex=r,this.#t=t||0}get parentItem(){return this.parentCache&&this.parentCache.items[this.parentCacheIndex]}get subCaches(){return Object.values(this.#e)}get isLoading(){return Object.keys(this.pendingRequests).length>0?!0:this.subCaches.some(i=>i.isLoading)}get flatSize(){return this.#t}get size(){return this.#i}set size(i){if(this.#i!==i){if(this.#i=i,this.context.placeholder!==void 0){this.items.length=i||0;for(let t=0;t<i;t++)this.items[t]||=this.context.placeholder}this.items.length>i&&(this.items.length=i||0),Object.keys(this.pendingRequests).forEach(t=>{parseInt(t)*this.pageSize>=this.size&&delete this.pendingRequests[t]})}}recalculateFlatSize(){this.#t=!this.parentItem||this.context.isExpanded(this.parentItem)?this.size+this.subCaches.reduce((i,e)=>(e.recalculateFlatSize(),i+e.flatSize),0):0}setPage(i,e){const t=i*this.pageSize;e.forEach((n,r)=>{const o=t+r;(this.size===void 0||o<this.size)&&(this.items[o]=n)})}getSubCache(i){return this.#e[i]}removeSubCache(i){delete this.#e[i]}removeSubCaches(){this.#e={}}createSubCache(i){const e=new ii(this.context,this.pageSize,0,this,i);return this.#e[i]=e,e}getFlatIndex(i){const e=Math.max(0,Math.min(this.size-1,i));return this.subCaches.reduce((t,n)=>{const r=n.parentCacheIndex;return e>r?t+n.flatSize:t},e)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Fs(s,i,e=0){let t=i;for(const n of s.subCaches){const r=n.parentCacheIndex;if(t<=r)break;if(t<=r+n.flatSize)return Fs(n,t-r-1,e+1);t-=n.flatSize}return{cache:s,item:s.items[t],index:t,page:Math.floor(t/s.pageSize),level:e}}function $s({getItemId:s},i,e,t=0,n=0){for(let r=0;r<i.items.length;r++){const o=i.items[r];if(o&&s(o)===s(e))return{cache:i,level:t,item:o,index:r,page:Math.floor(r/i.pageSize),subCache:i.getSubCache(r),flatIndex:n+i.getFlatIndex(r)}}for(const r of i.subCaches){const o=n+i.getFlatIndex(r.parentCacheIndex),a=$s({getItemId:s},r,e,t+1,o+1);if(a)return a}}function Ds(s,[i,...e],t=0){i===1/0&&(i=s.size-1);const n=s.getFlatIndex(i),r=s.getSubCache(i);return r&&r.flatSize>0&&e.length?Ds(r,e,t+n+1):t+n}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ga extends EventTarget{host;dataProvider;dataProviderParams;pageSize;isExpanded;getItemId;rootCache;placeholder;isPlaceholder;constructor(i,{size:e,pageSize:t,isExpanded:n,getItemId:r,isPlaceholder:o,placeholder:a,dataProvider:l,dataProviderParams:d}){super(),this.host=i,this.pageSize=t,this.getItemId=r,this.isExpanded=n,this.placeholder=a,this.isPlaceholder=o,this.dataProvider=l,this.dataProviderParams=d,this.rootCache=this.#i(e)}get flatSize(){return this.rootCache.flatSize}get#e(){return{isExpanded:this.isExpanded,placeholder:this.placeholder}}isLoading(){return this.rootCache.isLoading}setPageSize(i){this.pageSize=i,this.clearCache()}setDataProvider(i){this.dataProvider=i,this.clearCache()}recalculateFlatSize(){this.rootCache.recalculateFlatSize()}clearCache(){this.rootCache=this.#i(this.rootCache.size)}getFlatIndexContext(i){return Fs(this.rootCache,i)}getItemContext(i){return $s({getItemId:this.getItemId},this.rootCache,i)}getFlatIndexByPath(i){return Ds(this.rootCache,i)}ensureFlatIndexLoaded(i){const{cache:e,page:t,item:n}=this.getFlatIndexContext(i);this.#s(n)||this.#t(e,t)}ensureFlatIndexHierarchy(i){const{cache:e,item:t,index:n}=this.getFlatIndexContext(i);if(this.#s(t)&&this.isExpanded(t)&&!e.getSubCache(n)){const r=e.createSubCache(n);this.#t(r,0)}}loadFirstPage(){this.#t(this.rootCache,0)}_shouldLoadCachePage(i,e){return!0}#i(i){return new ii(this.#e,this.pageSize,i)}#t(i,e){if(!this.dataProvider||i.pendingRequests[e]||!this._shouldLoadCachePage(i,e))return;let t={page:e,pageSize:this.pageSize,parentItem:i.parentItem};this.dataProviderParams&&(t={...t,...this.dataProviderParams()});const n=(r,o)=>{i.pendingRequests[e]===n&&(o!==void 0?i.size=o:t.parentItem&&(i.size=r.length),i.setPage(e,r),this.recalculateFlatSize(),this.dispatchEvent(new CustomEvent("page-received")),delete i.pendingRequests[e],this.dispatchEvent(new CustomEvent("page-loaded")))};i.pendingRequests[e]=n,this.dispatchEvent(new CustomEvent("page-requested")),this.dataProvider(t,n)}#s(i){return this.isPlaceholder?!this.isPlaceholder(i):this.placeholder?i!==this.placeholder:!!i}}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ma=s=>class extends s{static get properties(){return{size:{type:Number,notify:!0,sync:!0},_flatSize:{type:Number,sync:!0},pageSize:{type:Number,value:50,observer:"_pageSizeChanged",sync:!0},dataProvider:{type:Object,notify:!0,observer:"_dataProviderChanged",sync:!0},loading:{type:Boolean,notify:!0,readOnly:!0,reflectToAttribute:!0},_hasData:{type:Boolean,value:!1,sync:!0},itemHasChildrenPath:{type:String,value:"children",observer:"__itemHasChildrenPathChanged",sync:!0},itemIdPath:{type:String,value:null,sync:!0},expandedItems:{type:Object,notify:!0,value:()=>[],sync:!0},__expandedKeys:{type:Object,computed:"__computeExpandedKeys(itemIdPath, expandedItems)"}}}static get observers(){return["_sizeChanged(size)","_expandedItemsChanged(expandedItems)"]}constructor(){super(),this._dataProviderController=new ga(this,{size:this.size||0,pageSize:this.pageSize,getItemId:this.getItemId.bind(this),isExpanded:this._isExpanded.bind(this),dataProvider:this.dataProvider?this.dataProvider.bind(this):null,dataProviderParams:()=>({sortOrders:this._mapSorters(),filters:this._mapFilters()})}),this._dataProviderController.addEventListener("page-requested",this._onDataProviderPageRequested.bind(this)),this._dataProviderController.addEventListener("page-received",this._onDataProviderPageReceived.bind(this)),this._dataProviderController.addEventListener("page-loaded",this._onDataProviderPageLoaded.bind(this))}_sizeChanged(e){this._dataProviderController.rootCache.size=e,this._dataProviderController.recalculateFlatSize(),this._flatSize=this._dataProviderController.flatSize}__itemHasChildrenPathChanged(e,t){!t&&e==="children"||this.requestContentUpdate()}__getRowLevel(e){const{level:t}=this._dataProviderController.getFlatIndexContext(e.index);return t}__getRowItem(e){const{item:t}=this._dataProviderController.getFlatIndexContext(e.index);return t}__ensureRowItem(e){this._dataProviderController.ensureFlatIndexLoaded(e.index)}__ensureRowHierarchy(e){this._dataProviderController.ensureFlatIndexHierarchy(e.index)}getItemId(e){return this.itemIdPath?Ke(this.itemIdPath,e):e}_isExpanded(e){return this.__expandedKeys&&this.__expandedKeys.has(this.getItemId(e))}_hasChildren(e){return this.itemHasChildrenPath&&e&&!!Ke(this.itemHasChildrenPath,e)}_expandedItemsChanged(){this._dataProviderController.recalculateFlatSize(),this._flatSize=this._dataProviderController.flatSize,this.__updateVisibleRows()}__computeExpandedKeys(e,t){const n=t||[],r=new Set;return n.forEach(o=>{r.add(this.getItemId(o))}),r}expandItem(e){this._isExpanded(e)||(this.expandedItems=[...this.expandedItems,e])}collapseItem(e){this._isExpanded(e)&&(this.expandedItems=this.expandedItems.filter(t=>!this._itemsEqual(t,e)))}_onDataProviderPageRequested(){this._setLoading(!0)}_onDataProviderPageReceived(){this._flatSize!==this._dataProviderController.flatSize&&(this._shouldLoadAllRenderedRowsAfterPageLoad=!0,this._flatSize=this._dataProviderController.flatSize),this._getRenderedRows().forEach(e=>this.__ensureRowHierarchy(e)),this._hasData=!0}_onDataProviderPageLoaded(){this._debouncerApplyCachedData=I.debounce(this._debouncerApplyCachedData,H.after(0),()=>{this._setLoading(!1);const e=this._shouldLoadAllRenderedRowsAfterPageLoad;this._shouldLoadAllRenderedRowsAfterPageLoad=!1,this._getRenderedRows().forEach(t=>{this.__updateRow(t),e&&this.__ensureRowItem(t)}),this.__scrollToPendingIndexes(),this.__dispatchPendingBodyCellFocus()}),this._dataProviderController.isLoading()||this._debouncerApplyCachedData.flush()}__debounceClearCache(){this.__clearCacheDebouncer=I.debounce(this.__clearCacheDebouncer,W,()=>this.clearCache())}clearCache(){this._dataProviderController.clearCache(),this._dataProviderController.rootCache.size=this.size||0,this._dataProviderController.recalculateFlatSize(),this._hasData=!1,this.__updateVisibleRows(),(!this.__virtualizer||!this.__virtualizer.size)&&this._dataProviderController.loadFirstPage()}_pageSizeChanged(e,t){this._dataProviderController.setPageSize(e),t!==void 0&&e!==t&&this.clearCache()}_checkSize(){this.size===void 0&&this._flatSize===0&&console.warn("The <vaadin-grid> needs the total number of items in order to display rows, which you can specify either by setting the `size` property, or by providing it to the second argument of the `dataProvider` function `callback` call.")}_dataProviderChanged(e,t){this._dataProviderController.setDataProvider(e?e.bind(this):null),t!==void 0&&this.clearCache(),this._ensureFirstPageLoaded(),this._debouncerCheckSize=I.debounce(this._debouncerCheckSize,H.after(2e3),this._checkSize.bind(this))}_ensureFirstPageLoaded(){this._hasData||this._dataProviderController.loadFirstPage()}_itemsEqual(e,t){return this.getItemId(e)===this.getItemId(t)}_getItemIndexInArray(e,t){let n=-1;return t.forEach((r,o)=>{this._itemsEqual(r,e)&&(n=o)}),n}scrollToIndex(...e){if(!this.__virtualizer||!this.clientHeight||!this._columnTree){this.__pendingScrollToIndexes=e;return}let t;for(;t!==(t=this._dataProviderController.getFlatIndexByPath(e));)this._scrollToFlatIndex(t);this._dataProviderController.isLoading()&&(this.__pendingScrollToIndexes=e)}__scrollToPendingIndexes(){if(this.__pendingScrollToIndexes&&this.$.items.children.length){const e=this.__pendingScrollToIndexes;delete this.__pendingScrollToIndexes,this.scrollToIndex(...e)}}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Te={BETWEEN:"between",ON_TOP_OR_BETWEEN:"on-top-or-between",ON_GRID:"on-grid"},J={ON_TOP:"on-top",ABOVE:"above",BELOW:"below",EMPTY:"empty"},va=s=>class extends s{static get properties(){return{dropMode:{type:String,sync:!0},rowsDraggable:{type:Boolean,sync:!0},dragFilter:{type:Function,sync:!0},dropFilter:{type:Function,sync:!0},__dndAutoScrollThreshold:{value:50},__draggedItems:{value:()=>[]}}}static get observers(){return["_dragDropAccessChanged(rowsDraggable, dropMode, dragFilter, dropFilter, loading)"]}constructor(){super(),this.__onDocumentDragStart=this.__onDocumentDragStart.bind(this)}ready(){super.ready(),this.$.table.addEventListener("dragstart",this._onDragStart.bind(this)),this.$.table.addEventListener("dragend",this._onDragEnd.bind(this)),this.$.table.addEventListener("dragover",this._onDragOver.bind(this)),this.$.table.addEventListener("dragleave",this._onDragLeave.bind(this)),this.$.table.addEventListener("drop",this._onDrop.bind(this)),this.$.table.addEventListener("dragenter",e=>{this.dropMode&&(e.preventDefault(),e.stopPropagation())})}connectedCallback(){super.connectedCallback(),document.addEventListener("dragstart",this.__onDocumentDragStart,{capture:!0})}disconnectedCallback(){super.disconnectedCallback(),document.removeEventListener("dragstart",this.__onDocumentDragStart,{capture:!0})}_onDragStart(e){if(this.rowsDraggable){let t=e.target;if(t.localName==="vaadin-grid-cell-content"&&(t=t.assignedSlot.parentNode.parentNode),t.parentNode!==this.$.items)return;if(e.stopPropagation(),this.toggleAttribute("dragging-rows",!0),this._safari){const a=t.style.transform;t.style.top=/translateY\((.*)\)/u.exec(a)[1],t.style.transform="none",requestAnimationFrame(()=>{t.style.top="",t.style.transform=a})}const n=t.getBoundingClientRect();e.dataTransfer.setDragImage(t,e.clientX-n.left,e.clientY-n.top);let r=[t];this._isSelected(t._item)&&(r=this.__getViewportRows().filter(a=>this._isSelected(a._item)).filter(a=>!this.dragFilter||this.dragFilter(this.__getRowModel(a)))),this.__draggedItems=r.map(a=>a._item),e.dataTransfer.setData("text",this.__formatDefaultTransferData(r)),_e(t,{dragstart:r.length>1?`${r.length}`:""}),this.style.setProperty("--_grid-drag-start-x",`${e.clientX-n.left+20}px`),this.style.setProperty("--_grid-drag-start-y",`${e.clientY-n.top+10}px`),requestAnimationFrame(()=>{_e(t,{dragstart:!1}),this.style.setProperty("--_grid-drag-start-x",""),this.style.setProperty("--_grid-drag-start-y",""),this.requestContentUpdate()});const o=new CustomEvent("grid-dragstart",{detail:{draggedItems:[...this.__draggedItems],setDragData:(a,l)=>e.dataTransfer.setData(a,l),setDraggedItemsCount:a=>t.setAttribute("dragstart",a)}});o.originalEvent=e,this.dispatchEvent(o)}}_onDragEnd(e){this.toggleAttribute("dragging-rows",!1),e.stopPropagation();const t=new CustomEvent("grid-dragend");t.originalEvent=e,this.dispatchEvent(t),this.__draggedItems=[],this.requestContentUpdate()}_onDragLeave(e){this.dropMode&&(e.stopPropagation(),this._clearDragStyles())}_onDragOver(e){if(this.dropMode){if(this._dropLocation=void 0,this._dragOverItem=void 0,this.__dndAutoScroll(e.clientY)){this._clearDragStyles();return}let t=e.composedPath().find(n=>n.localName==="tr");if(this.__updateRowScrollPositionProperty(t),!this._flatSize||this.dropMode===Te.ON_GRID)this._dropLocation=J.EMPTY;else if(!t||t.parentNode!==this.$.items){if(t)return;if(this.dropMode===Te.BETWEEN||this.dropMode===Te.ON_TOP_OR_BETWEEN)t=Array.from(this.$.items.children).filter(n=>!n.hidden).pop(),this._dropLocation=J.BELOW;else return}else{const n=t.getBoundingClientRect();if(this._dropLocation=J.ON_TOP,this.dropMode===Te.BETWEEN){const r=e.clientY-n.top<n.bottom-e.clientY;this._dropLocation=r?J.ABOVE:J.BELOW}else this.dropMode===Te.ON_TOP_OR_BETWEEN&&(e.clientY-n.top<n.height/3?this._dropLocation=J.ABOVE:e.clientY-n.top>n.height/3*2&&(this._dropLocation=J.BELOW))}if(t&&t.hasAttribute("drop-disabled")){this._dropLocation=void 0;return}e.stopPropagation(),e.preventDefault(),this._dropLocation===J.EMPTY?this.toggleAttribute("dragover",!0):t?(this._dragOverItem=t._item,t.getAttribute("dragover")!==this._dropLocation&&Ei(t,{dragover:this._dropLocation})):this._clearDragStyles()}}__onDocumentDragStart(e){if(e.target.contains(this)){const t=[e.target,this.$.items,this.$.scroller],n=t.map(r=>r.style.cssText);this.$.table.scrollHeight>2e4&&(this.$.scroller.style.display="none"),ji&&(e.target.style.willChange="transform"),Bt&&(this.$.items.style.flexShrink=1),requestAnimationFrame(()=>{t.forEach((r,o)=>{r.style.cssText=n[o]})})}}__dndAutoScroll(e){if(this.__dndAutoScrolling)return!0;const t=this.$.header.getBoundingClientRect().bottom,n=this.$.footer.getBoundingClientRect().top,r=t-e+this.__dndAutoScrollThreshold,o=e-n+this.__dndAutoScrollThreshold;let a=0;if(o>0?a=o*2:r>0&&(a=-r*2),a){const l=this.$.table.scrollTop;if(this.$.table.scrollTop+=a,l!==this.$.table.scrollTop)return this.__dndAutoScrolling=!0,setTimeout(()=>{this.__dndAutoScrolling=!1},20),!0}}__getViewportRows(){const e=this.$.header.getBoundingClientRect().bottom,t=this.$.footer.getBoundingClientRect().top;return Array.from(this.$.items.children).filter(n=>{const r=n.getBoundingClientRect();return r.bottom>e&&r.top<t})}_clearDragStyles(){this.removeAttribute("dragover"),D(this.$.items,e=>{Ei(e,{dragover:null})})}__updateDragSourceParts(e,t){_e(e,{"drag-source":this.__draggedItems.includes(t.item)})}_onDrop(e){if(this.dropMode&&this._dropLocation){e.stopPropagation(),e.preventDefault();const t=e.dataTransfer.types&&Array.from(e.dataTransfer.types).map(r=>({type:r,data:e.dataTransfer.getData(r)}));this._clearDragStyles();const n=new CustomEvent("grid-drop",{bubbles:e.bubbles,cancelable:e.cancelable,detail:{dropTargetItem:this._dragOverItem,dropLocation:this._dropLocation,dragData:t}});n.originalEvent=e,this.dispatchEvent(n)}}__formatDefaultTransferData(e){return e.map(t=>Array.from(t.children).filter(n=>!n.hidden&&!n.part.contains("details-cell")).sort((n,r)=>n._column._order>r._column._order?1:-1).map(n=>n._content.textContent.trim()).filter(n=>n).join("	")).join(`
`)}_dragDropAccessChanged(){this.filterDragAndDrop()}filterDragAndDrop(){D(this.$.items,e=>{e.hidden||this._filterDragAndDrop(e,this.__getRowModel(e))})}_filterDragAndDrop(e,t){const n=this.loading||e.hasAttribute("loading"),r=!this.rowsDraggable||n||this.dragFilter&&!this.dragFilter(t),o=!this.dropMode||n||this.dropFilter&&!this.dropFilter(t);Pe(e,a=>{r?a._content.removeAttribute("draggable"):a._content.setAttribute("draggable",!0)}),_e(e,{"drag-disabled":!!r,"drop-disabled":!!o})}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Ns(s,i){if(!s||!i||s.length!==i.length)return!1;for(let e=0,t=s.length;e<t;e++)if(s[e]instanceof Array&&i[e]instanceof Array){if(!Ns(s[e],i[e]))return!1}else if(s[e]!==i[e])return!1;return!0}const ba=s=>class extends s{static get properties(){return{_columnTree:{type:Object,sync:!0}}}ready(){super.ready(),this._addNodeObserver()}_hasColumnGroups(e){return e.some(t=>t.localName==="vaadin-grid-column-group")}_getChildColumns(e){return se.getColumns(e)}_flattenColumnGroups(e){return e.map(t=>t.localName==="vaadin-grid-column-group"?this._getChildColumns(t):[t]).reduce((t,n)=>t.concat(n),[])}_getColumnTree(){const e=se.getColumns(this),t=[e];let n=e;for(;this._hasColumnGroups(n);)n=this._flattenColumnGroups(n),t.push(n);return t}_debounceUpdateColumnTree(){this.__updateColumnTreeDebouncer=I.debounce(this.__updateColumnTreeDebouncer,W,()=>this._updateColumnTree())}_updateColumnTree(){const e=this._getColumnTree();Ns(e,this._columnTree)||(this._columnTree=e)}_addNodeObserver(){this._observer=new se(this,(e,t)=>{const n=t.flatMap(o=>o._allCells),r=o=>n.filter(a=>a&&a._content.contains(o)).length;this.__removeSorters(this._sorters.filter(r)),this.__removeFilters(this._filters.filter(r)),this._debounceUpdateColumnTree(),this._debouncerCheckImports=I.debounce(this._debouncerCheckImports,H.after(2e3),this._checkImports.bind(this)),this._ensureFirstPageLoaded()})}_checkImports(){["vaadin-grid-column-group","vaadin-grid-filter","vaadin-grid-filter-column","vaadin-grid-tree-toggle","vaadin-grid-selection-column","vaadin-grid-sort-column","vaadin-grid-sorter"].forEach(e=>{this.querySelector(e)&&!customElements.get(e)&&console.warn(`Make sure you have imported the required module for <${e}> element.`)})}_updateFirstAndLastColumn(){Array.from(this.shadowRoot.querySelectorAll("tr")).forEach(e=>this._updateFirstAndLastColumnForRow(e))}_updateFirstAndLastColumnForRow(e){Array.from(e.querySelectorAll('[part~="cell"]:not([part~="details-cell"])')).sort((t,n)=>t._column._order-n._column._order).forEach((t,n,r)=>{oe(t,"first-column",n===0),oe(t,"last-column",n===r.length-1)})}_isColumnElement(e){return e.nodeType===Node.ELEMENT_NODE&&/\bcolumn\b/u.test(e.localName)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ya=s=>class extends s{getEventContext(e){const t={},{cell:n}=this._getGridEventLocation(e);return n&&(t.section=["body","header","footer","details"].find(r=>n.part.contains(`${r}-cell`)),n._column&&(t.column=n._column),(t.section==="body"||t.section==="details")&&Object.assign(t,this.__getRowModel(n.parentElement))),t}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ca=s=>class extends s{static get properties(){return{_filters:{type:Array,value:()=>[]}}}constructor(){super(),this._filterChanged=this._filterChanged.bind(this),this.addEventListener("filter-changed",this._filterChanged)}_filterChanged(e){e.stopPropagation(),this.__addFilter(e.target),this.__applyFilters()}__removeFilters(e){e.length!==0&&(this._filters=this._filters.filter(t=>e.indexOf(t)<0),this.__applyFilters())}__addFilter(e){this._filters.indexOf(e)===-1&&this._filters.push(e)}__applyFilters(){this.dataProvider&&this.isAttached&&this.clearCache()}_mapFilters(){return this._filters.map(e=>({path:e.path,value:e.value}))}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function We(s){return s instanceof HTMLTableRowElement}function qe(s){return s instanceof HTMLTableCellElement}function re(s){return s.matches('[part~="details-cell"]')}const wa=s=>class extends s{static get properties(){return{_headerFocusable:{type:Object,observer:"_focusableChanged",sync:!0},_itemsFocusable:{type:Object,observer:"_focusableChanged",sync:!0},_footerFocusable:{type:Object,observer:"_focusableChanged",sync:!0},_navigatingIsHidden:Boolean,_focusedItemIndex:{type:Number,value:0},_focusedColumnOrder:Number,_focusedCell:{type:Object,observer:"_focusedCellChanged",sync:!0},interacting:{type:Boolean,value:!1,reflectToAttribute:!0,readOnly:!0,observer:"_interactingChanged"}}}get __rowFocusMode(){return[this._headerFocusable,this._itemsFocusable,this._footerFocusable].some(We)}set __rowFocusMode(e){["_itemsFocusable","_footerFocusable","_headerFocusable"].forEach(t=>{const n=this[t];if(e){const r=n&&n.parentElement;qe(n)?this[t]=r:qe(r)&&(this[t]=r.parentElement)}else if(!e&&We(n)){const r=n.firstElementChild;this[t]=r._focusButton||r}})}get _visibleItemsCount(){return this._lastVisibleIndex-this._firstVisibleIndex-1}ready(){super.ready(),!(this._ios||this._android)&&(this.addEventListener("keydown",this._onKeyDown),this.addEventListener("keyup",this._onKeyUp),this.addEventListener("focusin",this._onFocusIn),this.addEventListener("focusout",this._onFocusOut),this.$.table.addEventListener("focusin",this._onContentFocusIn.bind(this)),this.addEventListener("mousedown",()=>{this.toggleAttribute("navigating",!1),this._isMousedown=!0,this._focusedColumnOrder=void 0}),this.addEventListener("mouseup",()=>{this._isMousedown=!1}))}_focusableChanged(e,t){t&&t.setAttribute("tabindex","-1"),e&&this._updateGridSectionFocusTarget(e)}_focusedCellChanged(e,t){t&&O(t,"focused-cell",!1),e&&O(e,"focused-cell",!0)}_interactingChanged(){this._updateGridSectionFocusTarget(this._headerFocusable),this._updateGridSectionFocusTarget(this._itemsFocusable),this._updateGridSectionFocusTarget(this._footerFocusable)}__updateItemsFocusable(){if(!this._itemsFocusable)return;const e=this.shadowRoot.activeElement===this._itemsFocusable;this._getRenderedRows().forEach(t=>{if(t.index===this._focusedItemIndex)if(this.__rowFocusMode)this._itemsFocusable=t;else{let n=this._itemsFocusable.parentElement,r=this._itemsFocusable;if(n){qe(n)&&(r=n,n=n.parentElement);const o=[...n.children].indexOf(r);this._itemsFocusable=this.__getFocusable(t,t.children[o])}}}),e&&this._itemsFocusable.focus()}_onKeyDown(e){const t=e.key;let n;switch(t){case"ArrowUp":case"ArrowDown":case"ArrowLeft":case"ArrowRight":case"PageUp":case"PageDown":case"Home":case"End":n="Navigation";break;case"Enter":case"Escape":case"F2":n="Interaction";break;case"Tab":n="Tab";break;case" ":n="Space";break}this._detectInteracting(e),this.interacting&&n!=="Interaction"&&(n=void 0),n&&this[`_on${n}KeyDown`](e,t)}__ensureFlatIndexInViewport(e){const t=[...this.$.items.children].find(n=>n.index===e);t?this.__scrollIntoViewport(t):this._scrollToFlatIndex(e)}__isRowExpandable(e){return this._hasChildren(e._item)&&!this._isExpanded(e._item)}__isRowCollapsible(e){return this._isExpanded(e._item)}_onNavigationKeyDown(e,t){e.preventDefault();const n=this.__isRTL,r=e.composedPath().find(We),o=e.composedPath().find(qe);let a=0,l=0;switch(t){case"ArrowRight":a=n?-1:1;break;case"ArrowLeft":a=n?1:-1;break;case"Home":this.__rowFocusMode||e.ctrlKey?l=-1/0:a=-1/0;break;case"End":this.__rowFocusMode||e.ctrlKey?l=1/0:a=1/0;break;case"ArrowDown":l=1;break;case"ArrowUp":l=-1;break;case"PageDown":if(this.$.items.contains(r)){const f=this.__getIndexInGroup(r,this._focusedItemIndex);this._scrollToFlatIndex(f)}l=this._visibleItemsCount;break;case"PageUp":l=-this._visibleItemsCount;break}if(this.__rowFocusMode&&!r||!this.__rowFocusMode&&!o)return;const d=n?"ArrowLeft":"ArrowRight",_=n?"ArrowRight":"ArrowLeft";if(t===d){if(this.__rowFocusMode){if(this.__isRowExpandable(r)){this.expandItem(r._item);return}this.__rowFocusMode=!1,this._onCellNavigation(r.firstElementChild,0,0);return}}else if(t===_)if(this.__rowFocusMode){if(this.__isRowCollapsible(r)){this.collapseItem(r._item);return}}else{const f=[...r.children].sort((g,b)=>g._order-b._order);if(o===f[0]||re(o)){this.__rowFocusMode=!0,this._onRowNavigation(r,0);return}}this.__rowFocusMode?this._onRowNavigation(r,l):this._onCellNavigation(o,a,l)}_onRowNavigation(e,t){const{dstRow:n}=this.__navigateRows(t,e);n&&n.focus()}__getIndexInGroup(e,t){const n=e.parentNode;return n===this.$.items?t!==void 0?t:e.index:[...n.children].indexOf(e)}__navigateRows(e,t,n){const r=this.__getIndexInGroup(t,this._focusedItemIndex),o=t.parentNode,a=(o===this.$.items?this._flatSize:o.children.length)-1;let l=Math.max(0,Math.min(r+e,a));if(o!==this.$.items){if(l>r)for(;l<a&&o.children[l].hidden;)l+=1;else if(l<r)for(;l>0&&o.children[l].hidden;)l-=1;return this.toggleAttribute("navigating",!0),{dstRow:o.children[l]}}let d=!1;if(n){const _=re(n);if(o===this.$.items){const f=t._item,{item:g}=this._dataProviderController.getFlatIndexContext(l);_?d=e===0:d=e===1&&this._isDetailsOpened(f)||e===-1&&l!==r&&this._isDetailsOpened(g),d!==_&&(e===1&&d||e===-1&&!d)&&(l=r)}}return this.__ensureFlatIndexInViewport(l),this._focusedItemIndex=l,this.toggleAttribute("navigating",!0),{dstRow:[...o.children].find(_=>!_.hidden&&_.index===l),dstIsRowDetails:d}}_onCellNavigation(e,t,n){const r=e.parentNode,{dstRow:o,dstIsRowDetails:a}=this.__navigateRows(n,r,e);if(!o)return;let l=[...r.children].indexOf(e);this.$.items.contains(e)&&(l=[...this.$.sizer.children].findIndex(g=>g._column===e._column));const d=re(e),_=r.parentNode,f=this.__getIndexInGroup(r,this._focusedItemIndex);if(this._focusedColumnOrder===void 0&&(d?this._focusedColumnOrder=0:this._focusedColumnOrder=this._getColumns(_,f).filter(g=>!g.hidden)[l]._order),a)[...o.children].find(re).focus();else{const g=this.__getIndexInGroup(o,this._focusedItemIndex),b=this._getColumns(_,g).filter(p=>!p.hidden),L=b.map(p=>p._order).sort((p,m)=>p-m),A=L.length-1,M=L.indexOf(L.slice(0).sort((p,m)=>Math.abs(p-this._focusedColumnOrder)-Math.abs(m-this._focusedColumnOrder))[0]),$=n===0&&d?M:Math.max(0,Math.min(M+t,A));$!==M&&(this._focusedColumnOrder=void 0);const c=b.reduce((p,m,R)=>(p[m._order]=R,p),{})[L[$]];let u;if(this.$.items.contains(e)){const p=this.$.sizer.children[c];this._lazyColumns&&(this.__isColumnInViewport(p._column)||p.scrollIntoView(),this.__updateColumnsBodyContentHidden(),this.__updateHorizontalScrollPosition()),u=[...o.children].find(m=>m._column===p._column),this._scrollHorizontallyToCell(u)}else u=o.children[c],this._scrollHorizontallyToCell(u);u.focus({preventScroll:!0})}}_onInteractionKeyDown(e,t){const n=e.composedPath()[0],r=n.localName==="input"&&!/^(button|checkbox|color|file|image|radio|range|reset|submit)$/iu.test(n.type);let o;switch(t){case"Enter":o=this.interacting?!r:!0;break;case"Escape":o=!1;break;case"F2":o=!this.interacting;break}const{cell:a}=this._getGridEventLocation(e);if(this.interacting!==o&&a!==null)if(o){const l=a._content.querySelector("[focus-target]")||[...a._content.querySelectorAll("*")].find(d=>this._isFocusable(d));l&&(e.preventDefault(),l.focus(),this._setInteracting(!0),this.toggleAttribute("navigating",!1))}else e.preventDefault(),this._focusedColumnOrder=void 0,a.focus(),this._setInteracting(!1),this.toggleAttribute("navigating",!0);t==="Escape"&&this._hideTooltip(!0)}_predictFocusStepTarget(e,t){const n=[this.$.table,this._headerFocusable,this.__emptyState?this.$.emptystatecell:this._itemsFocusable,this._footerFocusable,this.$.focusexit];let r=n.indexOf(e);for(r+=t;r>=0&&r<=n.length-1;){let a=n[r];if(a&&!this.__rowFocusMode&&(a=n[r].parentNode),!a||a.hidden)r+=t;else break}let o=n[r];if(o&&!this.__isHorizontallyInViewport(o)){const a=this._getColumnsInOrder().find(l=>this.__isColumnInViewport(l));if(a)if(o===this._headerFocusable)o=a._headerCell;else if(o===this._itemsFocusable){const l=o._column._cells.indexOf(o);o=a._cells[l]}else o===this._footerFocusable&&(o=a._footerCell)}return o}_onTabKeyDown(e){let t=this._predictFocusStepTarget(e.composedPath()[0],e.shiftKey?-1:1);t&&(e.stopPropagation(),t===this._itemsFocusable&&(this.__ensureFlatIndexInViewport(this._focusedItemIndex),this.__updateItemsFocusable(),t=this._itemsFocusable),t.focus(),t!==this.$.table&&t!==this.$.focusexit&&e.preventDefault(),this.toggleAttribute("navigating",!0))}_onSpaceKeyDown(e){e.preventDefault();const t=e.composedPath()[0],n=We(t);(n||!t._content||!t._content.firstElementChild)&&this.dispatchEvent(new CustomEvent(n?"row-activate":"cell-activate",{detail:{model:this.__getRowModel(n?t:t.parentElement)}}))}_onKeyUp(e){if(!/^( |SpaceBar)$/u.test(e.key)||this.interacting)return;e.preventDefault();const t=e.composedPath()[0];if(t._content&&t._content.firstElementChild){const n=this.hasAttribute("navigating");t._content.firstElementChild.dispatchEvent(new MouseEvent("click",{shiftKey:e.shiftKey,bubbles:!0,composed:!0,cancelable:!0})),this.toggleAttribute("navigating",n)}}_onFocusIn(e){this._isMousedown||this.toggleAttribute("navigating",!0);const t=e.composedPath()[0];t===this.$.table||t===this.$.focusexit?(this._isMousedown||this._predictFocusStepTarget(t,t===this.$.table?1:-1).focus(),this._setInteracting(!1)):this._detectInteracting(e)}_onFocusOut(e){this.toggleAttribute("navigating",!1),this._detectInteracting(e),this._hideTooltip(),this._focusedCell=null}_onContentFocusIn(e){const{section:t,cell:n,row:r}=this._getGridEventLocation(e);if(!(!n&&!this.__rowFocusMode)&&(this._detectInteracting(e),t&&(n||r)))if(this._activeRowGroup=t,t===this.$.header?this._headerFocusable=this.__getFocusable(r,n):t===this.$.items?(this._itemsFocusable=this.__getFocusable(r,n),this._focusedItemIndex=r.index):t===this.$.footer&&(this._footerFocusable=this.__getFocusable(r,n)),n){const o=this.getEventContext(e);this.__pendingBodyCellFocus=this.loading&&o.section==="body",!this.__pendingBodyCellFocus&&n!==this.$.emptystatecell&&n.dispatchEvent(new CustomEvent("cell-focus",{bubbles:!0,composed:!0,detail:{context:o}})),this._focusedCell=n._focusButton||n,ne()&&e.target===n&&this._showTooltip(e)}else this._focusedCell=null}__dispatchPendingBodyCellFocus(){this.__pendingBodyCellFocus&&this.shadowRoot.activeElement===this._itemsFocusable&&this._itemsFocusable.dispatchEvent(new Event("focusin",{bubbles:!0,composed:!0}))}__getFocusable(e,t){return this.__rowFocusMode?e:t._focusButton||t}_detectInteracting(e){const t=e.composedPath().some(n=>n.localName==="slot"&&this.shadowRoot.contains(n));this._setInteracting(t),this.__updateHorizontalScrollPosition()}_updateGridSectionFocusTarget(e){if(!e)return;const t=this._getGridSectionFromFocusTarget(e),n=this.interacting&&t===this._activeRowGroup;e.tabIndex=n?-1:0}_preventScrollerRotatingCellFocus(){this._activeRowGroup===this.$.items&&(this.__preventScrollerRotatingCellFocusDebouncer=I.debounce(this.__preventScrollerRotatingCellFocusDebouncer,X,()=>{const e=this._activeRowGroup===this.$.items;this._getRenderedRows().some(n=>n.index===this._focusedItemIndex)?(this.__updateItemsFocusable(),e&&!this.__rowFocusMode&&(this._focusedCell=this._itemsFocusable),this._navigatingIsHidden&&(this.toggleAttribute("navigating",!0),this._navigatingIsHidden=!1)):e&&(this._focusedCell=null,this.hasAttribute("navigating")&&(this._navigatingIsHidden=!0,this.toggleAttribute("navigating",!1)))}))}_getColumns(e,t){let n=this._columnTree.length-1;return e===this.$.header?n=t:e===this.$.footer&&(n=this._columnTree.length-1-t),this._columnTree[n]}__isValidFocusable(e){return this.$.table.contains(e)&&e.offsetHeight}_resetKeyboardNavigation(){if(!this.$&&this.performUpdate&&this.performUpdate(),["header","footer"].forEach(e=>{if(!this.__isValidFocusable(this[`_${e}Focusable`])){const t=[...this.$[e].children].find(r=>r.offsetHeight),n=t?[...t.children].find(r=>!r.hidden):null;t&&n&&(this[`_${e}Focusable`]=this.__getFocusable(t,n))}}),!this.__isValidFocusable(this._itemsFocusable)&&this.$.items.firstElementChild){const e=this.__getFirstVisibleItem(),t=e?[...e.children].find(n=>!n.hidden):null;t&&e&&(this._focusedColumnOrder=void 0,this._itemsFocusable=this.__getFocusable(e,t))}else this.__updateItemsFocusable()}_scrollHorizontallyToCell(e){if(e.hasAttribute("frozen")||e.hasAttribute("frozen-to-end")||re(e))return;const t=e.getBoundingClientRect(),n=e.parentNode,r=Array.from(n.children).indexOf(e),o=this.$.table.getBoundingClientRect(),a=this.$.table.clientWidth-this.$.table.offsetWidth;let l=o.left-(this.__isRTL?a:0),d=o.right+(this.__isRTL?0:a);for(let _=r-1;_>=0;_--){const f=n.children[_];if(!(f.hasAttribute("hidden")||re(f))&&(f.hasAttribute("frozen")||f.hasAttribute("frozen-to-end"))){l=f.getBoundingClientRect().right;break}}for(let _=r+1;_<n.children.length;_++){const f=n.children[_];if(!(f.hasAttribute("hidden")||re(f))&&(f.hasAttribute("frozen")||f.hasAttribute("frozen-to-end"))){d=f.getBoundingClientRect().left;break}}t.left<l&&(this.$.table.scrollLeft+=t.left-l),t.right>d&&(this.$.table.scrollLeft+=t.right-d)}_getGridEventLocation(e){const t=e.__composedPath||e.composedPath(),n=t.indexOf(this.$.table),r=n>=1?t[n-1]:null,o=n>=2?t[n-2]:null,a=n>=3?t[n-3]:null;return{section:r,row:o,cell:a}}_getGridSectionFromFocusTarget(e){return e===this._headerFocusable?this.$.header:e===this._itemsFocusable?this.$.items:e===this._footerFocusable?this.$.footer:null}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const xa=s=>class extends s{static get properties(){return{__hostVisible:{type:Boolean,value:!1},__tableRect:Object,__headerRect:Object,__itemsRect:Object,__footerRect:Object}}ready(){super.ready();const i=new ResizeObserver(e=>{e.findLast(({target:l})=>l===this)&&(this.__hostVisible=this.checkVisibility());const n=e.findLast(({target:l})=>l===this.$.table);n&&(this.__tableRect=n.contentRect);const r=e.findLast(({target:l})=>l===this.$.header);r&&(this.__headerRect=r.contentRect);const o=e.findLast(({target:l})=>l===this.$.items);o&&(this.__itemsRect=o.contentRect);const a=e.findLast(({target:l})=>l===this.$.footer);a&&(this.__footerRect=a.contentRect)});i.observe(this),i.observe(this.$.table),i.observe(this.$.header),i.observe(this.$.items),i.observe(this.$.footer)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ea=s=>class extends s{static get properties(){return{detailsOpenedItems:{type:Array,value:()=>[],sync:!0},rowDetailsRenderer:{type:Function,sync:!0},_detailsCells:{type:Array}}}static get observers(){return["_detailsOpenedItemsChanged(detailsOpenedItems, rowDetailsRenderer)","_rowDetailsRendererChanged(rowDetailsRenderer)"]}ready(){super.ready(),this._detailsCellResizeObserver=new ResizeObserver(e=>{e.forEach(({target:t})=>{this._updateDetailsCellHeight(t.parentElement)})})}_rowDetailsRendererChanged(e){e&&this._columnTree&&D(this.$.items,t=>{t.querySelector("[part~=details-cell]")||(this.__initRow(t,this._columnTree[this._columnTree.length-1]),this.__updateRow(t))})}_detailsOpenedItemsChanged(e,t){D(this.$.items,n=>{if(n.hasAttribute("details-opened")){this.__updateRow(n);return}t&&this._isDetailsOpened(n._item)&&this.__updateRow(n)})}_configureDetailsCell(e){O(e,"cell",!0),O(e,"details-cell",!0),e.toggleAttribute("frozen",!0),this._detailsCellResizeObserver.observe(e)}_toggleDetailsCell(e,t){const n=e.querySelector('[part~="details-cell"]');n&&(n.hidden=!t,!n.hidden&&this.rowDetailsRenderer&&(n._renderer=this.rowDetailsRenderer))}_updateDetailsCellHeight(e){const t=e.querySelector('[part~="details-cell"]');t&&(this.__updateDetailsRowPadding(e,t),requestAnimationFrame(()=>this.__updateDetailsRowPadding(e,t)))}__updateDetailsRowPadding(e,t){t.hidden?e.style.removeProperty("padding-bottom"):e.style.setProperty("padding-bottom",`${t.offsetHeight}px`)}_updateDetailsCellHeights(){D(this.$.items,e=>{this._updateDetailsCellHeight(e)})}_isDetailsOpened(e){return this.detailsOpenedItems&&this._getItemIndexInArray(e,this.detailsOpenedItems)!==-1}openItemDetails(e){this._isDetailsOpened(e)||(this.detailsOpenedItems=[...this.detailsOpenedItems,e])}closeItemDetails(e){this._isDetailsOpened(e)&&(this.detailsOpenedItems=this.detailsOpenedItems.filter(t=>!this._itemsEqual(t,e)))}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Sa{constructor(i,e){this.host=i,this.scrollTarget=e||i,this.__boundOnScroll=this.__onScroll.bind(this)}hostConnected(){this.initialized||(this.initialized=!0,this.observe())}observe(){const{host:i}=this;this.__resizeObserver=new ResizeObserver(()=>{this.__debounceOverflow=I.debounce(this.__debounceOverflow,X,()=>{this.__updateOverflow()})}),this.__resizeObserver.observe(i),[...i.children].forEach(e=>{this.__resizeObserver.observe(e)}),this.__childObserver=new MutationObserver(e=>{e.forEach(({addedNodes:t,removedNodes:n})=>{t.forEach(r=>{r.nodeType===Node.ELEMENT_NODE&&this.__resizeObserver.observe(r)}),n.forEach(r=>{r.nodeType===Node.ELEMENT_NODE&&this.__resizeObserver.unobserve(r)})}),this.__updateOverflow()}),this.__childObserver.observe(i,{childList:!0}),this.scrollTarget.addEventListener("scroll",this.__boundOnScroll),this.__updateOverflow()}__onScroll(){this.__updateOverflow()}__updateOverflow(){const i=this.scrollTarget;let e="";i.scrollTop>0&&(e+=" top"),Math.ceil(i.scrollTop)<Math.ceil(i.scrollHeight-i.clientHeight)&&(e+=" bottom");const t=Math.abs(i.scrollLeft);t>0&&(e+=" start"),Math.ceil(t)<Math.ceil(i.scrollWidth-i.clientWidth)&&(e+=" end"),e=e.trim(),e.length>0&&this.host.getAttribute("overflow")!==e?this.host.setAttribute("overflow",e):e.length===0&&this.host.hasAttribute("overflow")&&this.host.removeAttribute("overflow")}}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ki={SCROLLING:500,UPDATE_CONTENT_VISIBILITY:100},Ia=s=>class extends s{static get properties(){return{columnRendering:{type:String,value:"eager",sync:!0},_frozenCells:{type:Array,value:()=>[]},_frozenToEndCells:{type:Array,value:()=>[]}}}static get observers(){return["__columnRenderingChanged(_columnTree, columnRendering)"]}get _scrollLeft(){return this.$.table.scrollLeft}get _scrollTop(){return this.$.table.scrollTop}set _scrollTop(e){this.$.table.scrollTop=e}get _lazyColumns(){return this.columnRendering==="lazy"}ready(){super.ready(),this.scrollTarget=this.$.table,this.$.items.addEventListener("focusin",e=>{const t=e.composedPath(),n=t[t.indexOf(this.$.items)-1];if(n){if(!this._isMousedown){const r=this.$.table.clientHeight,o=this.$.header.clientHeight,a=this.$.footer.clientHeight,l=r-o-a,_=n.clientHeight>l?e.target:n;this.__scrollIntoViewport(_)}this.$.table.contains(e.relatedTarget)||this.$.table.dispatchEvent(new CustomEvent("virtualizer-element-focused",{detail:{element:n}}))}}),this.$.table.addEventListener("scroll",()=>this._afterScroll()),this.__overflowController=new Sa(this,this.$.table),this.addController(this.__overflowController)}_scrollToFlatIndex(e){e=Math.min(this._flatSize-1,Math.max(0,e)),this.__virtualizer.scrollToIndex(e);const t=[...this.$.items.children].find(n=>n.index===e);this.__scrollIntoViewport(t)}__scrollIntoViewport(e){if(!e)return;const t=e.getBoundingClientRect(),n=getComputedStyle(e),r=t.top+parseInt(n.scrollMarginTop||0),o=t.bottom+parseInt(n.scrollMarginBottom||0),a=this.$.footer.getBoundingClientRect().top,l=this.$.header.getBoundingClientRect().bottom;o>a?this.$.table.scrollTop+=o-a:r<l&&(this.$.table.scrollTop-=l-r)}_scheduleScrolling(){this._scrollingFrame||(this._scrollingFrame=requestAnimationFrame(()=>this.$.scroller.toggleAttribute("scrolling",!0))),this._debounceScrolling=I.debounce(this._debounceScrolling,H.after(ki.SCROLLING),()=>{cancelAnimationFrame(this._scrollingFrame),delete this._scrollingFrame,this.$.scroller.toggleAttribute("scrolling",!1)})}_afterScroll(){this.__updateHorizontalScrollPosition(),this.hasAttribute("reordering")||this._scheduleScrolling(),this.hasAttribute("navigating")||this._hideTooltip(!0),this._debounceColumnContentVisibility=I.debounce(this._debounceColumnContentVisibility,H.after(ki.UPDATE_CONTENT_VISIBILITY),()=>{this._lazyColumns&&this.__cachedScrollLeft!==this._scrollLeft&&(this.__cachedScrollLeft=this._scrollLeft,this.__updateColumnsBodyContentHidden())})}__updateColumnsBodyContentHidden(){if(!this._columnTree||!this._areSizerCellsAssigned())return;const e=this._getColumnsInOrder();let t=!1;if(e.forEach(n=>{const r=this._lazyColumns&&!this.__isColumnInViewport(n);n._bodyContentHidden!==r&&(t=!0,n._cells.forEach(o=>{if(o!==n._sizerCell){if(r)o.remove();else if(o.__parentRow){const a=[...o.__parentRow.children].find(l=>e.indexOf(l._column)>e.indexOf(n));o.__parentRow.insertBefore(o,a)}}})),n._bodyContentHidden=r}),t&&this._frozenCellsChanged(),this._lazyColumns){const n=[...e].reverse().find(a=>a.frozen),r=this.__getColumnEnd(n),o=e.find(a=>!a.frozen&&!a._bodyContentHidden);this.__lazyColumnsStart=this.__getColumnStart(o)-r,this.$.items.style.setProperty("--_grid-lazy-columns-start",`${this.__lazyColumnsStart}px`),this._resetKeyboardNavigation()}}__getColumnEnd(e){return e?e._sizerCell.offsetLeft+(this.__isRTL?0:e._sizerCell.offsetWidth):this.__isRTL?this.$.table.clientWidth:0}__getColumnStart(e){return e?e._sizerCell.offsetLeft+(this.__isRTL?e._sizerCell.offsetWidth:0):this.__isRTL?this.$.table.clientWidth:0}__isColumnInViewport(e){return e.frozen||e.frozenToEnd?!0:this.__isHorizontallyInViewport(e._sizerCell)}__isHorizontallyInViewport(e){return e.offsetLeft+e.offsetWidth>=this._scrollLeft&&e.offsetLeft<=this._scrollLeft+this.clientWidth}__columnRenderingChanged(e,t){t==="eager"?this.$.scroller.removeAttribute("column-rendering"):this.$.scroller.setAttribute("column-rendering",t),this.__updateColumnsBodyContentHidden()}_frozenCellsChanged(){this._debouncerCacheElements=I.debounce(this._debouncerCacheElements,W,()=>{Array.from(this.shadowRoot.querySelectorAll('[part~="cell"]')).forEach(e=>{e.style.transform=""}),this._frozenCells=Array.prototype.slice.call(this.$.table.querySelectorAll("[frozen]")),this._frozenToEndCells=Array.prototype.slice.call(this.$.table.querySelectorAll("[frozen-to-end]")),this.__updateHorizontalScrollPosition()}),this._debounceUpdateFrozenColumn()}_debounceUpdateFrozenColumn(){this.__debounceUpdateFrozenColumn=I.debounce(this.__debounceUpdateFrozenColumn,W,()=>this._updateFrozenColumn())}_updateFrozenColumn(){if(!this._columnTree)return;const e=this._columnTree[this._columnTree.length-1].slice(0);e.sort((r,o)=>r._order-o._order);let t,n;for(let r=0;r<e.length;r++){const o=e[r];o._lastFrozen=!1,o._firstFrozenToEnd=!1,n===void 0&&o.frozenToEnd&&!o.hidden&&(n=r),o.frozen&&!o.hidden&&(t=r)}t!==void 0&&(e[t]._lastFrozen=!0),n!==void 0&&(e[n]._firstFrozenToEnd=!0),this.__updateColumnsBodyContentHidden()}__updateHorizontalScrollPosition(){if(!this._columnTree)return;const e=this.$.table.scrollWidth,t=this.$.table.clientWidth,n=Math.max(0,this.$.table.scrollLeft),r=Is(this.$.table,this.getAttribute("dir")),o=`translate(${-n}px, 0)`;this.$.header.style.transform=o,this.$.footer.style.transform=o,this.$.items.style.transform=o;const a=this.__isRTL?r+t-e:n;this.__horizontalScrollPosition=a;const l=`translate(${a}px, 0)`;this._frozenCells.forEach(A=>{A.style.transform=l});const d=this.__isRTL?r:n+t-e,_=`translate(${d}px, 0)`;let f=_;if(this._lazyColumns&&this._areSizerCellsAssigned()){const A=this._getColumnsInOrder(),M=[...A].reverse().find(p=>!p.frozenToEnd&&!p._bodyContentHidden),$=this.__getColumnEnd(M),h=A.find(p=>p.frozenToEnd),c=this.__getColumnStart(h);f=`translate(${d+(c-$)+this.__lazyColumnsStart}px, 0)`}this._frozenToEndCells.forEach(A=>{this.$.items.contains(A)?A.style.transform=f:A.style.transform=_});const g=this.shadowRoot.querySelector("[part~='row']:focus");g&&this.__updateRowScrollPositionProperty(g);const b=this.$.header.querySelector("[part~='last-header-row']");b&&this.__updateRowScrollPositionProperty(b);const L=this.$.footer.querySelector("[part~='first-footer-row']");L&&this.__updateRowScrollPositionProperty(L)}__updateRowScrollPositionProperty(e){if(!(e instanceof HTMLTableRowElement))return;const t=`${this.__horizontalScrollPosition}px`;e.style.getPropertyValue("--_grid-horizontal-scroll-position")!==t&&e.style.setProperty("--_grid-horizontal-scroll-position",t)}_areSizerCellsAssigned(){return this._getColumnsInOrder().every(e=>e._sizerCell)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Aa=s=>class extends s{static get properties(){return{selectedItems:{type:Object,notify:!0,value:()=>[],sync:!0},isItemSelectable:{type:Function,notify:!0},__selectedKeys:{type:Object,computed:"__computeSelectedKeys(itemIdPath, selectedItems)"}}}static get observers(){return["__selectedItemsChanged(itemIdPath, selectedItems, isItemSelectable)"]}_isSelected(e){return this.__selectedKeys.has(this.getItemId(e))}__isItemSelectable(e){return!this.isItemSelectable||!e?!0:this.isItemSelectable(e)}selectItem(e){this._isSelected(e)||(this.selectedItems=[...this.selectedItems,e])}deselectItem(e){this._isSelected(e)&&(this.selectedItems=this.selectedItems.filter(t=>!this._itemsEqual(t,e)))}__selectedItemsChanged(){this.requestContentUpdate()}__computeSelectedKeys(e,t){const n=t||[],r=new Set;return n.forEach(o=>{r.add(this.getItemId(o))}),r}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let Ri="prepend";const Ta=s=>class extends s{static get properties(){return{multiSort:{type:Boolean,value:!1},multiSortPriority:{type:String,value:()=>Ri},multiSortOnShiftClick:{type:Boolean,value:!1},_sorters:{type:Array,value:()=>[]},_previousSorters:{type:Array,value:()=>[]}}}static setDefaultMultiSortPriority(e){Ri=["append","prepend"].includes(e)?e:"prepend"}ready(){super.ready(),this.addEventListener("sorter-changed",this._onSorterChanged)}_onSorterChanged(e){const t=e.target;e.stopPropagation(),t._grid=this,this.__updateSorter(t,e.detail.shiftClick,e.detail.fromSorterClick),this.__applySorters()}__removeSorters(e){e.length!==0&&(this._sorters=this._sorters.filter(t=>!e.includes(t)),this.__applySorters())}__updateSortOrders(){this._sorters.forEach(t=>{t._order=null});const e=this._getActiveSorters();e.length>1&&e.forEach((t,n)=>{t._order=n})}__updateSorter(e,t,n){if(!e.direction&&!this._sorters.includes(e))return;e._order=null;const r=this._sorters.filter(o=>o!==e);this.multiSort&&(!this.multiSortOnShiftClick||!n)||this.multiSortOnShiftClick&&t?this.multiSortPriority==="append"?this._sorters=[...r,e]:this._sorters=[e,...r]:(e.direction||this.multiSortOnShiftClick)&&(this._sorters=e.direction?[e]:[],r.forEach(o=>{o._order=null,o.direction=null}))}__applySorters(){this.__updateSortOrders(),this.dataProvider&&this.isAttached&&JSON.stringify(this._previousSorters)!==JSON.stringify(this._mapSorters())&&this.__debounceClearCache(),this.__a11yUpdateSorters(),this._previousSorters=this._mapSorters()}_getActiveSorters(){return this._sorters.filter(e=>e.direction&&e.isConnected)}_mapSorters(){return this._getActiveSorters().map(e=>({path:e.path,direction:e.direction}))}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ka=s=>class extends s{static get properties(){return{cellPartNameGenerator:{type:Function,sync:!0}}}static get observers(){return["__cellPartNameGeneratorChanged(cellPartNameGenerator)"]}__cellPartNameGeneratorChanged(){this.generateCellPartNames()}generateCellPartNames(){D(this.$.items,e=>{e.hidden||this._generateCellPartNames(e,this.__getRowModel(e))})}_generateCellPartNames(e,t){Pe(e,n=>{if(n.__generatedParts&&n.__generatedParts.forEach(r=>{O(n,r,null)}),this.cellPartNameGenerator&&!e.hasAttribute("loading")){const r=this.cellPartNameGenerator(n._column,t);n.__generatedParts=r&&r.split(" ").filter(o=>o.length>0),n.__generatedParts&&n.__generatedParts.forEach(o=>{O(n,o,!0)})}})}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ra=s=>class extends _a(ua(ma(ba(la(Ia(Aa(Ta(Ea(wa(aa(Ca(pa(fa(ya(va(ka(jt(xa(s))))))))))))))))))){static get observers(){return["_columnTreeChanged(_columnTree)","_flatSizeChanged(_flatSize, __virtualizer, _hasData, _columnTree)"]}static get properties(){return{_safari:{type:Boolean,value:Bt},_ios:{type:Boolean,value:ve},_firefox:{type:Boolean,value:Gi},_android:{type:Boolean,value:Pt},_touchDevice:{type:Boolean,value:Me},allRowsVisible:{type:Boolean,value:!1,reflectToAttribute:!0},isAttached:{value:!1},__gridElement:{type:Boolean,value:!0},__hasEmptyStateContent:{type:Boolean,value:!1},__emptyState:{type:Boolean,computed:"__computeEmptyState(_flatSize, __hasEmptyStateContent)"}}}get _firstVisibleIndex(){const i=this.__getFirstVisibleItem();return i?i.index:void 0}get _lastVisibleIndex(){const i=this.__getLastVisibleItem();return i?i.index:void 0}connectedCallback(){super.connectedCallback(),this.isAttached=!0,this.__virtualizer.hostConnected()}disconnectedCallback(){super.disconnectedCallback(),this.isAttached=!1,this._hideTooltip(!0)}__getFirstVisibleItem(){return this._getRenderedRows().find(i=>this._isInViewport(i))}__getLastVisibleItem(){return this._getRenderedRows().reverse().find(i=>this._isInViewport(i))}_isInViewport(i){const e=this.$.table.getBoundingClientRect(),t=i.getBoundingClientRect(),n=this.$.header.getBoundingClientRect().height,r=this.$.footer.getBoundingClientRect().height;return t.bottom>e.top+n&&t.top<e.bottom-r}_getRenderedRows(){return Array.from(this.$.items.children).filter(i=>!i.hidden).sort((i,e)=>i.index-e.index)}_getRowContainingNode(i){const e=ss("vaadin-grid-cell-content",i);return e?e.assignedSlot.parentElement.parentElement:void 0}_isItemAssignedToRow(i,e){const t=this.__getRowModel(e);return this.getItemId(i)===this.getItemId(t.item)}ready(){super.ready(),this.__virtualizer=new oa({createElements:this._createScrollerRows.bind(this),updateElement:this._updateScrollerItem.bind(this),scrollContainer:this.$.items,scrollTarget:this.$.table,reorderElements:!0,__disableHeightPlaceholder:!0}),this._tooltipController=new Q(this),this.addController(this._tooltipController),this._tooltipController.setManual(!0),this.__emptyStateContentObserver=new te(this.$.emptystateslot,({currentNodes:i})=>{this.$.emptystatecell._content=i[0],this.__hasEmptyStateContent=!!this.$.emptystatecell._content})}updated(i){super.updated(i),i.has("__hostVisible")&&!i.get("__hostVisible")&&(this._resetKeyboardNavigation(),requestAnimationFrame(()=>this.__scrollToPendingIndexes())),(i.has("__headerRect")||i.has("__footerRect")||i.has("__itemsRect"))&&setTimeout(()=>this.__updateMinHeight()),i.has("__tableRect")&&(setTimeout(()=>this.__updateColumnsBodyContentHidden()),this.__updateHorizontalScrollPosition())}__getBodyCellCoordinates(i){if(this.$.items.contains(i)&&i.localName==="td")return{item:i.parentElement._item,column:i._column}}__focusBodyCell({item:i,column:e}){const t=this._getRenderedRows().find(r=>r._item===i),n=t&&[...t.children].find(r=>r._column===e);n&&n.focus()}_focusFirstVisibleRow(){const i=this.__getFirstVisibleItem();this.__rowFocusMode=!0,i.focus()}_flatSizeChanged(i,e,t,n){if(e&&t&&n){const r=this.shadowRoot.activeElement,o=this.__getBodyCellCoordinates(r),a=e.size||0;e.size=i,e.update(a-1,a-1),i<a&&e.update(i-1,i-1),o&&r.parentElement.hidden&&this.__focusBodyCell(o),this._resetKeyboardNavigation()}}_createScrollerRows(i){const e=[];for(let t=0;t<i;t++){const n=document.createElement("tr");n.setAttribute("role","row"),n.setAttribute("tabindex","-1"),O(n,"row",!0),O(n,"body-row",!0),this._columnTree&&this.__initRow(n,this._columnTree[this._columnTree.length-1],"body",!1,!0),e.push(n)}return this._columnTree&&this._columnTree[this._columnTree.length-1].forEach(t=>{t.isConnected&&t._cells&&(t._cells=[...t._cells])}),this.__afterCreateScrollerRowsDebouncer=I.debounce(this.__afterCreateScrollerRowsDebouncer,X,()=>{this._afterScroll()}),e}_createCell(i,e){const n=`vaadin-grid-cell-content-${this._contentIndex=this._contentIndex+1||0}`,r=document.createElement("vaadin-grid-cell-content");r.setAttribute("slot",n);const o=document.createElement(i);o.id=n.replace("-content-","-"),o.setAttribute("role",i==="td"?"gridcell":"columnheader"),!Pt&&!ve&&(o.addEventListener("mouseenter",l=>{this.$.scroller.hasAttribute("scrolling")||this._showTooltip(l)}),o.addEventListener("mouseleave",()=>{this._hideTooltip()}),o.addEventListener("mousedown",()=>{this._hideTooltip(!0)}));const a=document.createElement("slot");if(a.setAttribute("name",n),e&&e._focusButtonMode){const l=document.createElement("div");l.setAttribute("role","button"),l.setAttribute("tabindex","-1"),o.appendChild(l),o._focusButton=l,o.focus=function(d){o._focusButton.focus(d)},l.appendChild(a)}else o.setAttribute("tabindex","-1"),o.appendChild(a);return o._content=r,r.addEventListener("mousedown",()=>{if(ji){const l=d=>{const _=r.contains(this.getRootNode().activeElement),f=d.composedPath().includes(r);!_&&f&&o.focus({preventScroll:!0}),document.removeEventListener("mouseup",l,!0)};document.addEventListener("mouseup",l,!0)}else setTimeout(()=>{r.contains(this.getRootNode().activeElement)||o.focus({preventScroll:!0})})}),o}__initRow(i,e,t="body",n=!1,r=!1){const o=document.createDocumentFragment();Pe(i,a=>{a._vacant=!0}),i.innerHTML="",t==="body"&&(i.__cells=[],i.__detailsCell=null),e.filter(a=>!a.hidden).forEach((a,l,d)=>{let _;if(t==="body"){a._cells||(a._cells=[]),_=a._cells.find(g=>g._vacant),_||(_=this._createCell("td",a),a._onCellKeyDown&&_.addEventListener("keydown",a._onCellKeyDown.bind(a)),a._cells.push(_)),O(_,"cell",!0),O(_,"body-cell",!0),_.__parentRow=i,i.__cells.push(_);const f=i===this.$.sizer;if((!a._bodyContentHidden||f)&&i.appendChild(_),f&&(a._sizerCell=_),l===d.length-1&&this.rowDetailsRenderer){this._detailsCells||(this._detailsCells=[]);const g=this._detailsCells.find(b=>b._vacant)||this._createCell("td");this._detailsCells.indexOf(g)===-1&&this._detailsCells.push(g),g._content.parentElement||o.appendChild(g._content),this._configureDetailsCell(g),i.appendChild(g),i.__detailsCell=g,this.__a11ySetRowDetailsCell(i,g),g._vacant=!1}r||(a._cells=[...a._cells])}else{const f=t==="header"?"th":"td";n||a.localName==="vaadin-grid-column-group"?(_=a[`_${t}Cell`],_||(_=this._createCell(f),a._onCellKeyDown&&_.addEventListener("keydown",a._onCellKeyDown.bind(a))),_._column=a,i.appendChild(_),a[`_${t}Cell`]=_):(a._emptyCells||(a._emptyCells=[]),_=a._emptyCells.find(g=>g._vacant)||this._createCell(f),_._column=a,i.appendChild(_),a._emptyCells.indexOf(_)===-1&&a._emptyCells.push(_)),O(_,"cell",!0),O(_,`${t}-cell`,!0)}_._content.parentElement||o.appendChild(_._content),_._vacant=!1,_._column=a}),t!=="body"&&this.__debounceUpdateHeaderFooterRowVisibility(i),this.appendChild(o),this._frozenCellsChanged(),this._updateFirstAndLastColumnForRow(i)}__debounceUpdateHeaderFooterRowVisibility(i){i.__debounceUpdateHeaderFooterRowVisibility=I.debounce(i.__debounceUpdateHeaderFooterRowVisibility,W,()=>this.__updateHeaderFooterRowVisibility(i))}__updateHeaderFooterRowVisibility(i){if(!i)return;const e=Array.from(i.children).filter(t=>{const n=t._column;if(n._emptyCells&&n._emptyCells.indexOf(t)>-1)return!1;if(i.parentElement===this.$.header){if(n.headerRenderer)return!0;if(n.header===null)return!1;if(n.path||n.header!==void 0)return!0}else if(n.footerRenderer)return!0;return!1});i.hidden!==!e.length&&(i.hidden=!e.length),i.parentElement===this.$.header&&(this.$.table.toggleAttribute("has-header",this.$.header.querySelector("tr:not([hidden])")),this.__updateHeaderFooterRowParts("header")),i.parentElement===this.$.footer&&(this.$.table.toggleAttribute("has-footer",this.$.footer.querySelector("tr:not([hidden])")),this.__updateHeaderFooterRowParts("footer")),this._resetKeyboardNavigation(),this.__a11yUpdateGridSize(this.size,this._columnTree,this.__emptyState)}_updateScrollerItem(i,e){this._preventScrollerRotatingCellFocus(i,e),this._columnTree&&(i.index=e,this.__ensureRowItem(i),this.__ensureRowHierarchy(i),this.__updateRow(i))}_columnTreeChanged(i){this._renderColumnTree(i),this.__updateColumnsBodyContentHidden()}__updateRowOrderParts(i){_e(i,{first:i.index===0,last:i.index===this._flatSize-1,odd:i.index%2!==0,even:i.index%2===0})}__updateRowStateParts(i,{item:e,expanded:t,selected:n,detailsOpened:r}){_e(i,{expanded:t,collapsed:this.__isRowExpandable(i),selected:n,nonselectable:this.__isItemSelectable(e)===!1,"details-opened":r})}__computeEmptyState(i,e){return i===0&&e}_renderColumnTree(i){for(D(this.$.items,e=>{this.__initRow(e,i[i.length-1],"body",!1,!0),this.__updateRow(e)});this.$.header.children.length<i.length;){const e=document.createElement("tr");e.setAttribute("role","row"),e.setAttribute("tabindex","-1"),O(e,"row",!0),O(e,"header-row",!0),this.$.header.appendChild(e);const t=document.createElement("tr");t.setAttribute("role","row"),t.setAttribute("tabindex","-1"),O(t,"row",!0),O(t,"footer-row",!0),this.$.footer.appendChild(t)}for(;this.$.header.children.length>i.length;)this.$.header.removeChild(this.$.header.firstElementChild),this.$.footer.removeChild(this.$.footer.firstElementChild);D(this.$.header,(e,t)=>{this.__initRow(e,i[t],"header",t===i.length-1)}),D(this.$.footer,(e,t)=>{this.__initRow(e,i[i.length-1-t],"footer",t===0)}),this.__initRow(this.$.sizer,i[i.length-1]),this.__updateHeaderFooterRowParts("header"),this.__updateHeaderFooterRowParts("footer"),this._resizeHandler(),this._frozenCellsChanged(),this._updateFirstAndLastColumn(),this._resetKeyboardNavigation(),this.__a11yUpdateHeaderRows(),this.__a11yUpdateFooterRows(),this.generateCellPartNames(),this.__updateHeaderAndFooter()}__updateHeaderFooterRowParts(i){const e=[...this.$[i].querySelectorAll("tr:not([hidden])")];[...this.$[i].children].forEach(t=>{O(t,`first-${i}-row`,t===e.at(0)),O(t,`last-${i}-row`,t===e.at(-1)),ye(t).forEach(n=>{O(n,`first-${i}-row-cell`,t===e.at(0)),O(n,`last-${i}-row-cell`,t===e.at(-1))})})}__updateRowLoading(i,e){const t=ye(i);pt(i,"loading",e),tt(t,"loading-row-cell",e),e&&this._generateCellPartNames(i)}__updateRow(i){this.__a11yUpdateRowRowindex(i),this.__updateRowOrderParts(i);const e=this.__getRowItem(i);if(e)this.__updateRowLoading(i,!1);else{this.__updateRowLoading(i,!0);return}i._item=e;const t=this.__getRowModel(i);this._toggleDetailsCell(i,t.detailsOpened),this.__a11yUpdateRowLevel(i,t.level),this.__a11yUpdateRowSelected(i,t.selected),this.__updateRowStateParts(i,t),this._generateCellPartNames(i,t),this._filterDragAndDrop(i,t),this.__updateDragSourceParts(i,t),D(i,n=>{if(!(n._column&&!n._column.isConnected)&&n._renderer){const r=n._column||this;n._renderer.call(r,n._content,r,t)}}),this._updateDetailsCellHeight(i),this.__a11yUpdateRowExpanded(i,t.expanded)}_resizeHandler(){this._updateDetailsCellHeights(),this.__updateHorizontalScrollPosition()}__getRowModel(i){return{index:i.index,item:i._item,level:this.__getRowLevel(i),expanded:this._isExpanded(i._item),selected:this._isSelected(i._item),hasChildren:this._hasChildren(i._item),detailsOpened:!!this.rowDetailsRenderer&&this._isDetailsOpened(i._item)}}_showTooltip(i){const e=this._tooltipController.node;if(e&&e.isConnected){const t=i.target;if(!this.__isCellFullyVisible(t))return;this._tooltipController.setTarget(t),this._tooltipController.setContext(this.getEventContext(i)),e._stateController.open({focus:i.type==="focusin",hover:i.type==="mouseenter"})}}__isCellFullyVisible(i){if(i.hasAttribute("frozen")||i.hasAttribute("frozen-to-end"))return!0;let{left:e,right:t}=this.getBoundingClientRect();const n=[...i.parentNode.children].find(a=>a.hasAttribute("last-frozen"));if(n){const a=n.getBoundingClientRect();e=this.__isRTL?e:a.right,t=this.__isRTL?a.left:t}const r=[...i.parentNode.children].find(a=>a.hasAttribute("first-frozen-to-end"));if(r){const a=r.getBoundingClientRect();e=this.__isRTL?a.right:e,t=this.__isRTL?t:a.left}const o=i.getBoundingClientRect();return o.left>=e&&o.right<=t}_hideTooltip(i){const e=this._tooltipController&&this._tooltipController.node;e&&e._stateController.close(i)}requestContentUpdate(){this.__updateHeaderAndFooter(),this.__updateVisibleRows()}__updateHeaderAndFooter(){(this._columnTree||[]).forEach(i=>{i.forEach(e=>{e._renderHeaderAndFooter&&e._renderHeaderAndFooter()})})}__updateVisibleRows(i,e){this.__virtualizer&&this.__virtualizer.update(i,e)}__updateMinHeight(){const e=this.$.header.clientHeight,t=this.$.footer.clientHeight,n=this.$.table.offsetHeight-this.$.table.clientHeight,r=e+36+t+n;this.__minHeightStyleSheet||(this.__minHeightStyleSheet=new CSSStyleSheet,this.shadowRoot.adoptedStyleSheets.push(this.__minHeightStyleSheet)),this.__minHeightStyleSheet.replaceSync(`:host { --_grid-min-height: ${r}px; }`)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Oa extends Ra(z(S(x(k(w))))){static get is(){return"vaadin-grid"}static get styles(){return ia}render(){return C`
      <div
        id="scroller"
        ?safari="${this._safari}"
        ?ios="${this._ios}"
        ?loading="${this.loading}"
        ?column-reordering-allowed="${this.columnReorderingAllowed}"
        ?empty-state="${this.__emptyState}"
      >
        <table
          id="table"
          role="treegrid"
          aria-multiselectable="true"
          tabindex="0"
          aria-label="${U(this.accessibleName)}"
        >
          <caption id="sizer" part="row"></caption>
          <thead id="header" role="rowgroup"></thead>
          <tbody id="items" role="rowgroup"></tbody>
          <tbody id="emptystatebody">
            <tr id="emptystaterow">
              <td part="empty-state" class="empty-state" id="emptystatecell" tabindex="0">
                <slot name="empty-state" id="emptystateslot"></slot>
              </td>
            </tr>
          </tbody>
          <tfoot id="footer" role="rowgroup"></tfoot>
        </table>

        <div part="reorder-ghost" class="reorder-ghost"></div>
      </div>

      <slot name="tooltip"></slot>

      <div id="focusexit" tabindex="0"></div>
    `}}y(Oa);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const La=v`
  :host {
    display: inline-flex;
    align-items: center;
    cursor: pointer;
    max-width: 100%;
    gap: var(--vaadin-gap-s);
    -webkit-user-select: none;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
  }

  [part='content'] {
    flex: 1 1 auto;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  [part='indicators'] {
    position: relative;
    flex: none;
    height: 1lh;
    color: var(--vaadin-text-color-disabled);
  }

  [part='order'] {
    display: inline;
    vertical-align: super;
    font-size: 0.75em;
    line-height: 1;
    color: var(--vaadin-text-color-secondary);
  }

  [part='indicators']::before {
    content: '';
    display: inline-block;
    height: 12px;
    width: 8px;
    mask-image: var(--_vaadin-icon-sort);
    background: currentColor;
  }

  :host([direction]) [part='indicators']::before {
    padding-bottom: 6px;
    height: 6px;
    mask-clip: content-box;
  }

  :host([direction='desc']) [part='indicators']::before {
    padding-block: 6px 0;
  }

  :host([direction]) [part='indicators'] {
    color: var(--vaadin-text-color-secondary);
  }

  @media (any-hover: hover) {
    :host(:hover) [part='indicators'] {
      color: var(--vaadin-text-color);
    }
  }

  @media (forced-colors: active) {
    [part='indicators']::before {
      background: CanvasText;
    }
  }
`;/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Pa=s=>class extends s{static get properties(){return{path:String,direction:{type:String,reflectToAttribute:!0,notify:!0,value:null,sync:!0},_order:{type:Number,value:null,sync:!0}}}static get observers(){return["_pathOrDirectionChanged(path, direction)"]}ready(){super.ready(),this.addEventListener("click",this._onClick.bind(this))}connectedCallback(){super.connectedCallback(),this._grid?this._grid.__applySorters():this.__dispatchSorterChangedEvenIfPossible()}disconnectedCallback(){super.disconnectedCallback(),!this.parentNode&&this._grid?this._grid.__removeSorters([this]):this._grid&&this._grid.__applySorters()}_pathOrDirectionChanged(){this.__dispatchSorterChangedEvenIfPossible()}__dispatchSorterChangedEvenIfPossible(){this.path===void 0||this.direction===void 0||!this.isConnected||(this.dispatchEvent(new CustomEvent("sorter-changed",{detail:{shiftClick:!!this._shiftClick,fromSorterClick:!!this._fromSorterClick},bubbles:!0,composed:!0})),this._fromSorterClick=!1,this._shiftClick=!1)}_getDisplayOrder(e){return e===null?"":e+1}_onClick(e){if(e.defaultPrevented)return;const t=this.getRootNode().activeElement;this!==t&&this.contains(t)||(e.preventDefault(),this._shiftClick=e.shiftKey,this._fromSorterClick=!0,this.direction==="asc"?this.direction="desc":this.direction==="desc"?this.direction=null:this.direction="asc")}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class za extends Pa(S(N(x(k(w))))){static get is(){return"vaadin-grid-sorter"}static get styles(){return La}render(){return C`
      <div part="content">
        <slot></slot>
      </div>
      <div part="indicators">
        <span part="order">${this._getDisplayOrder(this._order)}</span>
      </div>
    `}}y(za);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ma=s=>class extends s{static get properties(){return{width:{type:String,value:"58px",sync:!0},autoWidth:{type:Boolean,value:!0},flexGrow:{type:Number,value:0,sync:!0},selectAll:{type:Boolean,value:!1,notify:!0,sync:!0},autoSelect:{type:Boolean,value:!1,sync:!0},dragSelect:{type:Boolean,value:!1,sync:!0},_indeterminate:{type:Boolean,sync:!0},_selectAllHidden:Boolean,_shiftKeyDown:{type:Boolean,value:!1}}}static get observers(){return["_onHeaderRendererOrBindingChanged(_headerRenderer, _headerCell, path, header, selectAll, _indeterminate, _selectAllHidden)"]}constructor(){super(),this.__onCellTrack=this.__onCellTrack.bind(this),this.__onCellClick=this.__onCellClick.bind(this),this.__onCellMouseDown=this.__onCellMouseDown.bind(this),this.__onGridInteraction=this.__onGridInteraction.bind(this),this.__onActiveItemChanged=this.__onActiveItemChanged.bind(this),this.__onSelectRowCheckboxChange=this.__onSelectRowCheckboxChange.bind(this),this.__onSelectAllCheckboxChange=this.__onSelectAllCheckboxChange.bind(this)}connectedCallback(){super.connectedCallback(),this._grid&&(this._grid.addEventListener("keyup",this.__onGridInteraction),this._grid.addEventListener("keydown",this.__onGridInteraction,{capture:!0}),this._grid.addEventListener("mousedown",this.__onGridInteraction),this._grid.addEventListener("active-item-changed",this.__onActiveItemChanged))}disconnectedCallback(){super.disconnectedCallback(),this._grid&&(this._grid.removeEventListener("keyup",this.__onGridInteraction),this._grid.removeEventListener("keydown",this.__onGridInteraction,{capture:!0}),this._grid.removeEventListener("mousedown",this.__onGridInteraction),this._grid.removeEventListener("active-item-changed",this.__onActiveItemChanged))}_defaultHeaderRenderer(e,t){let n=e.firstElementChild;n||(n=document.createElement("vaadin-checkbox"),n.accessibleName="Select All",n.classList.add("vaadin-grid-select-all-checkbox"),n.addEventListener("change",this.__onSelectAllCheckboxChange),e.appendChild(n));const r=this.__isChecked(this.selectAll,this._indeterminate);n.checked=r,n.indeterminate=this._indeterminate,n.style.visibility=this._selectAllHidden?"hidden":""}_defaultRenderer(e,t,{item:n,selected:r}){let o=e.firstElementChild;o||(o=document.createElement("vaadin-checkbox"),o.accessibleName="Select Row",o.addEventListener("change",this.__onSelectRowCheckboxChange),e.appendChild(o),de(e,"track",this.__onCellTrack),e.addEventListener("mousedown",this.__onCellMouseDown),e.addEventListener("click",this.__onCellClick)),o.__item=n,o.checked=r;const a=this._grid.__isItemSelectable(n);o.readonly=!a;const l=!a&&!r;o.style.visibility=l?"hidden":""}__onSelectAllCheckboxChange(e){this._indeterminate||e.currentTarget.checked?this._selectAll():this._deselectAll()}__onGridInteraction(e){this._shiftKeyDown=e.shiftKey,this.autoSelect&&this._grid.$.scroller.toggleAttribute("range-selecting",this._shiftKeyDown)}__onSelectRowCheckboxChange(e){this.__toggleItem(e.currentTarget.__item,e.currentTarget.checked)}__onCellTrack(e){if(this.dragSelect)if(this.__dragCurrentY=e.detail.y,this.__dragDy=e.detail.dy,e.detail.state==="start"){const n=this._grid._getRenderedRows().find(r=>r.contains(e.currentTarget.assignedSlot));this.__selectOnDrag=!this._grid._isSelected(n._item),this.__dragStartIndex=n.index,this.__dragStartItem=n._item,this.__dragAutoScroller()}else e.detail.state==="end"&&(this.__dragStartItem&&this.__toggleItem(this.__dragStartItem,this.__selectOnDrag),setTimeout(()=>{this.__dragStartIndex=void 0}))}__onCellMouseDown(e){this.dragSelect&&e.preventDefault()}__onCellClick(e){this.__dragStartIndex!==void 0&&e.preventDefault()}_onCellKeyDown(e){const t=e.composedPath()[0];if(e.keyCode===32){if(t===this._headerCell)this.selectAll?this._deselectAll():this._selectAll();else if(this._cells.includes(t)&&!this.autoSelect){const n=t._content.firstElementChild;this.__toggleItem(n.__item)}}}__onActiveItemChanged(e){const t=e.detail.value;if(this.autoSelect){const n=t||this.__previousActiveItem;n&&this.__toggleItem(n)}this.__previousActiveItem=t}__dragAutoScroller(){if(this.__dragStartIndex===void 0)return;const e=this._grid._getRenderedRows(),t=e.find(l=>{const d=l.getBoundingClientRect();return this.__dragCurrentY>=d.top&&this.__dragCurrentY<=d.bottom});let n=t?t.index:void 0;const r=this.__getScrollableArea();this.__dragCurrentY<r.top?n=this._grid._firstVisibleIndex:this.__dragCurrentY>r.bottom&&(n=this._grid._lastVisibleIndex),n!==void 0&&e.forEach(l=>{(n>this.__dragStartIndex&&l.index>=this.__dragStartIndex&&l.index<=n||n<this.__dragStartIndex&&l.index<=this.__dragStartIndex&&l.index>=n)&&(this.__toggleItem(l._item,this.__selectOnDrag),this.__dragStartItem=void 0)});const o=r.height*.15,a=10;if(this.__dragDy<0&&this.__dragCurrentY<r.top+o){const l=r.top+o-this.__dragCurrentY,d=Math.min(1,l/o);this._grid.$.table.scrollTop-=d*a}if(this.__dragDy>0&&this.__dragCurrentY>r.bottom-o){const l=this.__dragCurrentY-(r.bottom-o),d=Math.min(1,l/o);this._grid.$.table.scrollTop+=d*a}setTimeout(()=>this.__dragAutoScroller(),10)}__getScrollableArea(){const e=this._grid.$.table.getBoundingClientRect(),t=this._grid.$.header.getBoundingClientRect(),n=this._grid.$.footer.getBoundingClientRect();return{top:e.top+t.height,bottom:e.bottom-n.height,left:e.left,right:e.right,height:e.height-t.height-n.height,width:e.width}}_selectAll(){}_deselectAll(){}_selectItem(e){}_deselectItem(e){}__toggleItem(e,t=!this._grid._isSelected(e)){t!==this._grid._isSelected(e)&&(t?this._selectItem(e):this._deselectItem(e))}__isChecked(e,t){return t||e}};class Ft extends Ma(Ps){static get is(){return"vaadin-grid-flow-selection-column"}static get properties(){return{autoWidth:{type:Boolean,value:!0},width:{type:String,value:"56px"}}}_defaultHeaderRenderer(i,e){super._defaultHeaderRenderer(i,e);const t=i.firstElementChild;t&&(t.id="selectAllCheckbox")}_selectAll(){this.selectAll=!0,this.$server.selectAll()}_deselectAll(){this.selectAll=!1,this.$server.deselectAll()}_selectItem(i){this.$server.setShiftKeyDown(this._shiftKeyDown),this._grid.$connector.doSelection([i],!0)}_deselectItem(i){this.$server.setShiftKeyDown(this._shiftKeyDown),this._grid.$connector.doDeselection([i],!0),this.selectAll=!1}}customElements.define(Ft.is,Ft);window.Vaadin.Flow.gridConnector={};window.Vaadin.Flow.gridConnector.initLazy=s=>{if(s.$connector)return;const i=s._dataProviderController;let e={};const t=150;let n,r=[0,0];const o=["SINGLE","NONE","MULTI"];let a={},l="SINGLE",d=!1;s.size=0,s.itemIdPath="key",s.$connector={},s.$connector.hasRootRequestQueue=()=>{const{pendingRequests:h}=i.rootCache;return Object.keys(h).length>0||!!n?.isActive()},s.$connector.doSelection=function(h,c){if(l==="NONE"||!h.length||c&&s.hasAttribute("disabled"))return;l==="SINGLE"&&(a={});let u=!1;h.forEach(p=>{const m=!c||s.isItemSelectable(p);u=u||m,p&&m&&(a[p.key]=p,p.selected=!0,c&&s.$server.select(p.key));const R=!s.activeItem||!p||p.key!=s.activeItem.key;!c&&l==="SINGLE"&&R&&(s.activeItem=p)}),u&&(s.selectedItems=Object.values(a))},s.$connector.doDeselection=function(h,c){if(l==="NONE"||!h.length||c&&s.hasAttribute("disabled"))return;const u=s.selectedItems.slice();for(;h.length;){const p=h.shift();if(!c||s.isItemSelectable(p)){for(let R=0;R<u.length;R++){const T=u[R];if(p?.key===T.key){u.splice(R,1);break}}p&&(delete a[p.key],delete p.selected,c&&s.$server.deselect(p.key))}}s.selectedItems=u},s.__activeItemChanged=function(h,c){l=="SINGLE"&&(h?a[h.key]||s.$connector.doSelection([h],!0):c&&a[c.key]&&(s.__deselectDisallowed?s.activeItem=c:(c=i.getItemContext(c).item,s.$connector.doDeselection([c],!0))))},s._createPropertyObserver("activeItem","__activeItemChanged",!0),s.__activeItemChangedDetails=function(h,c){s.__disallowDetailsOnClick||h==null&&c===void 0||(h&&!h.detailsOpened?s.$server.setDetailsVisible(h.key):s.$server.setDetailsVisible(null))},s._createPropertyObserver("activeItem","__activeItemChangedDetails",!0),s.$connector.debounceRootRequest=function(h){const c=s._hasData?t:0;n=I.debounce(n,H.after(c),()=>{s.$connector.fetchPage((u,p)=>s.$server.setViewportRange(u,p),h)})},s.$connector.fetchPage=function(h,c){c=Math.min(c,Math.floor((s.size-1)/s.pageSize));const u=s._getRenderedRows();let p=u.length>0?u[0].index:0,m=u.length>0?u[u.length-1].index:0,R=m-p;p=Math.max(0,p-R),m=Math.min(m+R,s.size);let T=[Math.floor(p/s.pageSize),Math.floor(m/s.pageSize)];if((c<T[0]||c>T[1])&&(T=[c,c]),r[0]!=T[0]||r[1]!=T[1]){r=T;let F=T[1]-T[0]+1;h(T[0]*s.pageSize,F*s.pageSize)}},s.dataProvider=function(h,c){if(h.pageSize!=s.pageSize)throw"Invalid pageSize";let u=h.page;if(s.size===0){c([],0);return}e[u]?c(e[u]):s.$connector.debounceRootRequest(u)},s.$connector.setSorterDirections=function(h){d=!0,setTimeout(()=>{try{const c=Array.from(s.querySelectorAll("vaadin-grid-sorter"));s._sorters.forEach(u=>{c.includes(u)||c.push(u)}),c.forEach(u=>{u.direction=null}),s.multiSortPriority!=="append"&&(h=h.reverse()),h.forEach(({column:u,direction:p})=>{c.forEach(m=>{m.getAttribute("path")===u&&(m.direction=p)})}),s.__applySorters()}finally{d=!1}})};let _=0;function f(h){try{_++,h()}finally{_--}}s.__updateVisibleRows=function(...h){_===0&&Object.getPrototypeOf(this).__updateVisibleRows.call(this,...h)},s.__updateRow=function(h,...c){Object.getPrototypeOf(this).__updateRow.call(this,h,...c),l===o[1]&&(h.removeAttribute("aria-selected"),Array.from(h.children).forEach(u=>u.removeAttribute("aria-selected")))};const g=function(h){if(!h||!Array.isArray(h))throw"Attempted to call itemsUpdated with an invalid value: "+JSON.stringify(h);let c=Array.from(s.detailsOpenedItems);for(let u=0;u<h.length;++u){const p=h[u];p&&(p.detailsOpened?s._getItemIndexInArray(p,c)<0&&c.push(p):s._getItemIndexInArray(p,c)>=0&&c.splice(s._getItemIndexInArray(p,c),1))}s.detailsOpenedItems=c},b=function(h){const{rootCache:c}=i;if(!(e[h]&&c.pendingRequests[h]))for(let u=0;u<s.pageSize;u++){const p=h*s.pageSize+u,m=e[h]?.[u];c.items[p]=m}};s.$connector.set=function(h,c){c.forEach((m,R)=>{const T=h+R,F=Math.floor(T/s.pageSize);e[F]??=[],e[F][T%s.pageSize]=m});const u=Math.floor(h/s.pageSize),p=Math.ceil(c.length/s.pageSize);for(let m=0;m<p;m++)b(u+m);f(()=>{s.$connector.doSelection(c.filter(m=>m.selected)),s.$connector.doDeselection(c.filter(m=>!m.selected&&a[m.key])),g(c)}),s.__updateVisibleRows(h,h+c.length-1)};const L=function(h){for(let c in e)for(let u in e[c])if(s.getItemId(e[c][u])===s.getItemId(h))return{page:c,index:u};return null};s.$connector.updateFlatData=function(h){const c=[];for(let u=0;u<h.length;u++){let p=L(h[u]);if(p){e[p.page][p.index]=h[u];const m=parseInt(p.page)*s.pageSize+parseInt(p.index),{rootCache:R}=i;R.items[m]&&(R.items[m]=h[u]),c.push(m)}}f(()=>{g(h)}),c.forEach(u=>s.__updateVisibleRows(u,u))},s.$connector.clear=function(h,c){if(!e||Object.keys(e).length===0)return;if(h%s.pageSize!=0)throw"Got cleared data for index "+h+" which is not aligned with the page size of "+s.pageSize;let u=Math.floor(h/s.pageSize),p=Math.ceil(c/s.pageSize);for(let m=0;m<p;m++){let R=u+m,T=e[R];T&&(f(()=>{s.$connector.doDeselection(T.filter(F=>a[F.key])),T.forEach(F=>s.closeItemDetails(F))}),delete e[R],b(R))}s.__updateVisibleRows(h,h+c-1)},s.$connector.reset=function(){e={},i.clearCache(),r=[-1,-1],n?.cancel(),s.__updateVisibleRows()},s.$connector.updateSize=h=>s.size=h,s.$connector.updateUniqueItemIdPath=h=>s.itemIdPath=h,s.$connector.confirm=function(h){const{pendingRequests:c}=i.rootCache;Object.entries(c).forEach(([u,p])=>{const m=s.size?Math.ceil(s.size/s.pageSize)-1:0,R=Math.min(r[1],m);e[u]?p(e[u]):u<r[0]||+u>R?(p(new Array(s.pageSize)),s.requestContentUpdate()):p&&s.size===0&&p([])}),Object.keys(c).length===0&&(n?.cancel(),r=[-1,-1]),s.$server.confirmUpdate(h)},s.$connector.setSelectionMode=function(h){if((typeof h=="string"||h instanceof String)&&o.indexOf(h)>=0)l=h,a={},s.selectedItems=[],s.$connector.updateMultiSelectable();else throw"Attempted to set an invalid selection mode"},s.$connector.updateMultiSelectable=function(){s.$&&(l===o[0]?s.$.table.setAttribute("aria-multiselectable",!1):l===o[1]?s.$.table.removeAttribute("aria-multiselectable"):s.$.table.setAttribute("aria-multiselectable",!0))},s._createPropertyObserver("isAttached",()=>s.$connector.updateMultiSelectable());const A=h=>c=>{h&&(h(c),h=null)};s.$connector.setHeaderRenderer=function(h,c){const{content:u,showSorter:p,sorterPath:m}=c;if(u===null){h.headerRenderer=null;return}h.headerRenderer=A(R=>{R.innerHTML="";let T=R;if(p){const F=document.createElement("vaadin-grid-sorter");F.setAttribute("path",m);const j=u instanceof Node?u.textContent:u;j&&F.setAttribute("aria-label",`Sort by ${j}`),R.appendChild(F),T=F}u instanceof Node?T.appendChild(u):T.textContent=u})},s._getActiveSorters=function(){return this._sorters.filter(h=>h.direction)},s.__applySorters=function(...h){const c=s._mapSorters(),u=JSON.stringify(s._previousSorters)!==JSON.stringify(c);s._previousSorters=c,Object.getPrototypeOf(this).__applySorters.call(this,...h),u&&!d&&s.$server.sortersChanged(c)},s.$connector.setFooterRenderer=function(h,c){const{content:u}=c;if(u===null){h.footerRenderer=null;return}h.footerRenderer=A(p=>{p.innerHTML="",u instanceof Node?p.appendChild(u):p.textContent=u})},s.addEventListener("vaadin-context-menu-before-open",function(h){const{key:c,columnId:u}=h.detail;s.$server.updateContextMenuTargetItem(c,u)}),s.getContextMenuBeforeOpenDetail=function(h){const c=h.detail.sourceEvent||h,u=s.getEventContext(c),p=u.item?.key||"",m=u.column?.id||"";return{key:p,columnId:m}},s.preventContextMenu=function(h){const c=h.type==="click",{column:u}=s.getEventContext(h);return c&&u instanceof Ft},s.addEventListener("click",h=>M(h,"item-click")),s.addEventListener("dblclick",h=>M(h,"item-double-click")),s.addEventListener("column-resize",h=>{s._getColumnsInOrder().filter(u=>!u.hidden).forEach(u=>{u.dispatchEvent(new CustomEvent("column-drag-resize"))}),s.dispatchEvent(new CustomEvent("column-drag-resize",{detail:{resizedColumnKey:h.detail.resizedColumn._flowId}}))}),s.addEventListener("column-reorder",h=>{const c=s._columnTree.slice(0).pop().filter(u=>u._flowId).sort((u,p)=>u._order-p._order).map(u=>u._flowId);s.dispatchEvent(new CustomEvent("column-reorder-all-columns",{detail:{columns:c}}))}),s.addEventListener("cell-focus",h=>{const c=s.getEventContext(h);["header","body","footer"].indexOf(c.section)!==-1&&s.dispatchEvent(new CustomEvent("grid-cell-focus",{detail:{itemKey:c.item?c.item.key:null,internalColumnId:c.column?c.column._flowId:null,section:c.section}}))});function M(h,c){if(h.defaultPrevented)return;const u=h.composedPath(),p=u.findIndex(j=>j.localName==="td"||j.localName==="th"),m=u[p];if(u.slice(0,p).some(j=>m?._focusButton!==j&&Ms(j)||j instanceof HTMLLabelElement))return;const T=s.getEventContext(h),F=T.section;T.item&&F!=="details"&&(h.itemKey=T.item.key,T.column&&(h.internalColumnId=T.column._flowId),s.dispatchEvent(new CustomEvent(c,{detail:h})))}s.cellPartNameGenerator=function(h,c){const u=c.item.part;if(u)return(u.row||"")+" "+(h&&u[h._flowId]||"")},s.dropFilter=h=>h.item&&!h.item.dropDisabled,s.dragFilter=h=>h.item&&!h.item.dragDisabled,s.addEventListener("grid-dragstart",h=>{s._isSelected(h.detail.draggedItems[0])?(s.__selectionDragData?Object.keys(s.__selectionDragData).forEach(c=>{h.detail.setDragData(c,s.__selectionDragData[c])}):(s.__dragDataTypes||[]).forEach(c=>{h.detail.setDragData(c,h.detail.draggedItems.map(u=>u.dragData[c]).join(`
`))}),s.__selectionDraggedItemsCount>1&&h.detail.setDraggedItemsCount(s.__selectionDraggedItemsCount)):(s.__dragDataTypes||[]).forEach(c=>{h.detail.setDragData(c,h.detail.draggedItems[0].dragData[c])})}),s.isItemSelectable=h=>h?.selectable===void 0||h.selectable;function $(h){const c=h.getBoundingClientRect(),u=s.$.table.getBoundingClientRect(),p=s.$.header.getBoundingClientRect(),m=s.$.footer.getBoundingClientRect();return c.top>=u.top+p.height&&c.bottom<=u.bottom-m.height}s.$connector.scrollToItem=function(h,...c){const u=s._getRenderedRows().find(p=>{const{item:m}=s.__getRowModel(p);return s.getItemId(m)===h});u&&$(u)||s.scrollToIndex(...c)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Fa=s=>class extends Ls(s){static get properties(){return{_childColumns:{value(){return this._getChildColumns(this)}},flexGrow:{type:Number,readOnly:!0,sync:!0},width:{type:String,readOnly:!0,sync:!0},_visibleChildColumns:Array,_colSpan:Number,_rootColumns:Array}}static get observers(){return["_groupFrozenChanged(frozen, _rootColumns)","_groupFrozenToEndChanged(frozenToEnd, _rootColumns)","_groupHiddenChanged(hidden)","_colSpanChanged(_colSpan, _headerCell, _footerCell)","_groupOrderChanged(_order, _rootColumns)","_groupReorderStatusChanged(_reorderStatus, _rootColumns)","_groupResizableChanged(resizable, _rootColumns)"]}connectedCallback(){super.connectedCallback(),this._addNodeObserver(),this._updateFlexAndWidth()}disconnectedCallback(){super.disconnectedCallback(),this._observer&&this._observer.disconnect()}_columnPropChanged(i,e){i==="hidden"&&(this._preventHiddenSynchronization=!0,this._updateVisibleChildColumns(this._childColumns),this._preventHiddenSynchronization=!1),/flexGrow|width|hidden|_childColumns/u.test(i)&&this._updateFlexAndWidth(),i==="frozen"&&!this.frozen&&(this.frozen=e),i==="lastFrozen"&&!this._lastFrozen&&(this._lastFrozen=e),i==="frozenToEnd"&&!this.frozenToEnd&&(this.frozenToEnd=e),i==="firstFrozenToEnd"&&!this._firstFrozenToEnd&&(this._firstFrozenToEnd=e)}_groupOrderChanged(i,e){if(e){const t=e.slice(0);if(!i){t.forEach(a=>{a._order=0});return}const n=/(0+)$/u.exec(i).pop().length,r=~~(Math.log(e.length)/Math.LN10)+1,o=10**(n-r);t[0]&&t[0]._order&&t.sort((a,l)=>a._order-l._order),Os(t,o,i)}}_groupReorderStatusChanged(i,e){i===void 0||e===void 0||e.forEach(t=>{t._reorderStatus=i})}_groupResizableChanged(i,e){i===void 0||e===void 0||e.forEach(t=>{t.resizable=i})}_updateVisibleChildColumns(i){this._visibleChildColumns=Array.prototype.filter.call(i,e=>!e.hidden),this._colSpan=this._visibleChildColumns.length,this._updateAutoHidden()}_updateFlexAndWidth(){if(this._visibleChildColumns){if(this._visibleChildColumns.length>0){const i=this._visibleChildColumns.reduce((e,t)=>(e+=` + ${(t.width||"0px").replace("calc","")}`,e),"").substring(3);this._setWidth(`calc(${i})`)}else this._setWidth("0px");this._setFlexGrow(Array.prototype.reduce.call(this._visibleChildColumns,(i,e)=>i+e.flexGrow,0))}}__scheduleAutoFreezeWarning(i,e){if(this._grid){const t=e.replace(/([A-Z])/gu,"-$1").toLowerCase(),n=i[0][e]||i[0].hasAttribute(t);i.every(o=>(o[e]||o.hasAttribute(t))===n)||(this._grid.__autoFreezeWarningDebouncer=I.debounce(this._grid.__autoFreezeWarningDebouncer,X,()=>{console.warn(`WARNING: Joining ${e} and non-${e} Grid columns inside the same column group! This will automatically freeze all the joined columns to avoid rendering issues. If this was intentional, consider marking each joined column explicitly as ${e}. Otherwise, exclude the ${e} columns from the joined group.`)}))}}_groupFrozenChanged(i,e){e===void 0||i===void 0||i!==!1&&(this.__scheduleAutoFreezeWarning(e,"frozen"),Array.from(e).forEach(t=>{t.frozen=i}))}_groupFrozenToEndChanged(i,e){e===void 0||i===void 0||i!==!1&&(this.__scheduleAutoFreezeWarning(e,"frozenToEnd"),Array.from(e).forEach(t=>{t.frozenToEnd=i}))}_groupHiddenChanged(i){(i||this.__groupHiddenInitialized)&&this._synchronizeHidden(),this.__groupHiddenInitialized=!0}_updateAutoHidden(){const i=this._autoHidden;this._autoHidden=(this._visibleChildColumns||[]).length===0,(i||this._autoHidden)&&(this.hidden=this._autoHidden)}_synchronizeHidden(){this._childColumns&&!this._preventHiddenSynchronization&&this._childColumns.forEach(i=>{i.hidden=this.hidden})}_colSpanChanged(i,e,t){e&&(e.setAttribute("colspan",i),this._grid&&this._grid.__a11yUpdateCellColspan(e,i)),t&&(t.setAttribute("colspan",i),this._grid&&this._grid.__a11yUpdateCellColspan(t,i))}_getChildColumns(i){return se.getColumns(i)}_addNodeObserver(){this._observer=new se(this,()=>{this._preventHiddenSynchronization=!0,this._rootColumns=this._getChildColumns(this),this._childColumns=this._rootColumns,this._updateVisibleChildColumns(this._childColumns),this._preventHiddenSynchronization=!1,this._grid&&this._grid._debounceUpdateColumnTree&&this._grid._debounceUpdateColumnTree()}),this._observer.flush()}_isColumnElement(i){return i.nodeType===Node.ELEMENT_NODE&&/\bcolumn\b/u.test(i.localName)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class $a extends Fa(x(w)){static get is(){return"vaadin-grid-column-group"}}y($a);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */ut({name:"vaadin-contextmenu",deps:["touchstart","touchmove","touchend","contextmenu"],flow:{start:["touchstart","contextmenu"],end:["contextmenu"]},emits:["vaadin-contextmenu"],info:{sourceEvent:null},reset(){this.info.sourceEvent=null,this._cancelTimer(),this.info.touchJob=null,this.info.touchStartCoords=null},_cancelTimer(){this._timerId&&(clearTimeout(this._timerId),delete this._fired)},_setSourceEvent(s){this.info.sourceEvent=s;const i=s.composedPath();this.info.sourceEvent.__composedPath=i},touchstart(s){this._setSourceEvent(s),this.info.touchStartCoords={x:s.changedTouches[0].clientX,y:s.changedTouches[0].clientY};const i=s.composedPath()[0]||s.target;this._timerId=setTimeout(()=>{const e=s.changedTouches[0];s.shiftKey||(ve&&(this._fired=!0,this.fire(i,e.clientX,e.clientY)),be("tap"))},500)},touchmove(s){const e=this.info.touchStartCoords;(Math.abs(e.x-s.changedTouches[0].clientX)>15||Math.abs(e.y-s.changedTouches[0].clientY)>15)&&this._cancelTimer()},touchend(s){this._fired&&s.preventDefault(),this._cancelTimer()},contextmenu(s){if(!s.shiftKey){if(this._setSourceEvent(s),Gi&&ne()){const i=s.composedPath()[0],e=i.getBoundingClientRect();this.fire(i,e.left,e.bottom)}else this.fire(s.target,s.clientX,s.clientY);be("tap")}},fire(s,i,e){const t=this.info.sourceEvent,n=new Event("vaadin-contextmenu",{bubbles:!0,cancelable:!0,composed:!0});n.detail={x:i,y:e,sourceEvent:t},s.dispatchEvent(n),n.defaultPrevented&&t&&t.preventDefault&&t.preventDefault()}});/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Da=v`
  :host([aria-haspopup='true'])::after {
    background: var(--vaadin-text-color-secondary);
    content: '';
    display: block;
    height: var(--vaadin-icon-size, 1lh);
    mask: var(--_vaadin-icon-chevron-down) 50% / var(--vaadin-icon-visual-size, 100%) no-repeat;
    rotate: -90deg;
    width: var(--vaadin-icon-size, 1lh);
  }

  :host([dir='rtl'])::after {
    rotate: 90deg;
  }

  /* TODO would be nice to only reserve the space if
    one or mote items in the list is checkable  */
  :host([menu-item-checked]) [part='checkmark'] {
    visibility: visible;
  }
`,Na=[Es,Da];/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ba extends Ss(S(N(x(k(w))))){static get is(){return"vaadin-context-menu-item"}static get styles(){return Na}render(){return C`
      <span part="checkmark" aria-hidden="true"></span>
      <div part="content">
        <slot></slot>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","menuitem")}}y(Ba);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Va extends As(S(N(x(k(w))))){static get is(){return"vaadin-context-menu-list-box"}static get styles(){return Ts}static get properties(){return{orientation:{type:String,readOnly:!0}}}get _scrollerElement(){return this.shadowRoot.querySelector('[part="items"]')}render(){return C`
      <div part="items">
        <slot></slot>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","menu")}}y(Va);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ha=v`
  :host {
    align-items: flex-start;
    justify-content: flex-start;
  }

  :host([right-aligned]),
  :host([end-aligned]) {
    align-items: flex-end;
  }

  :host([bottom-aligned]) {
    justify-content: flex-end;
  }

  [part='backdrop'] {
    background: transparent;
  }

  [part='content'] {
    padding: var(--vaadin-item-overlay-padding, 4px);
  }

  /* TODO keyboard focus becomes visible even when navigating the menu with the mouse */
  [part='overlay']:focus-visible {
    outline: none;
  }
`;/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Wa=v`
  :host {
    --_default-offset: 4px;
  }

  :host([position^='top'][top-aligned]) [part='overlay'],
  :host([position^='bottom'][top-aligned]) [part='overlay'] {
    margin-top: var(--vaadin-context-menu-offset-top, var(--_default-offset));
  }

  :host([position^='top'][bottom-aligned]) [part='overlay'],
  :host([position^='bottom'][bottom-aligned]) [part='overlay'] {
    margin-bottom: var(--vaadin-context-menu-offset-bottom, var(--_default-offset));
  }

  :host([position^='start'][start-aligned]) [part='overlay'],
  :host([position^='end'][start-aligned]) [part='overlay'] {
    margin-inline-start: var(--vaadin-context-menu-offset-start, var(--_default-offset));
  }

  :host([position^='start'][end-aligned]) [part='overlay'],
  :host([position^='end'][end-aligned]) [part='overlay'] {
    margin-inline-end: var(--vaadin-context-menu-offset-end, var(--_default-offset));
  }
`,qa=[st,Ha,Wa];/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ua=s=>class extends Xi(Qt(s)){static get properties(){return{parentOverlay:{type:Object,readOnly:!0},_theme:{type:String,readOnly:!0,sync:!0}}}static get observers(){return["_themeChanged(_theme)"]}get _contentRoot(){return this._rendererRoot}get _rendererRoot(){if(!this.__savedRoot){const e=document.createElement("div");e.setAttribute("slot","overlay"),e.style.display="contents",this.owner.appendChild(e),this.__savedRoot=e}return this.__savedRoot}ready(){super.ready(),this.restoreFocusOnClose=!0,this.addEventListener("keydown",e=>{if(!e.defaultPrevented&&e.composedPath()[0]===this.$.overlay&&[38,40].indexOf(e.keyCode)>-1){const t=this._contentRoot.firstElementChild;t&&Array.isArray(t.items)&&t.items.length&&(e.preventDefault(),e.keyCode===38?t.items[t.items.length-1].focus():t.focus())}})}_themeChanged(){this.close()}getBoundaries(){const e=this.getBoundingClientRect(),t=this.$.overlay.getBoundingClientRect();let n=e.bottom-t.height;const r=this.parentOverlay;if(r&&r.hasAttribute("bottom-aligned")){const o=getComputedStyle(r);n=n-parseFloat(o.bottom)-parseFloat(o.height)}return{xMax:e.right-t.width,xMin:e.left+t.width,yMax:n}}_updatePosition(){if(super._updatePosition(),this.positionTarget&&this.parentOverlay&&this.opened){const e=this.$.content,t=getComputedStyle(e);!!this.style.left?this.style.left=`${parseFloat(this.style.left)+parseFloat(t.paddingLeft)}px`:this.style.right=`${parseFloat(this.style.right)+parseFloat(t.paddingRight)}px`,!!this.style.bottom?this.style.bottom=`${parseFloat(this.style.bottom)-parseFloat(t.paddingBottom)}px`:this.style.top=`${parseFloat(this.style.top)-parseFloat(t.paddingTop)}px`}}_shouldRestoreFocus(){return this.parentOverlay?!1:super._shouldRestoreFocus()}_deepContains(e){return this.owner.contains(e)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ja extends Ua(rt(N(S(x(k(w)))))){static get is(){return"vaadin-context-menu-overlay"}static get properties(){return{position:{type:String,reflectToAttribute:!0}}}static get styles(){return qa}_updatePosition(){if(super._updatePosition(),this.parentOverlay==null&&this.positionTarget&&this.position&&this.opened){if(this.position==="bottom"||this.position==="top"){const i=this.positionTarget.getBoundingClientRect(),e=this.$.overlay.getBoundingClientRect(),t=i.width/2-e.width/2;if(this.style.left){const n=e.left+t;n>0&&(this.style.left=`${n}px`)}if(this.style.right){const n=parseFloat(this.style.right)+t;n>0&&(this.style.right=`${n}px`)}}if(this.position==="start"||this.position==="end"){const i=this.positionTarget.getBoundingClientRect(),e=this.$.overlay.getBoundingClientRect(),t=i.height/2-e.height/2;this.style.top=`${e.top+t}px`}}}render(){return C`
      <div id="backdrop" part="backdrop" ?hidden="${!this.withBackdrop}"></div>
      <div part="overlay" id="overlay" tabindex="0">
        <div part="content" id="content">
          <slot></slot>
          <slot name="submenu"></slot>
        </div>
      </div>
    `}}y(ja);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ga=s=>class extends s{static get properties(){return{items:{type:Array,sync:!0},_positionTarget:{type:Object,sync:!0}}}constructor(){super(),this.__itemsOutsideClickListener=e=>{this._shouldCloseOnOutsideClick(e)&&this.dispatchEvent(new CustomEvent("items-outside-click"))},this.addEventListener("items-outside-click",()=>{this.items&&this.close()})}get _tagNamePrefix(){return"vaadin-context-menu"}connectedCallback(){super.connectedCallback(),document.documentElement.addEventListener("click",this.__itemsOutsideClickListener)}disconnectedCallback(){super.disconnectedCallback(),document.documentElement.removeEventListener("click",this.__itemsOutsideClickListener)}_shouldCloseOnOutsideClick(e){return!e.composedPath().some(t=>t.localName===`${this._tagNamePrefix}-overlay`)}__forwardFocus(){const e=this._overlayElement,t=e._contentRoot.firstElementChild;if(e.parentOverlay){const n=e.parentOverlay._contentRoot.querySelector("[expanded]");n&&n.hasAttribute("focused")&&t?t.focus():e.$.overlay.focus()}else t&&t.focus()}__openSubMenu(e,t){this.__updateSubMenuForItem(e,t);const n=this._overlayElement,r=e._overlayElement;r._setParentOverlay(n),n.hasAttribute("theme")?e.setAttribute("theme",n.getAttribute("theme")):e.removeAttribute("theme");const o=r.$.content;o.style.minWidth="",t.dispatchEvent(new CustomEvent("opensubmenu",{detail:{children:t._item.children}}))}__updateSubMenuForItem(e,t){e.items=t._item.children,e.listenOn=t,e._positionTarget=t,e._overlayElement.requestContentUpdate()}__createComponent(e){let t;return e.component instanceof HTMLElement?t=e.component:t=document.createElement(e.component||`${this._tagNamePrefix}-item`),t._hasVaadinItemMixin&&(t.setAttribute("role","menuitem"),t.tabIndex=-1),t.localName==="hr"?t.setAttribute("role","separator"):t.setAttribute("aria-haspopup","false"),this._setMenuItemTheme(t,e,this._theme),t._item=e,e.text&&(t.textContent=e.text),e.className&&t.setAttribute("class",e.className),this.__toggleMenuComponentAttribute(t,"menu-item-checked",e.checked),this.__toggleMenuComponentAttribute(t,"disabled",e.disabled),e.children&&e.children.length&&(this.__updateExpanded(t,!1),t.setAttribute("aria-haspopup","true")),t}__initListBox(){const e=document.createElement(`${this._tagNamePrefix}-list-box`);return this._theme&&e.setAttribute("theme",this._theme),e.addEventListener("selected-changed",t=>{const{value:n}=t.detail;if(typeof n=="number"){const r=e.items[n]._item;e.selected=null,r.children||this.dispatchEvent(new CustomEvent("item-selected",{detail:{value:r}}))}}),e}__initOverlay(){const e=this._overlayElement;e.$.backdrop.addEventListener("click",()=>{this.close()}),e.addEventListener(Me?"click":"mouseover",t=>{t.composedPath().includes(this._subMenu)||this.__showSubMenu(t)}),e.addEventListener("keydown",t=>{if(t.composedPath().includes(this._subMenu))return;const{key:n}=t,r=this.__isRTL,o=n==="ArrowRight",a=n==="ArrowLeft";!r&&o||r&&a||n==="Enter"||n===" "?this.__showSubMenu(t):!r&&a||r&&o||n==="Escape"?(n==="Escape"&&t.stopPropagation(),this.close(),this.listenOn.focus()):n==="Tab"&&!t.defaultPrevented&&this.dispatchEvent(new CustomEvent("close-all-menus"))})}__initSubMenu(){const e=document.createElement(this.constructor.is);return e._modeless=!0,e.openOn="opensubmenu",this.addEventListener("opened-changed",t=>{t.detail.value||this._subMenu.close()}),e.addEventListener("close-all-menus",()=>{this.dispatchEvent(new CustomEvent("close-all-menus"))}),e.addEventListener("item-selected",t=>{const{detail:n}=t;this.dispatchEvent(new CustomEvent("item-selected",{detail:n}))}),this.addEventListener("close-all-menus",()=>{this._overlayElement.close()}),this.addEventListener("item-selected",t=>{const n=t.target,r=t.detail.value,o=n.items.indexOf(r);r.keepOpen&&o>-1&&n.opened?(n.__selectedIndex=o,n.requestContentUpdate()):r.keepOpen||this.close()}),e.addEventListener("opened-changed",t=>{if(!t.detail.value){const n=this._listBox.querySelector("[expanded]");n&&this.__updateExpanded(n,!1)}}),e}__showSubMenu(e,t=e.composedPath().find(n=>n.localName===`${this._tagNamePrefix}-item`)){if(!this.__openListenerActive)return;if(this._overlayElement.hasAttribute("opening")){requestAnimationFrame(()=>{this.__showSubMenu(e,t)});return}const n=this._subMenu,r=this._listBox.querySelector("[expanded]");if(t&&t!==r){const{children:o}=t._item,a=n._overlayElement._contentRoot.firstElementChild,l=a&&a.focused;if(r&&this.__updateExpanded(r,!1),(!o||!o.length)&&n.close(),!this.opened)return;o&&o.length?(this.__updateExpanded(t,!0),this.__openSubMenu(n,t)):l?n.listenOn.focus():this._listBox.focused||this._overlayElement.$.overlay.focus()}}__getListBox(){return this._overlayElement._contentRoot.querySelector(`${this._tagNamePrefix}-list-box`)}__itemsRenderer(e,t){this.__initMenu(e,t),this._subMenu.closeOn=t.closeOn,this._listBox.innerHTML="",t.items.forEach(n=>{const r=this.__createComponent(n);this._listBox.appendChild(r)})}_setMenuItemTheme(e,t,n){let r=e.getAttribute("theme")||n;t.theme!=null&&(r=Array.isArray(t.theme)?t.theme.join(" "):t.theme),this.__updateTheme(e,r)}__toggleMenuComponentAttribute(e,t,n){n?(e.setAttribute(t,""),e[`__has-${t}`]=!0):e[`__has-${t}`]&&(e.removeAttribute(t),e[`__has-${t}`]=!1)}__initMenu(e,t){if(e.firstElementChild)this.__updateTheme(this._listBox,this._theme);else{this.__initOverlay();const n=this.__initListBox();this._listBox=n,e.appendChild(n);const r=this.__initSubMenu();r.slot="submenu",this._subMenu=r,this.appendChild(r),requestAnimationFrame(()=>{this.__openListenerActive=!0})}}__updateExpanded(e,t){e.setAttribute("aria-expanded",t.toString()),e.toggleAttribute("expanded",t)}__updateTheme(e,t){t?e.setAttribute("theme",t):e.removeAttribute("theme")}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ka=s=>class extends Ga(s){static get properties(){return{selector:{type:String},opened:{type:Boolean,reflectToAttribute:!0,observer:"_openedChanged",value:!1,notify:!0,readOnly:!0},openOn:{type:String,value:"vaadin-contextmenu",sync:!0},listenOn:{type:Object,sync:!0,value(){return this}},closeOn:{type:String,value:"click",observer:"_closeOnChanged",sync:!0},renderer:{type:Function,sync:!0},_modeless:{type:Boolean,sync:!0},_context:{type:Object,sync:!0},_phone:{type:Boolean},_fullscreen:{type:Boolean},_fullscreenMediaQuery:{type:String,value:"(max-width: 450px), (max-height: 450px)"}}}static get observers(){return["_targetOrOpenOnChanged(listenOn, openOn)","_rendererChanged(renderer, items)","_fullscreenChanged(_fullscreen)"]}constructor(){super(),this._boundOpen=this.open.bind(this),this._boundClose=this.close.bind(this),this._boundPreventDefault=this._preventDefault.bind(this),this._boundOnGlobalContextMenu=this._onGlobalContextMenu.bind(this)}connectedCallback(){super.connectedCallback(),this.__boundOnScroll=this.__onScroll.bind(this),window.addEventListener("scroll",this.__boundOnScroll,!0),this.__restoreOpened&&this._setOpened(!0)}disconnectedCallback(){super.disconnectedCallback(),window.removeEventListener("scroll",this.__boundOnScroll,!0),this.__restoreOpened=this.opened,this.close()}firstUpdated(){super.firstUpdated(),this._overlayElement=this.$.overlay,this.addController(new ks(this._fullscreenMediaQuery,e=>{this._fullscreen=e}))}_onOverlayOpened(e){if(e.target!==this._overlayElement)return;const t=e.detail.value;this._setOpened(t),t&&this.__alignOverlayPosition()}_onVaadinOverlayOpen(e){e.target===this._overlayElement&&(this.__alignOverlayPosition(),this._overlayElement.style.visibility="",this.__forwardFocus())}_onVaadinOverlayClosed(){this.dispatchEvent(new CustomEvent("closed"))}_targetOrOpenOnChanged(e,t){this._oldListenOn&&this._oldOpenOn&&(this._unlisten(this._oldListenOn,this._oldOpenOn,this._boundOpen),this._oldListenOn.style.webkitTouchCallout="",this._oldListenOn.style.webkitUserSelect="",this._oldListenOn.style.userSelect="",this._oldListenOn=null,this._oldOpenOn=null),e&&t&&(this._listen(e,t,this._boundOpen),this._oldListenOn=e,this._oldOpenOn=t)}_fullscreenChanged(e){this._phone=e}__setListenOnUserSelect(e){const t=e?"none":"";this.listenOn.style.webkitTouchCallout=t,this.listenOn.style.webkitUserSelect=t,this.listenOn.style.userSelect=t,e&&document.getSelection().removeAllRanges()}_closeOnChanged(e,t){const n="vaadin-overlay-outside-click",r=this._overlayElement;t&&this._unlisten(r,t,this._boundClose),e?(this._listen(r,e,this._boundClose),r.removeEventListener(n,this._boundPreventDefault)):r.addEventListener(n,this._boundPreventDefault)}_preventDefault(e){e.preventDefault()}_openedChanged(e,t){e?document.documentElement.addEventListener("contextmenu",this._boundOnGlobalContextMenu,!0):t&&document.documentElement.removeEventListener("contextmenu",this._boundOnGlobalContextMenu,!0),this.__setListenOnUserSelect(e)}requestContentUpdate(){this._overlayElement&&(this.__preserveMenuState(),this._overlayElement.requestContentUpdate(),this.__restoreMenuState())}_rendererChanged(e,t){if(t){if(e)throw new Error("The items API cannot be used together with a renderer");this.closeOn==="click"&&(this.closeOn="")}}close(){this._setOpened(!1)}_contextTarget(e){if(this.selector){const t=this.listenOn.querySelectorAll(this.selector);return Array.prototype.filter.call(t,n=>e.composedPath().indexOf(n)>-1)[0]}else if(this.listenOn&&this.listenOn!==this&&this.position)return this.listenOn;return e.target}open(e){this._overlayElement&&e.composedPath().includes(this._overlayElement)||e&&!this.opened&&(this._context={detail:e.detail,target:this._contextTarget(e)},this._context.target&&(e.preventDefault(),e.stopPropagation(),this.__x=this._getEventCoordinate(e,"x"),this.__pageXOffset=window.pageXOffset,this.__y=this._getEventCoordinate(e,"y"),this.__pageYOffset=window.pageYOffset,this._overlayElement.style.visibility="hidden",this._setOpened(!0)))}__preserveMenuState(){const e=this.__getListBox();e&&(this.__focusedIndex=e.items.indexOf(e.focused),this._subMenu&&this._subMenu.opened&&(this.__subMenuIndex=e.items.indexOf(this._subMenu.listenOn)))}__restoreMenuState(){const e=this.__focusedIndex,t=this.__subMenuIndex,n=this.__selectedIndex,r=this.__getListBox();if(r){if(r._observer.flush(),t>-1){const o=r.items[t];o?Array.isArray(o._item.children)&&o._item.children.length?(this.__updateSubMenuForItem(this._subMenu,o),this._subMenu.requestContentUpdate()):(this._subMenu.close(),this.__focusItem(o)):r.focus()}this.__focusItem(n>-1?r.children[n]:r.items[e])}this.__focusedIndex=void 0,this.__subMenuIndex=void 0,this.__selectedIndex=void 0}__focusItem(e){e&&e.focus({focusVisible:ne()})}__onScroll(){if(!this.opened||this.position)return;const e=window.pageYOffset-this.__pageYOffset,t=window.pageXOffset-this.__pageXOffset;this.__adjustPosition("left",-t),this.__adjustPosition("right",t),this.__adjustPosition("top",-e),this.__adjustPosition("bottom",e),this.__pageYOffset+=e,this.__pageXOffset+=t}__adjustPosition(e,t){const r=this._overlayElement.style;r[e]=`${(parseInt(r[e])||0)+t}px`}__alignOverlayPosition(){const e=this._overlayElement;if(e.positionTarget)return;const t=e.style;["top","right","bottom","left"].forEach(f=>t.removeProperty(f)),["right-aligned","end-aligned","bottom-aligned"].forEach(f=>e.removeAttribute(f));const{xMax:n,xMin:r,yMax:o}=e.getBoundaries(),a=this.__x,l=this.__y,d=document.documentElement.clientWidth,_=document.documentElement.clientHeight;this.__isRTL?a>d/2||a>r?t.right=`${Math.max(0,d-a)}px`:(t.left=`${a}px`,this._setEndAligned(e)):a<d/2||a<n?t.left=`${a}px`:(t.right=`${Math.max(0,d-a)}px`,this._setEndAligned(e)),l<_/2||l<o?t.top=`${l}px`:(t.bottom=`${Math.max(0,_-l)}px`,e.setAttribute("bottom-aligned",""))}_setEndAligned(e){e.setAttribute("end-aligned",""),this.__isRTL||e.setAttribute("right-aligned","")}_getEventCoordinate(e,t){if(e.detail instanceof Object){if(e.detail[t])return e.detail[t];if(e.detail.sourceEvent)return this._getEventCoordinate(e.detail.sourceEvent,t)}else{const n=`client${t.toUpperCase()}`,r=e.changedTouches?e.changedTouches[0][n]:e[n];if(r===0){const o=e.target.getBoundingClientRect();return t==="x"?o.left:o.top+o.height}return r}}_listen(e,t,n){Z[t]?de(e,t,n):e.addEventListener(t,n)}_unlisten(e,t,n){Z[t]?bs(e,t,n):e.removeEventListener(t,n)}__createMouseEvent(e,t,n){return new MouseEvent(e,{bubbles:!0,composed:!0,cancelable:!0,clientX:t,clientY:n})}__focusClosestFocusable(e){let t=e;for(;t;){if(t instanceof HTMLElement&&Ht(t)){t.focus();return}t=t.parentNode||t.host}}__contextMenuAt(e,t){const n=ms(e,t);n&&queueMicrotask(()=>{n.dispatchEvent(this.__createMouseEvent("mousedown",e,t)),n.dispatchEvent(this.__createMouseEvent("mouseup",e,t)),this.__focusClosestFocusable(n),n.dispatchEvent(this.__createMouseEvent("contextmenu",e,t))})}_onGlobalContextMenu(e){e.shiftKey||(Pt||ve||(e.stopPropagation(),this._overlayElement.__focusRestorationController.focusNode=null,this._overlayElement.addEventListener("vaadin-overlay-closed",n=>{n.target===this._overlayElement&&this.__contextMenuAt(e.clientX,e.clientY)},{once:!0})),e.preventDefault(),this.close())}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ya extends Ka(z(ze(x(w)))){static get is(){return"vaadin-context-menu"}static get styles(){return v`
      :host {
        display: block;
      }

      :host([hidden]) {
        display: none !important;
      }
    `}static get properties(){return{position:{type:String}}}render(){const{_context:i,position:e}=this;return C`
      <slot id="slot"></slot>
      <vaadin-context-menu-overlay
        id="overlay"
        .owner="${this}"
        .opened="${this.opened}"
        .model="${i}"
        .modeless="${this._modeless}"
        .renderer="${this.items?this.__itemsRenderer:this.renderer}"
        .position="${e}"
        .positionTarget="${e?i&&i.target:this._positionTarget}"
        .horizontalAlign="${this.__computeHorizontalAlign(e)}"
        .verticalAlign="${this.__computeVerticalAlign(e)}"
        ?no-horizontal-overlap="${this.__computeNoHorizontalOverlap(e)}"
        ?no-vertical-overlap="${this.__computeNoVerticalOverlap(e)}"
        .withBackdrop="${this._phone}"
        ?phone="${this._phone}"
        theme="${U(this._theme)}"
        exportparts="backdrop, overlay, content"
        @opened-changed="${this._onOverlayOpened}"
        @vaadin-overlay-open="${this._onVaadinOverlayOpen}"
        @vaadin-overlay-closed="${this._onVaadinOverlayClosed}"
      >
        <slot name="overlay"></slot>
        <slot name="submenu" slot="submenu"></slot>
      </vaadin-context-menu-overlay>
    `}__computeHorizontalAlign(i){return i&&["top-end","bottom-end","start-top","start","start-bottom"].includes(i)?"end":"start"}__computeNoHorizontalOverlap(i){return i?["start-top","start","start-bottom","end-top","end","end-bottom"].includes(i):!!this._positionTarget}__computeNoVerticalOverlap(i){return i?["top-start","top-end","top","bottom-start","bottom","bottom-end"].includes(i):!1}__computeVerticalAlign(i){return i&&["top-start","top-end","top","start-bottom","end-bottom"].includes(i)?"bottom":"top"}}y(Ya);function Xa(s,i){try{return window.Vaadin.Flow.clients[s].getByNodeId(i)}catch(e){console.error("Could not get node %s from app %s",i,s),console.error(e)}}function Za(s,i){s.$connector||(s.$connector={generateItems(e){const t=si(i,e);s.items=t}})}function si(s,i){const e=Xa(s,i);if(e)return Array.from(e.children).map(t=>{const n={component:t,checked:t._checked,keepOpen:t._keepOpen,className:t.className,theme:t.__theme};return t._hasVaadinItemMixin&&t._containerNodeId&&(n.children=si(s,t._containerNodeId)),t._item=n,n})}function Qa(s,i){s._item&&(s._item.checked=i,s._item.keepOpen&&s.toggleAttribute("menu-item-checked",i))}function Ja(s,i){s._item&&(s._item.keepOpen=i)}function el(s,i){s._item&&(s._item.theme=i)}window.Vaadin.Flow.contextMenuConnector={initLazy:Za,generateItemsTree:si,setChecked:Qa,setKeepOpen:Ja,setTheme:el};function tl(s){s.$contextMenuTargetConnector||(s.$contextMenuTargetConnector={openOnHandler(i){if(s.preventContextMenu&&s.preventContextMenu(i))return;i.preventDefault(),i.stopPropagation(),this.$contextMenuTargetConnector.openEvent=i;let e={};s.getContextMenuBeforeOpenDetail&&(e=s.getContextMenuBeforeOpenDetail(i)),s.dispatchEvent(new CustomEvent("vaadin-context-menu-before-open",{detail:e}))},updateOpenOn(i){this.removeListener(),this.openOnEventType=i,customElements.whenDefined("vaadin-context-menu").then(()=>{Z[i]?de(s,i,this.openOnHandler):s.addEventListener(i,this.openOnHandler)})},removeListener(){this.openOnEventType&&(Z[this.openOnEventType]?bs(s,this.openOnEventType,this.openOnHandler):s.removeEventListener(this.openOnEventType,this.openOnHandler))},openMenu(i){i.open(this.openEvent)},removeConnector(){this.removeListener(),s.$contextMenuTargetConnector=void 0}})}window.Vaadin.Flow.contextMenuTargetConnector={init:tl};document.addEventListener("click",s=>{const i=s.composedPath().find(e=>e.hasAttribute&&e.hasAttribute("disableonclick"));i&&(i.disabled=!0)});/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class il extends ti(z(S(x(k(w))))){static get is(){return"vaadin-button"}static get styles(){return ys}static get properties(){return{disabled:{type:Boolean,value:!1,observer:"_disabledChanged",reflectToAttribute:!0,sync:!0}}}render(){return C`
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
    `}ready(){super.ready(),this._tooltipController=new Q(this),this.addController(this._tooltipController)}__shouldAllowFocusWhenDisabled(){return window.Vaadin.featureFlags.accessibleDisabledButtons}}y(il);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Oi=v`
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
`,sl=window.Vaadin.featureFlags.layoutComponentImprovements,nl=v`
  ::slotted([data-width-full]) {
    flex: 1;
  }

  ::slotted(vaadin-horizontal-layout[data-width-full]),
  ::slotted(vaadin-vertical-layout[data-width-full]) {
    min-width: 0;
  }
`,rl=sl?[Oi,nl]:[Oi];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ol=s=>class extends s{ready(){super.ready();const i=this.shadowRoot.querySelector("slot:not([name])");this.__startSlotObserver=new te(i,({currentNodes:n,removedNodes:r})=>{r.length&&this.__clearAttribute(r,"last-start-child");const o=n.filter(l=>l.nodeType===Node.ELEMENT_NODE);this.__updateAttributes(o,"start",!1,!0);const a=n.filter(l=>!ns(l));this.toggleAttribute("has-start",a.length>0)});const e=this.shadowRoot.querySelector('[name="end"]');this.__endSlotObserver=new te(e,({currentNodes:n,removedNodes:r})=>{r.length&&this.__clearAttribute(r,"first-end-child"),this.__updateAttributes(n,"end",!0,!1),this.toggleAttribute("has-end",n.length>0)});const t=this.shadowRoot.querySelector('[name="middle"]');this.__middleSlotObserver=new te(t,({currentNodes:n,removedNodes:r})=>{r.length&&(this.__clearAttribute(r,"first-middle-child"),this.__clearAttribute(r,"last-middle-child")),this.__updateAttributes(n,"middle",!0,!0),this.toggleAttribute("has-middle",n.length>0)})}__clearAttribute(i,e){const t=i.find(n=>n.nodeType===Node.ELEMENT_NODE&&n.hasAttribute(e));t&&t.removeAttribute(e)}__updateAttributes(i,e,t,n){i.forEach((r,o)=>{if(t){const a=`first-${e}-child`;o===0?r.setAttribute(a,""):r.hasAttribute(a)&&r.removeAttribute(a)}if(n){const a=`last-${e}-child`;o===i.length-1?r.setAttribute(a,""):r.hasAttribute(a)&&r.removeAttribute(a)}})}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class al extends ol(S(z(x(k(w))))){static get is(){return"vaadin-horizontal-layout"}static get styles(){return rl}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return C`
      <slot></slot>
      <slot name="middle"></slot>
      <slot name="end"></slot>
    `}}y(al);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ll=v`
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
 */const dl=v`
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
 */const hl=s=>class extends s{static get properties(){return{overlayClass:{type:String},_overlayElement:{type:Object}}}static get observers(){return["__updateOverlayClassNames(overlayClass, _overlayElement)"]}__updateOverlayClassNames(e,t){if(!t||e===void 0)return;const{classList:n}=t;if(this.__initialClasses||(this.__initialClasses=new Set(n)),Array.isArray(this.__previousClasses)){const o=this.__previousClasses.filter(a=>!this.__initialClasses.has(a));o.length>0&&n.remove(...o)}const r=typeof e=="string"?e.split(" ").filter(Boolean):[];r.length>0&&n.add(...r),this.__previousClasses=r}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const cl=s=>class extends s{static get properties(){return{opened:{type:Boolean,value:!1,sync:!0,observer:"_openedChanged"}}}constructor(){super(),this._boundVaadinOverlayClose=this._onVaadinOverlayClose.bind(this),ve&&(this._boundIosResizeListener=()=>this._detectIosNavbar())}firstUpdated(i){super.firstUpdated(i),this.popover="manual"}bringToFront(){this.matches(":popover-open")&&(this.hidePopover(),this.showPopover())}_openedChanged(i){i?(document.body.appendChild(this),this.showPopover(),document.addEventListener("vaadin-overlay-close",this._boundVaadinOverlayClose),this._boundIosResizeListener&&(this._detectIosNavbar(),window.addEventListener("resize",this._boundIosResizeListener))):(document.body.removeChild(this),this.hidePopover(),document.removeEventListener("vaadin-overlay-close",this._boundVaadinOverlayClose),this._boundIosResizeListener&&window.removeEventListener("resize",this._boundIosResizeListener))}_detectIosNavbar(){const i=window.innerHeight,t=window.innerWidth>i,n=document.documentElement.clientHeight;t&&n>i?this.style.bottom=`${n-i}px`:this.style.bottom="0"}_onVaadinOverlayClose(i){const e=i.detail.sourceEvent;e&&e.composedPath().indexOf(this)>=0&&i.preventDefault()}},ul=s=>class extends ze(hl(s)){static get properties(){return{assertive:{type:Boolean,value:!1,sync:!0},duration:{type:Number,value:5e3,sync:!0},opened:{type:Boolean,value:!1,notify:!0,sync:!0,observer:"_openedChanged"},position:{type:String,value:"bottom-start",observer:"_positionChanged",sync:!0},renderer:{type:Function,sync:!0}}}static get observers(){return["_durationChanged(duration, opened)","_rendererChanged(renderer, opened, _overlayElement)"]}static show(i,e){const t=customElements.get("vaadin-notification");return Yn(i)?t._createAndShowNotification(n=>{$t(i,n)},e):t._createAndShowNotification(n=>{n.innerText=i},e)}static _createAndShowNotification(i,e){const t=document.createElement("vaadin-notification");return e&&Number.isFinite(e.duration)&&(t.duration=e.duration),e&&e.position&&(t.position=e.position),e&&e.assertive&&(t.assertive=e.assertive),e&&e.theme&&t.setAttribute("theme",e.theme),t.renderer=i,document.body.appendChild(t),t.opened=!0,t.addEventListener("opened-changed",n=>{n.detail.value||t.remove()}),t}get _container(){const i=customElements.get("vaadin-notification");return i._container||(i._container=document.createElement("vaadin-notification-container"),document.body.appendChild(i._container)),i._container}get _card(){return this._overlayElement}ready(){super.ready(),this._overlayElement=this.shadowRoot.querySelector("vaadin-notification-card")}disconnectedCallback(){super.disconnectedCallback(),queueMicrotask(()=>{this.isConnected||(this.opened=!1)})}requestContentUpdate(){!this.renderer||!this._card||this.renderer(this._card,this)}__computeAriaLive(i){return i?"assertive":"polite"}_rendererChanged(i,e,t){if(!t)return;const n=this._oldRenderer!==i;this._oldRenderer=i,n&&(t.innerHTML="",delete t._$litPart$),e&&(this._didAnimateNotificationAppend||this._animatedAppendNotificationCard(),this.requestContentUpdate())}open(){this.opened=!0}close(){this.opened=!1}_openedChanged(i){i?(this._container.opened=!0,this._animatedAppendNotificationCard()):this._card&&this._closeNotificationCard()}__cleanUpOpeningClosingState(){this._card.removeAttribute("opening"),this._card.removeAttribute("closing"),this._card.removeEventListener("animationend",this.__animationEndListener)}_animatedAppendNotificationCard(){this._card?(this.__cleanUpOpeningClosingState(),this._card.setAttribute("opening",""),this._appendNotificationCard(),this.__animationEndListener=()=>this.__cleanUpOpeningClosingState(),this._card.addEventListener("animationend",this.__animationEndListener),this._didAnimateNotificationAppend=!0):this._didAnimateNotificationAppend=!1}_appendNotificationCard(){if(this._card){if(!this._container.shadowRoot.querySelector(`slot[name="${this.position}"]`)){console.warn(`Invalid alignment parameter provided: position=${this.position}`);return}this._container.firstElementChild&&this._container.bringToFront(),this._card.slot=this.position,this._container.firstElementChild&&/top/u.test(this.position)?this._container.insertBefore(this._card,this._container.firstElementChild):this._container.appendChild(this._card)}}_removeNotificationCard(){this._card&&(this._card.parentNode&&this._card.parentNode.removeChild(this._card),this._card.removeAttribute("closing"),this._container.opened=!!this._container.firstElementChild,this.dispatchEvent(new CustomEvent("closed")))}_closeNotificationCard(){this._durationTimeoutId&&clearTimeout(this._durationTimeoutId),this._animatedRemoveNotificationCard()}_animatedRemoveNotificationCard(){this.__cleanUpOpeningClosingState(),this._card.setAttribute("closing","");const i=getComputedStyle(this._card).getPropertyValue("animation-name");i&&i!=="none"?(this.__animationEndListener=()=>{this._removeNotificationCard(),this.__cleanUpOpeningClosingState()},this._card.addEventListener("animationend",this.__animationEndListener)):this._removeNotificationCard()}_positionChanged(){this.opened&&this._animatedAppendNotificationCard()}_durationChanged(i,e){e&&(clearTimeout(this._durationTimeoutId),i>0&&(this._durationTimeoutId=setTimeout(()=>this.close(),i)))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class _l extends cl(S(z(x(k(w))))){static get is(){return"vaadin-notification-container"}static get styles(){return dl}render(){return C`
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
    `}}class pl extends S(x(k(w))){static get is(){return"vaadin-notification-card"}static get styles(){return ll}render(){return C`
      <div part="overlay">
        <div part="content">
          <slot></slot>
        </div>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","alert")}}class fl extends ul(z(S(x(w)))){static get is(){return"vaadin-notification"}static get styles(){return v`
      :host {
        display: none !important;
      }
    `}render(){return C`
      <vaadin-notification-card
        theme="${U(this._theme)}"
        aria-live="${this.__computeAriaLive(this.assertive)}"
      ></vaadin-notification-card>
    `}}y(_l);y(pl);y(fl);function gl(s,i){if(i.type==="stateKeyChanged"){const{value:e}=i;return{...s,key:e}}else return s}const ml=()=>{};class vl extends HTMLElement{#e=void 0;#i=!1;#t=void 0;#s=Object.create(null);#r=new Map;#n=new Map;#o=ml;#d=new Map;#h;#a;#l;constructor(){super(),this.#h={useState:this.useState.bind(this),useCustomEvent:this.useCustomEvent.bind(this),useContent:this.useContent.bind(this)},this.#a=this.#u.bind(this),this.#_()}async connectedCallback(){this.#t=Ee.createElement(this.#a),!(!this.dispatchEvent(new CustomEvent("flow-portal-add",{bubbles:!0,cancelable:!0,composed:!0,detail:{children:this.#t,domNode:this}}))||this.#e)&&(await this.#l,this.#e=Ws.createRoot(this),this.#c(),this.#e.render(this.#t))}addReadyCallback(i,e){this.#d.set(i,e)}async disconnectedCallback(){this.#e?(this.#l=Promise.resolve(),await this.#l,this.#e.unmount(),this.#e=void 0):this.dispatchEvent(new CustomEvent("flow-portal-remove",{bubbles:!0,cancelable:!0,composed:!0,detail:{children:this.#t,domNode:this}})),this.#i=!1,this.#t=void 0}useState(i,e){if(this.#r.has(i))return[this.#s[i],this.#r.get(i)];const t=this[i]??e;this.#s[i]=t,Object.defineProperty(this,i,{enumerable:!0,get(){return this.#s[i]},set(o){this.#s[i]=o,this.#o({type:"stateKeyChanged",key:i,value:t})}});const n=this.useCustomEvent(`${i}-changed`,{detail:{value:t}}),r=o=>{this.#s[i]=o,n({value:o}),this.#o({type:"stateKeyChanged",key:i,value:o})};return this.#r.set(i,r),[t,r]}useCustomEvent(i,e={}){if(!this.#n.has(i)){const t=(n=>{const r=n===void 0?e:{...e,detail:n},o=new CustomEvent(i,r);return this.dispatchEvent(o)});return this.#n.set(i,t),t}return this.#n.get(i)}useContent(i){return Ee.useEffect(()=>{this.#d.get(i)?.()},[]),Ee.createElement("flow-content-container",{name:i,style:{display:"contents"}})}#c(){this.#i||!this.#e||(this.#e.render(Ee.createElement(this.#a)),this.#i=!0)}#u(){const[i,e]=Ee.useReducer(gl,this.#s);return this.#s=i,this.#o=e,this.render(this.#h)}#_(){let i=window.Vaadin||{};i.developmentMode&&(i.registrations=i.registrations||[],i.registrations.push({is:"ReactAdapterElement",version:"25.0.5"}))}}class bl extends vl{async connectedCallback(){await super.connectedCallback(),this.style.display="contents"}render(){return qs.jsx(Us,{})}}customElements.define("react-router-outlet",bl);const yl=s=>Promise.resolve(0);window.Vaadin=window.Vaadin||{};window.Vaadin.Flow=window.Vaadin.Flow||{};window.Vaadin.Flow.loadOnDemand=yl;window.Vaadin.Flow.resetFocus=()=>{let s=document.activeElement;for(;s&&s.shadowRoot;)s=s.shadowRoot.activeElement;return!s||s.blur()||s.focus()||!0};
