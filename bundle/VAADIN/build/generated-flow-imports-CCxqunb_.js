import{f as Br,S as Vr,i as C,b as y,a as E,A as Ue,c as Li,t as we,e as Fi,E as Re,D as Ut,_ as Hr,r as O,d as rt,g as Wr,j as qr,O as Ur}from"./indexhtml-Dt_kNJgh.js";import"./commonjsHelpers-CqkleIqs.js";/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */window.Vaadin||={};window.Vaadin.featureFlags||={};function Yr(s){return s.replace(/-[a-z]/gu,i=>i[1].toUpperCase())}const le={};function w(s,i="25.0.3"){if(Object.defineProperty(s,"version",{get(){return i}}),s.experimental){const t=typeof s.experimental=="string"?s.experimental:`${Yr(s.is.split("-").slice(1).join("-"))}Component`;if(!window.Vaadin.featureFlags[t]&&!le[t]){le[t]=new Set,le[t].add(s),Object.defineProperty(window.Vaadin.featureFlags,t,{get(){return le[t].size===0},set(n){n&&le[t].size>0&&(le[t].forEach(r=>{customElements.define(r.is,r)}),le[t].clear())}});return}else if(le[t]){le[t].add(s);return}}const e=customElements.get(s.is);if(!e)customElements.define(s.is,s);else{const t=e.version;t&&s.version&&t===s.version?console.warn(`The component ${s.is} has been loaded twice`):console.error(`Tried to define ${s.is} version ${s.version} when version ${e.version} is already in use. Something will probably break.`)}}const jr=/\/\*[\*!]\s+vaadin-dev-mode:start([\s\S]*)vaadin-dev-mode:end\s+\*\*\//i,Ot=window.Vaadin&&window.Vaadin.Flow&&window.Vaadin.Flow.clients;function Gr(){function s(){return!0}return Js(s)}function Kr(){try{return Xr()?!0:Qr()?Ot?!Zr():!Gr():!1}catch{return!1}}function Xr(){return localStorage.getItem("vaadin.developmentmode.force")}function Qr(){return["localhost","127.0.0.1"].indexOf(window.location.hostname)>=0}function Zr(){return!!(Ot&&Object.keys(Ot).map(i=>Ot[i]).filter(i=>i.productionMode).length>0)}function Js(s,i){if(typeof s!="function")return;const e=jr.exec(s.toString());if(e)try{s=new Function(e[1])}catch(t){console.log("vaadin-development-mode-detector: uncommentAndRun() failed",t)}return s(i)}window.Vaadin=window.Vaadin||{};const _s=function(s,i){if(window.Vaadin.developmentMode)return Js(s,i)};window.Vaadin.developmentMode===void 0&&(window.Vaadin.developmentMode=Kr());function Jr(){/*! vaadin-dev-mode:start
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

  vaadin-dev-mode:end **/}const eo=function(){if(typeof _s=="function")return _s(Jr)};/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
 */let ps=0,en=0;const Ke=[];let wi=!1;function to(){wi=!1;const s=Ke.length;for(let i=0;i<s;i++){const e=Ke[i];if(e)try{e()}catch(t){setTimeout(()=>{throw t})}}Ke.splice(0,s),en+=s}const K={after(s){return{run(i){return window.setTimeout(i,s)},cancel(i){window.clearTimeout(i)}}},run(s,i){return window.setTimeout(s,i)},cancel(s){window.clearTimeout(s)}},ue={run(s){return window.requestAnimationFrame(s)},cancel(s){window.cancelAnimationFrame(s)}},tn={run(s){return window.requestIdleCallback?window.requestIdleCallback(s):window.setTimeout(s,16)},cancel(s){window.cancelIdleCallback?window.cancelIdleCallback(s):window.clearTimeout(s)}},te={run(s){wi||(wi=!0,queueMicrotask(()=>to())),Ke.push(s);const i=ps;return ps+=1,i},cancel(s){const i=s-en;if(i>=0){if(!Ke[i])throw new Error(`invalid async handle: ${s}`);Ke[i]=null}}};/**
@license
Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/const pt=new Set;class D{static debounce(i,e,t){return i instanceof D?i._cancelAsync():i=new D,i.setConfig(e,t),i}constructor(){this._asyncModule=null,this._callback=null,this._timer=null}setConfig(i,e){this._asyncModule=i,this._callback=e,this._timer=this._asyncModule.run(()=>{this._timer=null,pt.delete(this),this._callback()})}cancel(){this.isActive()&&(this._cancelAsync(),pt.delete(this))}_cancelAsync(){this.isActive()&&(this._asyncModule.cancel(this._timer),this._timer=null)}flush(){this.isActive()&&(this.cancel(),this._callback())}isActive(){return this._timer!=null}}function sn(s){pt.add(s)}function io(){const s=!!pt.size;return pt.forEach(i=>{try{i.flush()}catch(e){setTimeout(()=>{throw e})}}),s}const ut=()=>{let s;do s=io();while(s)};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const de=[];function Ci(s,i,e=s.getAttribute("dir")){i?s.setAttribute("dir",i):e!=null&&s.removeAttribute("dir")}function xi(){return document.documentElement.getAttribute("dir")}function so(){const s=xi();de.forEach(i=>{Ci(i,s)})}const no=new MutationObserver(so);no.observe(document.documentElement,{attributes:!0,attributeFilter:["dir"]});const z=s=>class extends s{static get properties(){return{dir:{type:String,value:"",reflectToAttribute:!0,converter:{fromAttribute:e=>e||"",toAttribute:e=>e===""?null:e}}}}get __isRTL(){return this.getAttribute("dir")==="rtl"}connectedCallback(){super.connectedCallback(),(!this.hasAttribute("dir")||this.__restoreSubscription)&&(this.__subscribe(),Ci(this,xi(),null))}attributeChangedCallback(e,t,n){if(super.attributeChangedCallback(e,t,n),e!=="dir")return;const r=xi(),o=n===r&&de.indexOf(this)===-1,a=!n&&t&&de.indexOf(this)===-1;o||a?(this.__subscribe(),Ci(this,r,n)):n!==r&&t===r&&this.__unsubscribe()}disconnectedCallback(){super.disconnectedCallback(),this.__restoreSubscription=de.includes(this),this.__unsubscribe()}_valueToNodeAttribute(e,t,n){n==="dir"&&t===""&&!e.hasAttribute("dir")||super._valueToNodeAttribute(e,t,n)}_attributeToProperty(e,t,n){e==="dir"&&!t?this.dir="":super._attributeToProperty(e,t,n)}__subscribe(){de.includes(this)||de.push(this)}__unsubscribe(){de.includes(this)&&de.splice(de.indexOf(this),1)}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */window.Vaadin||(window.Vaadin={});window.Vaadin.registrations||(window.Vaadin.registrations=[]);window.Vaadin.developmentModeCallback||(window.Vaadin.developmentModeCallback={});window.Vaadin.developmentModeCallback["vaadin-usage-statistics"]=function(){eo()};let ni;const fs=new Set,L=s=>class extends z(s){static finalize(){super.finalize();const{is:e}=this;if(e&&!fs.has(e)){window.Vaadin.registrations.push(this),fs.add(e);const t=window.Vaadin.developmentModeCallback;t&&(ni=D.debounce(ni,tn,()=>{t["vaadin-usage-statistics"]()}),sn(ni))}}constructor(){super(),document.doctype===null&&console.warn('Vaadin components require the "standards mode" declaration. Please add <!DOCTYPE html> to the HTML document.')}},nn=new WeakMap;function ro(s,i){let e=i;for(;e;){if(nn.get(e)===s)return!0;e=Object.getPrototypeOf(e)}return!1}function J(s){return i=>{if(ro(s,i))return i;const e=s(i);return nn.set(e,s),e}}/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Ee(s,i){return s.split(".").reduce((e,t)=>e?e[t]:void 0,i)}function oo(s,i,e){const t=s.split("."),n=t.pop(),r=t.reduce((o,a)=>o[a],e);r[n]=i}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ri={},ao=/([A-Z])/gu;function ms(s){return ri[s]||(ri[s]=s.replace(ao,"-$1").toLowerCase()),ri[s]}function gs(s){return s[0].toUpperCase()+s.substring(1)}function oi(s){const[i,e]=s.split("("),t=e.replace(")","").split(",").map(n=>n.trim());return{method:i,observerProps:t}}function ai(s,i){return Object.prototype.hasOwnProperty.call(s,i)||(s[i]=new Map(s[i])),s[i]}const lo=s=>{class i extends s{static enabledWarnings=[];static createProperty(t,n){[String,Boolean,Number,Array].includes(n)&&(n={type:n}),n&&n.reflectToAttribute&&(n.reflect=!0),super.createProperty(t,n)}static getOrCreateMap(t){return ai(this,t)}static finalize(){if(window.litIssuedWarnings&&(window.litIssuedWarnings.add("no-override-create-property"),window.litIssuedWarnings.add("no-override-get-property-descriptor")),super.finalize(),Array.isArray(this.observers)){const t=this.getOrCreateMap("__complexObservers");this.observers.forEach(n=>{const{method:r,observerProps:o}=oi(n);t.set(r,o)})}}static addCheckedInitializer(t){super.addInitializer(n=>{n instanceof this&&t(n)})}static getPropertyDescriptor(t,n,r){const o=super.getPropertyDescriptor(t,n,r);let a=o;if(this.getOrCreateMap("__propKeys").set(t,n),r.sync&&(a={get:o.get,set(l){const d=this[t];Br(l,d)&&(this[n]=l,this.requestUpdate(t,d,r),this.hasUpdated&&this.performUpdate())},configurable:!0,enumerable:!0}),r.readOnly){const l=a.set;this.addCheckedInitializer(d=>{d[`_set${gs(t)}`]=function(h){l.call(d,h)}}),a={get:a.get,set(){},configurable:!0,enumerable:!0}}if("value"in r&&this.addCheckedInitializer(l=>{const d=typeof r.value=="function"?r.value.call(l):r.value;r.readOnly?l[`_set${gs(t)}`](d):l[t]=d}),r.observer){const l=r.observer;this.getOrCreateMap("__observers").set(t,l),this.addCheckedInitializer(d=>{d[l]||console.warn(`observer method ${l} not defined`)})}if(r.notify){if(!this.__notifyProps)this.__notifyProps=new Set;else if(!this.hasOwnProperty("__notifyProps")){const l=this.__notifyProps;this.__notifyProps=new Set(l)}this.__notifyProps.add(t)}if(r.computed){const l=`__assignComputed${t}`,d=oi(r.computed);this.prototype[l]=function(...h){this[t]=this[d.method](...h)},this.getOrCreateMap("__computedObservers").set(l,d.observerProps)}return r.attribute||(r.attribute=ms(t)),a}static get polylitConfig(){return{asyncFirstRender:!1}}connectedCallback(){super.connectedCallback();const{polylitConfig:t}=this.constructor;!this.hasUpdated&&!t.asyncFirstRender&&this.performUpdate()}firstUpdated(){super.firstUpdated(),this.$||(this.$={}),this.renderRoot.querySelectorAll("[id]").forEach(t=>{this.$[t.id]=t})}ready(){}willUpdate(t){this.constructor.__computedObservers&&this.__runComplexObservers(t,this.constructor.__computedObservers)}updated(t){const n=this.__isReadyInvoked;this.__isReadyInvoked=!0,this.constructor.__observers&&this.__runObservers(t,this.constructor.__observers),this.constructor.__complexObservers&&this.__runComplexObservers(t,this.constructor.__complexObservers),this.__dynamicPropertyObservers&&this.__runDynamicObservers(t,this.__dynamicPropertyObservers),this.__dynamicMethodObservers&&this.__runComplexObservers(t,this.__dynamicMethodObservers),this.constructor.__notifyProps&&this.__runNotifyProps(t,this.constructor.__notifyProps),n||this.ready()}setProperties(t){Object.entries(t).forEach(([n,r])=>{const o=this.constructor.__propKeys.get(n),a=this[o];this[o]=r,this.requestUpdate(n,a)}),this.hasUpdated&&this.performUpdate()}_createMethodObserver(t){const n=ai(this,"__dynamicMethodObservers"),{method:r,observerProps:o}=oi(t);n.set(r,o)}_createPropertyObserver(t,n){ai(this,"__dynamicPropertyObservers").set(n,t)}__runComplexObservers(t,n){n.forEach((r,o)=>{r.some(a=>t.has(a))&&(this[o]?this[o](...r.map(a=>this[a])):console.warn(`observer method ${o} not defined`))})}__runDynamicObservers(t,n){n.forEach((r,o)=>{t.has(r)&&this[o]&&this[o](this[r],t.get(r))})}__runObservers(t,n){t.forEach((r,o)=>{const a=n.get(o);a!==void 0&&this[a]&&this[a](this[o],r)})}__runNotifyProps(t,n){t.forEach((r,o)=>{n.has(o)&&this.dispatchEvent(new CustomEvent(`${ms(o)}-changed`,{detail:{value:this[o]}}))})}_get(t,n){return Ee(t,n)}_set(t,n,r){oo(t,n,r)}}return i},I=J(lo);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class $i extends EventTarget{#e;#i=new Set;#t;#s=!1;constructor(i){super(),this.#e=i,this.#t=new CSSStyleSheet}#r(i){const{propertyName:e}=i;this.#i.has(e)&&this.dispatchEvent(new CustomEvent("property-changed",{detail:{propertyName:e}}))}observe(i){this.connect(),!this.#i.has(i)&&(this.#i.add(i),this.#t.replaceSync(`
      :root::before, :host::before {
        content: '' !important;
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
        visibility: hidden !important;
        transition: 1ms allow-discrete step-end !important;
        transition-property: ${[...this.#i].join(", ")} !important;
      }
    `))}connect(){this.#s||(this.#e.adoptedStyleSheets.unshift(this.#t),this.#n.addEventListener("transitionstart",i=>this.#r(i)),this.#n.addEventListener("transitionend",i=>this.#r(i)),this.#s=!0)}disconnect(){this.#i.clear(),this.#e.adoptedStyleSheets=this.#e.adoptedStyleSheets.filter(i=>i!==this.#t),this.#n.removeEventListener("transitionstart",this.#r),this.#n.removeEventListener("transitionend",this.#r),this.#s=!1}get#n(){return this.#e.documentElement??this.#e.host}static for(i){return i.__cssPropertyObserver||=new $i(i),i.__cssPropertyObserver}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function ho(s){const{baseStyles:i,themeStyles:e,elementStyles:t,lumoInjector:n}=s.constructor,r=s.__lumoStyleSheet;return r&&(i||e)?[...n.includeBaseStyles?i:[],r,...e]:[r,...t].filter(Boolean)}function rn(s){Vr(s.shadowRoot,ho(s))}function vs(s,i){s.__lumoStyleSheet=i,rn(s)}function li(s){s.__lumoStyleSheet=void 0,rn(s)}/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const bs=new Set;function zi(s){bs.has(s)||(bs.add(s),console.warn(s))}/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ys=new WeakMap;function ws(s){try{return s.media.mediaText}catch{return zi('[LumoInjector] Browser denied to access property "mediaText" for some CSS rules, so they were skipped.'),""}}function co(s){try{return s.cssRules}catch{return zi('[LumoInjector] Browser denied to access property "cssRules" for some CSS stylesheets, so they were skipped.'),[]}}function on(s,i={tags:new Map,modules:new Map}){for(const e of co(s)){if(e instanceof CSSImportRule){const t=ws(e);t.startsWith("lumo_")?i.modules.set(t,[...e.styleSheet.cssRules]):on(e.styleSheet,i);continue}if(e instanceof CSSMediaRule){const t=ws(e);t.startsWith("lumo_")&&i.modules.set(t,[...e.cssRules]);continue}if(e instanceof CSSStyleRule&&e.cssText.includes("-inject")){for(const t of e.style){const n=t.match(/^--_lumo-(.*)-inject-modules$/u)?.[1];if(!n)continue;const r=e.style.getPropertyValue(t);i.tags.set(n,r.split(",").map(o=>o.trim().replace(/'|"/gu,"")))}continue}}return i}function uo(s){let i=new Map,e=new Map;for(const t of s){let n=ys.get(t);n||(n=on(t),ys.set(t,n)),i=new Map([...i,...n.tags]),e=new Map([...e,...n.modules])}return{tags:i,modules:e}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function an(s){return`--_lumo-${s.is}-inject`}class _o{#e;#i;#t=new Map;#s=new Map;constructor(i=document){this.#e=i,this.handlePropertyChange=this.handlePropertyChange.bind(this),this.#i=$i.for(i),this.#i.addEventListener("property-changed",this.handlePropertyChange)}disconnect(){this.#i.removeEventListener("property-changed",this.handlePropertyChange),this.#t.clear(),this.#s.values().forEach(i=>i.forEach(li))}forceUpdate(){for(const i of this.#t.keys())this.#n(i)}componentConnected(i){const{lumoInjector:e}=i.constructor,{is:t}=e;this.#s.set(t,this.#s.get(t)??new Set),this.#s.get(t).add(i);const n=this.#t.get(t);if(n){n.cssRules.length>0&&vs(i,n);return}this.#r(t);const r=an(e);this.#i.observe(r)}componentDisconnected(i){const{is:e}=i.constructor.lumoInjector;this.#s.get(e)?.delete(i),li(i)}handlePropertyChange(i){const{propertyName:e}=i.detail,t=e.match(/^--_lumo-(.*)-inject$/u)?.[1];t&&this.#n(t)}#r(i){this.#t.set(i,new CSSStyleSheet),this.#n(i)}#n(i){const{tags:e,modules:t}=uo(this.#o),n=(e.get(i)??[]).flatMap(o=>t.get(o)??[]).map(o=>o.cssText).join(`
`),r=this.#t.get(i);r.replaceSync(n),this.#s.get(i)?.forEach(o=>{n?vs(o,r):li(o)})}get#o(){let i=new Set;for(const e of[this.#e,document])i=i.union(new Set(e.styleSheets)),i=i.union(new Set(e.adoptedStyleSheets));return[...i]}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Cs=new Set;function ln(s){const i=s.getRootNode();return i.host&&i.host.constructor.version?ln(i.host):i}const A=s=>class extends s{static finalize(){super.finalize();const e=an(this.lumoInjector);this.is&&!Cs.has(e)&&(Cs.add(e),CSS.registerProperty({name:e,syntax:"<number>",inherits:!0,initialValue:"0"}))}static get lumoInjector(){return{is:this.is,includeBaseStyles:!1}}connectedCallback(){super.connectedCallback();const e=ln(this);e.__lumoInjectorDisabled||this.isConnected&&(e.__lumoInjector||=new _o(e),this.__lumoInjector=e.__lumoInjector,this.__lumoInjector.componentConnected(this))}disconnectedCallback(){super.disconnectedCallback(),this.__lumoInjector&&(this.__lumoInjector.componentDisconnected(this),this.__lumoInjector=void 0)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const st=s=>class extends s{static get properties(){return{_theme:{type:String,readOnly:!0}}}static get observedAttributes(){return[...super.observedAttributes,"theme"]}attributeChangedCallback(e,t,n){super.attributeChangedCallback(e,t,n),e==="theme"&&this._set_theme(n)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ei=[],po=new Set,fo=new Set;function mo(s){return s&&Object.prototype.hasOwnProperty.call(s,"__themes")}function go(s,i){return(s||"").split(" ").some(e=>new RegExp(`^${e.split("*").join(".*")}$`,"u").test(i))}function vo(s){return s.map(i=>i.cssText).join(`
`)}const bo="vaadin-themable-mixin-style";function yo(s,i){const e=document.createElement("style");e.id=bo,e.textContent=vo(s),i.content.appendChild(e)}function wo(s=""){let i=0;return s.startsWith("lumo-")||s.startsWith("material-")?i=1:s.startsWith("vaadin-")&&(i=2),i}function dn(s){const i=[];return s.include&&[].concat(s.include).forEach(e=>{const t=Ei.find(n=>n.moduleId===e);t?i.push(...dn(t),...t.styles):console.warn(`Included moduleId ${e} not found in style registry`)},s.styles),i}function Co(s){const i=`${s}-default-theme`,e=Ei.filter(t=>t.moduleId!==i&&go(t.themeFor,s)).map(t=>({...t,styles:[...dn(t),...t.styles],includePriority:wo(t.moduleId)})).sort((t,n)=>n.includePriority-t.includePriority);return e.length>0?e:Ei.filter(t=>t.moduleId===i)}const T=s=>class extends st(s){constructor(){super(),po.add(new WeakRef(this))}static finalize(){if(super.finalize(),this.is&&fo.add(this.is),this.elementStyles)return;const e=this.prototype._template;!e||mo(this)||yo(this.getStylesForThis(),e)}static finalizeStyles(e){return this.baseStyles=e?[e].flat(1/0):[],this.themeStyles=this.getStylesForThis(),[...this.baseStyles,...this.themeStyles]}static getStylesForThis(){const e=s.__themes||[],t=Object.getPrototypeOf(this.prototype),n=(t?t.constructor.__themes:[])||[];this.__themes=[...e,...n,...Co(this.is)];const r=this.__themes.flatMap(o=>o.styles);return r.filter((o,a)=>a===r.lastIndexOf(o))}};/**
 * @license
 * Copyright (c) 2026 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const hn=(s,...i)=>{const e=document.createElement("style");e.id=s,e.textContent=i.map(t=>t.toString()).join(`
`),document.head.insertAdjacentElement("afterbegin",e)};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */["--vaadin-text-color","--vaadin-text-color-disabled","--vaadin-text-color-secondary","--vaadin-border-color","--vaadin-border-color-secondary","--vaadin-background-color"].forEach(s=>{CSS.registerProperty({name:s,syntax:"<color>",inherits:!0,initialValue:"light-dark(black, white)"})});hn("vaadin-base",C`
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
 */const xs=C`
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
`,xo=window.Vaadin.featureFlags.layoutComponentImprovements,Eo=C`
  ::slotted([data-height-full]) {
    flex: 1;
  }

  ::slotted(vaadin-horizontal-layout[data-height-full]),
  ::slotted(vaadin-vertical-layout[data-height-full]) {
    min-height: 0;
  }
`,Io=xo?[xs,Eo]:[xs];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class So extends T(L(I(A(E)))){static get is(){return"vaadin-vertical-layout"}static get styles(){return Io}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return y`<slot></slot>`}}w(So);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const me=C`
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
 */const ko=C`
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
`,To=C`
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
`,Ao=[me,ko,To];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Yt=s=>s.test(navigator.userAgent),Ii=s=>s.test(navigator.platform),Do=s=>s.test(navigator.vendor),Si=Yt(/Android/u),cn=Yt(/Chrome/u)&&Do(/Google Inc/u),un=Yt(/Firefox/u),Oo=Ii(/^iPad/u)||Ii(/^Mac/u)&&navigator.maxTouchPoints>1,Po=Ii(/^iPhone/u),ze=Po||Oo,Ni=Yt(/^((?!chrome|android).)*safari/iu),Ne=(()=>{try{return document.createEvent("TouchEvent"),!0}catch{return!1}})();/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let Bi=!1;window.addEventListener("keydown",()=>{Bi=!0},{capture:!0});window.addEventListener("mousedown",()=>{Bi=!1},{capture:!0});function Lt(){let s=document.activeElement||document.body;for(;s.shadowRoot&&s.shadowRoot.activeElement;)s=s.shadowRoot.activeElement;return s}function Q(){return Bi}function _n(s){const i=s.style;if(i.visibility==="hidden"||i.display==="none")return!0;const e=window.getComputedStyle(s);return e.visibility==="hidden"||e.display==="none"}function Mo(s,i){const e=Math.max(s.tabIndex,0),t=Math.max(i.tabIndex,0);return e===0||t===0?t>e:e>t}function Ro(s,i){const e=[];for(;s.length>0&&i.length>0;)Mo(s[0],i[0])?e.push(i.shift()):e.push(s.shift());return e.concat(s,i)}function ki(s){const i=s.length;if(i<2)return s;const e=Math.ceil(i/2),t=ki(s.slice(0,e)),n=ki(s.slice(e));return Ro(t,n)}function se(s){return s.checkVisibility?!s.checkVisibility({visibilityProperty:!0}):s.offsetParent===null&&s.clientWidth===0&&s.clientHeight===0?!0:_n(s)}function mt(s){return s.matches('[tabindex="-1"]')?!1:s.matches("input, select, textarea, button, object")?s.matches(":not([disabled])"):s.matches("a[href], area[href], iframe, [tabindex], [contentEditable]")}function Je(s){return s.getRootNode().activeElement===s}function Lo(s){if(!mt(s))return-1;const i=s.getAttribute("tabindex")||0;return Number(i)}function pn(s,i){if(s.nodeType!==Node.ELEMENT_NODE||_n(s))return!1;const e=s,t=Lo(e);let n=t>0;t>=0&&i.push(e);let r=[];return e.localName==="slot"?r=e.assignedNodes({flatten:!0}):r=(e.shadowRoot||e).children,[...r].forEach(o=>{n=pn(o,i)||n}),n}function Fo(s){const i=[];return pn(s,i)?ki(i):i}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class $o{saveFocus(i){this.focusNode=i||Lt()}restoreFocus(i){const e=this.focusNode;if(!e)return;const t={preventScroll:i?i.preventScroll:!1,focusVisible:i?i.focusVisible:!1};Lt()===document.body?setTimeout(()=>e.focus(t)):e.focus(t),this.focusNode=null}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const di=[];class zo{constructor(i){this.host=i,this.__trapNode=null,this.__onKeyDown=this.__onKeyDown.bind(this)}get __focusableElements(){return Fo(this.__trapNode)}get __focusedElementIndex(){const i=this.__focusableElements;return i.indexOf(i.filter(Je).pop())}hostConnected(){document.addEventListener("keydown",this.__onKeyDown)}hostDisconnected(){document.removeEventListener("keydown",this.__onKeyDown)}trapFocus(i){if(this.__trapNode=i,this.__focusableElements.length===0)throw this.__trapNode=null,new Error("The trap node should have at least one focusable descendant or be focusable itself.");di.push(this),this.__focusedElementIndex===-1&&this.__focusableElements[0].focus({focusVisible:Q()})}releaseFocus(){this.__trapNode=null,di.pop()}__onKeyDown(i){if(this.__trapNode&&this===Array.from(di).pop()&&i.key==="Tab"){i.preventDefault();const e=i.shiftKey;this.__focusNextElement(e)}}__focusNextElement(i=!1){const e=this.__focusableElements,t=i?-1:1,n=this.__focusedElementIndex,r=(e.length+n+t)%e.length,o=e[r];o.focus({focusVisible:!0}),o.localName==="input"&&o.select()}}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const fn=s=>class extends s{static get properties(){return{focusTrap:{type:Boolean,value:!1},restoreFocusOnClose:{type:Boolean,value:!1},restoreFocusNode:{type:HTMLElement}}}constructor(){super(),this.__focusTrapController=new zo(this),this.__focusRestorationController=new $o}get _contentRoot(){return this}ready(){super.ready(),this.addController(this.__focusTrapController),this.addController(this.__focusRestorationController)}get _focusTrapRoot(){return this.$.overlay}_resetFocus(){if(this.focusTrap&&this.__focusTrapController.releaseFocus(),this.restoreFocusOnClose&&this._shouldRestoreFocus()){const e=Q(),t=!e;this.__focusRestorationController.restoreFocus({preventScroll:t,focusVisible:e})}}_saveFocus(){this.restoreFocusOnClose&&this.__focusRestorationController.saveFocus(this.restoreFocusNode)}_trapFocus(){this.focusTrap&&!se(this._focusTrapRoot)&&this.__focusTrapController.trapFocus(this._focusTrapRoot)}_shouldRestoreFocus(){const e=Lt();return e===document.body||this._deepContains(e)}_deepContains(e){if(this._contentRoot.contains(e))return!0;let t=e;const n=e.ownerDocument;for(;t&&t!==n&&t!==this._contentRoot;)t=t.parentNode||t.host;return t===this._contentRoot}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Pt=new Set,Ft=()=>[...Pt].filter(s=>!s.hasAttribute("closing")),mn=s=>{const i=Ft(),e=i[i.indexOf(s)+1];return e?s._deepContains(e)?mn(e):!1:!0},Es=(s,i=e=>!0)=>{const e=Ft().filter(i);return s===e.pop()},No=s=>class extends s{get _last(){return Es(this)}get _isAttached(){return Pt.has(this)}bringToFront(){Es(this)||mn(this)||(this.matches(":popover-open")&&(this.hidePopover(),this.showPopover()),this._removeAttachedInstance(),this._appendAttachedInstance())}_enterModalState(){document.body.style.pointerEvents!=="none"&&(this._previousDocumentPointerEvents=document.body.style.pointerEvents,document.body.style.pointerEvents="none"),Ft().forEach(e=>{e!==this&&(e.$.overlay.style.pointerEvents="none")})}_exitModalState(){this._previousDocumentPointerEvents!==void 0&&(document.body.style.pointerEvents=this._previousDocumentPointerEvents,delete this._previousDocumentPointerEvents);const e=Ft();let t;for(;(t=e.pop())&&!(t!==this&&(t.$.overlay.style.removeProperty("pointer-events"),!t.modeless)););}_appendAttachedInstance(){Pt.add(this)}_removeAttachedInstance(){this._isAttached&&Pt.delete(this)}};/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Bo(s,i){let e=null,t;const n=document.documentElement;function r(){t&&clearTimeout(t),e&&e.disconnect(),e=null}function o(a=!1,l=1){r();const{left:d,top:h,width:c,height:f}=s.getBoundingClientRect();if(a||i(),!c||!f)return;const m=Math.floor(h),v=Math.floor(n.clientWidth-(d+c)),x=Math.floor(n.clientHeight-(h+f)),b=Math.floor(d),u={rootMargin:`${-m}px ${-v}px ${-x}px ${-b}px`,threshold:Math.max(0,Math.min(1,l))||1};let _=!0;function p(g){const S=g[0].intersectionRatio;if(S!==l){if(!_)return o();S?o(!1,S):t=setTimeout(()=>{o(!1,1e-7)},1e3)}_=!1}e=new IntersectionObserver(p,u),e.observe(s)}return o(!0),r}function U(s,i,e){const t=[s];s.owner&&t.push(s.owner),typeof e=="string"?t.forEach(n=>{n.setAttribute(i,e)}):e?t.forEach(n=>{n.setAttribute(i,"")}):t.forEach(n=>{n.removeAttribute(i)})}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ge=s=>class extends fn(No(s)){static get properties(){return{opened:{type:Boolean,notify:!0,observer:"_openedChanged",reflectToAttribute:!0,sync:!0},owner:{type:Object,sync:!0},model:{type:Object,sync:!0},renderer:{type:Object,sync:!0},modeless:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_modelessChanged",sync:!0},hidden:{type:Boolean,reflectToAttribute:!0,observer:"_hiddenChanged",sync:!0},withBackdrop:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_withBackdropChanged",sync:!0}}}static get observers(){return["_rendererOrDataChanged(renderer, owner, model, opened)"]}get _rendererRoot(){return this}constructor(){super(),this._boundMouseDownListener=this._mouseDownListener.bind(this),this._boundMouseUpListener=this._mouseUpListener.bind(this),this._boundOutsideClickListener=this._outsideClickListener.bind(this),this._boundKeydownListener=this._keydownListener.bind(this),ze&&(this._boundIosResizeListener=()=>this._detectIosNavbar())}firstUpdated(){super.firstUpdated(),this.popover="manual",this.addEventListener("click",()=>{}),this.$.backdrop&&this.$.backdrop.addEventListener("click",()=>{}),this.addEventListener("mouseup",()=>{document.activeElement===document.body&&this.$.overlay.getAttribute("tabindex")==="0"&&this.$.overlay.focus()}),this.addEventListener("animationcancel",()=>{this._flushAnimation("opening"),this._flushAnimation("closing")})}connectedCallback(){super.connectedCallback(),this._boundIosResizeListener&&(this._detectIosNavbar(),window.addEventListener("resize",this._boundIosResizeListener))}disconnectedCallback(){super.disconnectedCallback(),this.__scheduledOpen&&(cancelAnimationFrame(this.__scheduledOpen),this.__scheduledOpen=null),this._boundIosResizeListener&&window.removeEventListener("resize",this._boundIosResizeListener)}requestContentUpdate(){this.renderer&&this.renderer.call(this.owner,this._rendererRoot,this.owner,this.model)}close(e){const t=new CustomEvent("vaadin-overlay-close",{bubbles:!0,cancelable:!0,detail:{overlay:this,sourceEvent:e}});this.dispatchEvent(t),document.body.dispatchEvent(t),t.defaultPrevented||(this.opened=!1)}setBounds(e,t=!0){const n=this.$.overlay,r={...e};t&&n.style.position!=="absolute"&&(n.style.position="absolute"),Object.keys(r).forEach(o=>{r[o]!==null&&!isNaN(r[o])&&(r[o]=`${r[o]}px`)}),Object.assign(n.style,r)}_detectIosNavbar(){if(!this.opened)return;const e=window.innerHeight,n=window.innerWidth>e,r=document.documentElement.clientHeight;n&&r>e?this.style.setProperty("--vaadin-overlay-viewport-bottom",`${r-e}px`):this.style.setProperty("--vaadin-overlay-viewport-bottom","0")}_shouldAddGlobalListeners(){return!this.modeless}_addGlobalListeners(){this.__hasGlobalListeners||(this.__hasGlobalListeners=!0,document.addEventListener("mousedown",this._boundMouseDownListener),document.addEventListener("mouseup",this._boundMouseUpListener),document.documentElement.addEventListener("click",this._boundOutsideClickListener,!0))}_removeGlobalListeners(){this.__hasGlobalListeners&&(this.__hasGlobalListeners=!1,document.removeEventListener("mousedown",this._boundMouseDownListener),document.removeEventListener("mouseup",this._boundMouseUpListener),document.documentElement.removeEventListener("click",this._boundOutsideClickListener,!0))}_rendererOrDataChanged(e,t,n,r){const o=this._oldOwner!==t||this._oldModel!==n;this._oldModel=n,this._oldOwner=t;const a=this._oldRenderer!==e,l=this._oldRenderer!==void 0;this._oldRenderer=e;const d=this._oldOpened!==r;this._oldOpened=r,a&&l&&(this._rendererRoot.innerHTML="",delete this._rendererRoot._$litPart$),r&&e&&(a||d||o)&&this.requestContentUpdate()}_modelessChanged(e){this.opened&&(this._shouldAddGlobalListeners()?this._addGlobalListeners():this._removeGlobalListeners()),e?this._exitModalState():this.opened&&this._enterModalState(),U(this,"modeless",e)}_withBackdropChanged(e){U(this,"with-backdrop",e)}_openedChanged(e,t){if(e){if(!this.isConnected){this.opened=!1;return}this._saveFocus(),this._animatedOpening(),this.__scheduledOpen=requestAnimationFrame(()=>{setTimeout(()=>{this._trapFocus();const n=new CustomEvent("vaadin-overlay-open",{detail:{overlay:this},bubbles:!0});this.dispatchEvent(n),document.body.dispatchEvent(n)})}),document.addEventListener("keydown",this._boundKeydownListener),this._shouldAddGlobalListeners()&&this._addGlobalListeners()}else t&&(this.__scheduledOpen&&(cancelAnimationFrame(this.__scheduledOpen),this.__scheduledOpen=null),this._resetFocus(),this._animatedClosing(),document.removeEventListener("keydown",this._boundKeydownListener),this._shouldAddGlobalListeners()&&this._removeGlobalListeners())}_hiddenChanged(e){e&&this.hasAttribute("closing")&&this._flushAnimation("closing")}_shouldAnimate(){const e=getComputedStyle(this),t=e.getPropertyValue("animation-name");return!(e.getPropertyValue("display")==="none")&&t&&t!=="none"}_enqueueAnimation(e,t){const n=`__${e}Handler`,r=o=>{o&&o.target!==this||(t(),this.removeEventListener("animationend",r),delete this[n])};this[n]=r,this.addEventListener("animationend",r)}_flushAnimation(e){const t=`__${e}Handler`;typeof this[t]=="function"&&this[t]()}_animatedOpening(){this._isAttached&&this.hasAttribute("closing")&&this._flushAnimation("closing"),this._attachOverlay(),this._appendAttachedInstance(),this.bringToFront(),this.modeless||this._enterModalState(),U(this,"opening",!0),this._shouldAnimate()?this._enqueueAnimation("opening",()=>{this._finishOpening()}):this._finishOpening()}_attachOverlay(){this.showPopover()}_finishOpening(){U(this,"opening",!1)}_finishClosing(){this._detachOverlay(),this._removeAttachedInstance(),this.$.overlay.style.removeProperty("pointer-events"),U(this,"closing",!1),this.dispatchEvent(new CustomEvent("vaadin-overlay-closed"))}_animatedClosing(){this.hasAttribute("opening")&&this._flushAnimation("opening"),this._isAttached&&(this._exitModalState(),U(this,"closing",!0),this.dispatchEvent(new CustomEvent("vaadin-overlay-closing")),this._shouldAnimate()?this._enqueueAnimation("closing",()=>{this._finishClosing()}):this._finishClosing())}_detachOverlay(){this.hidePopover()}_mouseDownListener(e){this._mouseDownInside=e.composedPath().indexOf(this.$.overlay)>=0}_mouseUpListener(e){this._mouseUpInside=e.composedPath().indexOf(this.$.overlay)>=0}_shouldCloseOnOutsideClick(e){return this._last}_outsideClickListener(e){if(e.composedPath().includes(this.$.overlay)||this._mouseDownInside||this._mouseUpInside){this._mouseDownInside=!1,this._mouseUpInside=!1;return}if(!this._shouldCloseOnOutsideClick(e))return;const t=new CustomEvent("vaadin-overlay-outside-click",{cancelable:!0,detail:{sourceEvent:e}});this.dispatchEvent(t),this.opened&&!t.defaultPrevented&&this.close(e)}_keydownListener(e){if(!(!this._last||e.defaultPrevented)&&!(!this._shouldAddGlobalListeners()&&!e.composedPath().includes(this._focusTrapRoot))&&e.key==="Escape"){const t=new CustomEvent("vaadin-overlay-escape-press",{cancelable:!0,detail:{sourceEvent:e}});this.dispatchEvent(t),this.opened&&!t.defaultPrevented&&this.close(e)}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Vo=s=>class extends ge(s){static get properties(){return{headerTitle:{type:String},headerRenderer:{type:Object},footerRenderer:{type:Object}}}static get observers(){return["_headerFooterRendererChange(headerRenderer, footerRenderer, opened)","_headerTitleChanged(headerTitle, opened)"]}get _contentRoot(){return this.owner}get _rendererRoot(){if(!this.__savedRoot){const e=document.createElement("vaadin-dialog-content");e.style.display="contents",this.owner.appendChild(e),this.__savedRoot=e}return this.__savedRoot}ready(){super.ready(),this.__resizeObserver=new ResizeObserver(()=>{requestAnimationFrame(()=>{this.__updateOverflow()})}),this.__resizeObserver.observe(this.$.resizerContainer),this.$.content.addEventListener("scroll",()=>{this.__updateOverflow()}),this.shadowRoot.addEventListener("slotchange",()=>{this.__updateOverflow()})}__createContainer(e){const t=document.createElement("vaadin-dialog-content");return t.setAttribute("slot",e),t}__clearContainer(e){e.innerHTML="",delete e._$litPart$}__initContainer(e,t){return e?this.__clearContainer(e):(e=this.__createContainer(t),this.owner.appendChild(e)),e}_headerFooterRendererChange(e,t,n){const r=this.__oldHeaderRenderer!==e;this.__oldHeaderRenderer=e;const o=this.__oldFooterRenderer!==t;this.__oldFooterRenderer=t;const a=this._oldOpenedFooterHeader!==n;this._oldOpenedFooterHeader=n,U(this,"has-header",!!e),U(this,"has-footer",!!t),r&&(e?this.headerContainer=this.__initContainer(this.headerContainer,"header-content"):this.headerContainer&&(this.headerContainer.remove(),this.headerContainer=null,this.__updateOverflow())),o&&(t?this.footerContainer=this.__initContainer(this.footerContainer,"footer"):this.footerContainer&&(this.footerContainer.remove(),this.footerContainer=null,this.__updateOverflow())),(e&&(r||a)||t&&(o||a))&&n&&this.requestContentUpdate()}_headerTitleChanged(e,t){U(this,"has-title",!!e),t&&(e||this._oldHeaderTitle)&&this.requestContentUpdate(),this._oldHeaderTitle=e}_headerTitleRenderer(){this.headerTitle?(this.headerTitleElement||(this.headerTitleElement=document.createElement("h2"),this.headerTitleElement.setAttribute("slot","title"),this.headerTitleElement.classList.add("draggable")),this.owner.appendChild(this.headerTitleElement),this.headerTitleElement.textContent=this.headerTitle):this.headerTitleElement&&(this.headerTitleElement.remove(),this.headerTitleElement=null)}requestContentUpdate(){super.requestContentUpdate(),this.headerContainer&&this.headerRenderer&&this.headerRenderer.call(this.owner,this.headerContainer,this.owner),this.footerContainer&&this.footerRenderer&&this.footerRenderer.call(this.owner,this.footerContainer,this.owner),this._headerTitleRenderer(),this.__updateOverflow()}getBounds(){const e=this.$.overlay.getBoundingClientRect(),t=this.getBoundingClientRect(),n=e.top-t.top,r=e.left-t.left,o=e.width,a=e.height;return{top:n,left:r,width:o,height:a}}__updateOverflow(){let e="";const t=this.$.content;t.scrollTop>0&&(e+=" top"),t.scrollTop<t.scrollHeight-t.clientHeight&&(e+=" bottom");const n=e.trim();n.length>0&&this.getAttribute("overflow")!==n?U(this,"overflow",n):n.length===0&&this.hasAttribute("overflow")&&U(this,"overflow",null)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ho extends Vo(z(T(I(A(E))))){static get is(){return"vaadin-dialog-overlay"}static get styles(){return Ao}get _focusTrapRoot(){return this.owner}render(){return y`
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
    `}}w(Ho);/**
 * @license
 * Copyright 2018 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const B=s=>s??Ue;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Wo=s=>class extends s{static get properties(){return{opened:{type:Boolean,reflectToAttribute:!0,value:!1,notify:!0,sync:!0},noCloseOnOutsideClick:{type:Boolean,value:!1},noCloseOnEsc:{type:Boolean,value:!1},modeless:{type:Boolean,value:!1},top:{type:String},left:{type:String},overlayRole:{type:String}}}static get observers(){return["__positionChanged(top, left)"]}ready(){super.ready();const e=this.$.overlay;e.addEventListener("vaadin-overlay-outside-click",this._handleOutsideClick.bind(this)),e.addEventListener("vaadin-overlay-escape-press",this._handleEscPress.bind(this)),e.addEventListener("vaadin-overlay-closed",this.__handleOverlayClosed.bind(this)),this._overlayElement=e,this.hasAttribute("role")||(this.role="dialog"),this.setAttribute("tabindex","0")}updated(e){super.updated(e),e.has("overlayRole")&&(this.role=this.overlayRole||"dialog"),e.has("modeless")&&(this.modeless?this.removeAttribute("aria-modal"):this.setAttribute("aria-modal","true"))}__handleOverlayClosed(){this.dispatchEvent(new CustomEvent("closed"))}connectedCallback(){super.connectedCallback(),this.__restoreOpened&&(this.opened=!0)}disconnectedCallback(){super.disconnectedCallback(),setTimeout(()=>{this.isConnected||(this.__restoreOpened=this.opened,this.opened=!1)})}_onOverlayOpened(e){e.detail.value===!1&&(this.opened=!1)}_handleOutsideClick(e){this.noCloseOnOutsideClick&&e.preventDefault()}_handleEscPress(e){this.noCloseOnEsc&&e.preventDefault()}_bringOverlayToFront(){this.modeless&&this._overlayElement.bringToFront()}__positionChanged(e,t){requestAnimationFrame(()=>this.$.overlay.setBounds({top:e,left:t}))}__sizeChanged(e,t){requestAnimationFrame(()=>this.$.overlay.setBounds({width:e,height:t},!1))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function $t(s){return s.touches?s.touches[0]:s}function gn(s){return s.clientX>=0&&s.clientX<=window.innerWidth&&s.clientY>=0&&s.clientY<=window.innerHeight}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const qo=s=>class extends s{static get properties(){return{draggable:{type:Boolean,value:!1,reflectToAttribute:!0},_touchDevice:{type:Boolean,value:Ne},__dragHandleClassName:{type:String}}}ready(){super.ready(),this._originalBounds={},this._originalMouseCoords={},this._startDrag=this._startDrag.bind(this),this._drag=this._drag.bind(this),this._stopDrag=this._stopDrag.bind(this),this.$.overlay.$.overlay.addEventListener("mousedown",this._startDrag),this.$.overlay.$.overlay.addEventListener("touchstart",this._startDrag)}_startDrag(e){if(!(e.type==="touchstart"&&e.touches.length>1)&&this.draggable&&(e.button===0||e.touches)){const t=this.$.overlay.$.resizerContainer,n=e.target===t,r=e.offsetX>t.clientWidth||e.offsetY>t.clientHeight,o=e.target===this.$.overlay.$.content,a=e.composedPath().some((l,d)=>{if(!l.classList)return!1;const h=l.classList.contains(this.__dragHandleClassName||"draggable"),c=l.classList.contains("draggable-leaf-only"),f=d===0;return c&&f||h&&(!c||f)});if(n&&!r||o||a){a||e.preventDefault(),this._originalBounds=this.$.overlay.getBounds();const l=$t(e);if(this._originalMouseCoords={top:l.pageY,left:l.pageX},window.addEventListener("mouseup",this._stopDrag),window.addEventListener("touchend",this._stopDrag),window.addEventListener("mousemove",this._drag),window.addEventListener("touchmove",this._drag),this.$.overlay.$.overlay.style.position!=="absolute"){const{top:d,left:h}=this._originalBounds;this.top=d,this.left=h}}}}_drag(e){const t=$t(e);if(gn(t)){const n=this._originalBounds.top+(t.pageY-this._originalMouseCoords.top),r=this._originalBounds.left+(t.pageX-this._originalMouseCoords.left);this.top=n,this.left=r}}_stopDrag(){this.dispatchEvent(new CustomEvent("dragged",{bubbles:!0,composed:!0,detail:{top:this.top,left:this.left}})),window.removeEventListener("mouseup",this._stopDrag),window.removeEventListener("touchend",this._stopDrag),window.removeEventListener("mousemove",this._drag),window.removeEventListener("touchmove",this._drag)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Uo=s=>class extends s{static get properties(){return{renderer:{type:Object},headerTitle:String,headerRenderer:{type:Object},footerRenderer:{type:Object}}}requestContentUpdate(){this._overlayElement&&this._overlayElement.requestContentUpdate()}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Yo=s=>class extends s{static get properties(){return{resizable:{type:Boolean,value:!1,reflectToAttribute:!0}}}ready(){super.ready(),this._originalBounds={},this._originalMouseCoords={},this._resizeListeners={start:{},resize:{},stop:{}},this._addResizeListeners()}_addResizeListeners(){["n","e","s","w","nw","ne","se","sw"].forEach(e=>{const t=document.createElement("div");this._resizeListeners.start[e]=n=>this._startResize(n,e),this._resizeListeners.resize[e]=n=>this._resize(n,e),this._resizeListeners.stop[e]=()=>this._stopResize(e),e.length===1&&t.classList.add("edge"),t.classList.add("resizer"),t.classList.add(e),t.addEventListener("mousedown",this._resizeListeners.start[e]),t.addEventListener("touchstart",this._resizeListeners.start[e]),this.$.overlay.$.resizerContainer.appendChild(t)})}_startResize(e,t){if(!(e.type==="touchstart"&&e.touches.length>1)&&(e.button===0||e.touches)){e.preventDefault(),this._originalBounds=this.$.overlay.getBounds();const n=$t(e);this._originalMouseCoords={top:n.pageY,left:n.pageX},window.addEventListener("mousemove",this._resizeListeners.resize[t]),window.addEventListener("touchmove",this._resizeListeners.resize[t]),window.addEventListener("mouseup",this._resizeListeners.stop[t]),window.addEventListener("touchend",this._resizeListeners.stop[t]),this.$.overlay.setBounds(this._originalBounds),this.$.overlay.setAttribute("has-bounds-set","")}}_resize(e,t){const n=$t(e);gn(n)&&t.split("").forEach(o=>{switch(o){case"n":{const a=this._originalBounds.height-(n.pageY-this._originalMouseCoords.top),l=this._originalBounds.top+(n.pageY-this._originalMouseCoords.top);a>40&&(this.top=l,this.height=a);break}case"e":{const a=this._originalBounds.width+(n.pageX-this._originalMouseCoords.left);a>40&&(this.width=a);break}case"s":{const a=this._originalBounds.height+(n.pageY-this._originalMouseCoords.top);a>40&&(this.height=a);break}case"w":{const a=this._originalBounds.width-(n.pageX-this._originalMouseCoords.left),l=this._originalBounds.left+(n.pageX-this._originalMouseCoords.left);a>40&&(this.left=l,this.width=a);break}}})}_stopResize(e){window.removeEventListener("mousemove",this._resizeListeners.resize[e]),window.removeEventListener("touchmove",this._resizeListeners.resize[e]),window.removeEventListener("mouseup",this._resizeListeners.stop[e]),window.removeEventListener("touchend",this._resizeListeners.stop[e]),this.dispatchEvent(new CustomEvent("resize",{detail:this._getResizeDimensions()}))}_getResizeDimensions(){const{width:e,height:t,top:n,left:r}=getComputedStyle(this.$.overlay.$.overlay);return{width:e,height:t,top:n,left:r}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const jo=s=>class extends s{static get properties(){return{width:{type:String},height:{type:String}}}static get observers(){return["__sizeChanged(width, height)"]}__sizeChanged(e,t){requestAnimationFrame(()=>this.$.overlay.setBounds({width:e,height:t},!1))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Go extends jo(qo(Yo(Uo(Wo(st(L(I(E)))))))){static get is(){return"vaadin-dialog"}static get styles(){return C`
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
    `}render(){return y`
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
        theme="${B(this._theme)}"
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
    `}updated(i){super.updated(i),i.has("headerTitle")&&(this.ariaLabel=this.headerTitle)}}w(Go);/**
 * @license
 * Copyright 2020 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Ko=(s,i)=>s?._$litType$!==void 0,vn=s=>s.strings===void 0,Xo={},Qo=(s,i=Xo)=>s._$AH=i;/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const _t=(s,i)=>{const e=s._$AN;if(e===void 0)return!1;for(const t of e)t._$AO?.(i,!1),_t(t,i);return!0},zt=s=>{let i,e;do{if((i=s._$AM)===void 0)break;e=i._$AN,e.delete(s),s=i}while(e?.size===0)},bn=s=>{for(let i;i=s._$AM;s=i){let e=i._$AN;if(e===void 0)i._$AN=e=new Set;else if(e.has(s))break;e.add(s),ea(i)}};function Zo(s){this._$AN!==void 0?(zt(this),this._$AM=s,bn(this)):this._$AM=s}function Jo(s,i=!1,e=0){const t=this._$AH,n=this._$AN;if(n!==void 0&&n.size!==0)if(i)if(Array.isArray(t))for(let r=e;r<t.length;r++)_t(t[r],!1),zt(t[r]);else t!=null&&(_t(t,!1),zt(t));else _t(this,s)}const ea=s=>{s.type==we.CHILD&&(s._$AP??=Jo,s._$AQ??=Zo)};class ta extends Li{constructor(){super(...arguments),this._$AN=void 0}_$AT(i,e,t){super._$AT(i,e,t),bn(this),this.isConnected=i._$AU}_$AO(i,e=!0){i!==this.isConnected&&(this.isConnected=i,i?this.reconnected?.():this.disconnected?.()),e&&(_t(this,i),zt(this))}setValue(i){if(vn(this._$Ct))this._$Ct._$AI(i,this);else{const e=[...this._$Ct._$AH];e[this._$Ci]=i,this._$Ct._$AI(e,this,0)}}disconnected(){}reconnected(){}}class ia extends ta{constructor(i){if(super(i),i.type!==we.CHILD)throw new Error(`${this.constructor.directiveName}() can only be used in child bindings`)}update(i,[e,t]){return this.updateContent(i,e,t),Re}updateContent(i,e,t){const{parentNode:n,startNode:r}=i;this.__parentNode=n;const o=t!=null,a=o?this.getNewNode(e,t):null,l=this.getOldNode(i);if(clearTimeout(this.__parentNode.__nodeRetryTimeout),o&&!a)this.__parentNode.__nodeRetryTimeout=setTimeout(()=>this.updateContent(i,e,t));else{if(l===a)return;l&&a?n.replaceChild(a,l):l?n.removeChild(l):a&&r.after(a)}}getNewNode(i,e){return window.Vaadin.Flow.clients[i].getByNodeId(e)}getOldNode(i){const{startNode:e,endNode:t}=i;if(e.nextSibling!==t)return e.nextSibling}disconnected(){clearTimeout(this.__parentNode.__nodeRetryTimeout)}}const yn=Fi(ia);function sa(s,i){return yn(s,i)}function na(s,i,e){Ut(y`${i.map(t=>yn(s,t))}`,e)}function ra(s){const i=s.insertBefore;s.insertBefore=function(e,t){return t&&t.parentNode===this?i.call(this,e,t):i.call(this,e,null)}}window.Vaadin||={};window.Vaadin.FlowComponentHost||={patchVirtualContainer:ra,getNode:sa,setChildNodes:na};/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */CSS.registerProperty({name:"--_min-width-labels-aside",syntax:"<length>",inherits:!1,initialValue:"0px"});hn("vaadin-form-layout-base",C`
    @layer vaadin.base {
      html {
        --vaadin-form-layout-label-spacing: var(--vaadin-gap-s);
        --vaadin-form-layout-label-width: 8em;
        --vaadin-form-layout-column-spacing: var(--vaadin-gap-l);
        --vaadin-form-layout-row-spacing: var(--vaadin-gap-l);
      }
    }
  `);const oa=C`
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
`,aa=C`
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
 */const hi=new WeakMap;function la(s){return hi.has(s)||hi.set(s,new Set),hi.get(s)}function da(s,i){const e=document.createElement("style");e.textContent=s,i===document?document.head.appendChild(e):i.insertBefore(e,i.firstChild)}const gt=J(s=>class extends s{get slotStyles(){return[]}connectedCallback(){super.connectedCallback(),this.__applySlotStyles()}__applySlotStyles(){const e=this.getRootNode(),t=la(e);this.slotStyles.forEach(n=>{t.has(n)||(da(n,e),t.add(n))})}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class wn{constructor(i,e){this.host=i,this.props={},this.config=e,this.isConnected=!1,this.__resizeObserver=new ResizeObserver(t=>setTimeout(()=>this._onResize(t))),this.__mutationObserver=new MutationObserver(t=>this._onMutation(t))}connect(){this.isConnected||(this.isConnected=!0,this.__resizeObserver.observe(this.host),this.__mutationObserver.observe(this.host,this.config.mutationObserverOptions))}disconnect(){this.isConnected&&(this.isConnected=!1,this.__resizeObserver.disconnect(),this.__mutationObserver.disconnect())}setProps(i){this.props=i}updateLayout(){}_onResize(i){}_onMutation(i){}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Is(s){return s.localName==="br"}class ha extends wn{constructor(i){super(i,{mutationObserverOptions:{subtree:!0,childList:!0,attributes:!0,attributeFilter:["colspan","data-colspan","hidden"]}})}connect(){this.isConnected||(super.connect(),this.updateLayout())}disconnect(){if(!this.isConnected)return;super.disconnect();const{host:i}=this;i.style.removeProperty("--_column-width"),i.style.removeProperty("--_max-columns"),i.$.layout.removeAttribute("fits-labels-aside"),i.$.layout.style.removeProperty("--_grid-rendered-column-count"),this.__children.forEach(e=>{e.style.removeProperty("--_grid-colstart"),e.style.removeProperty("--_grid-colspan")})}setProps(i){super.setProps(i),this.isConnected&&this.updateLayout()}updateLayout(){const{host:i,props:e}=this;if(!this.isConnected||se(i))return;let t=0,n=0;const r=this.__children;r.filter(o=>Is(o)||!se(o)).forEach((o,a,l)=>{const d=l[a-1];if(Is(o)){t=0;return}(d&&d.parentElement!==o.parentElement||!e.autoRows&&o.parentElement===i)&&(t=0),e.autoRows&&t===0?o.style.setProperty("--_grid-colstart",1):o.style.removeProperty("--_grid-colstart");const h=o.getAttribute("colspan")||o.getAttribute("data-colspan");h?(t+=parseInt(h),o.style.setProperty("--_grid-colspan",h)):(t+=1,o.style.removeProperty("--_grid-colspan")),n=Math.max(n,t)}),r.filter(se).forEach(o=>{o.style.removeProperty("--_grid-colstart")}),e.columnWidth?i.style.setProperty("--_column-width",e.columnWidth):i.style.removeProperty("--_column-width"),i.style.setProperty("--_min-columns",e.minColumns),i.style.setProperty("--_max-columns",Math.min(Math.max(e.minColumns,e.maxColumns),n)),i.$.layout.toggleAttribute("fits-labels-aside",this.props.labelsAside&&this.__fitsLabelsAside),i.$.layout.style.setProperty("--_grid-rendered-column-count",this.__renderedColumnCount)}_onResize(){this.updateLayout()}_onMutation(i){i.some(({target:t})=>t===this.host||t.parentElement===this.host||t.parentElement.localName==="vaadin-form-row")&&this.updateLayout()}get __children(){return[...this.host.children].flatMap(i=>i.localName==="vaadin-form-row"?[...i.children]:i)}get __renderedColumnCount(){const{gridTemplateColumns:i}=getComputedStyle(this.host.$.layout);return i.split(" ").filter(e=>e!=="0px").length}get __minWidthLabelsAside(){return parseFloat(getComputedStyle(this.host).getPropertyValue("--_min-width-labels-aside"))}get __fitsLabelsAside(){return this.host.offsetWidth>=this.__minWidthLabelsAside}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function ca(s){return CSS.supports("word-spacing",s)&&!["inherit","normal"].includes(s)}function Ss(s){return typeof s=="number"&&s>=1&&s<1/0?Math.floor(s):1}class ua extends wn{constructor(i){super(i,{mutationObserverOptions:{subtree:!0,childList:!0,attributes:!0,attributeFilter:["colspan","data-colspan","hidden"]}})}connect(){this.isConnected||(super.connect(),this.__selectResponsiveStep(),this.updateLayout(),requestAnimationFrame(()=>this.__selectResponsiveStep()),requestAnimationFrame(()=>this.updateLayout()))}disconnect(){if(!this.isConnected)return;super.disconnect();const{host:i}=this;i.$.layout.style.removeProperty("opacity"),[...i.children].forEach(e=>{e.style.removeProperty("width"),e.style.removeProperty("margin-left"),e.style.removeProperty("margin-right"),e.removeAttribute("label-position")})}setProps(i){const{responsiveSteps:e}=i;if(!Array.isArray(e))throw new Error('Invalid "responsiveSteps" type, an Array is required.');if(e.length<1)throw new Error('Invalid empty "responsiveSteps" array, at least one item is required.');e.forEach(t=>{if(Ss(t.columns)!==t.columns)throw new Error(`Invalid 'columns' value of ${t.columns}, a natural number is required.`);if(t.minWidth!==void 0&&!ca(t.minWidth))throw new Error(`Invalid 'minWidth' value of ${t.minWidth}, a valid CSS length required.`);if(t.labelsPosition!==void 0&&["aside","top"].indexOf(t.labelsPosition)===-1)throw new Error(`Invalid 'labelsPosition' value of ${t.labelsPosition}, 'aside' or 'top' string is required.`)}),super.setProps(i),this.isConnected&&(this.__selectResponsiveStep(),this.updateLayout())}updateLayout(){const{host:i}=this;if(!this.isConnected||se(i))return;const e=getComputedStyle(i),t=e.getPropertyValue("--_column-spacing"),n=e.direction,r=`margin-${n==="ltr"?"left":"right"}`,o=`margin-${n==="ltr"?"right":"left"}`,a=i.offsetWidth;let l=0;Array.from(i.children).filter(d=>d.localName==="br"||getComputedStyle(d).display!=="none").forEach((d,h,c)=>{if(d.localName==="br"){l=0;return}const f=d.getAttribute("colspan")||d.getAttribute("data-colspan");let m;m=Ss(parseFloat(f)),m=Math.min(m,this.__columnCount);const v=m/this.__columnCount;d.style.width=`calc(${v*100}% - ${1-v} * ${t})`,l+m>this.__columnCount&&(l=0),l===0?d.style.setProperty(r,"0px"):d.style.removeProperty(r);const x=h+1,b=x<c.length&&c[x].localName==="br";if(l+m===this.__columnCount)d.style.setProperty(o,"0px");else if(b){const k=(this.__columnCount-l-m)/this.__columnCount;d.style.setProperty(o,`calc(${k*a}px + ${k} * ${t})`)}else d.style.removeProperty(o);l=(l+m)%this.__columnCount,d.localName==="vaadin-form-item"&&(this.__labelsOnTop?d.getAttribute("label-position")!=="top"&&(d.__useLayoutLabelPosition=!0,d.setAttribute("label-position","top")):d.__useLayoutLabelPosition&&(delete d.__useLayoutLabelPosition,d.removeAttribute("label-position")))})}_onResize(){const{host:i}=this;if(se(i)){i.$.layout.style.opacity="0";return}this.__selectResponsiveStep(),this.updateLayout(),i.$.layout.style.opacity=""}_onMutation(i){i.some(({target:t})=>t===this.host||t.parentElement===this.host)&&this.updateLayout()}__selectResponsiveStep(){if(!this.isConnected)return;const{host:i,props:e}=this;let t;const n="background-position";e.responsiveSteps.forEach(r=>{i.$.layout.style.setProperty(n,r.minWidth),parseFloat(getComputedStyle(i.$.layout).getPropertyValue(n))<=i.offsetWidth&&(t=r)}),i.$.layout.style.removeProperty(n),t&&(this.__columnCount=t.columns,this.__labelsOnTop=t.labelsPosition==="top")}}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const _a=s=>class extends gt(s){static get properties(){return{responsiveSteps:{type:Array,value(){return[{minWidth:0,columns:1,labelsPosition:"top"},{minWidth:"20em",columns:1},{minWidth:"40em",columns:2}]},observer:"__responsiveStepsChanged",sync:!0},autoResponsive:{type:Boolean,sync:!0,value:()=>!!(window.Vaadin&&window.Vaadin.featureFlags&&window.Vaadin.featureFlags.defaultAutoResponsiveFormLayout),reflectToAttribute:!0},columnWidth:{type:String,sync:!0},maxColumns:{type:Number,sync:!0,value:10},minColumns:{type:Number,sync:!0,value:1},autoRows:{type:Boolean,sync:!0,value:!1,reflectToAttribute:!0},labelsAside:{type:Boolean,sync:!0,value:!1,reflectToAttribute:!0},expandColumns:{type:Boolean,sync:!0,value:!1,reflectToAttribute:!0},expandFields:{type:Boolean,sync:!0,value:!1,reflectToAttribute:!0}}}static get observers(){return["__autoResponsiveLayoutPropsChanged(columnWidth, maxColumns, minColumns, autoRows, labelsAside, expandColumns, expandFields)","__autoResponsiveChanged(autoResponsive)"]}constructor(){super(),this.__currentLayout,this.__autoResponsiveLayout=new ha(this),this.__responsiveStepsLayout=new ua(this)}connectedCallback(){super.connectedCallback(),this.__currentLayout.connect()}disconnectedCallback(){super.disconnectedCallback(),this.__currentLayout.disconnect()}get slotStyles(){return[`${aa}`.replace("vaadin-form-layout",this.localName)]}_updateLayout(){this.__currentLayout.updateLayout()}__responsiveStepsChanged(i,e){try{this.__responsiveStepsLayout.setProps({responsiveSteps:i})}catch(t){e&&e!==i?(console.warn(`${t.message} Using previously set 'responsiveSteps' instead.`),this.responsiveSteps=e):(console.warn(`${t.message} Using default 'responsiveSteps' instead.`),this.responsiveSteps=[{minWidth:0,columns:1,labelsPosition:"top"},{minWidth:"20em",columns:1},{minWidth:"40em",columns:2}])}}__autoResponsiveLayoutPropsChanged(i,e,t,n,r,o,a){this.__autoResponsiveLayout.setProps({columnWidth:i,maxColumns:e,minColumns:t,autoRows:n,labelsAside:r,expandColumns:o,expandFields:a})}__autoResponsiveChanged(i){this.__currentLayout&&this.__currentLayout.disconnect(),i?this.__currentLayout=this.__autoResponsiveLayout:this.__currentLayout=this.__responsiveStepsLayout,this.__currentLayout.connect()}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class pa extends _a(T(L(I(E)))){static get is(){return"vaadin-form-layout"}static get styles(){return oa}render(){return y`
      <div id="layout">
        <slot id="slot"></slot>
      </div>
    `}}w(pa);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const fa=C`
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
 */function ma(s){const i=[];for(;s;){if(s.nodeType===Node.DOCUMENT_NODE){i.push(s);break}if(s.nodeType===Node.DOCUMENT_FRAGMENT_NODE){i.push(s),s=s.host;continue}if(s.assignedSlot){s=s.assignedSlot;continue}s=s.parentNode}return i}function Cn(s,i){return i?i.closest(s)||Cn(s,i.getRootNode().host):null}function Vi(s){return s?new Set(s.split(" ")):new Set}function jt(s){return s?[...s].join(" "):""}function Gt(s,i,e){const t=Vi(s.getAttribute(i));t.add(e),s.setAttribute(i,jt(t))}function Hi(s,i,e){const t=Vi(s.getAttribute(i));if(t.delete(e),t.size===0){s.removeAttribute(i);return}s.setAttribute(i,jt(t))}function xn(s){return s.nodeType===Node.TEXT_NODE&&s.textContent.trim()===""}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let ga=0;function Se(){return ga++}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const va=s=>class extends s{constructor(){super(),this.__onFieldInteraction=this.__onFieldInteraction.bind(this),this.__fieldNodeObserver=new MutationObserver(()=>this.__synchronizeAttributes()),this.__labelNode=null,this.__fieldNode=null,this.__isFieldDirty=!1}ready(){super.ready()}_getFieldAriaTarget(i){return i.ariaTarget||i}__linkLabelToField(i){Gt(this._getFieldAriaTarget(i),"aria-labelledby",this.__labelId)}__unlinkLabelFromField(i){Hi(this._getFieldAriaTarget(i),"aria-labelledby",this.__labelId)}__onLabelClick(){const i=this.__fieldNode;i&&(i.focus({focusVisible:!1}),i.click())}__onLabelSlotChange(){this.__labelNode&&(this.__labelNode=null,this.__fieldNode&&this.__unlinkLabelFromField(this.__fieldNode));const i=this.$.labelSlot.assignedElements()[0];i&&(this.__labelNode=i,this.__labelNode.id?this.__labelId=this.__labelNode.id:(this.__labelId=`label-${this.localName}-${Se()}`,this.__labelNode.id=this.__labelId),this.__fieldNode&&this.__linkLabelToField(this.__fieldNode))}__onContentSlotChange(){this.__fieldNode&&(this.__unlinkLabelFromField(this.__fieldNode),this.__fieldNodeObserver.disconnect(),this.__fieldNode.removeEventListener("blur",this.__onFieldInteraction),this.__fieldNode.removeEventListener("change",this.__onFieldInteraction),this.__fieldNode=null,this.__isFieldDirty=!1);const i=this.$.contentSlot.assignedElements();i.length>1&&zi(`WARNING: Since Vaadin 23, placing multiple fields directly to a <vaadin-form-item> is deprecated.
Please wrap fields with a <vaadin-custom-field> instead.`);const e=i.find(t=>t.validate||t.checkValidity);e&&(this.__fieldNode=e,this.__fieldNode.addEventListener("blur",this.__onFieldInteraction),this.__fieldNode.addEventListener("change",this.__onFieldInteraction),this.__fieldNodeObserver.observe(this.__fieldNode,{attributes:!0,attributeFilter:["required","invalid"]}),this.__labelNode&&this.__linkLabelToField(this.__fieldNode)),this.__synchronizeAttributes()}__onFieldInteraction(){this.__isFieldDirty=!0,this.__synchronizeAttributes()}__synchronizeAttributes(){const i=this.__fieldNode;if(!i){this.removeAttribute("required"),this.removeAttribute("invalid");return}this.toggleAttribute("required",i.hasAttribute("required")),this.toggleAttribute("invalid",i.hasAttribute("invalid")||i.matches(":invalid")&&this.__isFieldDirty)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ba extends va(T(I(A(E)))){static get is(){return"vaadin-form-item"}static get styles(){return fa}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return y`
      <div id="label" part="label" @click="${this.__onLabelClick}">
        <slot name="label" id="labelSlot" @slotchange="${this.__onLabelSlotChange}"></slot>
        <span part="required-indicator" aria-hidden="true"></span>
      </div>
      <div id="spacing"></div>
      <div id="content">
        <slot id="contentSlot" @slotchange="${this.__onContentSlotChange}"></slot>
      </div>
    `}}w(ba);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ya=C`
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
 */class wa extends T(I(E)){static get is(){return"vaadin-form-row"}static get styles(){return ya}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return y`<slot></slot>`}}w(wa);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ca=C`
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
 */class En extends T(z(I(A(E)))){static get is(){return"vaadin-input-container"}static get styles(){return Ca}static get properties(){return{disabled:{type:Boolean,reflectToAttribute:!0},readonly:{type:Boolean,reflectToAttribute:!0},invalid:{type:Boolean,reflectToAttribute:!0}}}render(){return y`
      <slot name="prefix"></slot>
      <slot></slot>
      <slot name="suffix"></slot>
    `}ready(){super.ready(),this.addEventListener("pointerdown",i=>{i.target===this&&i.preventDefault()}),this.addEventListener("click",i=>{i.target===this&&this.shadowRoot.querySelector("slot:not([name])").assignedNodes({flatten:!0}).forEach(e=>e.focus&&e.focus())})}}w(En);/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ce{constructor(i,e){this.slot=i,this.callback=e,this._storedNodes=[],this._connected=!1,this._scheduled=!1,this._boundSchedule=()=>{this._schedule()},this.connect(),this._schedule()}connect(){this.slot.addEventListener("slotchange",this._boundSchedule),this._connected=!0}disconnect(){this.slot.removeEventListener("slotchange",this._boundSchedule),this._connected=!1}_schedule(){this._scheduled||(this._scheduled=!0,queueMicrotask(()=>{this.flush()}))}flush(){this._connected&&(this._scheduled=!1,this._processNodes())}_processNodes(){const i=this.slot.assignedNodes({flatten:!0});let e=[];const t=[],n=[];i.length&&(e=i.filter(r=>!this._storedNodes.includes(r))),this._storedNodes.length&&this._storedNodes.forEach((r,o)=>{const a=i.indexOf(r);a===-1?t.push(r):a!==o&&n.push(r)}),(e.length||t.length||n.length)&&this.callback({addedNodes:e,currentNodes:i,movedNodes:n,removedNodes:t}),this._storedNodes=i}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class G extends EventTarget{static generateId(i,e="default"){return`${e}-${i.localName}-${Se()}`}constructor(i,e,t,n={}){super();const{initializer:r,multiple:o,observe:a,useUniqueId:l,uniqueIdPrefix:d}=n;this.host=i,this.slotName=e,this.tagName=t,this.observe=typeof a=="boolean"?a:!0,this.multiple=typeof o=="boolean"?o:!1,this.slotInitializer=r,o&&(this.nodes=[]),l&&(this.defaultId=this.constructor.generateId(i,d||e))}hostConnected(){this.initialized||(this.multiple?this.initMultiple():this.initSingle(),this.observe&&this.observeSlot(),this.initialized=!0)}initSingle(){let i=this.getSlotChild();i?(this.node=i,this.initAddedNode(i)):(i=this.attachDefaultNode(),this.initNode(i))}initMultiple(){const i=this.getSlotChildren();if(i.length===0){const e=this.attachDefaultNode();e&&(this.nodes=[e],this.initNode(e))}else this.nodes=i,i.forEach(e=>{this.initAddedNode(e)})}attachDefaultNode(){const{host:i,slotName:e,tagName:t}=this;let n=this.defaultNode;return!n&&t&&(n=document.createElement(t),n instanceof Element&&(e!==""&&n.setAttribute("slot",e),this.defaultNode=n)),n&&(this.node=n,i.appendChild(n)),n}getSlotChildren(){const{slotName:i}=this;return Array.from(this.host.childNodes).filter(e=>e.nodeType===Node.ELEMENT_NODE&&e.hasAttribute("data-slot-ignore")?!1:e.nodeType===Node.ELEMENT_NODE&&e.slot===i||e.nodeType===Node.TEXT_NODE&&e.textContent.trim()&&i==="")}getSlotChild(){return this.getSlotChildren()[0]}initNode(i){const{slotInitializer:e}=this;e&&e(i,this.host)}initCustomNode(i){}teardownNode(i){}initAddedNode(i){i!==this.defaultNode&&(this.initCustomNode(i),this.initNode(i))}observeSlot(){const{slotName:i}=this,e=i===""?"slot:not([name])":`slot[name=${i}]`,t=this.host.shadowRoot.querySelector(e);this.__slotObserver=new ce(t,({addedNodes:n,removedNodes:r})=>{const o=this.multiple?this.nodes:[this.node],a=n.filter(l=>!xn(l)&&!o.includes(l)&&!(l.nodeType===Node.ELEMENT_NODE&&l.hasAttribute("data-slot-ignore")));r.length&&(this.nodes=o.filter(l=>!r.includes(l)),r.forEach(l=>{this.teardownNode(l)})),a&&a.length>0&&(this.multiple?(this.defaultNode&&this.defaultNode.remove(),this.nodes=[...o,...a].filter(l=>l!==this.defaultNode),a.forEach(l=>{this.initAddedNode(l)})):(this.node&&this.node.remove(),this.node=a[0],this.initAddedNode(this.node)))})}}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class X extends G{constructor(i){super(i,"tooltip"),this.setTarget(i),this.__onContentChange=this.__onContentChange.bind(this)}initCustomNode(i){i.target=this.target,this.ariaTarget!==void 0&&(i.ariaTarget=this.ariaTarget),this.context!==void 0&&(i.context=this.context),this.manual!==void 0&&(i.manual=this.manual),this.opened!==void 0&&(i.opened=this.opened),this.position!==void 0&&(i._position=this.position),this.shouldShow!==void 0&&(i.shouldShow=this.shouldShow),this.manual||this.host.setAttribute("has-tooltip",""),this.__notifyChange(i),i.addEventListener("content-changed",this.__onContentChange)}teardownNode(i){this.manual||this.host.removeAttribute("has-tooltip"),i.removeEventListener("content-changed",this.__onContentChange),this.__notifyChange(null)}setAriaTarget(i){this.ariaTarget=i;const e=this.node;e&&(e.ariaTarget=i)}setContext(i){this.context=i;const e=this.node;e&&(e.context=i)}setManual(i){this.manual=i;const e=this.node;e&&(e.manual=i)}setOpened(i){this.opened=i;const e=this.node;e&&(e.opened=i)}setPosition(i){this.position=i;const e=this.node;e&&(e._position=i)}setShouldShow(i){this.shouldShow=i;const e=this.node;e&&(e.shouldShow=i)}setTarget(i){this.target=i;const e=this.node;e&&(e.target=i)}__onContentChange(i){this.__notifyChange(i.target)}__notifyChange(i){this.dispatchEvent(new CustomEvent("tooltip-changed",{detail:{node:i}}))}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const xa=C`
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
 */const vt=C`
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
 */const ke=[vt,xa];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Te extends G{constructor(i,e,t={}){const{uniqueIdPrefix:n}=t;super(i,"input","input",{initializer:(r,o)=>{o.value&&(r.value=o.value),o.type&&r.setAttribute("type",o.type),r.id=this.defaultId,typeof e=="function"&&e(r)},useUniqueId:!0,uniqueIdPrefix:n})}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const oe=J(s=>class extends s{get _keyboardActive(){return Q()}ready(){this.addEventListener("focusin",e=>{this._shouldSetFocus(e)&&this._setFocused(!0)}),this.addEventListener("focusout",e=>{this._shouldRemoveFocus(e)&&this._setFocused(!1)}),super.ready()}disconnectedCallback(){super.disconnectedCallback(),this.hasAttribute("focused")&&this._setFocused(!1)}focus(e){super.focus(e),e&&e.focusVisible===!1||this.setAttribute("focus-ring","")}_setFocused(e){this.toggleAttribute("focused",e),this.toggleAttribute("focus-ring",e&&this._keyboardActive)}_shouldSetFocus(e){return!0}_shouldRemoveFocus(e){return!0}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ae=J(s=>class extends s{static get properties(){return{disabled:{type:Boolean,value:!1,observer:"_disabledChanged",reflectToAttribute:!0,sync:!0}}}_disabledChanged(e){this._setAriaDisabled(e)}_setAriaDisabled(e){e?this.setAttribute("aria-disabled","true"):this.removeAttribute("aria-disabled")}click(){this.disabled||super.click()}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Wi=s=>class extends Ae(s){static get properties(){return{tabindex:{type:Number,reflectToAttribute:!0,observer:"_tabindexChanged",sync:!0},_lastTabIndex:{type:Number}}}_disabledChanged(e,t){super._disabledChanged(e,t),!this.__shouldAllowFocusWhenDisabled()&&(e?(this.tabindex!==void 0&&(this._lastTabIndex=this.tabindex),this.setAttribute("tabindex","-1")):t&&(this._lastTabIndex!==void 0?this.setAttribute("tabindex",this._lastTabIndex):this.tabindex=void 0))}_tabindexChanged(e){this.__shouldAllowFocusWhenDisabled()||this.disabled&&e!==-1&&(this._lastTabIndex=e,this.setAttribute("tabindex","-1"))}focus(e){(!this.disabled||this.__shouldAllowFocusWhenDisabled())&&super.focus(e)}__shouldAllowFocusWhenDisabled(){return!1}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const bt=J(s=>class extends oe(Wi(s)){static get properties(){return{autofocus:{type:Boolean},focusElement:{type:Object,readOnly:!0,observer:"_focusElementChanged",sync:!0},_lastTabIndex:{value:0}}}constructor(){super(),this._boundOnBlur=this._onBlur.bind(this),this._boundOnFocus=this._onFocus.bind(this)}ready(){super.ready(),this.autofocus&&!this.disabled&&requestAnimationFrame(()=>{this.focus()})}focus(e){this.focusElement&&!this.disabled&&(this.focusElement.focus(),e&&e.focusVisible===!1||this.setAttribute("focus-ring",""))}blur(){this.focusElement&&this.focusElement.blur()}click(){this.focusElement&&!this.disabled&&this.focusElement.click()}_focusElementChanged(e,t){e?(e.disabled=this.disabled,this._addFocusListeners(e),this.__forwardTabIndex(this.tabindex)):t&&this._removeFocusListeners(t)}_addFocusListeners(e){e.addEventListener("blur",this._boundOnBlur),e.addEventListener("focus",this._boundOnFocus)}_removeFocusListeners(e){e.removeEventListener("blur",this._boundOnBlur),e.removeEventListener("focus",this._boundOnFocus)}_onFocus(e){e.stopPropagation(),this.dispatchEvent(new Event("focus"))}_onBlur(e){e.stopPropagation(),this.dispatchEvent(new Event("blur"))}_shouldSetFocus(e){return e.target===this.focusElement}_shouldRemoveFocus(e){return e.target===this.focusElement}_disabledChanged(e,t){super._disabledChanged(e,t),this.focusElement&&(this.focusElement.disabled=e),e&&this.blur()}_tabindexChanged(e){this.__forwardTabIndex(e)}__forwardTabIndex(e){e!==void 0&&this.focusElement&&(this.focusElement.tabIndex=e,e!==-1&&(this.tabindex=void 0)),this.disabled&&e&&(e!==-1&&(this._lastTabIndex=e),this.tabindex=void 0),e===void 0&&this.hasAttribute("tabindex")&&this.removeAttribute("tabindex")}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const De=J(s=>class extends s{ready(){super.ready(),this.addEventListener("keydown",e=>{this._onKeyDown(e)}),this.addEventListener("keyup",e=>{this._onKeyUp(e)})}_onKeyDown(e){switch(e.key){case"Enter":this._onEnter(e);break;case"Escape":this._onEscape(e);break}}_onKeyUp(e){}_onEnter(e){}_onEscape(e){}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const yt=J(s=>class extends s{static get properties(){return{inputElement:{type:Object,readOnly:!0,observer:"_inputElementChanged",sync:!0},type:{type:String,readOnly:!0},value:{type:String,value:"",observer:"_valueChanged",notify:!0,sync:!0}}}constructor(){super(),this._boundOnInput=this._onInput.bind(this),this._boundOnChange=this._onChange.bind(this)}get _hasValue(){return this.value!=null&&this.value!==""}get _inputElementValueProperty(){return"value"}get _inputElementValue(){return this.inputElement?this.inputElement[this._inputElementValueProperty]:void 0}set _inputElementValue(e){this.inputElement&&(this.inputElement[this._inputElementValueProperty]=e)}clear(){this.value="",this._inputElementValue=""}_addInputListeners(e){e.addEventListener("input",this._boundOnInput),e.addEventListener("change",this._boundOnChange)}_removeInputListeners(e){e.removeEventListener("input",this._boundOnInput),e.removeEventListener("change",this._boundOnChange)}_forwardInputValue(e){this.inputElement&&(this._inputElementValue=e??"")}_inputElementChanged(e,t){e?this._addInputListeners(e):t&&this._removeInputListeners(t)}_onInput(e){const t=e.composedPath()[0];this.__userInput=e.isTrusted,this.value=t.value,this.__userInput=!1}_onChange(e){}_toggleHasValue(e){this.toggleAttribute("has-value",e)}_valueChanged(e,t){this._toggleHasValue(this._hasValue),!(e===""&&t===void 0)&&(this.__userInput||this._forwardInputValue(e))}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ea=s=>class extends yt(De(s)){static get properties(){return{clearButtonVisible:{type:Boolean,reflectToAttribute:!0,value:!1}}}get clearElement(){return console.warn(`Please implement the 'clearElement' property in <${this.localName}>`),null}ready(){super.ready(),this.clearElement&&(this.clearElement.addEventListener("mousedown",e=>this._onClearButtonMouseDown(e)),this.clearElement.addEventListener("click",e=>this._onClearButtonClick(e)))}_onClearButtonClick(e){e.preventDefault(),this._onClearAction()}_onClearButtonMouseDown(e){this._shouldKeepFocusOnClearMousedown()&&e.preventDefault(),Ne||this.inputElement.focus()}_onEscape(e){super._onEscape(e),this.clearButtonVisible&&this.value&&!this.readonly&&(e.stopPropagation(),this._onClearAction())}_onClearAction(){this._inputElementValue="",this.inputElement.dispatchEvent(new Event("input",{bubbles:!0,composed:!0})),this.inputElement.dispatchEvent(new Event("change",{bubbles:!0}))}_shouldKeepFocusOnClearMousedown(){return Je(this.inputElement)}};/**
 * @license
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ci=new Map;function qi(s){return ci.has(s)||ci.set(s,new WeakMap),ci.get(s)}function In(s,i){s&&s.removeAttribute(i)}function Sn(s,i){if(!s||!i)return;const e=qi(i);if(e.has(s))return;const t=Vi(s.getAttribute(i));e.set(s,new Set(t))}function Ia(s,i){if(!s||!i)return;const e=qi(i),t=e.get(s);!t||t.size===0?s.removeAttribute(i):Gt(s,i,jt(t)),e.delete(s)}function Mt(s,i,e={newId:null,oldId:null,fromUser:!1}){if(!s||!i)return;const{newId:t,oldId:n,fromUser:r}=e,o=qi(i),a=o.get(s);if(!r&&a){n&&a.delete(n),t&&a.add(t);return}r&&(a?t||o.delete(s):Sn(s,i),In(s,i)),Hi(s,i,n);const l=t||jt(a);l&&Gt(s,i,l)}function Sa(s,i){Sn(s,i),In(s,i)}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ka{constructor(i){this.host=i,this.__required=!1}setTarget(i){this.__target=i,this.__setAriaRequiredAttribute(this.__required),this.__setLabelIdToAriaAttribute(this.__labelId,this.__labelId),this.__labelIdFromUser!=null&&this.__setLabelIdToAriaAttribute(this.__labelIdFromUser,this.__labelIdFromUser,!0),this.__setErrorIdToAriaAttribute(this.__errorId),this.__setHelperIdToAriaAttribute(this.__helperId),this.setAriaLabel(this.__label)}setRequired(i){this.__setAriaRequiredAttribute(i),this.__required=i}setAriaLabel(i){this.__setAriaLabelToAttribute(i),this.__label=i}setLabelId(i,e=!1){const t=e?this.__labelIdFromUser:this.__labelId;this.__setLabelIdToAriaAttribute(i,t,e),e?this.__labelIdFromUser=i:this.__labelId=i}setErrorId(i){this.__setErrorIdToAriaAttribute(i,this.__errorId),this.__errorId=i}setHelperId(i){this.__setHelperIdToAriaAttribute(i,this.__helperId),this.__helperId=i}__setAriaLabelToAttribute(i){this.__target&&(i?(Sa(this.__target,"aria-labelledby"),this.__target.setAttribute("aria-label",i)):this.__label&&(Ia(this.__target,"aria-labelledby"),this.__target.removeAttribute("aria-label")))}__setLabelIdToAriaAttribute(i,e,t){Mt(this.__target,"aria-labelledby",{newId:i,oldId:e,fromUser:t})}__setErrorIdToAriaAttribute(i,e){Mt(this.__target,"aria-describedby",{newId:i,oldId:e,fromUser:!1})}__setHelperIdToAriaAttribute(i,e){Mt(this.__target,"aria-describedby",{newId:i,oldId:e,fromUser:!1})}__setAriaRequiredAttribute(i){this.__target&&(["input","textarea"].includes(this.__target.localName)||(i?this.__target.setAttribute("aria-required","true"):this.__target.removeAttribute("aria-required")))}}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ie=document.createElement("div");ie.style.position="fixed";ie.style.clip="rect(0px, 0px, 0px, 0px)";ie.setAttribute("aria-live","polite");document.body.appendChild(ie);let It;function Rt(s,i={}){const e=i.mode||"polite",t=i.timeout===void 0?150:i.timeout;e==="alert"?(ie.removeAttribute("aria-live"),ie.removeAttribute("role"),It=D.debounce(It,ue,()=>{ie.setAttribute("role","alert")})):(It&&It.cancel(),ie.removeAttribute("role"),ie.setAttribute("aria-live",e)),ie.textContent="",setTimeout(()=>{ie.textContent=s},t)}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ui extends G{constructor(i,e,t,n={}){super(i,e,t,{...n,useUniqueId:!0})}initCustomNode(i){this.__updateNodeId(i),this.__notifyChange(i)}teardownNode(i){const e=this.getSlotChild();e&&e!==this.defaultNode?this.__notifyChange(e):(this.restoreDefaultNode(),this.updateDefaultNode(this.node))}attachDefaultNode(){const i=super.attachDefaultNode();return i&&this.__updateNodeId(i),i}restoreDefaultNode(){}updateDefaultNode(i){this.__notifyChange(i)}observeNode(i){this.__nodeObserver&&this.__nodeObserver.disconnect(),this.__nodeObserver=new MutationObserver(e=>{e.forEach(t=>{const n=t.target,r=n===this.node;t.type==="attributes"?r&&this.__updateNodeId(n):(r||n.parentElement===this.node)&&this.__notifyChange(this.node)})}),this.__nodeObserver.observe(i,{attributes:!0,attributeFilter:["id"],childList:!0,subtree:!0,characterData:!0})}__hasContent(i){return i?i.nodeType===Node.ELEMENT_NODE&&(customElements.get(i.localName)||i.children.length>0)||i.textContent&&i.textContent.trim()!=="":!1}__notifyChange(i){this.dispatchEvent(new CustomEvent("slot-content-changed",{detail:{hasContent:this.__hasContent(i),node:i}}))}__updateNodeId(i){const e=!this.nodes||i===this.nodes[0];i.nodeType===Node.ELEMENT_NODE&&(!this.multiple||e)&&!i.id&&(i.id=this.defaultId)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ta extends Ui{constructor(i){super(i,"error-message","div")}setErrorMessage(i){this.errorMessage=i,this.updateDefaultNode(this.node)}setInvalid(i){this.invalid=i,this.updateDefaultNode(this.node)}initAddedNode(i){i!==this.defaultNode&&this.initCustomNode(i)}initNode(i){this.updateDefaultNode(i)}initCustomNode(i){i.textContent&&!this.errorMessage&&(this.errorMessage=i.textContent.trim()),super.initCustomNode(i)}restoreDefaultNode(){this.attachDefaultNode()}updateDefaultNode(i){const{errorMessage:e,invalid:t}=this,n=!!(t&&e&&e.trim()!=="");i&&(i.textContent=n?e:"",i.hidden=!n,n&&Rt(e,{mode:"assertive"})),super.updateDefaultNode(i)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Aa extends Ui{constructor(i){super(i,"helper",null)}setHelperText(i){this.helperText=i,this.getSlotChild()||this.restoreDefaultNode(),this.node===this.defaultNode&&this.updateDefaultNode(this.node)}restoreDefaultNode(){const{helperText:i}=this;if(i&&i.trim()!==""){this.tagName="div";const e=this.attachDefaultNode();this.observeNode(e)}}updateDefaultNode(i){i&&(i.textContent=this.helperText),super.updateDefaultNode(i)}initCustomNode(i){super.initCustomNode(i),this.observeNode(i)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class kn extends Ui{constructor(i){super(i,"label","label")}setLabel(i){this.label=i,this.getSlotChild()||this.restoreDefaultNode(),this.node===this.defaultNode&&this.updateDefaultNode(this.node)}restoreDefaultNode(){const{label:i}=this;if(i&&i.trim()!==""){const e=this.attachDefaultNode();this.observeNode(e)}}updateDefaultNode(i){i&&(i.textContent=this.label),super.updateDefaultNode(i)}initCustomNode(i){super.initCustomNode(i),this.observeNode(i)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Tn=J(s=>class extends s{static get properties(){return{label:{type:String,observer:"_labelChanged"}}}constructor(){super(),this._labelController=new kn(this),this._labelController.addEventListener("slot-content-changed",e=>{this.toggleAttribute("has-label",e.detail.hasContent)})}get _labelId(){const e=this._labelNode;return e&&e.id}get _labelNode(){return this._labelController.node}ready(){super.ready(),this.addController(this._labelController)}_labelChanged(e){this._labelController.setLabel(e)}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Yi=J(s=>class extends s{static get properties(){return{invalid:{type:Boolean,reflectToAttribute:!0,notify:!0,value:!1,sync:!0},manualValidation:{type:Boolean,value:!1},required:{type:Boolean,reflectToAttribute:!0,sync:!0}}}validate(){const e=this.checkValidity();return this._setInvalid(!e),this.dispatchEvent(new CustomEvent("validated",{detail:{valid:e}})),e}checkValidity(){return!this.required||!!this.value}_setInvalid(e){this._shouldSetInvalid(e)&&(this.invalid=e)}_shouldSetInvalid(e){return!0}_requestValidation(){this.manualValidation||this.validate()}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const wt=s=>class extends Yi(Tn(s)){static get properties(){return{ariaTarget:{type:Object,observer:"_ariaTargetChanged"},errorMessage:{type:String,observer:"_errorMessageChanged"},helperText:{type:String,observer:"_helperTextChanged"},accessibleName:{type:String,observer:"_accessibleNameChanged"},accessibleNameRef:{type:String,observer:"_accessibleNameRefChanged"}}}static get observers(){return["_invalidChanged(invalid)","_requiredChanged(required)"]}constructor(){super(),this._fieldAriaController=new ka(this),this._helperController=new Aa(this),this._errorController=new Ta(this),this._errorController.addEventListener("slot-content-changed",e=>{this.toggleAttribute("has-error-message",e.detail.hasContent)}),this._labelController.addEventListener("slot-content-changed",e=>{const{hasContent:t,node:n}=e.detail;this.__labelChanged(t,n)}),this._helperController.addEventListener("slot-content-changed",e=>{const{hasContent:t,node:n}=e.detail;this.toggleAttribute("has-helper",t),this.__helperChanged(t,n)})}get _errorNode(){return this._errorController.node}get _helperNode(){return this._helperController.node}ready(){super.ready(),this.addController(this._fieldAriaController),this.addController(this._helperController),this.addController(this._errorController)}__helperChanged(e,t){e?this._fieldAriaController.setHelperId(t.id):this._fieldAriaController.setHelperId(null)}_accessibleNameChanged(e){this._fieldAriaController.setAriaLabel(e)}_accessibleNameRefChanged(e){this._fieldAriaController.setLabelId(e,!0)}__labelChanged(e,t){e?this._fieldAriaController.setLabelId(t.id):this._fieldAriaController.setLabelId(null)}_errorMessageChanged(e){this._errorController.setErrorMessage(e)}_helperTextChanged(e){this._helperController.setHelperText(e)}_ariaTargetChanged(e){e&&this._fieldAriaController.setTarget(e)}_requiredChanged(e){this._fieldAriaController.setRequired(e)}_invalidChanged(e){this._errorController.setInvalid(e),setTimeout(()=>{if(e){const t=this._errorNode;this._fieldAriaController.setErrorId(t&&t.id)}else this._fieldAriaController.setErrorId(null)})}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Kt=J(s=>class extends s{static get properties(){return{stateTarget:{type:Object,observer:"_stateTargetChanged"}}}static get delegateAttrs(){return[]}static get delegateProps(){return[]}ready(){super.ready(),this._createDelegateAttrsObserver(),this._createDelegatePropsObserver()}_stateTargetChanged(e){e&&(this._ensureAttrsDelegated(),this._ensurePropsDelegated())}_createDelegateAttrsObserver(){this._createMethodObserver(`_delegateAttrsChanged(${this.constructor.delegateAttrs.join(", ")})`)}_createDelegatePropsObserver(){this._createMethodObserver(`_delegatePropsChanged(${this.constructor.delegateProps.join(", ")})`)}_ensureAttrsDelegated(){this.constructor.delegateAttrs.forEach(e=>{this._delegateAttribute(e,this[e])})}_ensurePropsDelegated(){this.constructor.delegateProps.forEach(e=>{this._delegateProperty(e,this[e])})}_delegateAttrsChanged(...e){this.constructor.delegateAttrs.forEach((t,n)=>{this._delegateAttribute(t,e[n])})}_delegatePropsChanged(...e){this.constructor.delegateProps.forEach((t,n)=>{this._delegateProperty(t,e[n])})}_delegateAttribute(e,t){this.stateTarget&&(e==="invalid"&&this._delegateAttribute("aria-invalid",t?"true":!1),typeof t=="boolean"?this.stateTarget.toggleAttribute(e,t):t?this.stateTarget.setAttribute(e,t):this.stateTarget.removeAttribute(e))}_delegateProperty(e,t){this.stateTarget&&(this.stateTarget[e]=t)}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ji=J(s=>class extends Kt(Yi(yt(s))){static get constraints(){return["required"]}static get delegateAttrs(){return[...super.delegateAttrs,"required"]}ready(){super.ready(),this._createConstraintsObserver()}checkValidity(){return this.inputElement&&this._hasValidConstraints(this.constructor.constraints.map(e=>this[e]))?this.inputElement.checkValidity():!this.invalid}_hasValidConstraints(e){return e.some(t=>this.__isValidConstraint(t))}_createConstraintsObserver(){this._createMethodObserver(`_constraintsChanged(stateTarget, ${this.constructor.constraints.join(", ")})`)}_constraintsChanged(e,...t){if(!e)return;const n=this._hasValidConstraints(t),r=this.__previousHasConstraints&&!n;(this._hasValue||this.invalid)&&n?this._requestValidation():r&&!this.manualValidation&&this._setInvalid(!1),this.__previousHasConstraints=n}_onChange(e){e.stopPropagation(),this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{detail:{sourceEvent:e},bubbles:e.bubbles,cancelable:e.cancelable}))}__isValidConstraint(e){return!!e||e===0}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ct=s=>class extends gt(bt(ji(wt(Ea(De(s)))))){static get properties(){return{allowedCharPattern:{type:String,observer:"_allowedCharPatternChanged"},autoselect:{type:Boolean,value:!1},name:{type:String,reflectToAttribute:!0},placeholder:{type:String,reflectToAttribute:!0},readonly:{type:Boolean,value:!1,reflectToAttribute:!0},title:{type:String,reflectToAttribute:!0}}}static get delegateAttrs(){return[...super.delegateAttrs,"name","type","placeholder","readonly","invalid","title"]}constructor(){super(),this._boundOnPaste=this._onPaste.bind(this),this._boundOnDrop=this._onDrop.bind(this),this._boundOnBeforeInput=this._onBeforeInput.bind(this)}get slotStyles(){const e=this.localName;return[`
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
        `]}_onFocus(e){super._onFocus(e),this.autoselect&&this.inputElement&&this.inputElement.select()}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("paste",this._boundOnPaste),e.addEventListener("drop",this._boundOnDrop),e.addEventListener("beforeinput",this._boundOnBeforeInput)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("paste",this._boundOnPaste),e.removeEventListener("drop",this._boundOnDrop),e.removeEventListener("beforeinput",this._boundOnBeforeInput)}_onKeyDown(e){super._onKeyDown(e),this.allowedCharPattern&&!this.__shouldAcceptKey(e)&&e.target===this.inputElement&&(e.preventDefault(),this._markInputPrevented())}_markInputPrevented(){this.setAttribute("input-prevented",""),this._preventInputDebouncer=D.debounce(this._preventInputDebouncer,K.after(200),()=>{this.removeAttribute("input-prevented")})}__shouldAcceptKey(e){return e.metaKey||e.ctrlKey||!e.key||e.key.length!==1||this.__allowedCharRegExp.test(e.key)}_onPaste(e){if(this.allowedCharPattern){const t=e.clipboardData.getData("text");this.__allowedTextRegExp.test(t)||(e.preventDefault(),this._markInputPrevented())}}_onDrop(e){if(this.allowedCharPattern){const t=e.dataTransfer.getData("text");this.__allowedTextRegExp.test(t)||(e.preventDefault(),this._markInputPrevented())}}_onBeforeInput(e){this.allowedCharPattern&&e.data&&!this.__allowedTextRegExp.test(e.data)&&(e.preventDefault(),this._markInputPrevented())}_allowedCharPatternChanged(e){if(e)try{this.__allowedCharRegExp=new RegExp(`^${e}$`,"u"),this.__allowedTextRegExp=new RegExp(`^${e}*$`,"u")}catch(t){console.error(t)}}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Gi=s=>class extends Ct(s){static get properties(){return{autocomplete:{type:String},autocorrect:{type:String,reflectToAttribute:!0},autocapitalize:{type:String,reflectToAttribute:!0}}}static get delegateAttrs(){return[...super.delegateAttrs,"autocapitalize","autocomplete","autocorrect"]}_inputElementChanged(e){super._inputElementChanged(e),e&&(e.value&&e.value!==this.value&&(console.warn(`Please define value on the <${this.localName}> component!`),e.value=""),this.value&&(e.value=this.value))}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}_onInput(e){super._onInput(e),this.invalid&&this._requestValidation()}_valueChanged(e,t){super._valueChanged(e,t),t!==void 0&&this.invalid&&this._requestValidation()}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ve{constructor(i,e){this.input=i,this.__preventDuplicateLabelClick=this.__preventDuplicateLabelClick.bind(this),e.addEventListener("slot-content-changed",t=>{this.__initLabel(t.detail.node)}),this.__initLabel(e.node)}__initLabel(i){i&&(i.addEventListener("click",this.__preventDuplicateLabelClick),this.input&&i.setAttribute("for",this.input.id))}__preventDuplicateLabelClick(){const i=e=>{e.stopImmediatePropagation(),this.input.removeEventListener("click",i)};this.input.addEventListener("click",i)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Da=s=>class extends Gi(s){static get properties(){return{maxlength:{type:Number},minlength:{type:Number},pattern:{type:String}}}static get delegateAttrs(){return[...super.delegateAttrs,"maxlength","minlength","pattern"]}static get constraints(){return[...super.constraints,"maxlength","minlength","pattern"]}constructor(){super(),this._setType("text")}get clearElement(){return this.$.clearButton}ready(){super.ready(),this.addController(new Te(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new ve(this.inputElement,this._labelController))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ki extends Da(T(L(I(A(E))))){static get is(){return"vaadin-text-field"}static get styles(){return[ke]}render(){return y`
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
          theme="${B(this._theme)}"
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
    `}ready(){super.ready(),this._tooltipController=new X(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}_renderSuffix(){return y`
      <slot name="suffix" slot="suffix"></slot>
      <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
    `}}w(Ki);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ui={start:"top",end:"bottom"},_i={start:"left",end:"right"},ks=new ResizeObserver(s=>{setTimeout(()=>{s.forEach(i=>{i.target.__overlay&&i.target.__overlay._updatePosition()})})}),xt=s=>class extends s{static get properties(){return{positionTarget:{type:Object,value:null,sync:!0},horizontalAlign:{type:String,value:"start",sync:!0},verticalAlign:{type:String,value:"top",sync:!0},noHorizontalOverlap:{type:Boolean,value:!1,sync:!0},noVerticalOverlap:{type:Boolean,value:!1,sync:!0},requiredVerticalSpace:{type:Number,value:0,sync:!0}}}constructor(){super(),this.__onScroll=this.__onScroll.bind(this),this._updatePosition=this._updatePosition.bind(this)}connectedCallback(){super.connectedCallback(),this.opened&&this.__addUpdatePositionEventListeners()}disconnectedCallback(){super.disconnectedCallback(),this.__removeUpdatePositionEventListeners()}updated(e){if(super.updated(e),e.has("positionTarget")){const n=e.get("positionTarget");(!this.positionTarget&&n||this.positionTarget&&!n&&this.__margins)&&this.__resetPosition()}(e.has("opened")||e.has("positionTarget"))&&this.__updatePositionSettings(this.opened,this.positionTarget),["horizontalAlign","verticalAlign","noHorizontalOverlap","noVerticalOverlap","requiredVerticalSpace"].some(n=>e.has(n))&&this._updatePosition()}__addUpdatePositionEventListeners(){window.visualViewport.addEventListener("resize",this._updatePosition),window.visualViewport.addEventListener("scroll",this.__onScroll,!0),this.__positionTargetAncestorRootNodes=ma(this.positionTarget),this.__positionTargetAncestorRootNodes.forEach(e=>{e.addEventListener("scroll",this.__onScroll,!0)}),this.positionTarget&&(this.__observePositionTargetMove=Bo(this.positionTarget,()=>{this._updatePosition()}))}__removeUpdatePositionEventListeners(){window.visualViewport.removeEventListener("resize",this._updatePosition),window.visualViewport.removeEventListener("scroll",this.__onScroll,!0),this.__positionTargetAncestorRootNodes&&(this.__positionTargetAncestorRootNodes.forEach(e=>{e.removeEventListener("scroll",this.__onScroll,!0)}),this.__positionTargetAncestorRootNodes=null),this.__observePositionTargetMove&&(this.__observePositionTargetMove(),this.__observePositionTargetMove=null)}__updatePositionSettings(e,t){if(this.__removeUpdatePositionEventListeners(),t&&(t.__overlay=null,ks.unobserve(t),e&&(this.__addUpdatePositionEventListeners(),t.__overlay=this,ks.observe(t))),e){const n=getComputedStyle(this);this.__margins||(this.__margins={},["top","bottom","left","right"].forEach(r=>{this.__margins[r]=parseInt(n[r],10)})),this._updatePosition(),requestAnimationFrame(()=>this._updatePosition())}}__onScroll(e){e.target instanceof Node&&this._deepContains(e.target)||this._updatePosition()}__resetPosition(){this.__margins=null,Object.assign(this.style,{justifyContent:"",alignItems:"",top:"",bottom:"",left:"",right:""}),U(this,"bottom-aligned",!1),U(this,"top-aligned",!1),U(this,"end-aligned",!1),U(this,"start-aligned",!1)}_updatePosition(){if(!this.positionTarget||!this.opened||!this.__margins)return;const e=this.positionTarget.getBoundingClientRect();if(e.width===0&&e.height===0&&this.opened){this.opened=!1;return}const t=this.__shouldAlignStartVertically(e);this.style.justifyContent=t?"flex-start":"flex-end";const n=this.__isRTL,r=this.__shouldAlignStartHorizontally(e,n),o=!n&&r||n&&!r;this.style.alignItems=o?"flex-start":"flex-end";const a=this.getBoundingClientRect(),l=this.__calculatePositionInOneDimension(e,a,this.noVerticalOverlap,ui,this,t),d=this.__calculatePositionInOneDimension(e,a,this.noHorizontalOverlap,_i,this,r);Object.assign(this.style,l,d),U(this,"bottom-aligned",!t),U(this,"top-aligned",t),U(this,"end-aligned",!o),U(this,"start-aligned",o)}__shouldAlignStartHorizontally(e,t){const n=Math.max(this.__oldContentWidth||0,this.$.overlay.offsetWidth);this.__oldContentWidth=this.$.overlay.offsetWidth;const r=Math.min(window.innerWidth,document.documentElement.clientWidth),o=!t&&this.horizontalAlign==="start"||t&&this.horizontalAlign==="end";return this.__shouldAlignStart(e,n,r,this.__margins,o,this.noHorizontalOverlap,_i)}__shouldAlignStartVertically(e){const t=this.requiredVerticalSpace||Math.max(this.__oldContentHeight||0,this.$.overlay.offsetHeight);this.__oldContentHeight=this.$.overlay.offsetHeight;const n=Math.min(window.innerHeight,document.documentElement.clientHeight),r=this.verticalAlign==="top";return this.__shouldAlignStart(e,t,n,this.__margins,r,this.noVerticalOverlap,ui)}__shouldAlignStart(e,t,n,r,o,a,l){const d=n-e[a?l.end:l.start]-r[l.end],h=e[a?l.start:l.end]-r[l.start],c=o?d:h,m=c>(o?h:d)||c>t;return o===m}__adjustBottomProperty(e,t,n){let r;if(e===t.end){if(t.end===ui.end){const o=Math.min(window.innerHeight,document.documentElement.clientHeight);if(n>o&&this.__oldViewportHeight){const a=this.__oldViewportHeight-o;r=n-a}this.__oldViewportHeight=o}if(t.end===_i.end){const o=Math.min(window.innerWidth,document.documentElement.clientWidth);if(n>o&&this.__oldViewportWidth){const a=this.__oldViewportWidth-o;r=n-a}this.__oldViewportWidth=o}}return r}__calculatePositionInOneDimension(e,t,n,r,o,a){const l=a?r.start:r.end,d=a?r.end:r.start,h=parseFloat(o.style[l]||getComputedStyle(o)[l]),c=this.__adjustBottomProperty(l,r,h),f=t[a?r.start:r.end]-e[n===a?r.end:r.start],m=c?`${c}px`:`${h+f*(a?-1:1)}px`;return{[l]:m,[d]:""}}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Oa=s=>class extends xt(ge(s)){static get properties(){return{position:{type:String,reflectToAttribute:!0}}}_updatePosition(){if(super._updatePosition(),!this.positionTarget||!this.opened)return;this.removeAttribute("arrow-centered");const e=this.positionTarget.getBoundingClientRect(),t=this.$.overlay.getBoundingClientRect(),n=Math.min(window.innerWidth,document.documentElement.clientWidth);let r=!1;if(t.left<0?(this.style.left="0px",this.style.right="",r=!0):t.right>n&&(this.style.right="0px",this.style.left="",r=!0),!r&&(this.position==="bottom"||this.position==="top")){const o=e.width/2-t.width/2;if(this.style.left){const a=t.left+o;a>0&&(this.style.left=`${a}px`,this.setAttribute("arrow-centered",""))}if(this.style.right){const a=parseFloat(this.style.right)+o;a>0&&(this.style.right=`${a}px`,this.setAttribute("arrow-centered",""))}}if(this.position==="start"||this.position==="end"){const o=e.height/2-t.height/2;this.style.top=`${t.top+o}px`}}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Pa=C`
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
 */class Ma extends Oa(z(T(I(A(E))))){static get is(){return"vaadin-tooltip-overlay"}static get styles(){return[me,Pa]}render(){return y`
      <div part="overlay" id="overlay">
        <div part="content" id="content"><slot></slot></div>
      </div>
    `}}w(Ma);/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ra=s=>class extends s{static get properties(){return{position:{type:String},_position:{type:String,value:"bottom"},__effectivePosition:{type:String,computed:"__computePosition(position, _position)"}}}__computeHorizontalAlign(e){return["top-end","bottom-end","start-top","start","start-bottom"].includes(e)?"end":"start"}__computeNoHorizontalOverlap(e){return["start-top","start","start-bottom","end-top","end","end-bottom"].includes(e)}__computeNoVerticalOverlap(e){return["top-start","top-end","top","bottom-start","bottom","bottom-end"].includes(e)}__computeVerticalAlign(e){return["top-start","top-end","top","start-bottom","end-bottom"].includes(e)?"bottom":"top"}__computePosition(e,t){return e||t}};/**
 * @license
 * Copyright (c) 2024 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const La=s=>class extends s{static get properties(){return{for:{type:String,observer:"__forChanged"},target:{type:Object},__isConnected:{type:Boolean,sync:!0}}}static get observers(){return["__targetOrConnectedChanged(target, __isConnected)"]}connectedCallback(){super.connectedCallback(),this.__isConnected=!0}disconnectedCallback(){super.disconnectedCallback(),this.__isConnected=!1}__forChanged(e){e&&(this.__setTargetByIdDebouncer=D.debounce(this.__setTargetByIdDebouncer,te,()=>this.__setTargetById(e)))}__setTargetById(e){if(!this.isConnected)return;const t=this.getRootNode().getElementById(e);t?this.target=t:console.warn(`No element with id="${e}" set via "for" property found on the page.`)}__targetOrConnectedChanged(e,t){this.__previousTarget&&(this.__previousTarget!==e||!t)&&this._removeTargetListeners(this.__previousTarget),e&&t&&this._addTargetListeners(e),this.__previousTarget=e}_addTargetListeners(e){}_removeTargetListeners(e){}},Xe=500;let An=Xe,Dn=Xe,On=Xe;const Be=new Set;let ot=!1,Ve=null,at=null;class Fa{constructor(i){this.host=i}get focusDelay(){const i=this.host;return i.focusDelay!=null&&i.focusDelay>=0?i.focusDelay:An}get hoverDelay(){const i=this.host;return i.hoverDelay!=null&&i.hoverDelay>=0?i.hoverDelay:Dn}get hideDelay(){const i=this.host;return i.hideDelay!=null&&i.hideDelay>=0?i.hideDelay:On}get isClosing(){return Be.has(this.host)}open(i={immediate:!1}){const{immediate:e,hover:t,focus:n}=i,r=t&&this.hoverDelay>0,o=n&&this.focusDelay>0;!e&&(r||o)&&!this.__closeTimeout?this.__warmupTooltip(o):this.__showTooltip()}close(i){!i&&this.hideDelay>0?this.__scheduleClose():(this.__abortClose(),this._setOpened(!1)),this.__abortWarmUp(),ot&&(this.__abortCooldown(),this.__scheduleCooldown())}_isOpened(){return this.host.opened}_setOpened(i){this.host.opened=i}__flushClosingTooltips(){Be.forEach(i=>{i._stateController.close(!0),Be.delete(i)})}__showTooltip(){this.__abortClose(),this.__flushClosingTooltips(),this._setOpened(!0),ot=!0,this.__abortWarmUp(),this.__abortCooldown()}__warmupTooltip(i){this._isOpened()||(ot?this.__showTooltip():Ve==null&&this.__scheduleWarmUp(i))}__abortClose(){this.__closeTimeout&&(clearTimeout(this.__closeTimeout),this.__closeTimeout=null),this.isClosing&&Be.delete(this.host)}__abortCooldown(){at&&(clearTimeout(at),at=null)}__abortWarmUp(){Ve&&(clearTimeout(Ve),Ve=null)}__scheduleClose(){this._isOpened()&&!this.isClosing&&(Be.add(this.host),this.__closeTimeout=setTimeout(()=>{Be.delete(this.host),this.__closeTimeout=null,this._setOpened(!1)},this.hideDelay))}__scheduleCooldown(){at=setTimeout(()=>{at=null,ot=!1},this.hideDelay)}__scheduleWarmUp(i){const e=i?this.focusDelay:this.hoverDelay;Ve=setTimeout(()=>{Ve=null,ot=!0,this.__showTooltip()},e)}}const $a=s=>class extends Ra(La(s)){static get properties(){return{ariaTarget:{type:Object},context:{type:Object,value:()=>({})},focusDelay:{type:Number},generator:{type:Object},hideDelay:{type:Number},hoverDelay:{type:Number},manual:{type:Boolean,value:!1,sync:!0},opened:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"__openedChanged",sync:!0},shouldShow:{type:Object,value:()=>(e,t)=>!0},text:{type:String},markdown:{type:Boolean,value:!1,reflectToAttribute:!0},_effectiveAriaTarget:{type:Object,computed:"__computeAriaTarget(ariaTarget, target)",observer:"__effectiveAriaTargetChanged"},__isTargetHidden:{type:Boolean,value:!1},_isConnected:{type:Boolean,sync:!0}}}static setDefaultFocusDelay(e){An=e!=null&&e>=0?e:Xe}static setDefaultHideDelay(e){On=e!=null&&e>=0?e:Xe}static setDefaultHoverDelay(e){Dn=e!=null&&e>=0?e:Xe}constructor(){super(),this._uniqueId=`vaadin-tooltip-${Se()}`,this.__onFocusin=this.__onFocusin.bind(this),this.__onFocusout=this.__onFocusout.bind(this),this.__onMouseDown=this.__onMouseDown.bind(this),this.__onMouseEnter=this.__onMouseEnter.bind(this),this.__onMouseLeave=this.__onMouseLeave.bind(this),this.__onKeyDown=this.__onKeyDown.bind(this),this.__onOverlayOpen=this.__onOverlayOpen.bind(this),this.__targetVisibilityObserver=new IntersectionObserver(e=>{e.forEach(t=>this.__onTargetVisibilityChange(t.isIntersecting))},{threshold:0}),this._stateController=new Fa(this)}connectedCallback(){super.connectedCallback(),this._isConnected=!0,document.body.addEventListener("vaadin-overlay-open",this.__onOverlayOpen)}disconnectedCallback(){super.disconnectedCallback(),this.opened&&!this.manual&&this._stateController.close(!0),this._isConnected=!1,document.body.removeEventListener("vaadin-overlay-open",this.__onOverlayOpen)}ready(){super.ready(),this._overlayElement=this.$.overlay,this.__contentController=new G(this,"overlay","div",{initializer:e=>{e.id=this._uniqueId,e.setAttribute("role","tooltip"),this.__contentNode=e}}),this.addController(this.__contentController)}updated(e){super.updated(e),(e.has("text")||e.has("generator")||e.has("context")||e.has("markdown"))&&this.__updateContent()}__openedChanged(e,t){e?document.addEventListener("keydown",this.__onKeyDown,!0):t&&document.removeEventListener("keydown",this.__onKeyDown,!0)}_addTargetListeners(e){e.addEventListener("mouseenter",this.__onMouseEnter),e.addEventListener("mouseleave",this.__onMouseLeave),e.addEventListener("focusin",this.__onFocusin),e.addEventListener("focusout",this.__onFocusout),e.addEventListener("mousedown",this.__onMouseDown),requestAnimationFrame(()=>{this.__targetVisibilityObserver.observe(e)})}_removeTargetListeners(e){e.removeEventListener("mouseenter",this.__onMouseEnter),e.removeEventListener("mouseleave",this.__onMouseLeave),e.removeEventListener("focusin",this.__onFocusin),e.removeEventListener("focusout",this.__onFocusout),e.removeEventListener("mousedown",this.__onMouseDown),this.__targetVisibilityObserver.unobserve(e)}__onFocusin(e){this.manual||Q()&&(this.target.contains(e.relatedTarget)||this.__isShouldShow()&&(this._overlayElement.hasAttribute("hidden")||(this.__focusInside=!0,!this.__isTargetHidden&&(!this.__hoverInside||!this.opened)&&this._stateController.open({focus:!0}))))}__onFocusout(e){this.manual||this.target.contains(e.relatedTarget)||(this.__focusInside=!1,this.__hoverInside||this._stateController.close(!0))}__onKeyDown(e){this.manual||e.key==="Escape"&&(e.stopPropagation(),this._stateController.close(!0))}__onMouseDown(){this.manual||this._stateController.close(!0)}__onMouseEnter(){this.manual||this.__isShouldShow()&&(this._overlayElement.hasAttribute("hidden")||this.__hoverInside||(this.__hoverInside=!0,!this.__isTargetHidden&&(!this.__focusInside||!this.opened)&&this._stateController.open({hover:!0})))}__onMouseLeave(e){e.relatedTarget!==this._overlayElement&&this.__handleMouseLeave()}__onOverlayMouseEnter(){this.manual||this._stateController.isClosing&&this._stateController.open({immediate:!0})}__onOverlayMouseLeave(e){e.relatedTarget!==this.target&&this.__handleMouseLeave()}__onOverlayMouseDown(e){e.stopPropagation()}__onOverlayClick(e){e.stopPropagation()}__handleMouseLeave(){this.manual||(this.__hoverInside=!1,this.__focusInside||this._stateController.close())}__onOverlayOpen(){this.manual||this._overlayElement.opened&&!this._overlayElement._last&&this._stateController.close(!0)}__onTargetVisibilityChange(e){if(this.manual)return;const t=this.__isTargetHidden;if(this.__isTargetHidden=!e,t&&e&&(this.__focusInside||this.__hoverInside)){this._stateController.open({immediate:!0});return}!e&&this.opened&&this._stateController.close(!0)}__isShouldShow(){return!(typeof this.shouldShow=="function"&&this.shouldShow(this.target,this.context)!==!0)}async __updateContent(){const e=typeof this.generator=="function"?this.generator(this.context):this.text;this.markdown&&e?(await this.constructor.__importMarkdownHelpers()).renderMarkdownToElement(this.__contentNode,e):this.__contentNode.textContent=e||"",this.$.overlay.toggleAttribute("hidden",this.__contentNode.textContent.trim()===""),this.dispatchEvent(new CustomEvent("content-changed",{detail:{content:this.__contentNode.textContent}}))}__computeAriaTarget(e,t){const n=o=>o&&o.nodeType===Node.ELEMENT_NODE,r=Array.isArray(e)?e.some(n):e;return e===null||r?e:t}__effectiveAriaTargetChanged(e,t){t&&[t].flat().forEach(n=>{Hi(n,"aria-describedby",this._uniqueId)}),e&&[e].flat().forEach(n=>{Gt(n,"aria-describedby",this._uniqueId)})}static __importMarkdownHelpers(){return this.__markdownHelpers||(this.__markdownHelpers=Hr(()=>import("./markdown-helpers-RM02npbm.js"),[],import.meta.url)),this.__markdownHelpers}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class za extends $a(st(L(I(E)))){static get is(){return"vaadin-tooltip"}static get styles(){return C`
      :host {
        display: contents;
      }
    `}render(){const i=this.__effectivePosition;return y`
      <vaadin-tooltip-overlay
        id="overlay"
        .owner="${this}"
        theme="${B(this._theme)}"
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
    `}}w(za);/**
@license
Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/const Na=s=>s,Pn=typeof document.head.style.touchAction=="string",Nt="__polymerGestures",pi="__polymerGesturesHandled",Ti="__polymerGesturesTouchAction",Ts=25,As=5,Ba=2,Va=["mousedown","mousemove","mouseup","click"],Ha=[0,1,4,2],Wa=(function(){try{return new MouseEvent("test",{buttons:1}).buttons===1}catch{return!1}})();function Xi(s){return Va.indexOf(s)>-1}let qa=!1;(function(){try{const s=Object.defineProperty({},"passive",{get(){qa=!0}});window.addEventListener("test",null,s),window.removeEventListener("test",null,s)}catch{}})();function Mn(s){Xi(s)}const Ua=navigator.userAgent.match(/iP(?:[oa]d|hone)|Android/u),Ya={button:!0,command:!0,fieldset:!0,input:!0,keygen:!0,optgroup:!0,option:!0,select:!0,textarea:!0};function $e(s){const i=s.type;if(!Xi(i))return!1;if(i==="mousemove"){let t=s.buttons===void 0?1:s.buttons;return s instanceof window.MouseEvent&&!Wa&&(t=Ha[s.which]||0),!!(t&1)}return(s.button===void 0?0:s.button)===0}function ja(s){if(s.type==="click"){if(s.detail===0)return!0;const i=Ce(s);if(!i.nodeType||i.nodeType!==Node.ELEMENT_NODE)return!0;const e=i.getBoundingClientRect(),t=s.pageX,n=s.pageY;return!(t>=e.left&&t<=e.right&&n>=e.top&&n<=e.bottom)}return!1}const he={touch:{x:0,y:0,id:-1,scrollDecided:!1}};function Ga(s){let i="auto";const e=Ln(s);for(let t=0,n;t<e.length;t++)if(n=e[t],n[Ti]){i=n[Ti];break}return i}function Rn(s,i,e){s.movefn=i,s.upfn=e,document.addEventListener("mousemove",i),document.addEventListener("mouseup",e)}function Qe(s){document.removeEventListener("mousemove",s.movefn),document.removeEventListener("mouseup",s.upfn),s.movefn=null,s.upfn=null}const Ln=window.ShadyDOM&&window.ShadyDOM.noPatch?window.ShadyDOM.composedPath:s=>s.composedPath&&s.composedPath()||[],_e={},Le=[];function Fn(s,i){let e=document.elementFromPoint(s,i),t=e;for(;t&&t.shadowRoot&&!window.ShadyDOM;){const n=t;if(t=t.shadowRoot.elementFromPoint(s,i),n===t)break;t&&(e=t)}return e}function Ce(s){const i=Ln(s);return i.length>0?i[0]:s.target}function $n(s){const i=s.type,t=s.currentTarget[Nt];if(!t)return;const n=t[i];if(!n)return;if(!s[pi]&&(s[pi]={},i.startsWith("touch"))){const o=s.changedTouches[0];if(i==="touchstart"&&s.touches.length===1&&(he.touch.id=o.identifier),he.touch.id!==o.identifier)return;Pn||(i==="touchstart"||i==="touchmove")&&Ka(s)}const r=s[pi];if(!r.skip){for(let o=0,a;o<Le.length;o++)a=Le[o],n[a.name]&&!r[a.name]&&a.flow&&a.flow.start.indexOf(s.type)>-1&&a.reset&&a.reset();for(let o=0,a;o<Le.length;o++)a=Le[o],n[a.name]&&!r[a.name]&&(r[a.name]=!0,a[i](s))}}function Ka(s){const i=s.changedTouches[0],e=s.type;if(e==="touchstart")he.touch.x=i.clientX,he.touch.y=i.clientY,he.touch.scrollDecided=!1;else if(e==="touchmove"){if(he.touch.scrollDecided)return;he.touch.scrollDecided=!0;const t=Ga(s);let n=!1;const r=Math.abs(he.touch.x-i.clientX),o=Math.abs(he.touch.y-i.clientY);s.cancelable&&(t==="none"?n=!0:t==="pan-x"?n=o>r:t==="pan-y"&&(n=r>o)),n?s.preventDefault():et("track")}}function pe(s,i,e){return _e[i]?(Xa(s,i,e),!0):!1}function zn(s,i,e){return _e[i]?(Qa(s,i,e),!0):!1}function Xa(s,i,e){const t=_e[i],n=t.deps,r=t.name;let o=s[Nt];o||(s[Nt]=o={});for(let a=0,l,d;a<n.length;a++)l=n[a],!(Ua&&Xi(l)&&l!=="click")&&(d=o[l],d||(o[l]=d={_count:0}),d._count===0&&s.addEventListener(l,$n,Mn(l)),d[r]=(d[r]||0)+1,d._count=(d._count||0)+1);s.addEventListener(i,e),t.touchAction&&Ja(s,t.touchAction)}function Qa(s,i,e){const t=_e[i],n=t.deps,r=t.name,o=s[Nt];if(o)for(let a=0,l,d;a<n.length;a++)l=n[a],d=o[l],d&&d[r]&&(d[r]=(d[r]||1)-1,d._count=(d._count||1)-1,d._count===0&&s.removeEventListener(l,$n,Mn(l)));s.removeEventListener(i,e)}function Xt(s){Le.push(s),s.emits.forEach(i=>{_e[i]=s})}function Za(s){for(let i=0,e;i<Le.length;i++){e=Le[i];for(let t=0,n;t<e.emits.length;t++)if(n=e.emits[t],n===s)return e}return null}function Ja(s,i){Pn&&s instanceof HTMLElement&&te.run(()=>{s.style.touchAction=i}),s[Ti]=i}function Qi(s,i,e){const t=new Event(i,{bubbles:!0,cancelable:!0,composed:!0});if(t.detail=e,Na(s).dispatchEvent(t),t.defaultPrevented){const n=e.preventer||e.sourceEvent;n&&n.preventDefault&&n.preventDefault()}}function et(s){const i=Za(s);i.info&&(i.info.prevent=!0)}Xt({name:"downup",deps:["mousedown","touchstart","touchend"],flow:{start:["mousedown","touchstart"],end:["mouseup","touchend"]},emits:["down","up"],info:{movefn:null,upfn:null},reset(){Qe(this.info)},mousedown(s){if(!$e(s))return;const i=Ce(s),e=this,t=r=>{$e(r)||(lt("up",i,r),Qe(e.info))},n=r=>{$e(r)&&lt("up",i,r),Qe(e.info)};Rn(this.info,t,n),lt("down",i,s)},touchstart(s){lt("down",Ce(s),s.changedTouches[0],s)},touchend(s){lt("up",Ce(s),s.changedTouches[0],s)}});function lt(s,i,e,t){i&&Qi(i,s,{x:e.clientX,y:e.clientY,sourceEvent:e,preventer:t,prevent(n){return et(n)}})}Xt({name:"track",touchAction:"none",deps:["mousedown","touchstart","touchmove","touchend"],flow:{start:["mousedown","touchstart"],end:["mouseup","touchend"]},emits:["track"],info:{x:0,y:0,state:"start",started:!1,moves:[],addMove(s){this.moves.length>Ba&&this.moves.shift(),this.moves.push(s)},movefn:null,upfn:null,prevent:!1},reset(){this.info.state="start",this.info.started=!1,this.info.moves=[],this.info.x=0,this.info.y=0,this.info.prevent=!1,Qe(this.info)},mousedown(s){if(!$e(s))return;const i=Ce(s),e=this,t=r=>{const o=r.clientX,a=r.clientY;Ds(e.info,o,a)&&(e.info.state=e.info.started?r.type==="mouseup"?"end":"track":"start",e.info.state==="start"&&et("tap"),e.info.addMove({x:o,y:a}),$e(r)||(e.info.state="end",Qe(e.info)),i&&fi(e.info,i,r),e.info.started=!0)},n=r=>{e.info.started&&t(r),Qe(e.info)};Rn(this.info,t,n),this.info.x=s.clientX,this.info.y=s.clientY},touchstart(s){const i=s.changedTouches[0];this.info.x=i.clientX,this.info.y=i.clientY},touchmove(s){const i=Ce(s),e=s.changedTouches[0],t=e.clientX,n=e.clientY;Ds(this.info,t,n)&&(this.info.state==="start"&&et("tap"),this.info.addMove({x:t,y:n}),fi(this.info,i,e),this.info.state="track",this.info.started=!0)},touchend(s){const i=Ce(s),e=s.changedTouches[0];this.info.started&&(this.info.state="end",this.info.addMove({x:e.clientX,y:e.clientY}),fi(this.info,i,e))}});function Ds(s,i,e){if(s.prevent)return!1;if(s.started)return!0;const t=Math.abs(s.x-i),n=Math.abs(s.y-e);return t>=As||n>=As}function fi(s,i,e){if(!i)return;const t=s.moves[s.moves.length-2],n=s.moves[s.moves.length-1],r=n.x-s.x,o=n.y-s.y;let a,l=0;t&&(a=n.x-t.x,l=n.y-t.y),Qi(i,"track",{state:s.state,x:e.clientX,y:e.clientY,dx:r,dy:o,ddx:a,ddy:l,sourceEvent:e,hover(){return Fn(e.clientX,e.clientY)}})}Xt({name:"tap",deps:["mousedown","click","touchstart","touchend"],flow:{start:["mousedown","touchstart"],end:["click","touchend"]},emits:["tap"],info:{x:NaN,y:NaN,prevent:!1},reset(){this.info.x=NaN,this.info.y=NaN,this.info.prevent=!1},mousedown(s){$e(s)&&(this.info.x=s.clientX,this.info.y=s.clientY)},click(s){$e(s)&&Os(this.info,s)},touchstart(s){const i=s.changedTouches[0];this.info.x=i.clientX,this.info.y=i.clientY},touchend(s){Os(this.info,s.changedTouches[0],s)}});function Os(s,i,e){const t=Math.abs(i.clientX-s.x),n=Math.abs(i.clientY-s.y),r=Ce(e||i);!r||Ya[r.localName]&&r.hasAttribute("disabled")||(isNaN(t)||isNaN(n)||t<=Ts&&n<=Ts||ja(i))&&(s.prevent||Qi(r,"tap",{x:i.clientX,y:i.clientY,sourceEvent:i,preventer:e}))}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Qt=s=>class extends Ae(De(s)){get _activeKeys(){return[" "]}ready(){super.ready(),pe(this,"down",e=>{this._shouldSetActive(e)&&this._setActive(!0)}),pe(this,"up",()=>{this._setActive(!1)})}disconnectedCallback(){super.disconnectedCallback(),this._setActive(!1)}_shouldSetActive(e){return!this.disabled}_onKeyDown(e){super._onKeyDown(e),this._shouldSetActive(e)&&this._activeKeys.includes(e.key)&&(this._setActive(!0),document.addEventListener("keyup",t=>{this._activeKeys.includes(t.key)&&this._setActive(!1)},{once:!0}))}_setActive(e){this.toggleAttribute("active",e)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const el=["mousedown","mouseup","click","dblclick","keypress","keydown","keyup"],Zi=s=>class extends Qt(Wi(oe(s))){constructor(){super(),this.__onInteractionEvent=this.__onInteractionEvent.bind(this),el.forEach(e=>{this.addEventListener(e,this.__onInteractionEvent,!0)}),this.tabindex=0}get _activeKeys(){return["Enter"," "]}ready(){super.ready(),this.hasAttribute("role")||this.setAttribute("role","button"),this.__shouldAllowFocusWhenDisabled()&&this.style.setProperty("--_vaadin-button-disabled-pointer-events","auto")}_onKeyDown(e){super._onKeyDown(e),!(e.altKey||e.shiftKey||e.ctrlKey||e.metaKey)&&this._activeKeys.includes(e.key)&&(e.preventDefault(),this.click())}__onInteractionEvent(e){this.__shouldSuppressInteractionEvent(e)&&e.stopImmediatePropagation()}__shouldSuppressInteractionEvent(e){return this.disabled}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Nn=C`
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
 */const tl=C`
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
`,il=[Nn,tl];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class sl extends Zi(z(T(I(A(E))))){static get is(){return"vaadin-password-field-button"}static get styles(){return il}render(){return y``}}w(sl);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const nl=C`
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
 */const rl=s=>class extends gt(Ae(oe(yt(s)))){static get properties(){return{revealButtonHidden:{type:Boolean,value:!1},passwordVisible:{type:Boolean,value:!1,reflectToAttribute:!0,readOnly:!0},i18n:{type:Object,value:()=>({reveal:"Show password"})}}}static get delegateAttrs(){return super.delegateAttrs.filter(e=>e!=="autocapitalize")}constructor(){super(),this._setType("password"),this.__boundRevealButtonClick=this._onRevealButtonClick.bind(this),this.__boundRevealButtonMouseDown=this._onRevealButtonMouseDown.bind(this),this.__lastChange=""}get slotStyles(){const e=this.localName;return[...super.slotStyles,`
          ${e} [slot="input"]::-ms-reveal {
            display: none;
          }
        `]}ready(){super.ready(),this._revealPart=this.shadowRoot.querySelector('[part~="reveal-button"]'),this._revealButtonController=new G(this,"reveal","vaadin-password-field-button",{initializer:e=>{this._revealNode=e,e.addEventListener("click",this.__boundRevealButtonClick),e.addEventListener("mousedown",this.__boundRevealButtonMouseDown)}}),this.addController(this._revealButtonController),this.inputElement&&(this.inputElement.autocapitalize="off")}updated(e){super.updated(e),e.has("disabled")&&(this._revealNode.disabled=this.disabled),e.has("revealButtonHidden")&&this._toggleRevealHidden(this.revealButtonHidden),e.has("passwordVisible")&&(this._setType(this.passwordVisible?"text":"password"),this._revealNode.setAttribute("aria-pressed",this.passwordVisible?"true":"false")),e.has("i18n")&&this.i18n&&this.i18n.reveal&&this._revealNode.setAttribute("aria-label",this.i18n.reveal)}_onChange(e){super._onChange(e),this.__lastChange=this.inputElement.value}_shouldSetFocus(e){return e.target===this.inputElement||e.target===this._revealNode}_shouldRemoveFocus(e){return!(e.relatedTarget===this._revealNode||e.relatedTarget===this.inputElement&&e.target===this._revealNode)}_setFocused(e){if(super._setFocused(e),!e)this._setPasswordVisible(!1),this.__lastChange!==this.inputElement.value&&(this.__lastChange=this.inputElement.value,this.dispatchEvent(new CustomEvent("change",{bubbles:!0})));else{const t=this.getRootNode().activeElement===this._revealNode;this.toggleAttribute("focus-ring",this._keyboardActive&&!t)}}_onRevealButtonClick(){this._setPasswordVisible(!this.passwordVisible)}_onRevealButtonMouseDown(e){e.preventDefault(),this.inputElement.focus()}_toggleRevealHidden(e){this._revealNode&&(e?(this._revealPart.setAttribute("hidden",""),this._revealNode.setAttribute("tabindex","-1"),this._revealNode.setAttribute("aria-hidden","true")):(this._revealPart.removeAttribute("hidden"),this._revealNode.setAttribute("tabindex","0"),this._revealNode.removeAttribute("aria-hidden")))}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ol extends rl(Ki){static get is(){return"vaadin-password-field"}static get styles(){return[...super.styles,nl]}_renderSuffix(){return y`
      ${super._renderSuffix()}
      <div part="field-button reveal-button" slot="suffix">
        <slot name="reveal"></slot>
      </div>
    `}}w(ol);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const al=C`
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
 */class ll extends Ki{static get is(){return"vaadin-email-field"}static get styles(){return[...super.styles,al]}static get delegateAttrs(){return super.delegateAttrs.filter(i=>i!=="autocapitalize")}constructor(){super(),this._setType("email"),this.pattern="^[a-zA-Z0-9_\\-+]+(?:\\.[a-zA-Z0-9_\\-+]+)*@[a-zA-Z0-9\\-.]+\\.[a-zA-Z0-9\\-]{2,}$"}ready(){super.ready(),this.inputElement&&(this.inputElement.autocapitalize="off")}}w(ll);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const dl=C`
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
 */const St=new ResizeObserver(s=>{setTimeout(()=>{s.forEach(i=>{i.target.isConnected&&(i.target.resizables?i.target.resizables.forEach(e=>{e._onResize(i.contentRect)}):i.target._onResize(i.contentRect))})})}),Zt=J(s=>class extends s{get _observeParent(){return!1}connectedCallback(){if(super.connectedCallback(),St.observe(this),this._observeParent){const e=this.parentNode instanceof ShadowRoot?this.parentNode.host:this.parentNode;e.resizables||(e.resizables=new Set,St.observe(e)),e.resizables.add(this),this.__parent=e}}disconnectedCallback(){super.disconnectedCallback(),St.unobserve(this);const e=this.__parent;if(this._observeParent&&e){const t=e.resizables;t&&(t.delete(this),t.size===0&&St.unobserve(e)),this.__parent=null}}_onResize(e){}});/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class hl extends G{constructor(i,e){super(i,"textarea","textarea",{initializer:(t,n)=>{const r=n.getAttribute("value");r&&(t.value=r);const o=n.getAttribute("name");o&&t.setAttribute("name",o),t.id=this.defaultId,typeof e=="function"&&e(t)},useUniqueId:!0})}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const cl=s=>class extends Zt(Gi(s)){static get properties(){return{maxlength:{type:Number},minlength:{type:Number},pattern:{type:String},minRows:{type:Number,value:2,observer:"__minRowsChanged"},maxRows:{type:Number}}}static get delegateAttrs(){return[...super.delegateAttrs,"maxlength","minlength","pattern"]}static get constraints(){return[...super.constraints,"maxlength","minlength","pattern"]}static get observers(){return["__updateMinHeight(minRows, inputElement)","__updateMaxHeight(maxRows, inputElement, _inputField)"]}get clearElement(){return this.$.clearButton}_onResize(){this._updateHeight(),this.__scrollPositionUpdated()}_onScroll(){this.__scrollPositionUpdated()}ready(){super.ready(),this.__textAreaController=new hl(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e}),this.addController(this.__textAreaController),this.addController(new ve(this.inputElement,this._labelController)),this._inputField=this.shadowRoot.querySelector("[part=input-field]"),this._inputField.addEventListener("wheel",e=>{const t=this._inputField.scrollTop;this._inputField.scrollTop+=e.deltaY,t!==this._inputField.scrollTop&&(e.preventDefault(),this.__scrollPositionUpdated())}),this._updateHeight(),this.__scrollPositionUpdated()}__scrollPositionUpdated(){this._inputField.style.setProperty("--_text-area-vertical-scroll-position","0px"),this._inputField.style.setProperty("--_text-area-vertical-scroll-position",`${this._inputField.scrollTop}px`)}_valueChanged(e,t){super._valueChanged(e,t),this._updateHeight()}_updateHeight(){const e=this.inputElement,t=this._inputField;if(!e||!t)return;const n=t.scrollTop,r=this.value?this.value.length:0;if(this._oldValueLength>=r){const a=getComputedStyle(t).height,l=getComputedStyle(e).width;t.style.height=a,e.style.maxWidth=l,e.style.alignSelf="flex-start",e.style.height="auto"}this._oldValueLength=r;const o=e.scrollHeight;o>e.clientHeight&&(e.style.height=`${o}px`),e.style.removeProperty("max-width"),e.style.removeProperty("align-self"),t.style.removeProperty("height"),t.scrollTop=n,this.__updateMaxHeight(this.maxRows)}__updateMinHeight(e){this.inputElement&&this.inputElement===this.__textAreaController.defaultNode&&(this.inputElement.rows=Math.max(e,1))}__updateMaxHeight(e){if(!(!this._inputField||!this.inputElement))if(e){const t=getComputedStyle(this.inputElement),n=getComputedStyle(this._inputField),o=parseFloat(t.lineHeight)*e,a=parseFloat(t.paddingTop)+parseFloat(t.paddingBottom)+parseFloat(t.marginTop)+parseFloat(t.marginBottom)+parseFloat(n.borderTopWidth)+parseFloat(n.borderBottomWidth)+parseFloat(n.paddingTop)+parseFloat(n.paddingBottom),l=Math.ceil(o+a);this._inputField.style.setProperty("max-height",`${l}px`)}else this._inputField.style.removeProperty("max-height")}__minRowsChanged(e){e<1&&console.warn("<vaadin-text-area> minRows must be at least 1.")}scrollToStart(){this._inputField.scrollTop=0}scrollToEnd(){this._inputField.scrollTop=this._inputField.scrollHeight}checkValidity(){if(!super.checkValidity())return!1;if(!this.pattern||!this.inputElement.value)return!0;try{const e=this.inputElement.value.match(this.pattern);return e?e[0]===e.input:!1}catch{return!0}}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ul extends cl(T(L(I(A(E))))){static get is(){return"vaadin-text-area"}static get styles(){return[ke,dl]}render(){return y`
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
          theme="${B(this._theme)}"
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
    `}ready(){super.ready(),this._tooltipController=new X(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}}w(ul);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const _l=C`
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
 */const Ps="NaN",pl=s=>class extends Gi(s){static get properties(){return{min:{type:Number},max:{type:Number},step:{type:Number},stepButtonsVisible:{type:Boolean,value:!1,reflectToAttribute:!0}}}static get observers(){return["_stepChanged(step, inputElement)"]}static get delegateProps(){return[...super.delegateProps,"min","max"]}static get constraints(){return[...super.constraints,"min","max","step"]}constructor(){super(),this._setType("number"),this.__onWheel=this.__onWheel.bind(this)}get slotStyles(){const e=this.localName;return[`
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
        `]}get clearElement(){return this.$.clearButton}get __hasUnparsableValue(){return this._inputElementValue===Ps}ready(){super.ready(),this.addController(new Te(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new ve(this.inputElement,this._labelController)),this._tooltipController=new X(this),this.addController(this._tooltipController),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement)}checkValidity(){return this.inputElement?this.inputElement.checkValidity():!this.invalid}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("wheel",this.__onWheel)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("wheel",this.__onWheel)}__onWheel(e){this.hasAttribute("focused")&&e.preventDefault()}_onDecreaseButtonTouchend(e){e.cancelable&&(e.preventDefault(),this.__blurActiveElement(),this._decreaseValue())}_onIncreaseButtonTouchend(e){e.cancelable&&(e.preventDefault(),this.__blurActiveElement(),this._increaseValue())}__blurActiveElement(){const e=Lt();e&&e!==this.inputElement&&e.blur()}_onDecreaseButtonClick(){this._decreaseValue()}_onIncreaseButtonClick(){this._increaseValue()}_decreaseValue(){this._incrementValue(-1)}_increaseValue(){this._incrementValue(1)}_incrementValue(e){if(this.disabled||this.readonly)return;const t=this.step||1;let n=parseFloat(this.value);this.value?n<this.min?(e=0,n=this.min):n>this.max&&(e=0,n=this.max):this.min===0&&e<0||this.max===0&&e>0||this.max===0&&this.min===0?(e=0,n=0):(this.max==null||this.max>=0)&&(this.min==null||this.min<=0)?n=0:this.min>0?(n=this.min,this.max<0&&e<0&&(n=this.max),e=0):this.max<0&&(n=this.max,e<0?e=0:this._getIncrement(1,n-t)>this.max?n-=2*t:n-=t);const r=this._getIncrement(e,n);(!this.value||e===0||this._incrementIsInsideTheLimits(e,n))&&(this.inputElement.value=String(parseFloat(r)),this.inputElement.dispatchEvent(new Event("input",{bubbles:!0,composed:!0})),this.__commitValueChange())}_getIncrement(e,t){let n=this.step||1,r=this.min||0;const o=Math.max(this._getMultiplier(t),this._getMultiplier(n),this._getMultiplier(r));n*=o,t=Math.round(t*o),r*=o;const a=(t-r)%n;return e>0?(t-a+n)/o:e<0?(t-(a||n))/o:t/o}_getDecimalCount(e){const t=String(e),n=t.indexOf(".");return n===-1?1:t.length-n-1}_getMultiplier(e){if(!isNaN(e))return 10**this._getDecimalCount(e)}_incrementIsInsideTheLimits(e,t){return e<0?this.min==null||this._getIncrement(e,t)>=this.min:e>0?this.max==null||this._getIncrement(e,t)<=this.max:this._getIncrement(e,t)<=this.max&&this._getIncrement(e,t)>=this.min}_isButtonEnabled(e){const t=e*(this.step||1),n=parseFloat(this.value);return!this.value||!this.disabled&&this._incrementIsInsideTheLimits(t,n)}_stepChanged(e,t){t&&(t.step=e||"any")}_valueChanged(e,t){e&&isNaN(parseFloat(e))?this.value="":typeof this.value!="string"&&(this.value=String(this.value)),super._valueChanged(this.value,t),this.__keepCommittedValue||(this.__committedValue=this.value,this.__committedUnparsableValueStatus=!1)}_onKeyDown(e){e.key==="ArrowUp"?(e.preventDefault(),this._increaseValue()):e.key==="ArrowDown"&&(e.preventDefault(),this._decreaseValue()),super._onKeyDown(e)}_onInput(e){this.__keepCommittedValue=!0,super._onInput(e),this.__keepCommittedValue=!1}_onChange(e){e.stopPropagation()}_onClearAction(e){super._onClearAction(e),this.__commitValueChange()}_setFocused(e){super._setFocused(e),e||this.__commitValueChange()}_onEnter(e){super._onEnter(e),this.__commitValueChange()}__commitValueChange(){this.__committedValue!==this.value?(this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{bubbles:!0}))):this.__committedUnparsableValueStatus!==this.__hasUnparsableValue&&(this._requestValidation(),this.dispatchEvent(new CustomEvent("unparsable-change"))),this.__committedValue=this.value,this.__committedUnparsableValueStatus=this.__hasUnparsableValue}get _inputElementValue(){return this.inputElement&&this.inputElement.validity.badInput?Ps:super._inputElementValue}set _inputElementValue(e){super._inputElementValue=e}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Bn extends pl(T(L(I(A(E))))){static get is(){return"vaadin-number-field"}static get styles(){return[ke,_l]}render(){return y`
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
          theme="${B(this._theme)}"
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
    `}}w(Bn);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class fl extends Bn{static get is(){return"vaadin-integer-field"}constructor(){super(),this.allowedCharPattern="[-+\\d]"}_valueChanged(i,e){if(i!==""&&!this.__isInteger(i)){console.warn(`Trying to set non-integer value "${i}" to <vaadin-integer-field>. Clearing the value.`),this.value="";return}super._valueChanged(i,e)}_stepChanged(i,e){if(i!=null&&!this.__hasOnlyDigits(i)){console.warn(`<vaadin-integer-field> The \`step\` property must be a positive integer but \`${i}\` was provided, so the property was reset to \`null\`.`),this.step=null;return}super._stepChanged(i,e)}__isInteger(i){return/^(-\d)?\d*$/u.test(String(i))}__hasOnlyDigits(i){return/^\d+$/u.test(String(i))}}w(fl);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ml=C`
  [part='overlay'] {
    display: flex;
    flex: auto;
    max-height: var(--vaadin-date-picker-overlay-max-height, 30rem);
    box-sizing: content-box;
    width: var(
      --vaadin-date-picker-overlay-width,
      calc(
        var(--vaadin-date-picker-date-width, 2rem) * 7 +
          var(--vaadin-date-picker-month-padding, var(--vaadin-padding-s)) * 2 +
          var(--vaadin-date-picker-year-scroller-width, 3rem)
      )
    );
    cursor: default;
  }

  :host([fullscreen]) {
    --vaadin-date-picker-date-width: calc(100% / 7);
  }

  :host([fullscreen]) [part='backdrop'] {
    display: block;
  }

  :host([fullscreen]) [part='overlay'] {
    border: none;
    border-radius: 0;
    max-height: 75vh;
    width: 100%;
  }

  [part~='content'] {
    flex: auto;
  }

  @media (max-width: 450px), (max-height: 450px) {
    :host {
      inset: auto 0 0 !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const gl=s=>class extends xt(ge(s)){_shouldCloseOnOutsideClick(e){return!e.composedPath().includes(this.positionTarget)}_mouseDownListener(e){super._mouseDownListener(e),this._shouldCloseOnOutsideClick(e)&&!mt(e.composedPath()[0])&&e.preventDefault()}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class vl extends gl(z(T(I(A(E))))){static get is(){return"vaadin-date-picker-overlay"}static get styles(){return[me,ml]}render(){return y`
      <div id="backdrop" part="backdrop" ?hidden="${!this.withBackdrop}"></div>
      <div part="overlay" id="overlay">
        <div part="content" id="content">
          <slot></slot>
        </div>
      </div>
    `}get _contentRoot(){return this.owner._overlayContent}}w(vl);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Vn extends Zi(L(T(I(A(E))))){static get is(){return"vaadin-button"}static get styles(){return Nn}static get properties(){return{disabled:{type:Boolean,value:!1,observer:"_disabledChanged",reflectToAttribute:!0,sync:!0}}}render(){return y`
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
    `}ready(){super.ready(),this._tooltipController=new X(this),this.addController(this._tooltipController)}__shouldAllowFocusWhenDisabled(){return window.Vaadin.featureFlags.accessibleDisabledButtons}}w(Vn);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function bl(s){let i=s.getDay();i===0&&(i=7);const e=4-i,t=new Date(s.getTime()+e*24*3600*1e3),n=new Date(0,0);n.setFullYear(t.getFullYear());const r=t.getTime()-n.getTime(),o=Math.round(r/(24*3600*1e3));return Math.floor(o/7+1)}function Ai(s){const i=new Date(s);return i.setHours(0,0,0,0),i}function ee(s,i,e=Ai){return s instanceof Date&&i instanceof Date&&e(s).getTime()===e(i).getTime()}function Ji(s){return{day:s.getDate(),month:s.getMonth(),year:s.getFullYear()}}function Ze(s,i,e,t){let n=!1;if(typeof t=="function"&&s){const r=Ji(s);n=t(r)}return(!i||s>=i)&&(!e||s<=e)&&!n}function Hn(s,i){return i.filter(e=>e!==void 0).reduce((e,t)=>{if(!t)return e;if(!e)return t;const n=Math.abs(s.getTime()-t.getTime()),r=Math.abs(e.getTime()-s.getTime());return n<r?t:e})}function Wn(s){const i=new Date,e=new Date(i);return e.setDate(1),e.setMonth(parseInt(s)+i.getMonth()),e}function yl(s,i,e=0,t=1){if(i>99)throw new Error("The provided year cannot have more than 2 digits.");if(i<0)throw new Error("The provided year cannot be negative.");let n=i+Math.floor(s.getFullYear()/100)*100;return s<new Date(n-50,e,t)?n-=100:s>new Date(n+50,e,t)&&(n+=100),n}function Fe(s){const i=/^([-+]\d{1}|\d{2,4}|[-+]\d{6})-(\d{1,2})-(\d{1,2})$/u.exec(s);if(!i)return;const e=new Date(0,0);return e.setFullYear(parseInt(i[1],10)),e.setMonth(parseInt(i[2],10)-1),e.setDate(parseInt(i[3],10)),e}function wl(s){const i=(l,d="00")=>(d+l).substr((d+l).length-d.length);let e="",t="0000",n=s.year;n<0?(n=-n,e="-",t="000000"):s.year>=1e4&&(e="+",t="000000");const r=e+i(n,t),o=i(s.month+1),a=i(s.day);return[r,o,a].join("-")}function Cl(s){return s instanceof Date?wl({year:s.getFullYear(),month:s.getMonth(),day:s.getDate()}):""}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const qn=document.createElement("template");qn.innerHTML=`
  <style>
    :host {
      display: block;
      overflow: hidden;
      height: 500px;
    }

    #scroller {
      position: relative;
      height: 100%;
      overflow: auto;
      outline: none;
      overflow-x: hidden;
      scrollbar-width: none;
    }

    #scroller::-webkit-scrollbar {
      display: none;
    }

    .buffer {
      position: absolute;
      width: var(--vaadin-infinite-scroller-buffer-width, 100%);
      box-sizing: border-box;
      top: var(--vaadin-infinite-scroller-buffer-offset, 0);
    }
  </style>

  <div id="scroller" tabindex="-1">
    <div class="buffer"></div>
    <div class="buffer"></div>
    <div id="fullHeight"></div>
  </div>
`;class Un extends HTMLElement{constructor(){super(),this.attachShadow({mode:"open"}).appendChild(qn.content.cloneNode(!0)),this.bufferSize=20,this._initialScroll=5e5,this._initialIndex=0,this._activated=!1}get active(){return this._activated}set active(i){i&&!this._activated&&(this._createPool(),this._activated=!0)}get bufferOffset(){return this._buffers[0].offsetTop}get itemHeight(){if(!this._itemHeightVal){const i=getComputedStyle(this).getPropertyValue("--vaadin-infinite-scroller-item-height"),e="background-position";this.$.fullHeight.style.setProperty(e,i);const t=getComputedStyle(this.$.fullHeight).getPropertyValue(e);this.$.fullHeight.style.removeProperty(e),this._itemHeightVal=parseFloat(t)}return this._itemHeightVal}get _bufferHeight(){return this.itemHeight*this.bufferSize}get position(){return(this.$.scroller.scrollTop-this._buffers[0].translateY)/this.itemHeight+this._firstIndex}set position(i){this._preventScrollEvent=!0,i>this._firstIndex&&i<this._firstIndex+this.bufferSize*2?this.$.scroller.scrollTop=this.itemHeight*(i-this._firstIndex)+this._buffers[0].translateY:(this._initialIndex=~~i,this._reset(),this._scrollDisabled=!0,this.$.scroller.scrollTop+=i%1*this.itemHeight,this._scrollDisabled=!1)}connectedCallback(){this._ready||(this._ready=!0,this.$={},this.shadowRoot.querySelectorAll("[id]").forEach(i=>{this.$[i.id]=i}),this.$.scroller.addEventListener("scroll",()=>this._scroll()),this._buffers=[...this.shadowRoot.querySelectorAll(".buffer")],this.$.fullHeight.style.height=`${this._initialScroll*2}px`)}disconnectedCallback(){this._debouncerScrollFinish&&this._debouncerScrollFinish.cancel(),this._debouncerUpdateClones&&this._debouncerUpdateClones.cancel(),this.__pendingFinishInit&&cancelAnimationFrame(this.__pendingFinishInit)}forceUpdate(){this._debouncerScrollFinish&&this._debouncerScrollFinish.flush(),this._debouncerUpdateClones&&(this._buffers[0].updated=this._buffers[1].updated=!1,this._updateClones(),this._debouncerUpdateClones.cancel())}_createElement(){}_updateElement(i,e){}_finishInit(){this._initDone||(this._buffers.forEach(i=>{[...i.children].forEach(e=>{this._ensureStampedInstance(e._itemWrapper)})}),this._buffers[0].translateY||this._reset(),this._initDone=!0,this.dispatchEvent(new CustomEvent("init-done")))}_translateBuffer(i){const e=i?1:0;this._buffers[e].translateY=this._buffers[e?0:1].translateY+this._bufferHeight*(e?-1:1),this._buffers[e].style.transform=`translate3d(0, ${this._buffers[e].translateY}px, 0)`,this._buffers[e].updated=!1,this._buffers.reverse()}_scroll(){if(this._scrollDisabled)return;const i=this.$.scroller.scrollTop;(i<this._bufferHeight||i>this._initialScroll*2-this._bufferHeight)&&(this._initialIndex=~~this.position,this._reset());const e=this.itemHeight+this.bufferOffset,t=i>this._buffers[1].translateY+e,n=i<this._buffers[0].translateY+e;(t||n)&&(this._translateBuffer(n),this._updateClones()),this._preventScrollEvent||this.dispatchEvent(new CustomEvent("custom-scroll",{bubbles:!1,composed:!0})),this._preventScrollEvent=!1,this._debouncerScrollFinish=D.debounce(this._debouncerScrollFinish,K.after(200),()=>{const r=this.$.scroller.getBoundingClientRect();!this._isVisible(this._buffers[0],r)&&!this._isVisible(this._buffers[1],r)&&(this.position=this.position)})}_reset(){this._scrollDisabled=!0,this.$.scroller.scrollTop=this._initialScroll,this._buffers[0].translateY=this._initialScroll-this._bufferHeight,this._buffers[1].translateY=this._initialScroll,this._buffers.forEach(i=>{i.style.transform=`translate3d(0, ${i.translateY}px, 0)`}),this._buffers[0].updated=this._buffers[1].updated=!1,this._updateClones(!0),this._debouncerUpdateClones=D.debounce(this._debouncerUpdateClones,K.after(200),()=>{this._buffers[0].updated=this._buffers[1].updated=!1,this._updateClones()}),this._scrollDisabled=!1}_createPool(){const i=this.innerHeight;this._buffers.forEach(e=>{for(let t=0;t<this.bufferSize;t++){const n=document.createElement("div");n.style.height=`${this.itemHeight}px`,n.instance={};const r=`vaadin-infinite-scroller-item-content-${Se()}`,o=document.createElement("slot");o.setAttribute("name",r),o._itemWrapper=n,e.appendChild(o),n.setAttribute("slot",r),this.appendChild(n),this.itemHeight*t<=i&&this._ensureStampedInstance(n)}}),this.__pendingFinishInit=requestAnimationFrame(()=>{this._finishInit(),this.__pendingFinishInit=null})}_ensureStampedInstance(i){if(i.firstElementChild)return;const e=i.instance;i.instance=this._createElement(),i.appendChild(i.instance),Object.keys(e).forEach(t=>{i.instance[t]=e[t]})}_updateClones(i){this._firstIndex=Math.round((this._buffers[0].translateY-this._initialScroll)/this.itemHeight)+this._initialIndex;const e=i?this.$.scroller.getBoundingClientRect():void 0;this._buffers.forEach((t,n)=>{if(!t.updated){const r=this._firstIndex+this.bufferSize*n;[...t.children].forEach((o,a)=>{const l=o._itemWrapper;(!i||this._isVisible(l,e))&&this._updateElement(l.instance,r+a)}),t.updated=!0}})}_isVisible(i,e){const t=i.getBoundingClientRect();return t.bottom>e.top&&t.top<e.bottom}}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Yn=document.createElement("template");Yn.innerHTML=`
  <style>
    :host {
      --vaadin-infinite-scroller-item-height: 270px;
      grid-area: months;
      height: auto;
    }
  </style>
`;class xl extends Un{static get is(){return"vaadin-date-picker-month-scroller"}constructor(){super(),this.bufferSize=3,this.shadowRoot.appendChild(Yn.content.cloneNode(!0))}_createElement(){return document.createElement("vaadin-month-calendar")}_updateElement(i,e){i.month=Wn(e)}}w(xl);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const jn=document.createElement("template");jn.innerHTML=`
  <style>
    :host {
      --vaadin-infinite-scroller-item-height: 80px;
      width: 50px;
      display: block;
      position: relative;
      grid-area: years;
      height: auto;
      -webkit-tap-highlight-color: transparent;
      -webkit-user-select: none;
      user-select: none;
      /* Center the year scroller position. */
      --vaadin-infinite-scroller-buffer-offset: 50%;
    }

    :host::before {
      content: '';
      display: block;
      background: transparent;
      width: 0;
      height: 0;
      position: absolute;
      left: 0;
      top: 50%;
      transform: translateY(-50%);
      border-width: 6px;
      border-style: solid;
      border-color: transparent;
      border-left-color: #000;
    }
  </style>
`;class El extends Un{static get is(){return"vaadin-date-picker-year-scroller"}constructor(){super(),this.bufferSize=12,this.shadowRoot.appendChild(jn.content.cloneNode(!0))}_createElement(){return document.createElement("vaadin-date-picker-year")}_updateElement(i,e){i.year=this._yearAfterXYears(e)}_yearAfterXYears(i){const e=new Date,t=new Date(e);return t.setFullYear(parseInt(i)+e.getFullYear()),t.getFullYear()}}w(El);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Il=C`
  :host {
    display: block;
    height: 100%;
  }

  [part='year-number'] {
    align-items: center;
    display: flex;
    height: 50%;
    justify-content: center;
    transform: translateY(-50%);
    color: var(--vaadin-text-color-secondary);
  }

  :host([current]) [part='year-number'] {
    color: var(--vaadin-date-picker-year-scroller-current-year-color, var(--vaadin-text-color));
  }
`;/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Sl extends T(I(A(E))){static get is(){return"vaadin-date-picker-year"}static get styles(){return Il}static get properties(){return{year:{type:String,sync:!0},selectedDate:{type:Object,sync:!0}}}render(){return y`
      <div part="year-number">${this.year}</div>
      <div part="year-separator" aria-hidden="true"></div>
    `}updated(i){super.updated(i),i.has("year")&&this.toggleAttribute("current",this.year===new Date().getFullYear()),(i.has("year")||i.has("selectedDate"))&&this.toggleAttribute("selected",this.selectedDate&&this.selectedDate.getFullYear()===this.year)}}w(Sl);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const kl=C`
  :host {
    display: block;
    padding: var(--vaadin-date-picker-month-padding, var(--vaadin-padding-s));
  }

  [part='month-header'] {
    color: var(--vaadin-date-picker-month-header-color, var(--vaadin-text-color));
    font-size: var(--vaadin-date-picker-month-header-font-size, 0.9375rem);
    font-weight: var(--vaadin-date-picker-month-header-font-weight, 500);
    line-height: inherit;
    margin-bottom: 0.75rem;
    text-align: center;
  }

  table {
    border-collapse: collapse;
    display: flex;
    flex-direction: column;
  }

  tr {
    display: flex;
    flex-wrap: wrap;
  }

  [part~='weekday'] {
    color: var(--vaadin-date-picker-weekday-color, var(--vaadin-text-color-secondary));
    font-size: var(--vaadin-date-picker-weekday-font-size, 0.75rem);
    font-weight: var(--vaadin-date-picker-weekday-font-weight, 500);
    margin-bottom: 0.375rem;
    width: var(--vaadin-date-picker-date-width, 2rem);
  }

  /* Week numbers are on a separate row, don't reserve space on weekday row. */
  [part~='weekday']:empty {
    display: none;
  }

  [part~='week-number'] {
    color: var(--vaadin-date-picker-week-number-color, var(--vaadin-text-color-secondary));
    font-size: var(--vaadin-date-picker-week-number-font-size, 0.7rem);
    line-height: 1;
    width: 100%;
    margin-top: 0.125em;
    margin-bottom: 0.125em;
    gap: 0.25em;
  }

  [part~='week-number']::after {
    content: '';
    height: 1px;
    flex: 1;
    background: var(
      --vaadin-date-picker-week-divider-color,
      var(--vaadin-divider-color, var(--vaadin-border-color-secondary))
    );
  }

  [part~='weekday'],
  [part~='week-number'],
  [part~='date'] {
    align-items: center;
    display: flex;
    justify-content: center;
    padding: 0;
  }

  [part~='date'] {
    border-radius: var(--vaadin-date-picker-date-border-radius, var(--vaadin-radius-m));
    position: relative;
    width: var(--vaadin-date-picker-date-width, 2rem);
    height: var(--vaadin-date-picker-date-height, 2rem);
    cursor: var(--vaadin-clickable-cursor);
    outline: none;
  }

  [part~='date']::after {
    border-radius: inherit;
    content: '';
    position: absolute;
    z-index: -1;
    height: inherit;
    aspect-ratio: 1;
  }

  :where([part~='date']:focus)::after {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--vaadin-focus-ring-width) * -1);
  }

  [part~='today'] {
    color: var(--vaadin-date-picker-date-today-color, var(--vaadin-text-color));
  }

  [part~='selected'] {
    color: var(--vaadin-date-picker-date-selected-color, var(--vaadin-background-color));
  }

  [part~='selected']::after {
    background: var(--vaadin-date-picker-date-selected-background, var(--vaadin-text-color));
    outline-offset: 1px;
  }

  [disabled] {
    cursor: var(--vaadin-disabled-cursor);
    color: var(--vaadin-date-picker-date-disabled-color, var(--vaadin-text-color-disabled));
    opacity: 0.7;
  }

  [hidden] {
    display: none;
  }

  @media (forced-colors: active) {
    [part~='week-number']::after {
      background: CanvasText;
    }

    [part~='today'] {
      font-weight: 600;
    }

    [part~='selected'] {
      forced-color-adjust: none;
      --vaadin-date-picker-date-selected-color: SelectedItemText;
      color: SelectedItemText !important;
      --vaadin-date-picker-date-selected-background: SelectedItem;
    }

    [disabled] {
      color: GrayText !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Tl=s=>class extends oe(s){static get properties(){return{month:{type:Object,value:new Date,sync:!0},selectedDate:{type:Object,notify:!0,sync:!0},focusedDate:{type:Object},showWeekNumbers:{type:Boolean,value:!1},i18n:{type:Object},ignoreTaps:{type:Boolean},minDate:{type:Date,value:null,sync:!0},maxDate:{type:Date,value:null,sync:!0},isDateDisabled:{type:Function,value:()=>!1},enteredDate:{type:Date},disabled:{type:Boolean,reflectToAttribute:!0,computed:"__computeDisabled(month, minDate, maxDate)"},_days:{type:Array,computed:"__computeDays(month, i18n, minDate, maxDate, isDateDisabled)"},_weeks:{type:Array,computed:"__computeWeeks(_days)"},_notTapping:{type:Boolean},__hasFocus:{type:Boolean}}}static get observers(){return["__focusedDateChanged(focusedDate, _days)","_showWeekNumbersChanged(showWeekNumbers, i18n)"]}get focusableDateElement(){return[...this.shadowRoot.querySelectorAll("[part~=date]")].find(e=>ee(e.date,this.focusedDate))}ready(){super.ready(),pe(this.$.monthGrid,"tap",this._handleTap.bind(this))}_setFocused(e){super._setFocused(e),this.__hasFocus=e}__computeDisabled(e,t,n){const r=new Date(0,0);r.setFullYear(e.getFullYear()),r.setMonth(e.getMonth()),r.setDate(1);const o=new Date(0,0);return o.setFullYear(e.getFullYear()),o.setMonth(e.getMonth()+1),o.setDate(0),t&&n&&t.getMonth()===n.getMonth()&&t.getMonth()===e.getMonth()&&n.getDate()-t.getDate()>=0?!1:!Ze(r,t,n)&&!Ze(o,t,n)}_getTitle(e,t){if(!(e===void 0||t===void 0))return t.formatTitle(t.monthNames[e.getMonth()],e.getFullYear())}_onMonthGridTouchStart(){this._notTapping=!1,setTimeout(()=>{this._notTapping=!0},300)}_dateAdd(e,t){e.setDate(e.getDate()+t)}_applyFirstDayOfWeek(e,t){if(!(e===void 0||t===void 0))return e.slice(t).concat(e.slice(0,t))}__computeWeekDayNames(e,t){if(e===void 0||t===void 0)return[];const{weekdays:n,weekdaysShort:r,firstDayOfWeek:o}=e,a=this._applyFirstDayOfWeek(r,o);return this._applyFirstDayOfWeek(n,o).map((d,h)=>({weekDay:d,weekDayShort:a[h]})).slice(0,7)}__focusedDateChanged(e,t){Array.isArray(t)&&t.some(n=>ee(n,e))?this.removeAttribute("aria-hidden"):this.setAttribute("aria-hidden","true")}_getDate(e){return e?e.getDate():""}__computeShowWeekSeparator(e,t){return e&&t&&t.firstDayOfWeek===1}_isToday(e){return ee(new Date,e)}__computeDays(e,t){if(e===void 0||t===void 0)return[];const n=new Date(0,0);for(n.setFullYear(e.getFullYear()),n.setMonth(e.getMonth()),n.setDate(1);n.getDay()!==t.firstDayOfWeek;)this._dateAdd(n,-1);const r=[],o=n.getMonth(),a=e.getMonth();for(;n.getMonth()===a||n.getMonth()===o;)r.push(n.getMonth()===a?new Date(n.getTime()):null),this._dateAdd(n,1);return r}__computeWeeks(e){return e.reduce((t,n,r)=>(r%7===0&&t.push([]),t[t.length-1].push(n),t),[])}_handleTap(e){!this.ignoreTaps&&!this._notTapping&&e.target.date&&!e.target.hasAttribute("disabled")&&(this.selectedDate=e.target.date,this.dispatchEvent(new CustomEvent("date-tap",{detail:{date:e.target.date},bubbles:!0,composed:!0})))}_preventDefault(e){e.preventDefault()}__computeWeekNumber(e){const t=e.reduce((n,r)=>!n&&r?r:n);return bl(t)}__computeDayAriaLabel(e){if(!e)return"";let t=`${this._getDate(e)} ${this.i18n.monthNames[e.getMonth()]} ${e.getFullYear()}, ${this.i18n.weekdays[e.getDay()]}`;return this._isToday(e)&&(t+=`, ${this.i18n.today}`),t}_showWeekNumbersChanged(e,t){this.__computeShowWeekSeparator(e,t)?this.setAttribute("week-numbers",""):this.removeAttribute("week-numbers")}__computeDatePart(e,t,n,r,o,a,l,d){const h=["date"];return this.__isDayDisabled(e,r,o,a)&&h.push("disabled"),ee(e,t)&&(d||ee(e,l))&&h.push("focused"),this.__isDaySelected(e,n)&&h.push("selected"),this._isToday(e)&&h.push("today"),e<Ai(new Date)&&h.push("past"),e>Ai(new Date)&&h.push("future"),h.join(" ")}__isDaySelected(e,t){return ee(e,t)}__computeDayAriaSelected(e,t){return String(this.__isDaySelected(e,t))}__isDayDisabled(e,t,n,r){return!Ze(e,t,n,r)}__computeDayAriaDisabled(e,t,n,r){return e===void 0||t===void 0&&n===void 0&&r===void 0?"false":String(this.__isDayDisabled(e,t,n,r))}__computeDayTabIndex(e,t){return ee(e,t)?"0":"-1"}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Al extends Tl(T(I(A(E)))){static get is(){return"vaadin-month-calendar"}static get styles(){return kl}render(){const i=this.__computeWeekDayNames(this.i18n,this.showWeekNumbers),e=this._weeks,t=!this.__computeShowWeekSeparator(this.showWeekNumbers,this.i18n);return y`
      <div part="month-header" id="month-header" aria-hidden="true">${this._getTitle(this.month,this.i18n)}</div>
      <table
        id="monthGrid"
        role="grid"
        aria-labelledby="month-header"
        @touchend="${this._preventDefault}"
        @touchstart="${this._onMonthGridTouchStart}"
      >
        <thead id="weekdays-container">
          <tr role="row" part="weekdays">
            <th part="weekday" aria-hidden="true" ?hidden="${t}"></th>
            ${i.map(n=>y`
                <th role="columnheader" part="weekday" scope="col" abbr="${n.weekDay}" aria-hidden="true">
                  ${n.weekDayShort}
                </th>
              `)}
          </tr>
        </thead>
        <tbody id="days-container">
          ${e.map(n=>y`
              <tr role="row">
                <td part="week-number" aria-hidden="true" ?hidden="${t}">
                  ${this.__computeWeekNumber(n)}
                </td>
                ${n.map(r=>y`
                    <td
                      role="gridcell"
                      part="${this.__computeDatePart(r,this.focusedDate,this.selectedDate,this.minDate,this.maxDate,this.isDateDisabled,this.enteredDate,this.__hasFocus)}"
                      .date="${r}"
                      ?disabled="${this.__isDayDisabled(r,this.minDate,this.maxDate,this.isDateDisabled)}"
                      tabindex="${this.__computeDayTabIndex(r,this.focusedDate)}"
                      aria-selected="${this.__computeDayAriaSelected(r,this.selectedDate)}"
                      aria-disabled="${this.__computeDayAriaDisabled(r,this.minDate,this.maxDate,this.isDateDisabled)}"
                      aria-label="${this.__computeDayAriaLabel(r)}"
                      >${this._getDate(r)}</td
                    >
                  `)}
              </tr>
            `)}
        </tbody>
      </table>
    `}}w(Al);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Dl=C`
  :host {
    display: grid;
    grid-template-areas:
      'header header'
      'months years'
      'toolbar years';
    grid-template-columns: minmax(0, 1fr) 0;
    height: 100%;
    outline: none;
    overflow: hidden;
  }

  :host([desktop]) {
    grid-template-columns: minmax(0, 1fr) auto;
  }

  :host([fullscreen][years-visible]) {
    grid-template-columns: minmax(0, 1fr) auto;
  }

  [part='years-toggle-button'] {
    display: inline-flex;
    align-items: center;
    border-radius: var(--vaadin-button-border-radius, var(--vaadin-radius-m));
    color: var(--vaadin-text-color);
    font-size: var(--vaadin-button-font-size, inherit);
    font-weight: var(--vaadin-button-font-weight, 500);
    height: var(--vaadin-button-height, auto);
    line-height: var(--vaadin-button-line-height, inherit);
    padding: var(--vaadin-button-padding, var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container));
    cursor: var(--vaadin-clickable-cursor);
  }

  :host([years-visible]) [part='years-toggle-button'] {
    background: var(--vaadin-text-color);
    color: var(--vaadin-background-color);
  }

  [hidden] {
    display: none !important;
  }

  ::slotted([slot='months']) {
    --vaadin-infinite-scroller-item-height: calc(
      16.5rem + var(--_vaadin-date-picker-week-numbers-visible, 0) *
        (var(--vaadin-date-picker-week-number-font-size, 0.7rem) * 1.25 * 6)
    );
  }

  :host([desktop]) ::slotted([slot='months']) {
    border-bottom: 1px solid var(--vaadin-border-color-secondary);
  }

  ::slotted([slot='years']) {
    visibility: hidden;
    background: var(--vaadin-date-picker-year-scroller-background, var(--vaadin-background-container));
    width: var(--vaadin-date-picker-year-scroller-width, 3rem);
    box-sizing: border-box;
    border-inline-start: 1px solid
      var(--vaadin-date-picker-year-scroller-border-color, var(--vaadin-border-color-secondary));
    overflow: visible;
    min-height: 0;
    clip-path: inset(0);
  }

  ::slotted([slot='years'])::before {
    background: var(--vaadin-overlay-background, var(--vaadin-background-color));
    border: 1px solid var(--vaadin-date-picker-year-scroller-border-color, var(--vaadin-border-color-secondary));
    width: 16px;
    height: 16px;
    position: absolute;
    left: auto;
    z-index: 1;
    rotate: 45deg;
    translate: calc(-50% - 1px) -50%;
    transform: none;
  }

  :host([dir='rtl']) ::slotted([slot='years'])::before {
    translate: calc(50% + 1px) -50%;
  }

  :host([desktop]) ::slotted([slot='years']),
  :host([years-visible]) ::slotted([slot='years']) {
    visibility: visible;
  }

  [part='toolbar'] {
    display: flex;
    grid-area: toolbar;
    justify-content: space-between;
    padding: var(--vaadin-date-picker-toolbar-padding, var(--vaadin-padding-s));
  }

  :host([fullscreen]) [part='toolbar'] {
    grid-area: header;
    border-bottom: 1px solid var(--vaadin-border-color-secondary);
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Jt{constructor(i,e){this.query=i,this.callback=e,this._boundQueryHandler=this._queryHandler.bind(this)}hostConnected(){this._removeListener(),this._mediaQuery=window.matchMedia(this.query),this._addListener(),this._queryHandler(this._mediaQuery)}hostDisconnected(){this._removeListener()}_addListener(){this._mediaQuery&&this._mediaQuery.addListener(this._boundQueryHandler)}_removeListener(){this._mediaQuery&&this._mediaQuery.removeListener(this._boundQueryHandler),this._mediaQuery=null}_queryHandler(i){typeof this.callback=="function"&&this.callback(i.matches)}}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ol=s=>class extends s{static get properties(){return{scrollDuration:{type:Number,value:300},selectedDate:{type:Object,value:null,sync:!0},focusedDate:{type:Object,notify:!0,observer:"_focusedDateChanged",sync:!0},_focusedMonthDate:Number,initialPosition:{type:Object,observer:"_initialPositionChanged",sync:!0},_originDate:{type:Object,value:new Date},_visibleMonthIndex:Number,_desktopMode:{type:Boolean,observer:"_desktopModeChanged"},_desktopMediaQuery:{type:String,value:"(min-width: 375px)"},i18n:{type:Object},showWeekNumbers:{type:Boolean,value:!1},_ignoreTaps:Boolean,_notTapping:Boolean,minDate:{type:Object,sync:!0},maxDate:{type:Object,sync:!0},isDateDisabled:{type:Function},enteredDate:{type:Date,sync:!0},label:String,_cancelButton:{type:Object},_todayButton:{type:Object},calendars:{type:Array,value:()=>[]},years:{type:Array,value:()=>[]}}}static get observers(){return["__updateCalendars(calendars, i18n, minDate, maxDate, selectedDate, focusedDate, showWeekNumbers, _ignoreTaps, _theme, isDateDisabled, enteredDate)","__updateCancelButton(_cancelButton, i18n)","__updateTodayButton(_todayButton, i18n, minDate, maxDate, isDateDisabled)","__updateYears(years, selectedDate, _theme)"]}get __useSubMonthScrolling(){return this._monthScroller.clientHeight<this._monthScroller.itemHeight+this._monthScroller.bufferOffset}get focusableDateElement(){return this.calendars.map(e=>e.focusableDateElement).find(Boolean)}_initControllers(){this.addController(new Jt(this._desktopMediaQuery,e=>{this._desktopMode=e})),this.addController(new G(this,"today-button","vaadin-button",{observe:!1,initializer:e=>{e.setAttribute("theme","tertiary"),e.addEventListener("keydown",t=>this.__onTodayButtonKeyDown(t)),e.addEventListener("click",this._onTodayTap.bind(this)),this._todayButton=e}})),this.addController(new G(this,"cancel-button","vaadin-button",{observe:!1,initializer:e=>{e.setAttribute("theme","tertiary"),e.addEventListener("keydown",t=>this.__onCancelButtonKeyDown(t)),e.addEventListener("click",this._cancel.bind(this)),this._cancelButton=e}})),this.__initMonthScroller(),this.__initYearScroller()}reset(){this._closeYearScroller()}focusCancel(){this._cancelButton.focus()}scrollToDate(e,t){const n=this.__useSubMonthScrolling?this._calculateWeekScrollOffset(e):0;this._scrollToPosition(this._differenceInMonths(e,this._originDate)+n,t),this._monthScroller.forceUpdate()}__initMonthScroller(){this.addController(new G(this,"months","vaadin-date-picker-month-scroller",{observe:!1,initializer:e=>{e.addEventListener("custom-scroll",()=>{this._onMonthScroll()}),e.addEventListener("touchstart",()=>{this._onMonthScrollTouchStart()}),e.addEventListener("keydown",t=>{this.__onMonthCalendarKeyDown(t)}),e.addEventListener("init-done",()=>{const t=[...this.querySelectorAll("vaadin-month-calendar")];t.forEach(n=>{n.addEventListener("selected-date-changed",r=>{this.selectedDate=r.detail.value})}),this.calendars=t}),this._monthScroller=e}}))}__initYearScroller(){this.addController(new G(this,"years","vaadin-date-picker-year-scroller",{observe:!1,initializer:e=>{e.setAttribute("aria-hidden","true"),pe(e,"tap",t=>{this._onYearTap(t)}),e.addEventListener("custom-scroll",()=>{this._onYearScroll()}),e.addEventListener("touchstart",()=>{this._onYearScrollTouchStart()}),e.addEventListener("init-done",()=>{this.years=[...this.querySelectorAll("vaadin-date-picker-year")]}),this._yearScroller=e}}))}__updateCancelButton(e,t){e&&(e.textContent=t&&t.cancel)}__updateTodayButton(e,t,n,r,o){e&&(e.textContent=t&&t.today,e.disabled=!this._isTodayAllowed(n,r,o))}__updateCalendars(e,t,n,r,o,a,l,d,h,c,f){e&&e.length&&e.forEach(m=>{m.i18n=t,m.minDate=n,m.maxDate=r,m.isDateDisabled=c,m.focusedDate=a,m.selectedDate=o,m.showWeekNumbers=l,m.ignoreTaps=d,m.enteredDate=f,h?m.setAttribute("theme",h):m.removeAttribute("theme")})}__updateYears(e,t,n){e&&e.length&&e.forEach(r=>{r.selectedDate=t,n?r.setAttribute("theme",n):r.removeAttribute("theme")})}_selectDate(e){return this._dateAllowed(e)?(this.selectedDate=e,this.dispatchEvent(new CustomEvent("date-selected",{detail:{date:e},bubbles:!0,composed:!0})),!0):!1}_desktopModeChanged(e){this.toggleAttribute("desktop",e)}_focusedDateChanged(e){this.revealDate(e)}revealDate(e,t=!0){if(!e)return;const n=this._differenceInMonths(e,this._originDate);if(this.__useSubMonthScrolling){const d=this._calculateWeekScrollOffset(e);this._scrollToPosition(n+d,t);return}const r=this._monthScroller.position>n,a=Math.max(this._monthScroller.itemHeight,this._monthScroller.clientHeight-this._monthScroller.bufferOffset*2)/this._monthScroller.itemHeight,l=this._monthScroller.position+a-1<n;r?this._scrollToPosition(n,t):l&&this._scrollToPosition(n-a+1,t)}_calculateWeekScrollOffset(e){const t=new Date(0,0);t.setFullYear(e.getFullYear()),t.setMonth(e.getMonth()),t.setDate(1);let n=0;for(;t.getDate()<e.getDate();)t.setDate(t.getDate()+1),t.getDay()===this.i18n.firstDayOfWeek&&(n+=1);return n/6}_initialPositionChanged(e){this._monthScroller&&this._yearScroller&&(this._monthScroller.active=!0,this._yearScroller.active=!0),this.scrollToDate(e)}_repositionYearScroller(){const e=this._monthScroller.position;this._visibleMonthIndex=Math.floor(e),this._yearScroller.position=(e+this._originDate.getMonth())/12}_repositionMonthScroller(){this._monthScroller.position=this._yearScroller.position*12-this._originDate.getMonth(),this._visibleMonthIndex=Math.floor(this._monthScroller.position)}_onMonthScroll(){this._repositionYearScroller(),this._doIgnoreTaps()}_onYearScroll(){this._repositionMonthScroller(),this._doIgnoreTaps()}_onYearScrollTouchStart(){this._notTapping=!1,setTimeout(()=>{this._notTapping=!0},300),this._repositionMonthScroller()}_onMonthScrollTouchStart(){this._repositionYearScroller()}_doIgnoreTaps(){this._ignoreTaps=!0,this._debouncer=D.debounce(this._debouncer,K.after(300),()=>{this._ignoreTaps=!1})}_onTodayTap(){const e=this._getTodayMidnight();Math.abs(this._monthScroller.position-this._differenceInMonths(e,this._originDate))<.001?(this._selectDate(e),this._close()):this._scrollToCurrentMonth()}_scrollToCurrentMonth(){this.focusedDate&&(this.focusedDate=new Date),this.scrollToDate(new Date,!0)}_onYearTap(e){if(!this._ignoreTaps&&!this._notTapping){const n=(e.detail.y-(this._yearScroller.getBoundingClientRect().top+this._yearScroller.clientHeight/2))/this._yearScroller.itemHeight;this._scrollToPosition(this._monthScroller.position+n*12,!0)}}_scrollToPosition(e,t){if(this._targetPosition!==void 0){this._targetPosition=e;return}if(!t){this._monthScroller.position=e,this._monthScroller.forceUpdate(),this._targetPosition=void 0,this._repositionYearScroller(),this.__tryFocusDate();return}this._targetPosition=e;let n;this._revealPromise=new Promise(d=>{n=d});const r=(d,h,c,f)=>(d/=f/2,d<1?c/2*d*d+h:(d-=1,-c/2*(d*(d-2)-1)+h));let o=0;const a=this._monthScroller.position,l=d=>{o||(o=d);const h=d-o;if(h<this.scrollDuration){const c=r(h,a,this._targetPosition-a,this.scrollDuration);this._monthScroller.position=c,window.requestAnimationFrame(l)}else this.dispatchEvent(new CustomEvent("scroll-animation-finished",{bubbles:!0,composed:!0,detail:{position:this._targetPosition,oldPosition:a}})),this._monthScroller.position=this._targetPosition,this._monthScroller.forceUpdate(),this._targetPosition=void 0,n(),this._revealPromise=void 0;setTimeout(this._repositionYearScroller.bind(this),1)};window.requestAnimationFrame(l)}_toggleYearScroller(){this.toggleAttribute("years-visible")}_closeYearScroller(){this.removeAttribute("years-visible")}_yearAfterXMonths(e){return Wn(e).getFullYear()}_differenceInMonths(e,t){return(e.getFullYear()-t.getFullYear())*12-t.getMonth()+e.getMonth()}_clear(){this._selectDate("")}_close(){this.dispatchEvent(new CustomEvent("close",{bubbles:!0,composed:!0}))}_cancel(){this.focusedDate=this.selectedDate,this._close()}__toggleDate(e){ee(e,this.selectedDate)?(this._clear(),this.focusedDate=e):this._selectDate(e)}__onMonthCalendarKeyDown(e){let t=!1;switch(e.key){case"ArrowDown":this._moveFocusByDays(7),t=!0;break;case"ArrowUp":this._moveFocusByDays(-7),t=!0;break;case"ArrowRight":this._moveFocusByDays(this.__isRTL?-1:1),t=!0;break;case"ArrowLeft":this._moveFocusByDays(this.__isRTL?1:-1),t=!0;break;case"Enter":this._selectDate(this.focusedDate)&&(this._close(),t=!0);break;case" ":this.__toggleDate(this.focusedDate),t=!0;break;case"Home":this._moveFocusInsideMonth(this.focusedDate,"minDate"),t=!0;break;case"End":this._moveFocusInsideMonth(this.focusedDate,"maxDate"),t=!0;break;case"PageDown":this._moveFocusByMonths(e.shiftKey?12:1),t=!0;break;case"PageUp":this._moveFocusByMonths(e.shiftKey?-12:-1),t=!0;break;case"Tab":this._onTabKeyDown(e,"calendar");break}t&&(e.preventDefault(),e.stopPropagation())}_onTabKeyDown(e,t){switch(e.stopPropagation(),t){case"calendar":e.shiftKey&&(e.preventDefault(),this.hasAttribute("fullscreen")?this.focusCancel():this.__focusInput());break;case"today":e.shiftKey&&(e.preventDefault(),this.focusDateElement());break;case"cancel":e.shiftKey||(e.preventDefault(),this.hasAttribute("fullscreen")?this.focusDateElement():this.__focusInput());break}}__onTodayButtonKeyDown(e){e.key==="Tab"&&this._onTabKeyDown(e,"today")}__onCancelButtonKeyDown(e){e.key==="Tab"&&this._onTabKeyDown(e,"cancel")}__focusInput(){this.dispatchEvent(new CustomEvent("focus-input",{bubbles:!0,composed:!0}))}__tryFocusDate(){if(this.__pendingDateFocus){const t=this.focusableDateElement;t&&ee(t.date,this.__pendingDateFocus)&&(delete this.__pendingDateFocus,t.focus())}}async focusDate(e,t){const n=e||this.selectedDate||this.initialPosition||new Date;this.focusedDate=n,t||(this._focusedMonthDate=n.getDate()),await this.focusDateElement(!1)}async focusDateElement(e=!0){this.__pendingDateFocus=this.focusedDate,this.calendars.length||await new Promise(t=>{requestAnimationFrame(()=>{setTimeout(()=>{t()})})}),e&&this.revealDate(this.focusedDate),this._revealPromise&&await this._revealPromise,this.__tryFocusDate()}_focusClosestDate(e){this.focusDate(Hn(e,[this.minDate,this.maxDate]))}_focusAllowedDate(e,t,n){this._dateAllowed(e,void 0,void 0,()=>!1)?this.focusDate(e,n):this._dateAllowed(this.focusedDate)?t>0?this.focusDate(this.maxDate):this.focusDate(this.minDate):this._focusClosestDate(this.focusedDate)}_getDateDiff(e,t){const n=new Date(0,0);return n.setFullYear(this.focusedDate.getFullYear()),n.setMonth(this.focusedDate.getMonth()+e),t&&n.setDate(this.focusedDate.getDate()+t),n}_moveFocusByDays(e){const t=this._getDateDiff(0,e);this._focusAllowedDate(t,e,!1)}_moveFocusByMonths(e){const t=this._getDateDiff(e),n=t.getMonth();this._focusedMonthDate||(this._focusedMonthDate=this.focusedDate.getDate()),t.setDate(this._focusedMonthDate),t.getMonth()!==n&&t.setDate(0),this._focusAllowedDate(t,e,!0)}_moveFocusInsideMonth(e,t){const n=new Date(0,0);n.setFullYear(e.getFullYear()),t==="minDate"?(n.setMonth(e.getMonth()),n.setDate(1)):(n.setMonth(e.getMonth()+1),n.setDate(0)),this._dateAllowed(n)?this.focusDate(n):this._dateAllowed(e)?this.focusDate(this[t]):this._focusClosestDate(e)}_dateAllowed(e,t=this.minDate,n=this.maxDate,r=this.isDateDisabled){return Ze(e,t,n,r)}_isTodayAllowed(e,t,n){return this._dateAllowed(this._getTodayMidnight(),e,t,n)}_getTodayMidnight(){const e=new Date,t=new Date(0,0);return t.setFullYear(e.getFullYear()),t.setMonth(e.getMonth()),t.setDate(e.getDate()),t}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Pl extends Ol(T(z(I(A(E))))){static get is(){return"vaadin-date-picker-overlay-content"}static get styles(){return Dl}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return y`
      <slot name="months"></slot>
      <slot name="years"></slot>

      <div role="toolbar" part="toolbar">
        <slot name="today-button"></slot>
        <div
          part="years-toggle-button"
          ?hidden="${this._desktopMode}"
          aria-hidden="true"
          @click="${this._toggleYearScroller}"
        >
          ${this._yearAfterXMonths(this._visibleMonthIndex)}
        </div>
        <slot name="cancel-button"></slot>
      </div>
    `}firstUpdated(){super.firstUpdated(),this.setAttribute("role","dialog"),this._initControllers()}}w(Pl);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ml=C`
  :host([opened]) {
    pointer-events: auto;
  }

  :host([week-numbers]) {
    --_vaadin-date-picker-week-numbers-visible: 1;
  }

  :host([dir='rtl']) [part='input-field'] {
    direction: ltr;
  }

  :host([dir='rtl']) [part='input-field'] ::slotted(input)::placeholder {
    direction: rtl;
    text-align: left;
  }

  [part~='toggle-button']::before {
    mask-image: var(--_vaadin-icon-calendar);
  }

  :host([readonly]) [part~='toggle-button'] {
    display: none;
  }
`;/**
 * @license
 * Copyright (c) 2017 Anton Korzunov
 * SPDX-License-Identifier: MIT
 */let He=new WeakMap,kt=new WeakMap,Tt={},mi=0;const Ms=s=>s&&s.nodeType===Node.ELEMENT_NODE,gi=(...s)=>{console.error(`Error: ${s.join(" ")}. Skip setting aria-hidden.`)},Rl=(s,i)=>Ms(s)?i.map(e=>{if(!Ms(e))return gi(e,"is not a valid element"),null;let t=e;for(;t&&t!==s;){if(s.contains(t))return e;t=t.getRootNode().host}return gi(e,"is not contained inside",s),null}).filter(e=>!!e):(gi(s,"is not a valid element"),[]),Ll=(s,i,e,t)=>{const n=Rl(i,Array.isArray(s)?s:[s]);Tt[e]||(Tt[e]=new WeakMap);const r=Tt[e],o=[],a=new Set,l=new Set(n),d=c=>{if(!c||a.has(c))return;a.add(c);const f=c.assignedSlot;f&&d(f),d(c.parentNode||c.host)};n.forEach(d);const h=c=>{if(!c||l.has(c))return;const f=c.shadowRoot;(f?[...c.children,...f.children]:[...c.children]).forEach(v=>{if(!["template","script","style"].includes(v.localName))if(a.has(v))h(v);else{const x=v.getAttribute(t),b=x!==null&&x!=="false",k=(He.get(v)||0)+1,u=(r.get(v)||0)+1;He.set(v,k),r.set(v,u),o.push(v),k===1&&b&&kt.set(v,!0),u===1&&v.setAttribute(e,"true"),b||v.setAttribute(t,"true")}})};return h(i),a.clear(),mi+=1,()=>{o.forEach(c=>{const f=He.get(c)-1,m=r.get(c)-1;He.set(c,f),r.set(c,m),f||(kt.has(c)?kt.delete(c):c.removeAttribute(t)),m||c.removeAttribute(e)}),mi-=1,mi||(He=new WeakMap,He=new WeakMap,kt=new WeakMap,Tt={})}},Fl=(s,i=document.body,e="data-aria-hidden")=>{const t=Array.from(Array.isArray(s)?s:[s]);return i&&t.push(...Array.from(i.querySelectorAll("[aria-live]"))),Ll(t,i,e,"aria-hidden")};/**
 * @license
 * Copyright (c) 2026 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Rs(s,...i){const e=r=>Array.isArray(r),t=r=>r&&typeof r=="object"&&!e(r),n=(r,o)=>{t(o)&&t(r)&&Object.keys(o).forEach(a=>{const l=o[a];t(l)?(r[a]||(r[a]={}),n(r[a],l)):e(l)?r[a]=[...l]:l!=null&&(r[a]=l)})};return i.forEach(r=>{n(s,r)}),s}const ei=(s,i)=>class extends i{static get properties(){return{i18n:{type:Object},__effectiveI18n:{type:Object,sync:!0}}}constructor(){super(),this.i18n=Rs({},s)}get i18n(){return this.__customI18n}set i18n(t){t!==this.__customI18n&&(this.__customI18n=t,this.__effectiveI18n=Rs({},s,this.__customI18n))}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Gn{constructor(i){this.host=i,i.addEventListener("opened-changed",()=>{i.opened||this.__setVirtualKeyboardEnabled(!1)}),i.addEventListener("blur",()=>this.__setVirtualKeyboardEnabled(!0)),i.addEventListener("touchstart",()=>this.__setVirtualKeyboardEnabled(!0))}__setVirtualKeyboardEnabled(i){this.host.inputElement&&(this.host.inputElement.inputMode=i?"":"none")}}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const $l=Object.freeze({monthNames:["January","February","March","April","May","June","July","August","September","October","November","December"],weekdays:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],weekdaysShort:["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],firstDayOfWeek:0,today:"Today",cancel:"Cancel",referenceDate:"",formatDate(s){const i=String(s.year).replace(/\d+/u,e=>"0000".substr(e.length)+e);return[s.month+1,s.day,i].join("/")},parseDate(s){const i=s.split("/"),e=new Date;let t,n=e.getMonth(),r=e.getFullYear();if(i.length===3){if(n=parseInt(i[0])-1,t=parseInt(i[1]),r=parseInt(i[2]),i[2].length<3&&r>=0){const o=this.referenceDate?Fe(this.referenceDate):new Date;r=yl(o,r,n,t)}}else i.length===2?(n=parseInt(i[0])-1,t=parseInt(i[1])):i.length===1&&(t=parseInt(i[0]));if(t!==void 0)return{day:t,month:n,year:r}},formatTitle:(s,i)=>`${s} ${i}`}),zl=s=>class extends ei($l,bt(ji(De(s)))){static get properties(){return{_selectedDate:{type:Object,sync:!0},_focusedDate:{type:Object,sync:!0},value:{type:String,notify:!0,value:"",sync:!0},initialPosition:String,opened:{type:Boolean,reflectToAttribute:!0,notify:!0,observer:"_openedChanged",sync:!0},autoOpenDisabled:{type:Boolean,sync:!0},showWeekNumbers:{type:Boolean,value:!1,sync:!0},_fullscreen:{type:Boolean,value:!1,sync:!0},_fullscreenMediaQuery:{value:"(max-width: 450px), (max-height: 450px)"},min:{type:String,sync:!0},max:{type:String,sync:!0},isDateDisabled:{type:Function},_minDate:{type:Date,computed:"__computeMinOrMaxDate(min)"},_maxDate:{type:Date,computed:"__computeMinOrMaxDate(max)"},_noInput:{type:Boolean,computed:"_isNoInput(inputElement, _fullscreen, _ios, __effectiveI18n, opened, autoOpenDisabled)"},_ios:{type:Boolean,value:ze},_focusOverlayOnOpen:Boolean,_overlayContent:{type:Object,sync:!0},__enteredDate:{type:Date,sync:!0}}}static get observers(){return["_selectedDateChanged(_selectedDate, __effectiveI18n)","_focusedDateChanged(_focusedDate, __effectiveI18n)","__updateOverlayContent(_overlayContent, __effectiveI18n, label, _minDate, _maxDate, _focusedDate, _selectedDate, showWeekNumbers, isDateDisabled, __enteredDate)","__updateOverlayContentTheme(_overlayContent, _theme)","__updateOverlayContentFullScreen(_overlayContent, _fullscreen)"]}static get constraints(){return[...super.constraints,"min","max"]}constructor(){super(),this._boundOnClick=this._onClick.bind(this),this._boundOnScroll=this._onScroll.bind(this)}get i18n(){return super.i18n}set i18n(e){super.i18n=e}get _inputElementValue(){return super._inputElementValue}set _inputElementValue(e){super._inputElementValue=e;const t=this.__parseDate(e);this.__setEnteredDate(t)}get __unparsableValue(){return!this._inputElementValue||this.__parseDate(this._inputElementValue)?"":this._inputElementValue}_onFocus(e){super._onFocus(e),this._noInput&&!Q()&&e.target.blur()}_onBlur(e){super._onBlur(e),this.opened||(this.__commitParsedOrFocusedDate(),document.hasFocus()&&this._requestValidation())}ready(){super.ready(),this.addEventListener("click",this._boundOnClick),this.addController(new Jt(this._fullscreenMediaQuery,e=>{this._fullscreen=e})),this.addController(new Gn(this)),this._overlayElement=this.$.overlay}updated(e){super.updated(e),(e.has("showWeekNumbers")||e.has("__effectiveI18n"))&&this.toggleAttribute("week-numbers",this.showWeekNumbers&&this.__effectiveI18n.firstDayOfWeek===1)}disconnectedCallback(){super.disconnectedCallback(),this.opened=!1}focus(e){this._noInput&&!Q()?this.open():super.focus(e)}open(){!this.disabled&&!this.readonly&&(this.opened=!0)}close(){this.$.overlay.close()}__ensureContent(){if(this._overlayContent)return;const e=document.createElement("vaadin-date-picker-overlay-content");e.setAttribute("slot","overlay"),this.appendChild(e),this._overlayContent=e,e.addEventListener("close",()=>{this._close()}),e.addEventListener("focus-input",this._focusAndSelect.bind(this)),e.addEventListener("date-tap",t=>{this.__commitDate(t.detail.date),this._close()}),e.addEventListener("date-selected",t=>{this.__commitDate(t.detail.date)}),e.addEventListener("focusin",()=>{this._keyboardActive&&this._setFocused(!0)}),e.addEventListener("focusout",t=>{this._shouldRemoveFocus(t)&&this._setFocused(!1)}),e.addEventListener("focused-date-changed",t=>{this._focusedDate=t.detail.value}),e.addEventListener("click",t=>t.stopPropagation())}__parseDate(e){if(!this.__effectiveI18n.parseDate)return;let t=this.__effectiveI18n.parseDate(e);if(t&&(t=Fe(`${t.year}-${t.month+1}-${t.day}`)),t&&!isNaN(t.getTime()))return t}__formatDate(e){if(this.__effectiveI18n.formatDate)return this.__effectiveI18n.formatDate(Ji(e))}checkValidity(){const e=this._inputElementValue,t=!e||!!this._selectedDate&&e===this.__formatDate(this._selectedDate),n=!this._selectedDate||Ze(this._selectedDate,this._minDate,this._maxDate,this.isDateDisabled);let r=!0;return this.inputElement&&this.inputElement.checkValidity&&(r=this.inputElement.checkValidity()),t&&n&&r}_shouldSetFocus(e){return!this._shouldKeepFocusRing}_shouldKeepFocusOnClearMousedown(){return this.opened?!0:super._shouldKeepFocusOnClearMousedown()}_shouldRemoveFocus(e){const{relatedTarget:t}=e;return this.opened&&t!==null&&t!==document.body&&!this.contains(t)&&!this._overlayContent.contains(t)?!0:!this.opened}_setFocused(e){super._setFocused(e),this._shouldKeepFocusRing=e&&this._keyboardActive}__commitValueChange(){const e=this.__unparsableValue;this.__committedValue!==this.value?(this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{bubbles:!0}))):this.__committedUnparsableValue!==e&&(this._requestValidation(),this.dispatchEvent(new CustomEvent("unparsable-change"))),this.__committedValue=this.value,this.__committedUnparsableValue=e}__commitDate(e){this.__keepCommittedValue=!0,this._selectedDate=e,this.__keepCommittedValue=!1,this.__commitValueChange()}_close(){this._focus(),this.close()}_isNoInput(e,t,n,r,o,a){return!e||t&&(!a||o)||n&&o||!r.parseDate}_formatISO(e){return Cl(e)}_inputElementChanged(e){super._inputElementChanged(e),e&&(e.autocomplete="off",e.setAttribute("role","combobox"),e.setAttribute("aria-haspopup","dialog"),e.setAttribute("aria-expanded",!!this.opened),this._applyInputValue(this._selectedDate))}_openedChanged(e){e&&this.__ensureContent(),this.inputElement&&this.inputElement.setAttribute("aria-expanded",e)}_selectedDateChanged(e,t){e===void 0||t===void 0||(this.__keepInputValue||this._applyInputValue(e),this.value=this._formatISO(e),this._ignoreFocusedDateChange=!0,this._focusedDate=e,this._ignoreFocusedDateChange=!1)}_focusedDateChanged(e,t){e===void 0||t===void 0||!this._ignoreFocusedDateChange&&!this._noInput&&this._applyInputValue(e)}_valueChanged(e,t){const n=Fe(e);if(e&&!n){this.value=t;return}e?ee(this._selectedDate,n)||(this._selectedDate=n,t!==void 0&&this._requestValidation()):this._selectedDate=null,this.__keepCommittedValue||(this.__committedValue=this.value,this.__committedUnparsableValue=""),this._toggleHasValue(this._hasValue)}__updateOverlayContent(e,t,n,r,o,a,l,d,h,c){e&&(e.i18n=t,e.label=n,e.minDate=r,e.maxDate=o,e.focusedDate=a,e.selectedDate=l,e.showWeekNumbers=d,e.isDateDisabled=h,e.enteredDate=c)}__updateOverlayContentTheme(e,t){e&&(t?e.setAttribute("theme",t):e.removeAttribute("theme"))}__updateOverlayContentFullScreen(e,t){e&&e.toggleAttribute("fullscreen",t)}_onOverlayEscapePress(e){e.stopPropagation(),this._focusedDate=this._selectedDate,this._applyInputValue(this._selectedDate),this._close()}_onOverlayOpened(){const e=this._overlayContent;e.reset();const t=this._getInitialPosition();e.initialPosition=t;const n=e.focusedDate||t;e.scrollToDate(n),this._ignoreFocusedDateChange=!0,e.focusedDate=n,this._ignoreFocusedDateChange=!1,window.addEventListener("scroll",this._boundOnScroll,!0),this._focusOverlayOnOpen?(e.focusDateElement(),this._focusOverlayOnOpen=!1):this._focus();const r=this.inputElement;this._noInput&&r&&(r.blur(),this._overlayContent.focusDateElement());const o=this._noInput?e:this;this.__showOthers=Fl(o)}_getInitialPosition(){const e=Fe(this.initialPosition),t=this._selectedDate||this._overlayContent.initialPosition||e||new Date;return e||Ze(t,this._minDate,this._maxDate,this.isDateDisabled)?t:this._minDate||this._maxDate?Hn(t,[this._minDate,this._maxDate]):new Date}__commitParsedOrFocusedDate(){if(this._ignoreFocusedDateChange=!0,this.__effectiveI18n.parseDate){const e=this._inputElementValue||"",t=this.__parseDate(e);t?this.__commitDate(t):(this.__keepInputValue=!0,this.__commitDate(null),this.__keepInputValue=!1)}else this._focusedDate&&this.__commitDate(this._focusedDate);this._ignoreFocusedDateChange=!1}_onOverlayClosed(){this.__showOthers&&(this.__showOthers(),this.__showOthers=null),window.removeEventListener("scroll",this._boundOnScroll,!0),this.__commitParsedOrFocusedDate(),this.inputElement&&this.inputElement.selectionStart&&(this.inputElement.selectionStart=this.inputElement.selectionEnd),!this.value&&!this._keyboardActive&&this._requestValidation()}_onScroll(e){(e.target===window||!this._overlayContent.contains(e.target))&&this._overlayContent._repositionYearScroller()}_focus(){this._noInput||this.inputElement.focus()}_focusAndSelect(){this._focus(),this._setSelectionRange(0,this._inputElementValue.length)}_applyInputValue(e){this._inputElementValue=e?this.__formatDate(e):""}_setSelectionRange(e,t){this.inputElement&&this.inputElement.setSelectionRange(e,t)}_onChange(e){e.stopPropagation()}_onClick(e){e.composedPath().includes(this._overlayElement)||this._isClearButton(e)||this._onHostClick(e)}_onHostClick(e){(!this.autoOpenDisabled||this._noInput)&&(e.preventDefault(),this.open())}_onClearButtonClick(e){e.preventDefault(),this.__commitDate(null)}_onKeyDown(e){switch(super._onKeyDown(e),this._noInput&&["Tab","Escape"].indexOf(e.key)===-1&&e.preventDefault(),e.key){case"ArrowDown":case"ArrowUp":e.preventDefault(),this.opened?this._overlayContent.focusDateElement():(this._focusOverlayOnOpen=!0,this.open());break;case"Tab":this.opened&&(e.preventDefault(),e.stopPropagation(),this._setSelectionRange(0,0),e.shiftKey?this._overlayContent.focusCancel():this._overlayContent.focusDateElement());break}}_onEnter(e){e.composedPath().includes(this._overlayContent)||(this.opened?this.close():this.__commitParsedOrFocusedDate())}_onEscape(e){if(this.opened){this._onOverlayEscapePress(e);return}if(this.clearButtonVisible&&this.value&&!this.readonly){e.stopPropagation(),this._onClearButtonClick(e);return}this.inputElement.value===""?this.__commitDate(null):this._applyInputValue(this._selectedDate)}_isClearButton(e){return e.composedPath()[0]===this.clearElement}_onInput(){!this.opened&&this._inputElementValue&&!this.autoOpenDisabled&&this.open();const e=this.__parseDate(this._inputElementValue||"");e&&(this._ignoreFocusedDateChange=!0,ee(e,this._focusedDate)||(this._focusedDate=e),this._ignoreFocusedDateChange=!1),this.__setEnteredDate(e)}__setEnteredDate(e){e?ee(this.__enteredDate,e)||(this.__enteredDate=e):this.__enteredDate=null}__computeMinOrMaxDate(e){return Fe(e)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Nl extends zl(Ct(T(L(I(A(E)))))){static get is(){return"vaadin-date-picker"}static get styles(){return[ke,Ml]}static get properties(){return{_positionTarget:{type:Object,sync:!0}}}get clearElement(){return this.$.clearButton}render(){return y`
      <div class="vaadin-date-picker-container">
        <div part="label">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true" @click="${this.focus}"></span>
        </div>

        <vaadin-input-container
          part="input-field"
          .readonly="${this.readonly}"
          .disabled="${this.disabled}"
          .invalid="${this.invalid}"
          theme="${B(this._theme)}"
        >
          <slot name="prefix" slot="prefix"></slot>
          <slot name="input"></slot>
          <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
          <div part="field-button toggle-button" slot="suffix" aria-hidden="true" @click="${this._toggle}"></div>
        </vaadin-input-container>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>

        <slot name="tooltip"></slot>
      </div>

      <vaadin-date-picker-overlay
        id="overlay"
        .owner="${this}"
        ?fullscreen="${this._fullscreen}"
        theme="${B(this._theme)}"
        .opened="${this.opened}"
        @opened-changed="${this._onOpenedChanged}"
        @vaadin-overlay-open="${this._onOverlayOpened}"
        @vaadin-overlay-close="${this._onVaadinOverlayClose}"
        @vaadin-overlay-closing="${this._onOverlayClosed}"
        restore-focus-on-close
        no-vertical-overlap
        exportparts="backdrop, overlay, content"
        .restoreFocusNode="${this.inputElement}"
        .positionTarget="${this._positionTarget}"
      >
        <slot name="overlay"></slot>
      </vaadin-date-picker-overlay>
    `}ready(){super.ready(),this.addController(new Te(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e},{uniqueIdPrefix:"search-input"})),this.addController(new ve(this.inputElement,this._labelController)),this._tooltipController=new X(this),this.addController(this._tooltipController),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this._tooltipController.setShouldShow(e=>!e.opened),this._positionTarget=this.shadowRoot.querySelector('[part="input-field"]'),this.shadowRoot.querySelector('[part="field-button toggle-button"]').addEventListener("mousedown",e=>e.preventDefault())}_onOpenedChanged(i){this.opened=i.detail.value}_onVaadinOverlayClose(i){const e=i.detail.sourceEvent;e&&e.composedPath().includes(this)&&!e.composedPath().includes(this._overlayElement)&&i.preventDefault()}_toggle(i){i.stopPropagation(),this.$.overlay.opened?this.close():this.open()}}w(Nl);const Bl={lessThanXSeconds:{one:"less than a second",other:"less than {{count}} seconds"},xSeconds:{one:"1 second",other:"{{count}} seconds"},halfAMinute:"half a minute",lessThanXMinutes:{one:"less than a minute",other:"less than {{count}} minutes"},xMinutes:{one:"1 minute",other:"{{count}} minutes"},aboutXHours:{one:"about 1 hour",other:"about {{count}} hours"},xHours:{one:"1 hour",other:"{{count}} hours"},xDays:{one:"1 day",other:"{{count}} days"},aboutXWeeks:{one:"about 1 week",other:"about {{count}} weeks"},xWeeks:{one:"1 week",other:"{{count}} weeks"},aboutXMonths:{one:"about 1 month",other:"about {{count}} months"},xMonths:{one:"1 month",other:"{{count}} months"},aboutXYears:{one:"about 1 year",other:"about {{count}} years"},xYears:{one:"1 year",other:"{{count}} years"},overXYears:{one:"over 1 year",other:"over {{count}} years"},almostXYears:{one:"almost 1 year",other:"almost {{count}} years"}},Vl=(s,i,e)=>{let t;const n=Bl[s];return typeof n=="string"?t=n:i===1?t=n.one:t=n.other.replace("{{count}}",i.toString()),e?.addSuffix?e.comparison&&e.comparison>0?"in "+t:t+" ago":t};function vi(s){return(i={})=>{const e=i.width?String(i.width):s.defaultWidth;return s.formats[e]||s.formats[s.defaultWidth]}}const Hl={full:"EEEE, MMMM do, y",long:"MMMM do, y",medium:"MMM d, y",short:"MM/dd/yyyy"},Wl={full:"h:mm:ss a zzzz",long:"h:mm:ss a z",medium:"h:mm:ss a",short:"h:mm a"},ql={full:"{{date}} 'at' {{time}}",long:"{{date}} 'at' {{time}}",medium:"{{date}}, {{time}}",short:"{{date}}, {{time}}"},Ul={date:vi({formats:Hl,defaultWidth:"full"}),time:vi({formats:Wl,defaultWidth:"full"}),dateTime:vi({formats:ql,defaultWidth:"full"})},Yl={lastWeek:"'last' eeee 'at' p",yesterday:"'yesterday at' p",today:"'today at' p",tomorrow:"'tomorrow at' p",nextWeek:"eeee 'at' p",other:"P"},jl=(s,i,e,t)=>Yl[s];function dt(s){return(i,e)=>{const t=e?.context?String(e.context):"standalone";let n;if(t==="formatting"&&s.formattingValues){const o=s.defaultFormattingWidth||s.defaultWidth,a=e?.width?String(e.width):o;n=s.formattingValues[a]||s.formattingValues[o]}else{const o=s.defaultWidth,a=e?.width?String(e.width):s.defaultWidth;n=s.values[a]||s.values[o]}const r=s.argumentCallback?s.argumentCallback(i):i;return n[r]}}const Gl={narrow:["B","A"],abbreviated:["BC","AD"],wide:["Before Christ","Anno Domini"]},Kl={narrow:["1","2","3","4"],abbreviated:["Q1","Q2","Q3","Q4"],wide:["1st quarter","2nd quarter","3rd quarter","4th quarter"]},Xl={narrow:["J","F","M","A","M","J","J","A","S","O","N","D"],abbreviated:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],wide:["January","February","March","April","May","June","July","August","September","October","November","December"]},Ql={narrow:["S","M","T","W","T","F","S"],short:["Su","Mo","Tu","We","Th","Fr","Sa"],abbreviated:["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],wide:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]},Zl={narrow:{am:"a",pm:"p",midnight:"mi",noon:"n",morning:"morning",afternoon:"afternoon",evening:"evening",night:"night"},abbreviated:{am:"AM",pm:"PM",midnight:"midnight",noon:"noon",morning:"morning",afternoon:"afternoon",evening:"evening",night:"night"},wide:{am:"a.m.",pm:"p.m.",midnight:"midnight",noon:"noon",morning:"morning",afternoon:"afternoon",evening:"evening",night:"night"}},Jl={narrow:{am:"a",pm:"p",midnight:"mi",noon:"n",morning:"in the morning",afternoon:"in the afternoon",evening:"in the evening",night:"at night"},abbreviated:{am:"AM",pm:"PM",midnight:"midnight",noon:"noon",morning:"in the morning",afternoon:"in the afternoon",evening:"in the evening",night:"at night"},wide:{am:"a.m.",pm:"p.m.",midnight:"midnight",noon:"noon",morning:"in the morning",afternoon:"in the afternoon",evening:"in the evening",night:"at night"}},ed=(s,i)=>{const e=Number(s),t=e%100;if(t>20||t<10)switch(t%10){case 1:return e+"st";case 2:return e+"nd";case 3:return e+"rd"}return e+"th"},td={ordinalNumber:ed,era:dt({values:Gl,defaultWidth:"wide"}),quarter:dt({values:Kl,defaultWidth:"wide",argumentCallback:s=>s-1}),month:dt({values:Xl,defaultWidth:"wide"}),day:dt({values:Ql,defaultWidth:"wide"}),dayPeriod:dt({values:Zl,defaultWidth:"wide",formattingValues:Jl,defaultFormattingWidth:"wide"})};function ht(s){return(i,e={})=>{const t=e.width,n=t&&s.matchPatterns[t]||s.matchPatterns[s.defaultMatchWidth],r=i.match(n);if(!r)return null;const o=r[0],a=t&&s.parsePatterns[t]||s.parsePatterns[s.defaultParseWidth],l=Array.isArray(a)?sd(a,c=>c.test(o)):id(a,c=>c.test(o));let d;d=s.valueCallback?s.valueCallback(l):l,d=e.valueCallback?e.valueCallback(d):d;const h=i.slice(o.length);return{value:d,rest:h}}}function id(s,i){for(const e in s)if(Object.prototype.hasOwnProperty.call(s,e)&&i(s[e]))return e}function sd(s,i){for(let e=0;e<s.length;e++)if(i(s[e]))return e}function nd(s){return(i,e={})=>{const t=i.match(s.matchPattern);if(!t)return null;const n=t[0],r=i.match(s.parsePattern);if(!r)return null;let o=s.valueCallback?s.valueCallback(r[0]):r[0];o=e.valueCallback?e.valueCallback(o):o;const a=i.slice(n.length);return{value:o,rest:a}}}const rd=/^(\d+)(th|st|nd|rd)?/i,od=/\d+/i,ad={narrow:/^(b|a)/i,abbreviated:/^(b\.?\s?c\.?|b\.?\s?c\.?\s?e\.?|a\.?\s?d\.?|c\.?\s?e\.?)/i,wide:/^(before christ|before common era|anno domini|common era)/i},ld={any:[/^b/i,/^(a|c)/i]},dd={narrow:/^[1234]/i,abbreviated:/^q[1234]/i,wide:/^[1234](th|st|nd|rd)? quarter/i},hd={any:[/1/i,/2/i,/3/i,/4/i]},cd={narrow:/^[jfmasond]/i,abbreviated:/^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)/i,wide:/^(january|february|march|april|may|june|july|august|september|october|november|december)/i},ud={narrow:[/^j/i,/^f/i,/^m/i,/^a/i,/^m/i,/^j/i,/^j/i,/^a/i,/^s/i,/^o/i,/^n/i,/^d/i],any:[/^ja/i,/^f/i,/^mar/i,/^ap/i,/^may/i,/^jun/i,/^jul/i,/^au/i,/^s/i,/^o/i,/^n/i,/^d/i]},_d={narrow:/^[smtwf]/i,short:/^(su|mo|tu|we|th|fr|sa)/i,abbreviated:/^(sun|mon|tue|wed|thu|fri|sat)/i,wide:/^(sunday|monday|tuesday|wednesday|thursday|friday|saturday)/i},pd={narrow:[/^s/i,/^m/i,/^t/i,/^w/i,/^t/i,/^f/i,/^s/i],any:[/^su/i,/^m/i,/^tu/i,/^w/i,/^th/i,/^f/i,/^sa/i]},fd={narrow:/^(a|p|mi|n|(in the|at) (morning|afternoon|evening|night))/i,any:/^([ap]\.?\s?m\.?|midnight|noon|(in the|at) (morning|afternoon|evening|night))/i},md={any:{am:/^a/i,pm:/^p/i,midnight:/^mi/i,noon:/^no/i,morning:/morning/i,afternoon:/afternoon/i,evening:/evening/i,night:/night/i}},gd={ordinalNumber:nd({matchPattern:rd,parsePattern:od,valueCallback:s=>parseInt(s,10)}),era:ht({matchPatterns:ad,defaultMatchWidth:"wide",parsePatterns:ld,defaultParseWidth:"any"}),quarter:ht({matchPatterns:dd,defaultMatchWidth:"wide",parsePatterns:hd,defaultParseWidth:"any",valueCallback:s=>s+1}),month:ht({matchPatterns:cd,defaultMatchWidth:"wide",parsePatterns:ud,defaultParseWidth:"any"}),day:ht({matchPatterns:_d,defaultMatchWidth:"wide",parsePatterns:pd,defaultParseWidth:"any"}),dayPeriod:ht({matchPatterns:fd,defaultMatchWidth:"any",parsePatterns:md,defaultParseWidth:"any"})},Kn={code:"en-US",formatDistance:Vl,formatLong:Ul,formatRelative:jl,localize:td,match:gd,options:{weekStartsOn:0,firstWeekContainsDate:1}};let vd={};function nt(){return vd}const Xn=6048e5,bd=864e5,yd=6e4,wd=36e5,Cd=1e3,Ls=Symbol.for("constructDateFrom");function Y(s,i){return typeof s=="function"?s(i):s&&typeof s=="object"&&Ls in s?s[Ls](i):s instanceof Date?new s.constructor(i):new Date(i)}function q(s,i){return Y(i||s,s)}function Bt(s){const i=q(s),e=new Date(Date.UTC(i.getFullYear(),i.getMonth(),i.getDate(),i.getHours(),i.getMinutes(),i.getSeconds(),i.getMilliseconds()));return e.setUTCFullYear(i.getFullYear()),+s-+e}function xd(s,...i){const e=Y.bind(null,i.find(t=>typeof t=="object"));return i.map(e)}function Fs(s,i){const e=q(s,i?.in);return e.setHours(0,0,0,0),e}function Ed(s,i,e){const[t,n]=xd(e?.in,s,i),r=Fs(t),o=Fs(n),a=+r-Bt(r),l=+o-Bt(o);return Math.round((a-l)/bd)}function Id(s,i){const e=q(s,i?.in);return e.setFullYear(e.getFullYear(),0,1),e.setHours(0,0,0,0),e}function Sd(s,i){const e=q(s,i?.in);return Ed(e,Id(e))+1}function Ie(s,i){const e=nt(),t=i?.weekStartsOn??i?.locale?.options?.weekStartsOn??e.weekStartsOn??e.locale?.options?.weekStartsOn??0,n=q(s,i?.in),r=n.getDay(),o=(r<t?7:0)+r-t;return n.setDate(n.getDate()-o),n.setHours(0,0,0,0),n}function tt(s,i){return Ie(s,{...i,weekStartsOn:1})}function Qn(s,i){const e=q(s,i?.in),t=e.getFullYear(),n=Y(e,0);n.setFullYear(t+1,0,4),n.setHours(0,0,0,0);const r=tt(n),o=Y(e,0);o.setFullYear(t,0,4),o.setHours(0,0,0,0);const a=tt(o);return e.getTime()>=r.getTime()?t+1:e.getTime()>=a.getTime()?t:t-1}function kd(s,i){const e=Qn(s,i),t=Y(s,0);return t.setFullYear(e,0,4),t.setHours(0,0,0,0),tt(t)}function Zn(s,i){const e=q(s,i?.in),t=+tt(e)-+kd(e);return Math.round(t/Xn)+1}function es(s,i){const e=q(s,i?.in),t=e.getFullYear(),n=nt(),r=i?.firstWeekContainsDate??i?.locale?.options?.firstWeekContainsDate??n.firstWeekContainsDate??n.locale?.options?.firstWeekContainsDate??1,o=Y(i?.in||s,0);o.setFullYear(t+1,0,r),o.setHours(0,0,0,0);const a=Ie(o,i),l=Y(i?.in||s,0);l.setFullYear(t,0,r),l.setHours(0,0,0,0);const d=Ie(l,i);return+e>=+a?t+1:+e>=+d?t:t-1}function Td(s,i){const e=nt(),t=i?.firstWeekContainsDate??i?.locale?.options?.firstWeekContainsDate??e.firstWeekContainsDate??e.locale?.options?.firstWeekContainsDate??1,n=es(s,i),r=Y(i?.in||s,0);return r.setFullYear(n,0,t),r.setHours(0,0,0,0),Ie(r,i)}function Jn(s,i){const e=q(s,i?.in),t=+Ie(e,i)-+Td(e,i);return Math.round(t/Xn)+1}function M(s,i){const e=s<0?"-":"",t=Math.abs(s).toString().padStart(i,"0");return e+t}const be={y(s,i){const e=s.getFullYear(),t=e>0?e:1-e;return M(i==="yy"?t%100:t,i.length)},M(s,i){const e=s.getMonth();return i==="M"?String(e+1):M(e+1,2)},d(s,i){return M(s.getDate(),i.length)},a(s,i){const e=s.getHours()/12>=1?"pm":"am";switch(i){case"a":case"aa":return e.toUpperCase();case"aaa":return e;case"aaaaa":return e[0];default:return e==="am"?"a.m.":"p.m."}},h(s,i){return M(s.getHours()%12||12,i.length)},H(s,i){return M(s.getHours(),i.length)},m(s,i){return M(s.getMinutes(),i.length)},s(s,i){return M(s.getSeconds(),i.length)},S(s,i){const e=i.length,t=s.getMilliseconds(),n=Math.trunc(t*Math.pow(10,e-3));return M(n,i.length)}},We={midnight:"midnight",noon:"noon",morning:"morning",afternoon:"afternoon",evening:"evening",night:"night"},$s={G:function(s,i,e){const t=s.getFullYear()>0?1:0;switch(i){case"G":case"GG":case"GGG":return e.era(t,{width:"abbreviated"});case"GGGGG":return e.era(t,{width:"narrow"});default:return e.era(t,{width:"wide"})}},y:function(s,i,e){if(i==="yo"){const t=s.getFullYear(),n=t>0?t:1-t;return e.ordinalNumber(n,{unit:"year"})}return be.y(s,i)},Y:function(s,i,e,t){const n=es(s,t),r=n>0?n:1-n;if(i==="YY"){const o=r%100;return M(o,2)}return i==="Yo"?e.ordinalNumber(r,{unit:"year"}):M(r,i.length)},R:function(s,i){const e=Qn(s);return M(e,i.length)},u:function(s,i){const e=s.getFullYear();return M(e,i.length)},Q:function(s,i,e){const t=Math.ceil((s.getMonth()+1)/3);switch(i){case"Q":return String(t);case"QQ":return M(t,2);case"Qo":return e.ordinalNumber(t,{unit:"quarter"});case"QQQ":return e.quarter(t,{width:"abbreviated",context:"formatting"});case"QQQQQ":return e.quarter(t,{width:"narrow",context:"formatting"});default:return e.quarter(t,{width:"wide",context:"formatting"})}},q:function(s,i,e){const t=Math.ceil((s.getMonth()+1)/3);switch(i){case"q":return String(t);case"qq":return M(t,2);case"qo":return e.ordinalNumber(t,{unit:"quarter"});case"qqq":return e.quarter(t,{width:"abbreviated",context:"standalone"});case"qqqqq":return e.quarter(t,{width:"narrow",context:"standalone"});default:return e.quarter(t,{width:"wide",context:"standalone"})}},M:function(s,i,e){const t=s.getMonth();switch(i){case"M":case"MM":return be.M(s,i);case"Mo":return e.ordinalNumber(t+1,{unit:"month"});case"MMM":return e.month(t,{width:"abbreviated",context:"formatting"});case"MMMMM":return e.month(t,{width:"narrow",context:"formatting"});default:return e.month(t,{width:"wide",context:"formatting"})}},L:function(s,i,e){const t=s.getMonth();switch(i){case"L":return String(t+1);case"LL":return M(t+1,2);case"Lo":return e.ordinalNumber(t+1,{unit:"month"});case"LLL":return e.month(t,{width:"abbreviated",context:"standalone"});case"LLLLL":return e.month(t,{width:"narrow",context:"standalone"});default:return e.month(t,{width:"wide",context:"standalone"})}},w:function(s,i,e,t){const n=Jn(s,t);return i==="wo"?e.ordinalNumber(n,{unit:"week"}):M(n,i.length)},I:function(s,i,e){const t=Zn(s);return i==="Io"?e.ordinalNumber(t,{unit:"week"}):M(t,i.length)},d:function(s,i,e){return i==="do"?e.ordinalNumber(s.getDate(),{unit:"date"}):be.d(s,i)},D:function(s,i,e){const t=Sd(s);return i==="Do"?e.ordinalNumber(t,{unit:"dayOfYear"}):M(t,i.length)},E:function(s,i,e){const t=s.getDay();switch(i){case"E":case"EE":case"EEE":return e.day(t,{width:"abbreviated",context:"formatting"});case"EEEEE":return e.day(t,{width:"narrow",context:"formatting"});case"EEEEEE":return e.day(t,{width:"short",context:"formatting"});default:return e.day(t,{width:"wide",context:"formatting"})}},e:function(s,i,e,t){const n=s.getDay(),r=(n-t.weekStartsOn+8)%7||7;switch(i){case"e":return String(r);case"ee":return M(r,2);case"eo":return e.ordinalNumber(r,{unit:"day"});case"eee":return e.day(n,{width:"abbreviated",context:"formatting"});case"eeeee":return e.day(n,{width:"narrow",context:"formatting"});case"eeeeee":return e.day(n,{width:"short",context:"formatting"});default:return e.day(n,{width:"wide",context:"formatting"})}},c:function(s,i,e,t){const n=s.getDay(),r=(n-t.weekStartsOn+8)%7||7;switch(i){case"c":return String(r);case"cc":return M(r,i.length);case"co":return e.ordinalNumber(r,{unit:"day"});case"ccc":return e.day(n,{width:"abbreviated",context:"standalone"});case"ccccc":return e.day(n,{width:"narrow",context:"standalone"});case"cccccc":return e.day(n,{width:"short",context:"standalone"});default:return e.day(n,{width:"wide",context:"standalone"})}},i:function(s,i,e){const t=s.getDay(),n=t===0?7:t;switch(i){case"i":return String(n);case"ii":return M(n,i.length);case"io":return e.ordinalNumber(n,{unit:"day"});case"iii":return e.day(t,{width:"abbreviated",context:"formatting"});case"iiiii":return e.day(t,{width:"narrow",context:"formatting"});case"iiiiii":return e.day(t,{width:"short",context:"formatting"});default:return e.day(t,{width:"wide",context:"formatting"})}},a:function(s,i,e){const n=s.getHours()/12>=1?"pm":"am";switch(i){case"a":case"aa":return e.dayPeriod(n,{width:"abbreviated",context:"formatting"});case"aaa":return e.dayPeriod(n,{width:"abbreviated",context:"formatting"}).toLowerCase();case"aaaaa":return e.dayPeriod(n,{width:"narrow",context:"formatting"});default:return e.dayPeriod(n,{width:"wide",context:"formatting"})}},b:function(s,i,e){const t=s.getHours();let n;switch(t===12?n=We.noon:t===0?n=We.midnight:n=t/12>=1?"pm":"am",i){case"b":case"bb":return e.dayPeriod(n,{width:"abbreviated",context:"formatting"});case"bbb":return e.dayPeriod(n,{width:"abbreviated",context:"formatting"}).toLowerCase();case"bbbbb":return e.dayPeriod(n,{width:"narrow",context:"formatting"});default:return e.dayPeriod(n,{width:"wide",context:"formatting"})}},B:function(s,i,e){const t=s.getHours();let n;switch(t>=17?n=We.evening:t>=12?n=We.afternoon:t>=4?n=We.morning:n=We.night,i){case"B":case"BB":case"BBB":return e.dayPeriod(n,{width:"abbreviated",context:"formatting"});case"BBBBB":return e.dayPeriod(n,{width:"narrow",context:"formatting"});default:return e.dayPeriod(n,{width:"wide",context:"formatting"})}},h:function(s,i,e){if(i==="ho"){let t=s.getHours()%12;return t===0&&(t=12),e.ordinalNumber(t,{unit:"hour"})}return be.h(s,i)},H:function(s,i,e){return i==="Ho"?e.ordinalNumber(s.getHours(),{unit:"hour"}):be.H(s,i)},K:function(s,i,e){const t=s.getHours()%12;return i==="Ko"?e.ordinalNumber(t,{unit:"hour"}):M(t,i.length)},k:function(s,i,e){let t=s.getHours();return t===0&&(t=24),i==="ko"?e.ordinalNumber(t,{unit:"hour"}):M(t,i.length)},m:function(s,i,e){return i==="mo"?e.ordinalNumber(s.getMinutes(),{unit:"minute"}):be.m(s,i)},s:function(s,i,e){return i==="so"?e.ordinalNumber(s.getSeconds(),{unit:"second"}):be.s(s,i)},S:function(s,i){return be.S(s,i)},X:function(s,i,e){const t=s.getTimezoneOffset();if(t===0)return"Z";switch(i){case"X":return Ns(t);case"XXXX":case"XX":return Pe(t);default:return Pe(t,":")}},x:function(s,i,e){const t=s.getTimezoneOffset();switch(i){case"x":return Ns(t);case"xxxx":case"xx":return Pe(t);default:return Pe(t,":")}},O:function(s,i,e){const t=s.getTimezoneOffset();switch(i){case"O":case"OO":case"OOO":return"GMT"+zs(t,":");default:return"GMT"+Pe(t,":")}},z:function(s,i,e){const t=s.getTimezoneOffset();switch(i){case"z":case"zz":case"zzz":return"GMT"+zs(t,":");default:return"GMT"+Pe(t,":")}},t:function(s,i,e){const t=Math.trunc(+s/1e3);return M(t,i.length)},T:function(s,i,e){return M(+s,i.length)}};function zs(s,i=""){const e=s>0?"-":"+",t=Math.abs(s),n=Math.trunc(t/60),r=t%60;return r===0?e+String(n):e+String(n)+i+M(r,2)}function Ns(s,i){return s%60===0?(s>0?"-":"+")+M(Math.abs(s)/60,2):Pe(s,i)}function Pe(s,i=""){const e=s>0?"-":"+",t=Math.abs(s),n=M(Math.trunc(t/60),2),r=M(t%60,2);return e+n+i+r}const Bs=(s,i)=>{switch(s){case"P":return i.date({width:"short"});case"PP":return i.date({width:"medium"});case"PPP":return i.date({width:"long"});default:return i.date({width:"full"})}},er=(s,i)=>{switch(s){case"p":return i.time({width:"short"});case"pp":return i.time({width:"medium"});case"ppp":return i.time({width:"long"});default:return i.time({width:"full"})}},Ad=(s,i)=>{const e=s.match(/(P+)(p+)?/)||[],t=e[1],n=e[2];if(!n)return Bs(s,i);let r;switch(t){case"P":r=i.dateTime({width:"short"});break;case"PP":r=i.dateTime({width:"medium"});break;case"PPP":r=i.dateTime({width:"long"});break;default:r=i.dateTime({width:"full"});break}return r.replace("{{date}}",Bs(t,i)).replace("{{time}}",er(n,i))},Di={p:er,P:Ad},Dd=/^D+$/,Od=/^Y+$/,Pd=["D","DD","YY","YYYY"];function tr(s){return Dd.test(s)}function ir(s){return Od.test(s)}function Oi(s,i,e){const t=Md(s,i,e);if(console.warn(t),Pd.includes(s))throw new RangeError(t)}function Md(s,i,e){const t=s[0]==="Y"?"years":"days of the month";return`Use \`${s.toLowerCase()}\` instead of \`${s}\` (in \`${i}\`) for formatting ${t} to the input \`${e}\`; see: https://github.com/date-fns/date-fns/blob/master/docs/unicodeTokens.md`}function Rd(s){return s instanceof Date||typeof s=="object"&&Object.prototype.toString.call(s)==="[object Date]"}function Pi(s){return!(!Rd(s)&&typeof s!="number"||isNaN(+q(s)))}const Ld=/[yYQqMLwIdDecihHKkms]o|(\w)\1*|''|'(''|[^'])+('|$)|./g,Fd=/P+p+|P+|p+|''|'(''|[^'])+('|$)|./g,$d=/^'([^]*?)'?$/,zd=/''/g,Nd=/[a-zA-Z]/;function Bd(s,i,e){const t=nt(),n=t.locale??Kn,r=t.firstWeekContainsDate??t.locale?.options?.firstWeekContainsDate??1,o=t.weekStartsOn??t.locale?.options?.weekStartsOn??0,a=q(s,e?.in);if(!Pi(a))throw new RangeError("Invalid time value");let l=i.match(Fd).map(h=>{const c=h[0];if(c==="p"||c==="P"){const f=Di[c];return f(h,n.formatLong)}return h}).join("").match(Ld).map(h=>{if(h==="''")return{isToken:!1,value:"'"};const c=h[0];if(c==="'")return{isToken:!1,value:Vd(h)};if($s[c])return{isToken:!0,value:h};if(c.match(Nd))throw new RangeError("Format string contains an unescaped latin alphabet character `"+c+"`");return{isToken:!1,value:h}});n.localize.preprocessor&&(l=n.localize.preprocessor(a,l));const d={firstWeekContainsDate:r,weekStartsOn:o,locale:n};return l.map(h=>{if(!h.isToken)return h.value;const c=h.value;(ir(c)||tr(c))&&Oi(c,i,String(s));const f=$s[c[0]];return f(a,c,n.localize,d)}).join("")}function Vd(s){const i=s.match($d);return i?i[1].replace(zd,"'"):s}function Hd(){return Object.assign({},nt())}function Wd(s,i){const e=qd(i)?new i(0):Y(i,0);return e.setFullYear(s.getFullYear(),s.getMonth(),s.getDate()),e.setHours(s.getHours(),s.getMinutes(),s.getSeconds(),s.getMilliseconds()),e}function qd(s){return typeof s=="function"&&s.prototype?.constructor===s}const Ud=10;class sr{subPriority=0;validate(i,e){return!0}}class Yd extends sr{constructor(i,e,t,n,r){super(),this.value=i,this.validateValue=e,this.setValue=t,this.priority=n,r&&(this.subPriority=r)}validate(i,e){return this.validateValue(i,this.value,e)}set(i,e,t){return this.setValue(i,e,this.value,t)}}class jd extends sr{priority=Ud;subPriority=-1;constructor(i,e){super(),this.context=i||(t=>Y(e,t))}set(i,e){return e.timestampIsSet?i:Y(i,Wd(i,this.context))}}class P{run(i,e,t,n){const r=this.parse(i,e,t,n);return r?{setter:new Yd(r.value,this.validate,this.set,this.priority,this.subPriority),rest:r.rest}:null}validate(i,e,t){return!0}}class Gd extends P{priority=140;parse(i,e,t){switch(e){case"G":case"GG":case"GGG":return t.era(i,{width:"abbreviated"})||t.era(i,{width:"narrow"});case"GGGGG":return t.era(i,{width:"narrow"});default:return t.era(i,{width:"wide"})||t.era(i,{width:"abbreviated"})||t.era(i,{width:"narrow"})}}set(i,e,t){return e.era=t,i.setFullYear(t,0,1),i.setHours(0,0,0,0),i}incompatibleTokens=["R","u","t","T"]}const H={month:/^(1[0-2]|0?\d)/,date:/^(3[0-1]|[0-2]?\d)/,dayOfYear:/^(36[0-6]|3[0-5]\d|[0-2]?\d?\d)/,week:/^(5[0-3]|[0-4]?\d)/,hour23h:/^(2[0-3]|[0-1]?\d)/,hour24h:/^(2[0-4]|[0-1]?\d)/,hour11h:/^(1[0-1]|0?\d)/,hour12h:/^(1[0-2]|0?\d)/,minute:/^[0-5]?\d/,second:/^[0-5]?\d/,singleDigit:/^\d/,twoDigits:/^\d{1,2}/,threeDigits:/^\d{1,3}/,fourDigits:/^\d{1,4}/,anyDigitsSigned:/^-?\d+/,singleDigitSigned:/^-?\d/,twoDigitsSigned:/^-?\d{1,2}/,threeDigitsSigned:/^-?\d{1,3}/,fourDigitsSigned:/^-?\d{1,4}/},ne={basicOptionalMinutes:/^([+-])(\d{2})(\d{2})?|Z/,basic:/^([+-])(\d{2})(\d{2})|Z/,basicOptionalSeconds:/^([+-])(\d{2})(\d{2})((\d{2}))?|Z/,extended:/^([+-])(\d{2}):(\d{2})|Z/,extendedOptionalSeconds:/^([+-])(\d{2}):(\d{2})(:(\d{2}))?|Z/};function W(s,i){return s&&{value:i(s.value),rest:s.rest}}function N(s,i){const e=i.match(s);return e?{value:parseInt(e[0],10),rest:i.slice(e[0].length)}:null}function re(s,i){const e=i.match(s);if(!e)return null;if(e[0]==="Z")return{value:0,rest:i.slice(1)};const t=e[1]==="+"?1:-1,n=e[2]?parseInt(e[2],10):0,r=e[3]?parseInt(e[3],10):0,o=e[5]?parseInt(e[5],10):0;return{value:t*(n*wd+r*yd+o*Cd),rest:i.slice(e[0].length)}}function nr(s){return N(H.anyDigitsSigned,s)}function V(s,i){switch(s){case 1:return N(H.singleDigit,i);case 2:return N(H.twoDigits,i);case 3:return N(H.threeDigits,i);case 4:return N(H.fourDigits,i);default:return N(new RegExp("^\\d{1,"+s+"}"),i)}}function Vt(s,i){switch(s){case 1:return N(H.singleDigitSigned,i);case 2:return N(H.twoDigitsSigned,i);case 3:return N(H.threeDigitsSigned,i);case 4:return N(H.fourDigitsSigned,i);default:return N(new RegExp("^-?\\d{1,"+s+"}"),i)}}function ts(s){switch(s){case"morning":return 4;case"evening":return 17;case"pm":case"noon":case"afternoon":return 12;default:return 0}}function rr(s,i){const e=i>0,t=e?i:1-i;let n;if(t<=50)n=s||100;else{const r=t+50,o=Math.trunc(r/100)*100,a=s>=r%100;n=s+o-(a?100:0)}return e?n:1-n}function or(s){return s%400===0||s%4===0&&s%100!==0}class Kd extends P{priority=130;incompatibleTokens=["Y","R","u","w","I","i","e","c","t","T"];parse(i,e,t){const n=r=>({year:r,isTwoDigitYear:e==="yy"});switch(e){case"y":return W(V(4,i),n);case"yo":return W(t.ordinalNumber(i,{unit:"year"}),n);default:return W(V(e.length,i),n)}}validate(i,e){return e.isTwoDigitYear||e.year>0}set(i,e,t){const n=i.getFullYear();if(t.isTwoDigitYear){const o=rr(t.year,n);return i.setFullYear(o,0,1),i.setHours(0,0,0,0),i}const r=!("era"in e)||e.era===1?t.year:1-t.year;return i.setFullYear(r,0,1),i.setHours(0,0,0,0),i}}class Xd extends P{priority=130;parse(i,e,t){const n=r=>({year:r,isTwoDigitYear:e==="YY"});switch(e){case"Y":return W(V(4,i),n);case"Yo":return W(t.ordinalNumber(i,{unit:"year"}),n);default:return W(V(e.length,i),n)}}validate(i,e){return e.isTwoDigitYear||e.year>0}set(i,e,t,n){const r=es(i,n);if(t.isTwoDigitYear){const a=rr(t.year,r);return i.setFullYear(a,0,n.firstWeekContainsDate),i.setHours(0,0,0,0),Ie(i,n)}const o=!("era"in e)||e.era===1?t.year:1-t.year;return i.setFullYear(o,0,n.firstWeekContainsDate),i.setHours(0,0,0,0),Ie(i,n)}incompatibleTokens=["y","R","u","Q","q","M","L","I","d","D","i","t","T"]}class Qd extends P{priority=130;parse(i,e){return Vt(e==="R"?4:e.length,i)}set(i,e,t){const n=Y(i,0);return n.setFullYear(t,0,4),n.setHours(0,0,0,0),tt(n)}incompatibleTokens=["G","y","Y","u","Q","q","M","L","w","d","D","e","c","t","T"]}class Zd extends P{priority=130;parse(i,e){return Vt(e==="u"?4:e.length,i)}set(i,e,t){return i.setFullYear(t,0,1),i.setHours(0,0,0,0),i}incompatibleTokens=["G","y","Y","R","w","I","i","e","c","t","T"]}class Jd extends P{priority=120;parse(i,e,t){switch(e){case"Q":case"QQ":return V(e.length,i);case"Qo":return t.ordinalNumber(i,{unit:"quarter"});case"QQQ":return t.quarter(i,{width:"abbreviated",context:"formatting"})||t.quarter(i,{width:"narrow",context:"formatting"});case"QQQQQ":return t.quarter(i,{width:"narrow",context:"formatting"});default:return t.quarter(i,{width:"wide",context:"formatting"})||t.quarter(i,{width:"abbreviated",context:"formatting"})||t.quarter(i,{width:"narrow",context:"formatting"})}}validate(i,e){return e>=1&&e<=4}set(i,e,t){return i.setMonth((t-1)*3,1),i.setHours(0,0,0,0),i}incompatibleTokens=["Y","R","q","M","L","w","I","d","D","i","e","c","t","T"]}class eh extends P{priority=120;parse(i,e,t){switch(e){case"q":case"qq":return V(e.length,i);case"qo":return t.ordinalNumber(i,{unit:"quarter"});case"qqq":return t.quarter(i,{width:"abbreviated",context:"standalone"})||t.quarter(i,{width:"narrow",context:"standalone"});case"qqqqq":return t.quarter(i,{width:"narrow",context:"standalone"});default:return t.quarter(i,{width:"wide",context:"standalone"})||t.quarter(i,{width:"abbreviated",context:"standalone"})||t.quarter(i,{width:"narrow",context:"standalone"})}}validate(i,e){return e>=1&&e<=4}set(i,e,t){return i.setMonth((t-1)*3,1),i.setHours(0,0,0,0),i}incompatibleTokens=["Y","R","Q","M","L","w","I","d","D","i","e","c","t","T"]}class th extends P{incompatibleTokens=["Y","R","q","Q","L","w","I","D","i","e","c","t","T"];priority=110;parse(i,e,t){const n=r=>r-1;switch(e){case"M":return W(N(H.month,i),n);case"MM":return W(V(2,i),n);case"Mo":return W(t.ordinalNumber(i,{unit:"month"}),n);case"MMM":return t.month(i,{width:"abbreviated",context:"formatting"})||t.month(i,{width:"narrow",context:"formatting"});case"MMMMM":return t.month(i,{width:"narrow",context:"formatting"});default:return t.month(i,{width:"wide",context:"formatting"})||t.month(i,{width:"abbreviated",context:"formatting"})||t.month(i,{width:"narrow",context:"formatting"})}}validate(i,e){return e>=0&&e<=11}set(i,e,t){return i.setMonth(t,1),i.setHours(0,0,0,0),i}}class ih extends P{priority=110;parse(i,e,t){const n=r=>r-1;switch(e){case"L":return W(N(H.month,i),n);case"LL":return W(V(2,i),n);case"Lo":return W(t.ordinalNumber(i,{unit:"month"}),n);case"LLL":return t.month(i,{width:"abbreviated",context:"standalone"})||t.month(i,{width:"narrow",context:"standalone"});case"LLLLL":return t.month(i,{width:"narrow",context:"standalone"});default:return t.month(i,{width:"wide",context:"standalone"})||t.month(i,{width:"abbreviated",context:"standalone"})||t.month(i,{width:"narrow",context:"standalone"})}}validate(i,e){return e>=0&&e<=11}set(i,e,t){return i.setMonth(t,1),i.setHours(0,0,0,0),i}incompatibleTokens=["Y","R","q","Q","M","w","I","D","i","e","c","t","T"]}function sh(s,i,e){const t=q(s,e?.in),n=Jn(t,e)-i;return t.setDate(t.getDate()-n*7),q(t,e?.in)}class nh extends P{priority=100;parse(i,e,t){switch(e){case"w":return N(H.week,i);case"wo":return t.ordinalNumber(i,{unit:"week"});default:return V(e.length,i)}}validate(i,e){return e>=1&&e<=53}set(i,e,t,n){return Ie(sh(i,t,n),n)}incompatibleTokens=["y","R","u","q","Q","M","L","I","d","D","i","t","T"]}function rh(s,i,e){const t=q(s,e?.in),n=Zn(t,e)-i;return t.setDate(t.getDate()-n*7),t}class oh extends P{priority=100;parse(i,e,t){switch(e){case"I":return N(H.week,i);case"Io":return t.ordinalNumber(i,{unit:"week"});default:return V(e.length,i)}}validate(i,e){return e>=1&&e<=53}set(i,e,t){return tt(rh(i,t))}incompatibleTokens=["y","Y","u","q","Q","M","L","w","d","D","e","c","t","T"]}const ah=[31,28,31,30,31,30,31,31,30,31,30,31],lh=[31,29,31,30,31,30,31,31,30,31,30,31];class dh extends P{priority=90;subPriority=1;parse(i,e,t){switch(e){case"d":return N(H.date,i);case"do":return t.ordinalNumber(i,{unit:"date"});default:return V(e.length,i)}}validate(i,e){const t=i.getFullYear(),n=or(t),r=i.getMonth();return n?e>=1&&e<=lh[r]:e>=1&&e<=ah[r]}set(i,e,t){return i.setDate(t),i.setHours(0,0,0,0),i}incompatibleTokens=["Y","R","q","Q","w","I","D","i","e","c","t","T"]}class hh extends P{priority=90;subpriority=1;parse(i,e,t){switch(e){case"D":case"DD":return N(H.dayOfYear,i);case"Do":return t.ordinalNumber(i,{unit:"date"});default:return V(e.length,i)}}validate(i,e){const t=i.getFullYear();return or(t)?e>=1&&e<=366:e>=1&&e<=365}set(i,e,t){return i.setMonth(0,t),i.setHours(0,0,0,0),i}incompatibleTokens=["Y","R","q","Q","M","L","w","I","d","E","i","e","c","t","T"]}function ar(s,i,e){const t=q(s,e?.in);return isNaN(i)?Y(e?.in||s,NaN):(i&&t.setDate(t.getDate()+i),t)}function is(s,i,e){const t=nt(),n=e?.weekStartsOn??e?.locale?.options?.weekStartsOn??t.weekStartsOn??t.locale?.options?.weekStartsOn??0,r=q(s,e?.in),o=r.getDay(),l=(i%7+7)%7,d=7-n,h=i<0||i>6?i-(o+d)%7:(l+d)%7-(o+d)%7;return ar(r,h,e)}class ch extends P{priority=90;parse(i,e,t){switch(e){case"E":case"EE":case"EEE":return t.day(i,{width:"abbreviated",context:"formatting"})||t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"});case"EEEEE":return t.day(i,{width:"narrow",context:"formatting"});case"EEEEEE":return t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"});default:return t.day(i,{width:"wide",context:"formatting"})||t.day(i,{width:"abbreviated",context:"formatting"})||t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"})}}validate(i,e){return e>=0&&e<=6}set(i,e,t,n){return i=is(i,t,n),i.setHours(0,0,0,0),i}incompatibleTokens=["D","i","e","c","t","T"]}class uh extends P{priority=90;parse(i,e,t,n){const r=o=>{const a=Math.floor((o-1)/7)*7;return(o+n.weekStartsOn+6)%7+a};switch(e){case"e":case"ee":return W(V(e.length,i),r);case"eo":return W(t.ordinalNumber(i,{unit:"day"}),r);case"eee":return t.day(i,{width:"abbreviated",context:"formatting"})||t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"});case"eeeee":return t.day(i,{width:"narrow",context:"formatting"});case"eeeeee":return t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"});default:return t.day(i,{width:"wide",context:"formatting"})||t.day(i,{width:"abbreviated",context:"formatting"})||t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"})}}validate(i,e){return e>=0&&e<=6}set(i,e,t,n){return i=is(i,t,n),i.setHours(0,0,0,0),i}incompatibleTokens=["y","R","u","q","Q","M","L","I","d","D","E","i","c","t","T"]}class _h extends P{priority=90;parse(i,e,t,n){const r=o=>{const a=Math.floor((o-1)/7)*7;return(o+n.weekStartsOn+6)%7+a};switch(e){case"c":case"cc":return W(V(e.length,i),r);case"co":return W(t.ordinalNumber(i,{unit:"day"}),r);case"ccc":return t.day(i,{width:"abbreviated",context:"standalone"})||t.day(i,{width:"short",context:"standalone"})||t.day(i,{width:"narrow",context:"standalone"});case"ccccc":return t.day(i,{width:"narrow",context:"standalone"});case"cccccc":return t.day(i,{width:"short",context:"standalone"})||t.day(i,{width:"narrow",context:"standalone"});default:return t.day(i,{width:"wide",context:"standalone"})||t.day(i,{width:"abbreviated",context:"standalone"})||t.day(i,{width:"short",context:"standalone"})||t.day(i,{width:"narrow",context:"standalone"})}}validate(i,e){return e>=0&&e<=6}set(i,e,t,n){return i=is(i,t,n),i.setHours(0,0,0,0),i}incompatibleTokens=["y","R","u","q","Q","M","L","I","d","D","E","i","e","t","T"]}function ph(s,i){const e=q(s,i?.in).getDay();return e===0?7:e}function fh(s,i,e){const t=q(s,e?.in),n=ph(t,e),r=i-n;return ar(t,r,e)}class mh extends P{priority=90;parse(i,e,t){const n=r=>r===0?7:r;switch(e){case"i":case"ii":return V(e.length,i);case"io":return t.ordinalNumber(i,{unit:"day"});case"iii":return W(t.day(i,{width:"abbreviated",context:"formatting"})||t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"}),n);case"iiiii":return W(t.day(i,{width:"narrow",context:"formatting"}),n);case"iiiiii":return W(t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"}),n);default:return W(t.day(i,{width:"wide",context:"formatting"})||t.day(i,{width:"abbreviated",context:"formatting"})||t.day(i,{width:"short",context:"formatting"})||t.day(i,{width:"narrow",context:"formatting"}),n)}}validate(i,e){return e>=1&&e<=7}set(i,e,t){return i=fh(i,t),i.setHours(0,0,0,0),i}incompatibleTokens=["y","Y","u","q","Q","M","L","w","d","D","E","e","c","t","T"]}class gh extends P{priority=80;parse(i,e,t){switch(e){case"a":case"aa":case"aaa":return t.dayPeriod(i,{width:"abbreviated",context:"formatting"})||t.dayPeriod(i,{width:"narrow",context:"formatting"});case"aaaaa":return t.dayPeriod(i,{width:"narrow",context:"formatting"});default:return t.dayPeriod(i,{width:"wide",context:"formatting"})||t.dayPeriod(i,{width:"abbreviated",context:"formatting"})||t.dayPeriod(i,{width:"narrow",context:"formatting"})}}set(i,e,t){return i.setHours(ts(t),0,0,0),i}incompatibleTokens=["b","B","H","k","t","T"]}class vh extends P{priority=80;parse(i,e,t){switch(e){case"b":case"bb":case"bbb":return t.dayPeriod(i,{width:"abbreviated",context:"formatting"})||t.dayPeriod(i,{width:"narrow",context:"formatting"});case"bbbbb":return t.dayPeriod(i,{width:"narrow",context:"formatting"});default:return t.dayPeriod(i,{width:"wide",context:"formatting"})||t.dayPeriod(i,{width:"abbreviated",context:"formatting"})||t.dayPeriod(i,{width:"narrow",context:"formatting"})}}set(i,e,t){return i.setHours(ts(t),0,0,0),i}incompatibleTokens=["a","B","H","k","t","T"]}class bh extends P{priority=80;parse(i,e,t){switch(e){case"B":case"BB":case"BBB":return t.dayPeriod(i,{width:"abbreviated",context:"formatting"})||t.dayPeriod(i,{width:"narrow",context:"formatting"});case"BBBBB":return t.dayPeriod(i,{width:"narrow",context:"formatting"});default:return t.dayPeriod(i,{width:"wide",context:"formatting"})||t.dayPeriod(i,{width:"abbreviated",context:"formatting"})||t.dayPeriod(i,{width:"narrow",context:"formatting"})}}set(i,e,t){return i.setHours(ts(t),0,0,0),i}incompatibleTokens=["a","b","t","T"]}class yh extends P{priority=70;parse(i,e,t){switch(e){case"h":return N(H.hour12h,i);case"ho":return t.ordinalNumber(i,{unit:"hour"});default:return V(e.length,i)}}validate(i,e){return e>=1&&e<=12}set(i,e,t){const n=i.getHours()>=12;return n&&t<12?i.setHours(t+12,0,0,0):!n&&t===12?i.setHours(0,0,0,0):i.setHours(t,0,0,0),i}incompatibleTokens=["H","K","k","t","T"]}class wh extends P{priority=70;parse(i,e,t){switch(e){case"H":return N(H.hour23h,i);case"Ho":return t.ordinalNumber(i,{unit:"hour"});default:return V(e.length,i)}}validate(i,e){return e>=0&&e<=23}set(i,e,t){return i.setHours(t,0,0,0),i}incompatibleTokens=["a","b","h","K","k","t","T"]}class Ch extends P{priority=70;parse(i,e,t){switch(e){case"K":return N(H.hour11h,i);case"Ko":return t.ordinalNumber(i,{unit:"hour"});default:return V(e.length,i)}}validate(i,e){return e>=0&&e<=11}set(i,e,t){return i.getHours()>=12&&t<12?i.setHours(t+12,0,0,0):i.setHours(t,0,0,0),i}incompatibleTokens=["h","H","k","t","T"]}class xh extends P{priority=70;parse(i,e,t){switch(e){case"k":return N(H.hour24h,i);case"ko":return t.ordinalNumber(i,{unit:"hour"});default:return V(e.length,i)}}validate(i,e){return e>=1&&e<=24}set(i,e,t){const n=t<=24?t%24:t;return i.setHours(n,0,0,0),i}incompatibleTokens=["a","b","h","H","K","t","T"]}class Eh extends P{priority=60;parse(i,e,t){switch(e){case"m":return N(H.minute,i);case"mo":return t.ordinalNumber(i,{unit:"minute"});default:return V(e.length,i)}}validate(i,e){return e>=0&&e<=59}set(i,e,t){return i.setMinutes(t,0,0),i}incompatibleTokens=["t","T"]}class Ih extends P{priority=50;parse(i,e,t){switch(e){case"s":return N(H.second,i);case"so":return t.ordinalNumber(i,{unit:"second"});default:return V(e.length,i)}}validate(i,e){return e>=0&&e<=59}set(i,e,t){return i.setSeconds(t,0),i}incompatibleTokens=["t","T"]}class Sh extends P{priority=30;parse(i,e){const t=n=>Math.trunc(n*Math.pow(10,-e.length+3));return W(V(e.length,i),t)}set(i,e,t){return i.setMilliseconds(t),i}incompatibleTokens=["t","T"]}class kh extends P{priority=10;parse(i,e){switch(e){case"X":return re(ne.basicOptionalMinutes,i);case"XX":return re(ne.basic,i);case"XXXX":return re(ne.basicOptionalSeconds,i);case"XXXXX":return re(ne.extendedOptionalSeconds,i);default:return re(ne.extended,i)}}set(i,e,t){return e.timestampIsSet?i:Y(i,i.getTime()-Bt(i)-t)}incompatibleTokens=["t","T","x"]}class Th extends P{priority=10;parse(i,e){switch(e){case"x":return re(ne.basicOptionalMinutes,i);case"xx":return re(ne.basic,i);case"xxxx":return re(ne.basicOptionalSeconds,i);case"xxxxx":return re(ne.extendedOptionalSeconds,i);default:return re(ne.extended,i)}}set(i,e,t){return e.timestampIsSet?i:Y(i,i.getTime()-Bt(i)-t)}incompatibleTokens=["t","T","X"]}class Ah extends P{priority=40;parse(i){return nr(i)}set(i,e,t){return[Y(i,t*1e3),{timestampIsSet:!0}]}incompatibleTokens="*"}class Dh extends P{priority=20;parse(i){return nr(i)}set(i,e,t){return[Y(i,t),{timestampIsSet:!0}]}incompatibleTokens="*"}const Oh={G:new Gd,y:new Kd,Y:new Xd,R:new Qd,u:new Zd,Q:new Jd,q:new eh,M:new th,L:new ih,w:new nh,I:new oh,d:new dh,D:new hh,E:new ch,e:new uh,c:new _h,i:new mh,a:new gh,b:new vh,B:new bh,h:new yh,H:new wh,K:new Ch,k:new xh,m:new Eh,s:new Ih,S:new Sh,X:new kh,x:new Th,t:new Ah,T:new Dh},Ph=/[yYQqMLwIdDecihHKkms]o|(\w)\1*|''|'(''|[^'])+('|$)|./g,Mh=/P+p+|P+|p+|''|'(''|[^'])+('|$)|./g,Rh=/^'([^]*?)'?$/,Lh=/''/g,Fh=/\S/,$h=/[a-zA-Z]/;function zh(s,i,e,t){const n=()=>Y(e,NaN),r=Hd(),o=r.locale??Kn,a=r.firstWeekContainsDate??r.locale?.options?.firstWeekContainsDate??1,l=r.weekStartsOn??r.locale?.options?.weekStartsOn??0;if(!i)return s?n():q(e,t?.in);const d={firstWeekContainsDate:a,weekStartsOn:l,locale:o},h=[new jd(t?.in,e)],c=i.match(Mh).map(b=>{const k=b[0];if(k in Di){const u=Di[k];return u(b,o.formatLong)}return b}).join("").match(Ph),f=[];for(let b of c){ir(b)&&Oi(b,i,s),tr(b)&&Oi(b,i,s);const k=b[0],u=Oh[k];if(u){const{incompatibleTokens:_}=u;if(Array.isArray(_)){const g=f.find(S=>_.includes(S.token)||S.token===k);if(g)throw new RangeError(`The format string mustn't contain \`${g.fullToken}\` and \`${b}\` at the same time`)}else if(u.incompatibleTokens==="*"&&f.length>0)throw new RangeError(`The format string mustn't contain \`${b}\` and any other token at the same time`);f.push({token:k,fullToken:b});const p=u.run(s,b,o.match,d);if(!p)return n();h.push(p.setter),s=p.rest}else{if(k.match($h))throw new RangeError("Format string contains an unescaped latin alphabet character `"+k+"`");if(b==="''"?b="'":k==="'"&&(b=Nh(b)),s.indexOf(b)===0)s=s.slice(b.length);else return n()}}if(s.length>0&&Fh.test(s))return n();const m=h.map(b=>b.priority).sort((b,k)=>k-b).filter((b,k,u)=>u.indexOf(b)===k).map(b=>h.filter(k=>k.priority===b).sort((k,u)=>u.subPriority-k.subPriority)).map(b=>b[0]);let v=q(e,t?.in);if(isNaN(+v))return n();const x={};for(const b of m){if(!b.validate(v,d))return n();const k=b.set(v,x,d);Array.isArray(k)?(v=k[0],Object.assign(x,k[1])):v=k}return v}function Nh(s){return s.match(Rh)[1].replace(Lh,"'")}window.Vaadin.Flow.datepickerConnector={};window.Vaadin.Flow.datepickerConnector.initLazy=s=>{if(s.$connector)return;s.$connector={};const i=function(n){try{new Date().toLocaleDateString(n)}catch{return console.warn("The locale is not supported, using default format setting (ISO 8601)."),"yyyy-MM-dd"}let o=new Date(Date.UTC(1234,4,6)).toLocaleDateString(n,{timeZone:"UTC"});return o=o.replace(/([a-zA-Z]+)/g,"'$1'").replace("06","dd").replace("6","d").replace("05","MM").replace("5","M").replace("1234","yyyy"),o.includes("d")&&o.includes("M")&&o.includes("y")?o:(console.warn("The locale is not supported, using default format setting (ISO 8601)."),"yyyy-MM-dd")};function e(n){if(!n||n.length===0)throw new Error("Array of custom date formats is null or empty");function r(m){if(m.includes("yyyy")&&!m.includes("yyyyy"))return m.replace("yyyy","yy");if(m.includes("YYYY")&&!m.includes("YYYYY"))return m.replace("YYYY","YY")}function o(m){return m.includes("y")||m.includes("Y")}function a(m){return!m.includes("yyyy")&&!m.includes("YYYY")}function l(m){return m.reduce((v,x)=>(o(x)&&!a(x)&&v.push(r(x)),v.push(x),v),[])}function d(m){if(s.$connector._lastParseStatus==="error")return;if(s.$connector._lastParseStatus==="successful"){s.$connector._lastParsedDate.day===m.getDate()&&s.$connector._lastParsedDate.month===m.getMonth()&&s.$connector._lastParsedDate.year%100===m.getFullYear()%100&&m.setFullYear(s.$connector._lastParsedDate.year);return}const v=Fe(s.value);Pi(v)&&v.getDate()===m.getDate()&&v.getMonth()===m.getMonth()&&v.getFullYear()%100===m.getFullYear()%100&&m.setFullYear(v.getFullYear())}function h(m){const v=n[0],x=Fe(`${m.year}-${m.month+1}-${m.day}`);return Bd(x,v)}function c(m,v,x){const b=o(v)?x:new Date,k=zh(m,v,b);if(Pi(k))return o(v)&&a(v)&&d(k),{day:k.getDate(),month:k.getMonth(),year:k.getFullYear()}}function f(m){const v=t();for(let x of l(n)){const b=c(m,x,v);if(b)return s.$connector._lastParseStatus="successful",s.$connector._lastParsedDate=b,b}return s.$connector._lastParseStatus="error",!1}return{formatDate:h,parseDate:f}}function t(){const{referenceDate:n}=s.i18n;return n?new Date(n.year,n.month,n.day):new Date}s.$connector.updateI18n=(n,r)=>{const o=r&&r.dateFormats&&r.dateFormats.length>0;r&&r.referenceDate&&(r.referenceDate=Ji(new Date(r.referenceDate)));const a=o?r.dateFormats:[i(n)],l=e(a);s.i18n=Object.assign({},s.i18n,r,l)},s.addEventListener("opened-changed",()=>s.$connector._lastParseStatus=void 0)};/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ss=s=>class extends s{static get properties(){return{index:{type:Number},item:{type:Object},label:{type:String},selected:{type:Boolean,value:!1,reflectToAttribute:!0},focused:{type:Boolean,value:!1,reflectToAttribute:!0},renderer:{type:Function}}}static get observers(){return["__rendererOrItemChanged(renderer, index, item, selected, focused)","__updateLabel(label, renderer)"]}static get observedAttributes(){return[...super.observedAttributes,"hidden"]}attributeChangedCallback(e,t,n){e==="hidden"&&n!==null?this.index=void 0:super.attributeChangedCallback(e,t,n)}connectedCallback(){super.connectedCallback(),this._owner=this.parentNode.owner;const e=this._getHostDir();e&&this.setAttribute("dir",e)}_getHostDir(){return this._owner&&this._owner.$.overlay.getAttribute("dir")}requestContentUpdate(){if(!this.renderer||this.hidden)return;const e={index:this.index,item:this.item,focused:this.focused,selected:this.selected};this.renderer(this,this._owner,e)}__rendererOrItemChanged(e,t,n){n===void 0||t===void 0||(this._oldRenderer!==e&&(this.innerHTML="",delete this._$litPart$),e&&(this._oldRenderer=e,this.requestContentUpdate()))}__updateLabel(e,t){t||(this.textContent=e)}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Et=C`
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
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Bh extends ss(T(z(I(A(E))))){static get is(){return"vaadin-time-picker-item"}static get styles(){return Et}render(){return y`
      <span part="checkmark" aria-hidden="true"></span>
      <div part="content">
        <slot></slot>
      </div>
    `}}w(Bh);/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ns=s=>class extends xt(s){static get observers(){return["_setOverlayWidth(positionTarget, opened)"]}constructor(){super(),this.requiredVerticalSpace=200}_shouldCloseOnOutsideClick(e){const t=e.composedPath();return!t.includes(this.positionTarget)&&!t.includes(this)}_mouseDownListener(e){super._mouseDownListener(e),this._shouldCloseOnOutsideClick(e)&&!mt(e.composedPath()[0])&&e.preventDefault()}_updateOverlayWidth(){this.style.setProperty(`--_${this.localName}-default-width`,`${this.positionTarget.offsetWidth}px`)}_setOverlayWidth(e,t){e&&t&&(this._updateOverlayWidth(),this._updatePosition())}};/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Vh=C`
  :host {
    --vaadin-item-checkmark-display: block;
  }

  #overlay {
    width: var(--vaadin-time-picker-overlay-width, var(--_vaadin-time-picker-overlay-default-width, auto));
  }

  [part='content'] {
    display: flex;
    flex-direction: column;
    height: 100%;
  }
`;/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Hh extends ns(ge(z(T(I(A(E)))))){static get is(){return"vaadin-time-picker-overlay"}static get styles(){return[me,Vh]}render(){return y`
      <div part="overlay" id="overlay">
        <div part="content" id="content">
          <slot></slot>
        </div>
      </div>
    `}}w(Hh);/**
 * @license
 * Copyright (c) 2016 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
 */const Vs=navigator.userAgent.match(/iP(?:hone|ad;(?: U;)? CPU) OS (\d+)/u),Wh=Vs&&Vs[1]>=8,Hs=3,qh={_ratio:.5,_scrollerPaddingTop:0,_scrollPosition:0,_physicalSize:0,_physicalAverage:0,_physicalAverageCount:0,_physicalTop:0,_virtualCount:0,_estScrollHeight:0,_scrollHeight:0,_viewportHeight:0,_viewportWidth:0,_physicalItems:null,_physicalSizes:null,_firstVisibleIndexVal:null,_lastVisibleIndexVal:null,_maxPages:2,_templateCost:0,get _physicalBottom(){return this._physicalTop+this._physicalSize},get _scrollBottom(){return this._scrollPosition+this._viewportHeight},get _virtualEnd(){return this._virtualStart+this._physicalCount-1},get _hiddenContentSize(){return this._physicalSize-this._viewportHeight},get _maxScrollTop(){return this._estScrollHeight-this._viewportHeight+this._scrollOffset},get _maxVirtualStart(){const s=this._virtualCount;return Math.max(0,s-this._physicalCount)},get _virtualStart(){return this._virtualStartVal||0},set _virtualStart(s){s=this._clamp(s,0,this._maxVirtualStart),this._virtualStartVal=s},get _physicalStart(){return this._physicalStartVal||0},set _physicalStart(s){s%=this._physicalCount,s<0&&(s=this._physicalCount+s),this._physicalStartVal=s},get _physicalEnd(){return(this._physicalStart+this._physicalCount-1)%this._physicalCount},get _physicalCount(){return this._physicalCountVal||0},set _physicalCount(s){this._physicalCountVal=s},get _optPhysicalSize(){return this._viewportHeight===0?1/0:this._viewportHeight*this._maxPages},get _isVisible(){return!!(this.offsetWidth||this.offsetHeight)},get firstVisibleIndex(){let s=this._firstVisibleIndexVal;if(s==null){let i=this._physicalTop+this._scrollOffset;s=this._iterateItems((e,t)=>{if(i+=this._getPhysicalSizeIncrement(e),i>this._scrollPosition)return t})||0,this._firstVisibleIndexVal=s}return s},get lastVisibleIndex(){let s=this._lastVisibleIndexVal;if(s==null){let i=this._physicalTop+this._scrollOffset;this._iterateItems((e,t)=>{i<this._scrollBottom&&(s=t),i+=this._getPhysicalSizeIncrement(e)}),this._lastVisibleIndexVal=s}return s},get _scrollOffset(){return this._scrollerPaddingTop+this.scrollOffset},_scrollHandler(){const s=Math.max(0,Math.min(this._maxScrollTop,this._scrollTop));let i=s-this._scrollPosition;const e=i>=0;if(this._scrollPosition=s,this._firstVisibleIndexVal=null,this._lastVisibleIndexVal=null,Math.abs(i)>this._physicalSize&&this._physicalSize>0){i-=this._scrollOffset;const t=Math.round(i/this._physicalAverage);this._virtualStart+=t,this._physicalStart+=t,this._physicalTop=Math.min(Math.floor(this._virtualStart)*this._physicalAverage,this._scrollPosition),this._update()}else if(this._physicalCount>0){const t=this._getReusables(e);e?(this._physicalTop=t.physicalTop,this._virtualStart+=t.indexes.length,this._physicalStart+=t.indexes.length):(this._virtualStart-=t.indexes.length,this._physicalStart-=t.indexes.length),this._update(t.indexes,e?null:t.indexes),this._debounce("_increasePoolIfNeeded",this._increasePoolIfNeeded.bind(this,0),te)}},_getReusables(s){let i,e,t;const n=[],r=this._hiddenContentSize*this._ratio,o=this._virtualStart,a=this._virtualEnd,l=this._physicalCount;let d=this._physicalTop+this._scrollOffset;const h=this._physicalBottom+this._scrollOffset,c=this._scrollPosition,f=this._scrollBottom;for(s?(i=this._physicalStart,e=c-d):(i=this._physicalEnd,e=h-f);t=this._getPhysicalSizeIncrement(i),e-=t,!(n.length>=l||e<=r);)if(s){if(a+n.length+1>=this._virtualCount||d+t>=c-this._scrollOffset)break;n.push(i),d+=t,i=(i+1)%l}else{if(o-n.length<=0||d+this._physicalSize-t<=f)break;n.push(i),d-=t,i=i===0?l-1:i-1}return{indexes:n,physicalTop:d-this._scrollOffset}},_update(s,i){if(!(s&&s.length===0||this._physicalCount===0)){if(this._assignModels(s),this._updateMetrics(s),i)for(;i.length;){const e=i.pop();this._physicalTop-=this._getPhysicalSizeIncrement(e)}this._positionItems(),this._updateScrollerSize()}},_isClientFull(){return this._scrollBottom!==0&&this._physicalBottom-1>=this._scrollBottom&&this._physicalTop<=this._scrollPosition},_increasePoolIfNeeded(s){const e=this._clamp(this._physicalCount+s,Hs,this._virtualCount-this._virtualStart)-this._physicalCount;let t=Math.round(this._physicalCount*.5);if(!(e<0)){if(e>0){const n=window.performance.now();[].push.apply(this._physicalItems,this._createPool(e));for(let r=0;r<e;r++)this._physicalSizes.push(0);this._physicalCount+=e,this._physicalStart>this._physicalEnd&&this._isIndexRendered(this._focusedVirtualIndex)&&this._getPhysicalIndex(this._focusedVirtualIndex)<this._physicalEnd&&(this._physicalStart+=e),this._update(),this._templateCost=(window.performance.now()-n)/e,t=Math.round(this._physicalCount*.5)}this._virtualEnd>=this._virtualCount-1||t===0||(this._isClientFull()?this._physicalSize<this._optPhysicalSize&&this._debounce("_increasePoolIfNeeded",this._increasePoolIfNeeded.bind(this,this._clamp(Math.round(50/this._templateCost),1,t)),tn):this._debounce("_increasePoolIfNeeded",this._increasePoolIfNeeded.bind(this,t),te))}},_render(){if(!(!this.isAttached||!this._isVisible))if(this._physicalCount!==0){const s=this._getReusables(!0);this._physicalTop=s.physicalTop,this._virtualStart+=s.indexes.length,this._physicalStart+=s.indexes.length,this._update(s.indexes),this._update(),this._increasePoolIfNeeded(0)}else this._virtualCount>0&&(this.updateViewportBoundaries(),this._increasePoolIfNeeded(Hs))},_itemsChanged(s){s.path==="items"&&(this._virtualStart=0,this._physicalTop=0,this._virtualCount=this.items?this.items.length:0,this._physicalIndexForKey={},this._firstVisibleIndexVal=null,this._lastVisibleIndexVal=null,this._physicalItems||(this._physicalItems=[]),this._physicalSizes||(this._physicalSizes=[]),this._physicalStart=0,this._scrollTop>this._scrollOffset&&this._resetScrollPosition(0),this._debounce("_render",this._render,ue))},_iterateItems(s,i){let e,t,n,r;if(arguments.length===2&&i){for(r=0;r<i.length;r++)if(e=i[r],t=this._computeVidx(e),(n=s.call(this,e,t))!=null)return n}else{for(e=this._physicalStart,t=this._virtualStart;e<this._physicalCount;e++,t++)if((n=s.call(this,e,t))!=null)return n;for(e=0;e<this._physicalStart;e++,t++)if((n=s.call(this,e,t))!=null)return n}},_computeVidx(s){return s>=this._physicalStart?this._virtualStart+(s-this._physicalStart):this._virtualStart+(this._physicalCount-this._physicalStart)+s},_positionItems(){this._adjustScrollPosition();let s=this._physicalTop;this._iterateItems(i=>{this.translate3d(0,`${s}px`,0,this._physicalItems[i]),s+=this._physicalSizes[i]})},_getPhysicalSizeIncrement(s){return this._physicalSizes[s]},_adjustScrollPosition(){const s=this._virtualStart===0?this._physicalTop:Math.min(this._scrollPosition+this._physicalTop,0);if(s!==0){this._physicalTop-=s;const i=this._scrollPosition;!Wh&&i>0&&this._resetScrollPosition(i-s)}},_resetScrollPosition(s){this.scrollTarget&&s>=0&&(this._scrollTop=s,this._scrollPosition=this._scrollTop)},_updateScrollerSize(s){const i=this._physicalBottom+Math.max(this._virtualCount-this._physicalCount-this._virtualStart,0)*this._physicalAverage;this._estScrollHeight=i,(s||this._scrollHeight===0||this._scrollPosition>=i-this._physicalSize||Math.abs(i-this._scrollHeight)>=this._viewportHeight)&&(this.$.items.style.height=`${i}px`,this._scrollHeight=i)},scrollToIndex(s){if(typeof s!="number"||s<0||s>this.items.length-1||(ut(),this._physicalCount===0))return;s=this._clamp(s,0,this._virtualCount-1),(!this._isIndexRendered(s)||s>=this._maxVirtualStart)&&(this._virtualStart=s-1),this._assignModels(),this._updateMetrics(),this._physicalTop=this._virtualStart*this._physicalAverage;let i=this._physicalStart,e=this._virtualStart,t=0;const n=this._hiddenContentSize;for(;e<s&&t<=n;)t+=this._getPhysicalSizeIncrement(i),i=(i+1)%this._physicalCount,e+=1;this._updateScrollerSize(!0),this._positionItems(),this._resetScrollPosition(this._physicalTop+this._scrollOffset+t),this._increasePoolIfNeeded(0),this._firstVisibleIndexVal=null,this._lastVisibleIndexVal=null},_resetAverage(){this._physicalAverage=0,this._physicalAverageCount=0},_resizeHandler(){this._debounce("_render",()=>{this._firstVisibleIndexVal=null,this._lastVisibleIndexVal=null,this._isVisible?(this.updateViewportBoundaries(),this.toggleScrollListener(!0),this._resetAverage(),this._render()):this.toggleScrollListener(!1)},ue)},_isIndexRendered(s){return s>=this._virtualStart&&s<=this._virtualEnd},_getPhysicalIndex(s){return(this._physicalStart+(s-this._virtualStart))%this._physicalCount},_clamp(s,i,e){return Math.min(e,Math.max(i,s))},_debounce(s,i,e){this._debouncers||(this._debouncers={}),this._debouncers[s]=D.debounce(this._debouncers[s],e,i.bind(this)),sn(this._debouncers[s])}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Uh=1e5,bi=1e3;class lr{constructor({createElements:i,updateElement:e,scrollTarget:t,scrollContainer:n,reorderElements:r,elementsContainer:o,__disableHeightPlaceholder:a}){this.isAttached=!0,this._vidxOffset=0,this.createElements=i,this.updateElement=e,this.scrollTarget=t,this.scrollContainer=n,this.reorderElements=r,this.elementsContainer=o||n,this.__disableHeightPlaceholder=a??!1,this._maxPages=1.3,this.__placeholderHeight=200,this.__elementHeightQueue=Array(10),this.timeouts={SCROLL_REORDER:500,PREVENT_OVERSCROLL:500,FIX_INVALID_ITEM_POSITIONING:100},this.__resizeObserver=new ResizeObserver(()=>this._resizeHandler()),getComputedStyle(this.scrollTarget).overflow==="visible"&&(this.scrollTarget.style.overflow="auto"),getComputedStyle(this.scrollContainer).position==="static"&&(this.scrollContainer.style.position="relative"),this.__resizeObserver.observe(this.scrollTarget),this.scrollTarget.addEventListener("scroll",()=>this._scrollHandler()),new ResizeObserver(([{contentRect:d}])=>{const h=d.width===0&&d.height===0;!h&&this.__scrollTargetHidden&&this.scrollTarget.scrollTop!==this._scrollPosition&&(this.scrollTarget.scrollTop=this._scrollPosition),this.__scrollTargetHidden=h}).observe(this.scrollTarget),this._scrollLineHeight=this._getScrollLineHeight(),this.scrollTarget.addEventListener("virtualizer-element-focused",d=>this.__onElementFocused(d)),this.elementsContainer.addEventListener("focusin",()=>{this.scrollTarget.dispatchEvent(new CustomEvent("virtualizer-element-focused",{detail:{element:this.__getFocusedElement()}}))}),this.reorderElements&&(this.scrollTarget.addEventListener("mousedown",()=>{this.__mouseDown=!0}),this.scrollTarget.addEventListener("mouseup",()=>{this.__mouseDown=!1,this.__pendingReorder&&this.__reorderElements()}))}get scrollOffset(){return 0}get adjustedFirstVisibleIndex(){return this.firstVisibleIndex+this._vidxOffset}get adjustedLastVisibleIndex(){return this.lastVisibleIndex+this._vidxOffset}get _maxVirtualIndexOffset(){return this.size-this._virtualCount}__hasPlaceholders(){return this.__getVisibleElements().some(i=>i.__virtualizerPlaceholder)}scrollToIndex(i){if(typeof i!="number"||isNaN(i)||this.size===0||!this.scrollTarget.offsetHeight)return;delete this.__pendingScrollToIndex,this._physicalCount<=3&&this.flush(),i=this._clamp(i,0,this.size-1);const e=this.__getVisibleElements().length;let t=Math.floor(i/this.size*this._virtualCount);this._virtualCount-t<e?(t=this._virtualCount-(this.size-i),this._vidxOffset=this._maxVirtualIndexOffset):t<e?i<bi?(t=i,this._vidxOffset=0):(t=bi,this._vidxOffset=i-t):this._vidxOffset=i-t,this.__skipNextVirtualIndexAdjust=!0,super.scrollToIndex(t),this.adjustedFirstVisibleIndex!==i&&this._scrollTop<this._maxScrollTop&&!this.grid&&(this._scrollTop-=this.__getIndexScrollOffset(i)||0),this._scrollHandler(),this.__hasPlaceholders()&&(this.__pendingScrollToIndex=i)}flush(){this.scrollTarget.offsetHeight!==0&&(this._resizeHandler(),ut(),this._scrollHandler(),this.__fixInvalidItemPositioningDebouncer&&this.__fixInvalidItemPositioningDebouncer.flush(),this.__scrollReorderDebouncer&&this.__scrollReorderDebouncer.flush(),this.__debouncerWheelAnimationFrame&&this.__debouncerWheelAnimationFrame.flush())}hostConnected(){this.scrollTarget.offsetParent&&this.scrollTarget.scrollTop!==this._scrollPosition&&(this.scrollTarget.scrollTop=this._scrollPosition)}update(i=0,e=this.size-1){const t=[];this.__getVisibleElements().forEach(n=>{n.__virtualIndex>=i&&n.__virtualIndex<=e&&(this.__updateElement(n,n.__virtualIndex,!0),t.push(n))}),this.__afterElementsUpdated(t)}_updateMetrics(i){ut();let e=0,t=0;const n=this._physicalAverageCount,r=this._physicalAverage;this._iterateItems((o,a)=>{t+=this._physicalSizes[o];const l=this._physicalSizes[o];this._physicalSizes[o]=Math.ceil(this.__getBorderBoxHeight(this._physicalItems[o])),this._physicalSizes[o]!==l&&(this.__resizeObserver.unobserve(this._physicalItems[o]),this.__resizeObserver.observe(this._physicalItems[o],{box:"border-box"})),e+=this._physicalSizes[o],this._physicalAverageCount+=this._physicalSizes[o]?1:0},i),this._physicalSize=this._physicalSize+e-t,this._physicalAverageCount!==n&&(this._physicalAverage=Math.round((r*n+e)/this._physicalAverageCount))}__getBorderBoxHeight(i){const e=getComputedStyle(i),t=parseFloat(e.height)||0;if(e.boxSizing==="border-box")return t;const n=parseFloat(e.paddingBottom)||0,r=parseFloat(e.paddingTop)||0,o=parseFloat(e.borderBottomWidth)||0,a=parseFloat(e.borderTopWidth)||0;return t+n+r+o+a}__updateElement(i,e,t){i.__virtualizerPlaceholder&&(i.style.paddingTop="",i.style.opacity="",i.__virtualizerPlaceholder=!1),!this.__preventElementUpdates&&(i.__lastUpdatedIndex!==e||t)&&(this.updateElement(i,e),i.__lastUpdatedIndex=e)}__afterElementsUpdated(i){this.__disableHeightPlaceholder||i.forEach(e=>{const t=e.offsetHeight;if(t===0)e.style.paddingTop=`${this.__placeholderHeight}px`,e.style.opacity="0",e.__virtualizerPlaceholder=!0,this.__placeholderClearDebouncer=D.debounce(this.__placeholderClearDebouncer,ue,()=>this._resizeHandler());else{this.__elementHeightQueue.push(t),this.__elementHeightQueue.shift();const n=this.__elementHeightQueue.filter(r=>r!==void 0);this.__placeholderHeight=Math.round(n.reduce((r,o)=>r+o,0)/n.length)}}),this.__pendingScrollToIndex!==void 0&&!this.__hasPlaceholders()&&this.scrollToIndex(this.__pendingScrollToIndex)}__getIndexScrollOffset(i){const e=this.__getVisibleElements().find(t=>t.__virtualIndex===i);return e?this.scrollTarget.getBoundingClientRect().top-e.getBoundingClientRect().top:void 0}get size(){return this.__size}set size(i){if(i===this.size)return;this.__fixInvalidItemPositioningDebouncer&&this.__fixInvalidItemPositioningDebouncer.cancel(),this._debouncers&&this._debouncers._increasePoolIfNeeded&&this._debouncers._increasePoolIfNeeded.cancel(),this.__preventElementUpdates=!0;let e,t;if(i>0&&(e=this.adjustedFirstVisibleIndex,t=this.__getIndexScrollOffset(e)),this.__size=i,this._itemsChanged({path:"items"}),ut(),i>0){e=Math.min(e,i-1),this.scrollToIndex(e);const n=this.__getIndexScrollOffset(e);t!==void 0&&n!==void 0&&(this._scrollTop+=t-n)}this.__preventElementUpdates=!1,this._isVisible||this._assignModels(),this.elementsContainer.children.length||requestAnimationFrame(()=>this._resizeHandler()),this._resizeHandler(),ut(),this._debounce("_update",this._update,te)}get _scrollTop(){return this.scrollTarget.scrollTop}set _scrollTop(i){this.scrollTarget.scrollTop=i}get items(){return{length:Math.min(this.size,Uh)}}get offsetHeight(){return this.scrollTarget.offsetHeight}get $(){return{items:this.scrollContainer}}updateViewportBoundaries(){const i=window.getComputedStyle(this.scrollTarget);this._scrollerPaddingTop=this.scrollTarget===this?0:parseInt(i["padding-top"],10),this._isRTL=i.direction==="rtl",this._viewportWidth=this.elementsContainer.offsetWidth,this._viewportHeight=this.scrollTarget.offsetHeight,this._scrollPageHeight=this._viewportHeight-this._scrollLineHeight,this.grid&&this._updateGridMetrics()}setAttribute(){}_createPool(i){const e=this.createElements(i),t=document.createDocumentFragment();return e.forEach(n=>{n.style.position="absolute",t.appendChild(n),this.__resizeObserver.observe(n,{box:"border-box"})}),this.elementsContainer.appendChild(t),e}_assignModels(i){const e=[];this._iterateItems((t,n)=>{const r=this._physicalItems[t];r.hidden=n>=this.size,r.hidden?delete r.__lastUpdatedIndex:(r.__virtualIndex=n+(this._vidxOffset||0),this.__updateElement(r,r.__virtualIndex),e.push(r))},i),this.__afterElementsUpdated(e)}_isClientFull(){return setTimeout(()=>{this.__clientFull=!0}),this.__clientFull||super._isClientFull()}translate3d(i,e,t,n){n.style.transform=`translateY(${e})`}toggleScrollListener(){}__getFocusedElement(i=this.__getVisibleElements()){return i.find(e=>e.contains(this.elementsContainer.getRootNode().activeElement)||e.contains(this.scrollTarget.getRootNode().activeElement))}__nextFocusableSiblingMissing(i,e){return e.indexOf(i)===e.length-1&&this.size>i.__virtualIndex+1}__previousFocusableSiblingMissing(i,e){return e.indexOf(i)===0&&i.__virtualIndex>0}__onElementFocused(i){if(!this.reorderElements)return;const e=i.detail.element;if(!e)return;const t=this.__getVisibleElements();(this.__previousFocusableSiblingMissing(e,t)||this.__nextFocusableSiblingMissing(e,t))&&this.flush();const n=this.__getVisibleElements();this.__nextFocusableSiblingMissing(e,n)?(this._scrollTop+=Math.ceil(e.getBoundingClientRect().bottom)-Math.floor(this.scrollTarget.getBoundingClientRect().bottom-1),this.flush()):this.__previousFocusableSiblingMissing(e,n)&&(this._scrollTop-=Math.ceil(this.scrollTarget.getBoundingClientRect().top+1)-Math.floor(e.getBoundingClientRect().top),this.flush())}_scrollHandler(){if(this.scrollTarget.offsetHeight===0)return;this._adjustVirtualIndexOffset(this._scrollTop-this._scrollPosition);const i=this._scrollTop-this._scrollPosition;if(super._scrollHandler(),this._physicalCount!==0){const e=i>=0,t=this._getReusables(!e);t.indexes.length&&(this._physicalTop=t.physicalTop,e?(this._virtualStart-=t.indexes.length,this._physicalStart-=t.indexes.length):(this._virtualStart+=t.indexes.length,this._physicalStart+=t.indexes.length),this._resizeHandler())}i&&(this.__fixInvalidItemPositioningDebouncer=D.debounce(this.__fixInvalidItemPositioningDebouncer,K.after(this.timeouts.FIX_INVALID_ITEM_POSITIONING),()=>this.__fixInvalidItemPositioning()),this.__overscrollDebouncer?.isActive()||(this.scrollTarget.style.overscrollBehavior="none"),this.__overscrollDebouncer=D.debounce(this.__overscrollDebouncer,K.after(this.timeouts.PREVENT_OVERSCROLL),()=>{this.scrollTarget.style.overscrollBehavior=null})),this.reorderElements&&(this.__scrollReorderDebouncer=D.debounce(this.__scrollReorderDebouncer,K.after(this.timeouts.SCROLL_REORDER),()=>this.__reorderElements())),this._scrollPosition===0&&this.firstVisibleIndex!==0&&Math.abs(i)>0&&this.scrollToIndex(0)}_resizeHandler(){super._resizeHandler();const i=this.adjustedLastVisibleIndex===this.size-1,e=this._physicalTop-this._scrollPosition;if(i&&e>0){const t=Math.ceil(e/this._physicalAverage);this._virtualStart=Math.max(0,this._virtualStart-t),this._physicalStart=Math.max(0,this._physicalStart-t),super.scrollToIndex(this._virtualCount-1),this.scrollTarget.scrollTop=this.scrollTarget.scrollHeight-this.scrollTarget.clientHeight}}__fixInvalidItemPositioning(){if(!this.scrollTarget.isConnected)return;const i=this._physicalTop>this._scrollTop,e=this._physicalBottom<this._scrollBottom,t=this.adjustedFirstVisibleIndex===0,n=this.adjustedLastVisibleIndex===this.size-1;if(i&&!t||e&&!n){const r=e,o=this._ratio;this._ratio=0,this._scrollPosition=this._scrollTop+(r?-1:1),this._scrollHandler(),this._ratio=o}}_increasePoolIfNeeded(i){if(this._physicalCount>2&&this._physicalAverage>0&&i>0){const t=Math.ceil(this._optPhysicalSize/this._physicalAverage)-this._physicalCount;super._increasePoolIfNeeded(Math.max(i,Math.min(100,t)))}else super._increasePoolIfNeeded(i)}get _optPhysicalSize(){const i=super._optPhysicalSize;return i<=0||this.__hasPlaceholders()?i:i+this.__getItemHeightBuffer()}__getItemHeightBuffer(){if(this._physicalCount===0)return 0;const i=Math.ceil(this._viewportHeight*(this._maxPages-1)/2),e=Math.max(...this._physicalSizes);return e>Math.min(...this._physicalSizes)?Math.max(0,e-i):0}_getScrollLineHeight(){const i=document.createElement("div");i.style.fontSize="initial",i.style.display="none",document.body.appendChild(i);const e=window.getComputedStyle(i).fontSize;return document.body.removeChild(i),e?window.parseInt(e):void 0}__getVisibleElements(){return Array.from(this.elementsContainer.children).filter(i=>!i.hidden)}__reorderElements(){if(this.__mouseDown){this.__pendingReorder=!0;return}this.__pendingReorder=!1;const i=this._virtualStart+(this._vidxOffset||0),e=this.__getVisibleElements(),t=this.__getFocusedElement(e)||e[0];if(!t)return;const n=t.__virtualIndex-i,r=e.indexOf(t)-n;if(r>0)for(let o=0;o<r;o++)this.elementsContainer.appendChild(e[o]);else if(r<0)for(let o=e.length+r;o<e.length;o++)this.elementsContainer.insertBefore(e[o],e[0]);if(Ni){const{transform:o}=this.scrollTarget.style;this.scrollTarget.style.transform="translateZ(0)",setTimeout(()=>{this.scrollTarget.style.transform=o})}}_adjustVirtualIndexOffset(i){const e=this._maxVirtualIndexOffset;if(this._virtualCount>=this.size)this._vidxOffset=0;else if(this.__skipNextVirtualIndexAdjust)this.__skipNextVirtualIndexAdjust=!1;else if(Math.abs(i)>1e4){const t=this._scrollTop/(this.scrollTarget.scrollHeight-this.scrollTarget.clientHeight);this._vidxOffset=Math.round(t*e)}else{const t=this._vidxOffset,n=bi,r=100;this._scrollTop===0?(this._vidxOffset=0,t!==this._vidxOffset&&super.scrollToIndex(0)):this.firstVisibleIndex<n&&this._vidxOffset>0&&(this._vidxOffset-=Math.min(this._vidxOffset,r),super.scrollToIndex(this.firstVisibleIndex+(t-this._vidxOffset))),this._scrollTop>=this._maxScrollTop&&this._maxScrollTop>0?(this._vidxOffset=e,t!==this._vidxOffset&&super.scrollToIndex(this._virtualCount-1)):this.firstVisibleIndex>this._virtualCount-n&&this._vidxOffset<e&&(this._vidxOffset+=Math.min(e-this._vidxOffset,r),super.scrollToIndex(this.firstVisibleIndex-(this._vidxOffset-t)))}}}Object.setPrototypeOf(lr.prototype,qh);/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class dr{constructor(i){this.__adapter=new lr(i)}get firstVisibleIndex(){return this.__adapter.adjustedFirstVisibleIndex}get lastVisibleIndex(){return this.__adapter.adjustedLastVisibleIndex}get size(){return this.__adapter.size}set size(i){this.__adapter.size=i}scrollToIndex(i){this.__adapter.scrollToIndex(i)}update(i=0,e=this.size-1){this.__adapter.update(i,e)}flush(){this.__adapter.flush()}hostConnected(){this.__adapter.hostConnected()}}/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const fe=class{toString(){return""}};/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const rs=s=>class extends s{static get properties(){return{items:{type:Array,sync:!0,observer:"__itemsChanged"},focusedIndex:{type:Number,sync:!0,observer:"__focusedIndexChanged"},loading:{type:Boolean,sync:!0,observer:"__loadingChanged"},opened:{type:Boolean,sync:!0,observer:"__openedChanged"},selectedItem:{type:Object,sync:!0,observer:"__selectedItemChanged"},itemClassNameGenerator:{type:Object,observer:"__itemClassNameGeneratorChanged"},itemIdPath:{type:String},owner:{type:Object},getItemLabel:{type:Object},renderer:{type:Object,sync:!0,observer:"__rendererChanged"},theme:{type:String}}}constructor(){super(),this.__boundOnItemClick=this.__onItemClick.bind(this)}get _viewportTotalPaddingBottom(){if(this._cachedViewportTotalPaddingBottom===void 0){const e=window.getComputedStyle(this.$.selector);this._cachedViewportTotalPaddingBottom=[e.paddingBottom,e.borderBottomWidth].map(t=>parseInt(t,10)).reduce((t,n)=>t+n)}return this._cachedViewportTotalPaddingBottom}ready(){super.ready(),this.setAttribute("role","listbox"),this.id=`${this.localName}-${Se()}`,this.__hostTagName=this.constructor.is.replace("-scroller",""),this.addEventListener("click",e=>e.stopPropagation()),this.__patchWheelOverScrolling()}requestContentUpdate(){this.__virtualizer&&(this.items&&(this.__virtualizer.size=this.items.length),this.opened&&this.__virtualizer.update())}scrollIntoView(e){if(!this.__virtualizer||!(this.opened&&e>=0))return;const t=this._visibleItemsCount();let n=e;e>this.__virtualizer.lastVisibleIndex-1?(this.__virtualizer.scrollToIndex(e),n=e-t+1):e>this.__virtualizer.firstVisibleIndex&&(n=this.__virtualizer.firstVisibleIndex),this.__virtualizer.scrollToIndex(Math.max(0,n));const r=[...this.children].find(d=>!d.hidden&&d.index===this.__virtualizer.lastVisibleIndex);if(!r||e!==r.index)return;const o=r.getBoundingClientRect(),a=this.getBoundingClientRect(),l=o.bottom-a.bottom+this._viewportTotalPaddingBottom;l>0&&(this.scrollTop+=l)}_isItemSelected(e,t,n){return e instanceof fe?!1:n&&e!==void 0&&t!==void 0?Ee(n,e)===Ee(n,t):e===t}__initVirtualizer(){this.__virtualizer=new dr({createElements:this.__createElements.bind(this),updateElement:this._updateElement.bind(this),elementsContainer:this,scrollTarget:this,scrollContainer:this.$.selector,reorderElements:!0,__disableHeightPlaceholder:!0})}__itemsChanged(e){e&&this.__virtualizer&&this.requestContentUpdate()}__loadingChanged(){this.requestContentUpdate()}__openedChanged(e){e&&(this.__virtualizer||this.__initVirtualizer(),this.requestContentUpdate())}__selectedItemChanged(){this.requestContentUpdate()}__itemClassNameGeneratorChanged(e,t){(e||t)&&this.requestContentUpdate()}__focusedIndexChanged(e,t){e!==t&&this.requestContentUpdate(),e>=0&&!this.loading&&this.scrollIntoView(e)}__rendererChanged(e,t){(e||t)&&this.requestContentUpdate()}__createElements(e){return[...Array(e)].map(()=>{const t=document.createElement(`${this.__hostTagName}-item`);return t.addEventListener("click",this.__boundOnItemClick),t.tabIndex="-1",t.style.width="100%",t})}_updateElement(e,t){const n=this.items[t],r=this.focusedIndex,o=this._isItemSelected(n,this.selectedItem,this.itemIdPath);e.setProperties({item:n,index:t,label:this.getItemLabel(n),selected:o,renderer:this.renderer,focused:!this.loading&&r===t}),typeof this.itemClassNameGenerator=="function"?e.className=this.itemClassNameGenerator(n):e.className!==""&&(e.className=""),e.id=`${this.__hostTagName}-item-${t}`,e.setAttribute("role",t!==void 0?"option":!1),e.setAttribute("aria-selected",o.toString()),e.setAttribute("aria-posinset",t+1),e.setAttribute("aria-setsize",this.items.length),this.theme?e.setAttribute("theme",this.theme):e.removeAttribute("theme"),n instanceof fe&&this.__requestItemByIndex(t)}__onItemClick(e){this.dispatchEvent(new CustomEvent("selection-changed",{detail:{item:e.currentTarget.item}}))}__patchWheelOverScrolling(){this.$.selector.addEventListener("wheel",e=>{const t=this.scrollTop===0,n=this.scrollHeight-this.scrollTop-this.clientHeight<=1;(t&&e.deltaY<0||n&&e.deltaY>0)&&e.preventDefault()})}__requestItemByIndex(e){requestAnimationFrame(()=>{this.dispatchEvent(new CustomEvent("index-requested",{detail:{index:e}}))})}_visibleItemsCount(){return this.__virtualizer.scrollToIndex(this.__virtualizer.firstVisibleIndex),this.__virtualizer.size>0?this.__virtualizer.lastVisibleIndex-this.__virtualizer.firstVisibleIndex+1:0}};/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const os=C`
  :host {
    /* Fixes scrollbar disappearing when 'Show scroll bars: Always' enabled in Safari */
    box-shadow: 0 0 0 white;
    display: block;
    min-height: 1px;
    overflow: auto;
    /* Fixes item background from getting on top of scrollbars on Safari */
    transform: translate3d(0, 0, 0);
  }

  #selector {
    border: 0 solid transparent;
    border-width: var(--vaadin-item-overlay-padding, 4px);
    position: relative;
    forced-color-adjust: none;
    min-height: var(--_items-min-height, auto);
  }

  #selector > * {
    forced-color-adjust: auto;
  }
`;/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Yh extends rs(I(E)){static get is(){return"vaadin-time-picker-scroller"}static get styles(){return os}render(){return y`
      <div id="selector">
        <slot></slot>
      </div>
    `}}w(Yh);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const jh=C`
  :host([opened]) {
    pointer-events: auto;
  }

  [part~='toggle-button']::before {
    mask-image: var(--_vaadin-icon-clock);
  }

  :host([readonly]) [part~='toggle-button'] {
    display: none;
  }

  /* See https://github.com/vaadin/vaadin-time-picker/issues/145 */
  :host([dir='rtl']) [part='input-field'] {
    direction: ltr;
  }

  :host([dir='rtl']) [part='input-field'] ::slotted(input)::placeholder {
    direction: rtl;
    text-align: left;
  }
`;/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const hr=s=>class extends De(yt(Ae(oe(s)))){static get properties(){return{opened:{type:Boolean,notify:!0,value:!1,reflectToAttribute:!0,sync:!0,observer:"_openedChanged"},autoOpenDisabled:{type:Boolean,sync:!0},readonly:{type:Boolean,value:!1,reflectToAttribute:!0},_focusedIndex:{type:Number,observer:"_focusedIndexChanged",value:-1,sync:!0},_toggleElement:{type:Object,observer:"_toggleElementChanged"},_dropdownItems:{type:Array,sync:!0},_overlayOpened:{type:Boolean,sync:!0,observer:"_overlayOpenedChanged"}}}constructor(){super(),this._scroller,this._closeOnBlurIsPrevented,this._boundOverlaySelectedItemChanged=this._overlaySelectedItemChanged.bind(this),this._boundOnClearButtonMouseDown=this.__onClearButtonMouseDown.bind(this),this._boundOnClick=this._onClick.bind(this),this._boundOnOverlayTouchAction=this._onOverlayTouchAction.bind(this),this._boundOnTouchend=this._onTouchend.bind(this)}get _tagNamePrefix(){return"vaadin-combo-box"}_inputElementChanged(e){super._inputElementChanged(e),e&&(e.autocomplete="off",e.autocapitalize="off",e.setAttribute("role","combobox"),e.setAttribute("aria-autocomplete","list"),e.setAttribute("aria-expanded",!!this.opened),e.setAttribute("spellcheck","false"),e.setAttribute("autocorrect","off"))}firstUpdated(){super.firstUpdated(),this._initScroller()}ready(){super.ready(),this._initOverlay(),this.addEventListener("click",this._boundOnClick),this.addEventListener("touchend",this._boundOnTouchend),this.clearElement&&this.clearElement.addEventListener("mousedown",this._boundOnClearButtonMouseDown),this.addController(new Gn(this))}disconnectedCallback(){super.disconnectedCallback(),this.close()}open(){!this.disabled&&!this.readonly&&(this.opened=!0)}close(){this.opened=!1}_initOverlay(){const e=this.$.overlay;e.addEventListener("touchend",this._boundOnOverlayTouchAction),e.addEventListener("touchmove",this._boundOnOverlayTouchAction),e.addEventListener("mousedown",t=>t.preventDefault()),e.addEventListener("opened-changed",t=>{this._overlayOpened=t.detail.value}),this._overlayElement=e}_initScroller(){const e=document.createElement(`${this._tagNamePrefix}-scroller`);e.owner=this,e.getItemLabel=this._getItemLabel.bind(this),e.addEventListener("selection-changed",this._boundOverlaySelectedItemChanged),this._renderScroller(e),this._scroller=e}_renderScroller(e){e.setAttribute("slot","overlay"),e.setAttribute("tabindex","-1"),this.appendChild(e)}get _hasDropdownItems(){return!!(this._dropdownItems&&this._dropdownItems.length)}_overlayOpenedChanged(e,t){e?this._onOpened():t&&this._hasDropdownItems&&(this.close(),this._onOverlayClosed())}_focusedIndexChanged(e,t){t!==void 0&&this._updateActiveDescendant(e)}_isInputFocused(){return this.inputElement&&Je(this.inputElement)}_updateActiveDescendant(e){const t=this.inputElement;if(!t)return;const n=this._getItemElements().find(r=>r.index===e);n?t.setAttribute("aria-activedescendant",n.id):t.removeAttribute("aria-activedescendant")}_openedChanged(e,t){if(t===void 0)return;e?!this._isInputFocused()&&!Ne&&this.inputElement&&this.inputElement.focus():this._onClosed();const n=this.inputElement;n&&(n.setAttribute("aria-expanded",!!e),e?n.setAttribute("aria-controls",this._scroller.id):n.removeAttribute("aria-controls"))}_onOverlayTouchAction(){this._closeOnBlurIsPrevented=!0,this.inputElement.blur(),this._closeOnBlurIsPrevented=!1}_isClearButton(e){return e.composedPath()[0]===this.clearElement}__onClearButtonMouseDown(e){e.preventDefault(),this.inputElement.focus()}_onClearButtonClick(e){e.preventDefault(),this._onClearAction()}_onToggleButtonClick(e){e.preventDefault(),this.opened?this.close():this.open()}_onHostClick(e){this.autoOpenDisabled||(e.preventDefault(),this.open())}_onClick(e){this._isClearButton(e)?this._onClearButtonClick(e):e.composedPath().includes(this._toggleElement)?this._onToggleButtonClick(e):this._onHostClick(e)}_onTouchend(e){!this.clearElement||e.composedPath()[0]!==this.clearElement||(e.preventDefault(),this._onClearAction())}_onKeyDown(e){super._onKeyDown(e),e.key==="ArrowDown"?(this._onArrowDown(),e.preventDefault()):e.key==="ArrowUp"&&(this._onArrowUp(),e.preventDefault())}_getItemLabel(e){return e?e.toString():""}_onArrowDown(){if(this.opened){const e=this._dropdownItems;e&&(this._focusedIndex=Math.min(e.length-1,this._focusedIndex+1),this._prefillFocusedItemLabel())}else this.open()}_onArrowUp(){if(this.opened){if(this._focusedIndex>-1)this._focusedIndex=Math.max(0,this._focusedIndex-1);else{const e=this._dropdownItems;e&&(this._focusedIndex=e.length-1)}this._prefillFocusedItemLabel()}else this.open()}_prefillFocusedItemLabel(){if(this._focusedIndex>-1){const e=this._dropdownItems[this._focusedIndex];this._inputElementValue=this._getItemLabel(e),this._markAllSelectionRange()}}_setSelectionRange(e,t){this._isInputFocused()&&this.inputElement.setSelectionRange&&this.inputElement.setSelectionRange(e,t)}_markAllSelectionRange(){this._inputElementValue!==void 0&&this._setSelectionRange(0,this._inputElementValue.length)}_clearSelectionRange(){if(this._inputElementValue!==void 0){const e=this._inputElementValue?this._inputElementValue.length:0;this._setSelectionRange(e,e)}}_closeOrCommit(){this.opened?this.close():this._commitValue()}_onEnter(e){if(!this._hasValidInputValue()){e.preventDefault(),e.stopPropagation();return}this.opened&&(e.preventDefault(),e.stopPropagation()),this._closeOrCommit()}_hasValidInputValue(){return!0}_onEscape(e){this.autoOpenDisabled&&(this.opened||this.value!==this._inputElementValue&&this._inputElementValue.length>0)?(e.stopPropagation(),this._focusedIndex=-1,this._onEscapeCancel()):this.opened?(e.stopPropagation(),this._focusedIndex>-1?(this._focusedIndex=-1,this._revertInputValue()):this._onEscapeCancel()):this.clearButtonVisible&&this.value&&!this.readonly&&(e.stopPropagation(),this._onClearAction())}_onEscapeCancel(){}_toggleElementChanged(e){e&&(e.addEventListener("mousedown",t=>t.preventDefault()),e.addEventListener("click",()=>{Ne&&!this._isInputFocused()&&document.activeElement.blur()}))}_onClearAction(){}_onOpened(){}_onClosed(){}_onOverlayClosed(){}_commitValue(){}_revertInputValue(){this._inputElementValue=this.value,this._clearSelectionRange()}_onInput(e){!this.opened&&!this._isClearButton(e)&&!this.autoOpenDisabled&&(this.opened=!0)}_getItemElements(){return Array.from(this._scroller.querySelectorAll(`${this._tagNamePrefix}-item`))}_scrollIntoView(e){this._scroller&&this._scroller.scrollIntoView(e)}_overlaySelectedItemChanged(e){e.stopPropagation(),!(e.detail.item instanceof fe)&&this.opened&&(this._focusedIndex=this._dropdownItems.indexOf(e.detail.item),this.close())}_setFocused(e){super._setFocused(e),!e&&!this.readonly&&!this._closeOnBlurIsPrevented&&this._handleFocusOut()}_handleFocusOut(){if(Q()){this._closeOrCommit();return}this.opened?this._overlayOpened||this.close():this._commitValue()}_shouldRemoveFocus(e){return e.relatedTarget&&e.relatedTarget.localName===`${this._tagNamePrefix}-item`?!1:e.relatedTarget===this._overlayElement?(e.composedPath()[0].focus(),!1):!0}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const cr=s=>class extends ji(s){static get properties(){return{pattern:{type:String}}}static get delegateAttrs(){return[...super.delegateAttrs,"pattern"]}static get constraints(){return[...super.constraints,"pattern"]}};/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Mi(s){if(!s)return"";const i=(t=0,n="00")=>(n+t).substr((n+t).length-n.length);let e=`${i(s.hours)}:${i(s.minutes)}`;return s.seconds!==void 0&&(e+=`:${i(s.seconds)}`),s.milliseconds!==void 0&&(e+=`.${i(s.milliseconds,"000")}`),e}const Gh="(\\d|[0-1]\\d|2[0-3])",ur="(\\d|[0-5]\\d)",Kh=ur,Xh="(\\d{1,3})",Qh=new RegExp(`^${Gh}(?::${ur}(?::${Kh}(?:\\.${Xh})?)?)?$`,"u");function Ye(s){const i=Qh.exec(s);if(i){if(i[4])for(;i[4].length<3;)i[4]+="0";return{hours:i[1],minutes:i[2],seconds:i[3],milliseconds:i[4]}}}function Zh(s){const i=s==null?60:parseFloat(s);if(i%3600===0)return 1;if(i%60===0||!i)return 2;if(i%1===0)return 3;if(i<1)return 4}function qe(s,i){if(s){const e=Zh(i);s.hours=parseInt(s.hours),s.minutes=parseInt(s.minutes||0),s.seconds=e<3?void 0:parseInt(s.seconds||0),s.milliseconds=e<4?void 0:parseInt(s.milliseconds||0)}return s}/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Jh=Object.freeze({formatTime:Mi,parseTime:Ye}),Ws="00:00:00.000",qs="23:59:59.999",ec=s=>class extends ei(Jh,cr(hr(Ct(s)))){static get properties(){return{value:{type:String,notify:!0,value:"",sync:!0},min:{type:String,value:"",sync:!0},max:{type:String,value:"",sync:!0},step:{type:Number,sync:!0},_comboBoxValue:{type:String,sync:!0,observer:"__comboBoxValueChanged"},_inputContainer:{type:Object}}}static get observers(){return["_openedOrItemsChanged(opened, _dropdownItems)","_updateScroller(opened, _dropdownItems, _focusedIndex, _theme)","__updateAriaAttributes(_dropdownItems, opened, inputElement)","__updateDropdownItems(__effectiveI18n, min, max, step)"]}static get constraints(){return[...super.constraints,"min","max"]}get _tagNamePrefix(){return"vaadin-time-picker"}get clearElement(){return this.$.clearButton}get i18n(){return super.i18n}set i18n(e){super.i18n=e}get __unparsableValue(){return this._inputElementValue&&!this.__effectiveI18n.parseTime(this._inputElementValue)?this._inputElementValue:""}ready(){super.ready(),this.addController(new Te(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e},{uniqueIdPrefix:"search-input"})),this.addController(new ve(this.inputElement,this._labelController)),this._inputContainer=this.shadowRoot.querySelector('[part~="input-field"]'),this._toggleElement=this.$.toggleButton,this._tooltipController=new X(this),this._tooltipController.setShouldShow(e=>!e.opened),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}updated(e){super.updated(e),e.has("_comboBoxValue")&&this._dropdownItems&&(this._scroller.selectedItem=this._dropdownItems.find(t=>t.value===this._comboBoxValue))}checkValidity(){return!!(this.inputElement.checkValidity()&&(!this.value||this._timeAllowed(this.__effectiveI18n.parseTime(this.value)))&&(!this._comboBoxValue||this.__effectiveI18n.parseTime(this._comboBoxValue)))}_getItemLabel(e){return e?e.label:""}_updateScroller(e,t,n,r){e&&(this._scroller.style.maxHeight=getComputedStyle(this).getPropertyValue(`--${this._tagNamePrefix}-overlay-max-height`)||"65vh"),this._scroller.setProperties({items:e?t:[],opened:e,focusedIndex:n,theme:r})}_openedOrItemsChanged(e,t){this._overlayOpened=e&&!!(t&&t.length)}_onClosed(){this._commitValue()}_onEscapeCancel(){this._inputElementValue=this._comboBoxValue,this._closeOrCommit()}_onClearAction(){this._comboBoxValue="",this._inputElementValue="",this.__commitValueChange()}_commitValue(){if(this._focusedIndex>-1){const e=this._dropdownItems[this._focusedIndex],t=this._getItemLabel(e);this._inputElementValue=t,this._comboBoxValue=t,this._focusedIndex=-1}else this._inputElementValue===""||this._inputElementValue===void 0?this._comboBoxValue="":this._comboBoxValue=this._inputElementValue;this.__commitValueChange(),this._clearSelectionRange()}_closeOrCommit(){this.opened?this.close():this._commitValue()}_revertInputValue(){this._inputElementValue=this._comboBoxValue,this._clearSelectionRange()}_setFocused(e){super._setFocused(e),e||document.hasFocus()&&this._requestValidation()}__validDayDivisor(e){return!e||24*3600%e===0||e<1&&e%1*1e3%1===0}_onKeyDown(e){if(super._onKeyDown(e),this.readonly||this.disabled||this._dropdownItems.length)return;const t=this.__validDayDivisor(this.step)&&this.step||60;e.keyCode===40?this.__onArrowPressWithStep(-t):e.keyCode===38&&this.__onArrowPressWithStep(t)}__onArrowPressWithStep(e){const t=this.__addStep(this.__getMsec(this.__memoValue),e,!0);this.__memoValue=t,this.__useMemo=!0,this._comboBoxValue=this.__effectiveI18n.formatTime(t),this.__useMemo=!1,this.__commitValueChange()}__commitValueChange(){const e=this.__unparsableValue;this.__committedValue!==this.value?(this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{bubbles:!0}))):this.__committedUnparsableValue!==e&&(this._requestValidation(),this.dispatchEvent(new CustomEvent("unparsable-change"))),this.__committedValue=this.value,this.__committedUnparsableValue=e}__getMsec(e){let t=(e&&e.hours||0)*60*60*1e3;return t+=(e&&e.minutes||0)*60*1e3,t+=(e&&e.seconds||0)*1e3,t+=e&&parseInt(e.milliseconds)||0,t}__getSec(e){let t=(e&&e.hours||0)*60*60;return t+=(e&&e.minutes||0)*60,t+=e&&e.seconds||0,t+=e&&e.milliseconds/1e3||0,t}__addStep(e,t,n){e===0&&t<0&&(e=1440*60*1e3);const r=t*1e3,o=e%r;r<0&&o&&n?e-=o:r>0&&o&&n?e-=o-r:e+=r;const a=Math.floor(e/1e3/60/60);e-=a*1e3*60*60;const l=Math.floor(e/1e3/60);e-=l*1e3*60;const d=Math.floor(e/1e3);return e-=d*1e3,{hours:a<24?a:0,minutes:l,seconds:d,milliseconds:e}}__updateDropdownItems(e,t,n,r){const o=qe(Ye(t||Ws),r),a=this.__getSec(o),l=qe(Ye(n||qs),r),d=this.__getSec(l);if(this._dropdownItems=this.__generateDropdownList(a,d,r),r!==this.__oldStep){this.__oldStep=r;const h=qe(Ye(this.value),r);this.__updateValue(h)}this.value&&(this._comboBoxValue=e.formatTime(e.parseTime(this.value)))}__updateAriaAttributes(e,t,n){e===void 0||n===void 0||(e.length===0?(n.removeAttribute("role"),n.removeAttribute("aria-expanded")):(n.setAttribute("role","combobox"),n.setAttribute("aria-expanded",!!t)))}__generateDropdownList(e,t,n){if(n<900||!this.__validDayDivisor(n))return[];const r=[];n||(n=3600);let o=-n+e;for(;o+n>=e&&o+n<=t;){const a=qe(this.__addStep(o*1e3,n),n);o+=n;const l=this.__effectiveI18n.formatTime(a);r.push({label:l,value:l})}return r}_valueChanged(e,t){const n=this.__memoValue=Ye(e),r=Mi(n)||"";this.__keepCommittedValue||(this.__committedValue=e,this.__committedUnparsableValue=""),e!==""&&e!==null&&!n?this.value=t===void 0?"":t:e!==r?this.value=r:this.__keepInvalidInput?delete this.__keepInvalidInput:this.__updateInputValue(n),this._toggleHasValue(this._hasValue)}__comboBoxValueChanged(e,t){if(e===""&&t===void 0)return;const n=this.__useMemo?this.__memoValue:this.__effectiveI18n.parseTime(e),r=this.__effectiveI18n.formatTime(n)||"";n?e!==r?this._comboBoxValue=r:(this.__keepCommittedValue=!0,this.__updateValue(n),this.__keepCommittedValue=!1):(this.value!==""&&e!==""&&(this.__keepInvalidInput=!0),this.__keepCommittedValue=!0,this.value="",this.__keepCommittedValue=!1)}__updateValue(e){const t=Mi(qe(e,this.step))||"";this.value=t,this.__updateInputValue(e)}__updateInputValue(e){const t=this.__effectiveI18n.formatTime(qe(e,this.step))||"";this._inputElementValue=t,this._comboBoxValue=t}_timeAllowed(e){const t=this.__effectiveI18n.parseTime(this.min||Ws),n=this.__effectiveI18n.parseTime(this.max||qs);return(!this.__getMsec(t)||this.__getMsec(e)>=this.__getMsec(t))&&(!this.__getMsec(n)||this.__getMsec(e)<=this.__getMsec(n))}_onClearButtonClick(e){e.stopPropagation(),super._onClearButtonClick(e),this.opened&&this._scroller.requestContentUpdate()}_onHostClick(e){const t=e.composedPath();(t.includes(this._labelNode)||t.includes(this._inputContainer))&&super._onHostClick(e)}_onChange(e){e.stopPropagation()}};/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class tc extends ec(T(L(I(A(E))))){static get is(){return"vaadin-time-picker"}static get styles(){return[ke,jh]}render(){return y`
      <div class="vaadin-time-picker-container">
        <div part="label">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true" @click="${this.focus}"></span>
        </div>

        <vaadin-input-container
          part="input-field"
          .readonly="${this.readonly}"
          .disabled="${this.disabled}"
          .invalid="${this.invalid}"
          theme="${B(this._theme)}"
        >
          <slot name="prefix" slot="prefix"></slot>
          <slot name="input"></slot>
          <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
          <div id="toggleButton" part="field-button toggle-button" slot="suffix" aria-hidden="true"></div>
        </vaadin-input-container>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>

        <slot name="tooltip"></slot>
      </div>

      <vaadin-time-picker-overlay
        id="overlay"
        dir="ltr"
        .owner="${this}"
        .opened="${this._overlayOpened}"
        theme="${B(this._theme)}"
        .positionTarget="${this._inputContainer}"
        no-vertical-overlap
        exportparts="overlay, content"
      >
        <slot name="overlay"></slot>
      </vaadin-time-picker-overlay>
    `}}w(tc);const ic={"\\u0660":"0","\\u0661":"1","\\u0662":"2","\\u0663":"3","\\u0664":"4","\\u0665":"5","\\u0666":"6","\\u0667":"7","\\u0668":"8","\\u0669":"9"};function sc(s){return s.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")}function _r(s){return s.replace(/[\u0660-\u0669]/g,function(i){const e="\\u0"+i.charCodeAt(0).toString(16);return ic[e]})}function pr(s,i){const e=i.toLocaleTimeString(s),t=/[^\d\u0660-\u0669]/,n=e.match(new RegExp(`${t.source}+$`,"g"))||e.match(new RegExp(`^${t.source}+`,"g"));return n&&n[0].trim()}function nc(s){let i=as.toLocaleTimeString(s);const e=fr(s);e&&i.startsWith(e)&&(i=i.replace(e,""));const t=i.match(/[^\u0660-\u0669\s\d]/);return t&&t[0]}function Us(s,i){if(!i)return null;const e=i.split(/\s*/).map(sc).join("\\s*"),t=new RegExp(e,"i"),n=s.match(t);if(n)return n[0]}const as=new Date("August 19, 1975 23:15:30"),rc=new Date("August 19, 1975 05:15:30");function fr(s){return pr(s,as)}function oc(s){return pr(s,rc)}function yi(s){return parseInt(_r(s))}function ac(s){return s=_r(s),s.length===1?s+="00":s.length===2&&(s+="0"),parseInt(s)}function lc(s,i,e,t){let n=s;if(s.endsWith(e)?n=s.replace(" "+e,""):s.endsWith(t)&&(n=s.replace(" "+t,"")),i){let r=i<10?"0":"";r+=i<100?"0":"",r+=i,n+="."+r}else n+=".000";return s.endsWith(e)?n=n+" "+e:s.endsWith(t)&&(n=n+" "+t),n}function mr(s,i,e=0){s()?i():setTimeout(()=>mr(s,i,200),e)}function dc(s){const i=Ye(s);return{hours:parseInt(i.hours||0),minutes:parseInt(i.minutes||0),seconds:parseInt(i.seconds||0),milliseconds:parseInt(i.milliseconds||0)}}window.Vaadin.Flow.timepickerConnector={};window.Vaadin.Flow.timepickerConnector.initLazy=s=>{s.$connector||(s.$connector={},s.$connector.setLocale=i=>{let e;s.value&&s.value!==""&&(e=dc(s.value));try{as.toLocaleTimeString(i)}catch{throw i="en-US",new Error("vaadin-time-picker: The locale "+i+" is not supported, falling back to default locale setting(en-US).")}const t=fr(i),n=oc(i),r=nc(i),o=function(){return s.step&&s.step<60},a=function(){return s.step&&s.step<1};let l,d;s.i18n={formatTime(h){if(!h)return;const c=new Date;c.setHours(h.hours),c.setMinutes(h.minutes),c.setSeconds(h.seconds!==void 0?h.seconds:0);let f=c.toLocaleTimeString(i,{hour:"numeric",minute:"numeric",second:o()?"numeric":void 0});return a()&&(f=lc(f,h.milliseconds,n,t)),f},parseTime(h){if(h&&h===l&&d)return d;if(!h)return;const c=Us(h,n),f=Us(h,t),m=h.replace(c||"","").replace(f||"","").trim(),v=new RegExp("([\\d\\u0660-\\u0669]){1,2}(?:"+r+")?","g");let x=v.exec(m);if(x){x=yi(x[0].replace(r,"")),c!==f&&(x===12&&c&&(x=0),x!==12&&f&&(x+=12));const b=v.exec(m),k=b&&v.exec(m),u=/[[\.][\d\u0660-\u0669]{1,3}$/;let _=k&&a()&&u.exec(m);return _&&_.index<=k.index&&(_=void 0),d=x!==void 0&&{hours:x,minutes:b?yi(b[0].replace(r,"")):0,seconds:k?yi(k[0].replace(r,"")):0,milliseconds:b&&k&&_?ac(_[0].replace(".","")):0},l=h,d}}},e&&mr(()=>s.$,()=>{const h=s.i18n.formatTime(e);s.inputElement.value!==h&&(s.inputElement.value=h,s.value=h)})})};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const gr=(s,i=s)=>C`
  :host {
    align-items: baseline;
    column-gap: var(--vaadin-${O(i)}-gap, var(--vaadin-gap-s));
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

  [part='${O(s)}'],
  ::slotted(input),
  [part='label'],
  ::slotted(label) {
    grid-row: 1;
  }

  [part='label'],
  ::slotted(label) {
    font-size: var(--vaadin-${O(i)}-label-font-size, var(--vaadin-input-field-label-font-size, inherit));
    line-height: var(--vaadin-${O(i)}-label-line-height, var(--vaadin-input-field-label-line-height, inherit));
    font-weight: var(--vaadin-${O(i)}-font-weight, var(--vaadin-input-field-label-font-weight, 500));
    color: var(--vaadin-${O(i)}-label-color, var(--vaadin-input-field-label-color, var(--vaadin-text-color)));
    word-break: break-word;
    cursor: var(--_cursor);
    /* TODO clicking the label part doesn't toggle the checked state, even though it triggers the active state */
  }

  [part='${O(s)}'],
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
  [part='${O(s)}'] {
    background: var(--vaadin-${O(i)}-background, var(--vaadin-background-color));
    border-color: var(--vaadin-${O(i)}-border-color, var(--vaadin-input-field-border-color, var(--vaadin-border-color)));
    border-radius: var(--vaadin-${O(i)}-border-radius, var(--vaadin-radius-s));
    border-style: var(--_border-style, solid);
    --_border-width: var(--vaadin-${O(i)}-border-width, var(--vaadin-input-field-border-width, 1px));
    border-width: var(--_border-width);
    box-sizing: border-box;
    --_color: var(--vaadin-${O(i)}-marker-color, var(--vaadin-${O(i)}-background, var(--vaadin-background-color)));
    color: var(--_color);
    height: var(--vaadin-${O(i)}-size, 1lh);
    width: var(--vaadin-${O(i)}-size, 1lh);
    position: relative;
    cursor: var(--_cursor);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  :host(:is([checked], [indeterminate])) {
    --vaadin-${O(i)}-background: var(--vaadin-text-color);
    --vaadin-${O(i)}-border-color: transparent;
  }

  :host([disabled]) {
    --vaadin-${O(i)}-background: var(--vaadin-input-field-disabled-background, var(--vaadin-background-container-strong));
    --vaadin-${O(i)}-border-color: transparent;
    --vaadin-${O(i)}-marker-color: var(--vaadin-text-color-disabled);
  }

  /* Focus ring */
  :host([focus-ring]) [part='${O(s)}'] {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--_border-width) * -1);
  }

  :host([focus-ring]:is([checked], [indeterminate])) [part='${O(s)}'] {
    outline-offset: 1px;
  }

  :host([readonly][focus-ring]) [part='${O(s)}'] {
    --vaadin-${O(i)}-border-color: transparent;
    outline-offset: calc(var(--_border-width) * -1);
    outline-style: dashed;
  }

  /* Checked indicator (checkmark, dot) */
  [part='${O(s)}']::after {
    content: '\\2003' / '';
    background: currentColor;
    border-radius: inherit;
    display: flex;
    align-items: center;
    --_filter: var(--vaadin-${O(i)}-marker-color, saturate(0) invert(1) hue-rotate(180deg) contrast(100) brightness(100));
    filter: var(--_filter);
  }

  :host(:not([checked], [indeterminate])) [part='${O(s)}']::after {
    opacity: 0;
  }

  @media (forced-colors: active) {
    :host(:is([checked], [indeterminate])) {
      --vaadin-${O(i)}-border-color: CanvasText !important;
    }

    :host(:is([checked], [indeterminate])) [part='${O(s)}'] {
      background: SelectedItem !important;
    }

    :host(:is([checked], [indeterminate])) [part='${O(s)}']::after {
      background: SelectedItemText !important;
    }

    :host([readonly]) [part='${O(s)}']::after {
      background: CanvasText !important;
    }

    :host([disabled]) {
      --vaadin-${O(i)}-border-color: GrayText !important;
    }

    :host([disabled]) [part='${O(s)}']::after {
      background: GrayText !important;
    }
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const hc=C`
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
`,cc=[vt,gr("checkbox"),hc];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const vr=J(s=>class extends Kt(Ae(yt(s))){static get properties(){return{checked:{type:Boolean,value:!1,notify:!0,reflectToAttribute:!0,sync:!0}}}static get delegateProps(){return[...super.delegateProps,"checked"]}_onChange(e){const t=e.target;this._toggleChecked(t.checked)}_toggleChecked(e){this.checked=e}});/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const uc=s=>class extends gt(wt(vr(bt(Qt(s))))){static get properties(){return{indeterminate:{type:Boolean,notify:!0,value:!1,reflectToAttribute:!0},name:{type:String,value:""},readonly:{type:Boolean,value:!1,reflectToAttribute:!0}}}static get observers(){return["__readonlyChanged(readonly, inputElement)"]}static get delegateProps(){return[...super.delegateProps,"indeterminate"]}static get delegateAttrs(){return[...super.delegateAttrs,"name","invalid","required"]}constructor(){super(),this._setType("checkbox"),this._boundOnInputClick=this._onInputClick.bind(this),this.value="on",this.tabindex=0}get slotStyles(){return[`
          ${this.localName} > input[slot='input'] {
            opacity: 0;
          }
        `]}ready(){super.ready(),this.addController(new Te(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new ve(this.inputElement,this._labelController)),this._createMethodObserver("_checkedChanged(checked)")}_shouldSetActive(e){return this.readonly||e.target.localName==="a"||e.target===this._helperNode||e.target===this._errorNode?!1:super._shouldSetActive(e)}_addInputListeners(e){super._addInputListeners(e),e.addEventListener("click",this._boundOnInputClick)}_removeInputListeners(e){super._removeInputListeners(e),e.removeEventListener("click",this._boundOnInputClick)}_onInputClick(e){this.readonly&&e.preventDefault()}__readonlyChanged(e,t){t&&(e?t.setAttribute("aria-readonly","true"):t.removeAttribute("aria-readonly"))}_toggleChecked(e){this.indeterminate&&(this.indeterminate=!1),super._toggleChecked(e)}checkValidity(){return!this.required||!!this.checked}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}_checkedChanged(e){(e||this.__oldChecked)&&this._requestValidation(),this.__oldChecked=e}_requiredChanged(e){super._requiredChanged(e),e===!1&&this._requestValidation()}_onRequiredIndicatorClick(){this._labelNode.click()}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class _c extends uc(L(T(I(A(E))))){static get is(){return"vaadin-checkbox"}static get styles(){return cc}render(){return y`
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
    `}ready(){super.ready(),this._tooltipController=new X(this),this._tooltipController.setAriaTarget(this.inputElement),this.addController(this._tooltipController)}}w(_c);/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class pc extends ss(T(z(I(A(E))))){static get is(){return"vaadin-combo-box-item"}static get styles(){return Et}render(){return y`
      <span part="checkmark" aria-hidden="true"></span>
      <div part="content">
        <slot></slot>
      </div>
    `}}w(pc);/**
 * @license
 * Copyright (c) 2026 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const br=C`
  @keyframes fade-in {
    0% {
      opacity: 0;
    }
  }

  @keyframes spin {
    to {
      rotate: 1turn;
    }
  }

  [part='loader'] {
    animation:
      spin var(--vaadin-spinner-animation-duration, 1s) linear infinite,
      fade-in 0.3s 0.3s both;
    border: var(--vaadin-spinner-width, 2px) solid;
    --_spinner-color: var(--vaadin-spinner-color, var(--vaadin-text-color));
    --_spinner-color2: color-mix(in srgb, var(--_spinner-color) 20%, transparent);
    border-color: var(--_spinner-color) var(--_spinner-color) var(--_spinner-color2) var(--_spinner-color2);
    border-radius: 50%;
    box-sizing: border-box;
    height: var(--vaadin-spinner-size, 1lh);
    pointer-events: none;
    width: var(--vaadin-spinner-size, 1lh);
  }

  :host(:not([loading])) [part~='loader'] {
    display: none;
  }

  @media (forced-colors: active) {
    [part='loader'] {
      forced-color-adjust: none;
      --vaadin-spinner-color: CanvasText;
    }
  }
`;/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const yr=[br,C`
    :host {
      --vaadin-item-checkmark-display: block;
    }

    [part='overlay'] {
      position: relative;
      width: var(--vaadin-combo-box-overlay-width, var(--_vaadin-combo-box-overlay-default-width, auto));
    }

    [part='content'] {
      display: flex;
      flex-direction: column;
      height: 100%;
    }

    :host([loading]) [part='content'] {
      --_items-min-height: calc(var(--vaadin-icon-size, 1lh) + 4px);
    }

    [part='loader'] {
      position: absolute;
      inset: var(--vaadin-item-overlay-padding, 4px);
      inset-block-end: auto;
      inset-inline-start: auto;
      margin: 2px;
    }
  `];/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class fc extends ns(ge(z(T(I(A(E)))))){static get is(){return"vaadin-combo-box-overlay"}static get styles(){return[me,yr]}render(){return y`
      <div part="overlay" id="overlay">
        <div part="loader"></div>
        <div part="content" id="content"><slot></slot></div>
      </div>
    `}}w(fc);/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class mc extends rs(I(E)){static get is(){return"vaadin-combo-box-scroller"}static get styles(){return os}render(){return y`
      <div id="selector">
        <slot></slot>
      </div>
    `}}w(mc);/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const wr=C`
  :host([opened]) {
    pointer-events: auto;
  }

  [part~='toggle-button']::before {
    mask-image: var(--_vaadin-icon-chevron-down);
  }

  :host([readonly]) [part~='toggle-button'] {
    display: none;
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ls{context;pageSize;items=[];pendingRequests={};#e={};#i=0;#t=0;constructor(i,e,t,n,r){this.context=i,this.pageSize=e,this.size=t,this.parentCache=n,this.parentCacheIndex=r,this.#t=t||0}get parentItem(){return this.parentCache&&this.parentCache.items[this.parentCacheIndex]}get subCaches(){return Object.values(this.#e)}get isLoading(){return Object.keys(this.pendingRequests).length>0?!0:this.subCaches.some(i=>i.isLoading)}get flatSize(){return this.#t}get size(){return this.#i}set size(i){if(this.#i!==i){if(this.#i=i,this.context.placeholder!==void 0){this.items.length=i||0;for(let t=0;t<i;t++)this.items[t]||=this.context.placeholder}this.items.length>i&&(this.items.length=i||0),Object.keys(this.pendingRequests).forEach(t=>{parseInt(t)*this.pageSize>=this.size&&delete this.pendingRequests[t]})}}recalculateFlatSize(){this.#t=!this.parentItem||this.context.isExpanded(this.parentItem)?this.size+this.subCaches.reduce((i,e)=>(e.recalculateFlatSize(),i+e.flatSize),0):0}setPage(i,e){const t=i*this.pageSize;e.forEach((n,r)=>{const o=t+r;(this.size===void 0||o<this.size)&&(this.items[o]=n)})}getSubCache(i){return this.#e[i]}removeSubCache(i){delete this.#e[i]}removeSubCaches(){this.#e={}}createSubCache(i){const e=new ls(this.context,this.pageSize,0,this,i);return this.#e[i]=e,e}getFlatIndex(i){const e=Math.max(0,Math.min(this.size-1,i));return this.subCaches.reduce((t,n)=>{const r=n.parentCacheIndex;return e>r?t+n.flatSize:t},e)}}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Cr(s,i,e=0){let t=i;for(const n of s.subCaches){const r=n.parentCacheIndex;if(t<=r)break;if(t<=r+n.flatSize)return Cr(n,t-r-1,e+1);t-=n.flatSize}return{cache:s,item:s.items[t],index:t,page:Math.floor(t/s.pageSize),level:e}}function xr({getItemId:s},i,e,t=0,n=0){for(let r=0;r<i.items.length;r++){const o=i.items[r];if(o&&s(o)===s(e))return{cache:i,level:t,item:o,index:r,page:Math.floor(r/i.pageSize),subCache:i.getSubCache(r),flatIndex:n+i.getFlatIndex(r)}}for(const r of i.subCaches){const o=n+i.getFlatIndex(r.parentCacheIndex),a=xr({getItemId:s},r,e,t+1,o+1);if(a)return a}}function Er(s,[i,...e],t=0){i===1/0&&(i=s.size-1);const n=s.getFlatIndex(i),r=s.getSubCache(i);return r&&r.flatSize>0&&e.length?Er(r,e,t+n+1):t+n}/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ir extends EventTarget{host;dataProvider;dataProviderParams;pageSize;isExpanded;getItemId;rootCache;placeholder;isPlaceholder;constructor(i,{size:e,pageSize:t,isExpanded:n,getItemId:r,isPlaceholder:o,placeholder:a,dataProvider:l,dataProviderParams:d}){super(),this.host=i,this.pageSize=t,this.getItemId=r,this.isExpanded=n,this.placeholder=a,this.isPlaceholder=o,this.dataProvider=l,this.dataProviderParams=d,this.rootCache=this.#i(e)}get flatSize(){return this.rootCache.flatSize}get#e(){return{isExpanded:this.isExpanded,placeholder:this.placeholder}}isLoading(){return this.rootCache.isLoading}setPageSize(i){this.pageSize=i,this.clearCache()}setDataProvider(i){this.dataProvider=i,this.clearCache()}recalculateFlatSize(){this.rootCache.recalculateFlatSize()}clearCache(){this.rootCache=this.#i(this.rootCache.size)}getFlatIndexContext(i){return Cr(this.rootCache,i)}getItemContext(i){return xr({getItemId:this.getItemId},this.rootCache,i)}getFlatIndexByPath(i){return Er(this.rootCache,i)}ensureFlatIndexLoaded(i){const{cache:e,page:t,item:n}=this.getFlatIndexContext(i);this.#s(n)||this.#t(e,t)}ensureFlatIndexHierarchy(i){const{cache:e,item:t,index:n}=this.getFlatIndexContext(i);if(this.#s(t)&&this.isExpanded(t)&&!e.getSubCache(n)){const r=e.createSubCache(n);this.#t(r,0)}}loadFirstPage(){this.#t(this.rootCache,0)}_shouldLoadCachePage(i,e){return!0}#i(i){return new ls(this.#e,this.pageSize,i)}#t(i,e){if(!this.dataProvider||i.pendingRequests[e]||!this._shouldLoadCachePage(i,e))return;let t={page:e,pageSize:this.pageSize,parentItem:i.parentItem};this.dataProviderParams&&(t={...t,...this.dataProviderParams()});const n=(r,o)=>{i.pendingRequests[e]===n&&(o!==void 0?i.size=o:t.parentItem&&(i.size=r.length),i.setPage(e,r),this.recalculateFlatSize(),this.dispatchEvent(new CustomEvent("page-received")),delete i.pendingRequests[e],this.dispatchEvent(new CustomEvent("page-loaded")))};i.pendingRequests[e]=n,this.dispatchEvent(new CustomEvent("page-requested")),this.dataProvider(t,n)}#s(i){return this.isPlaceholder?!this.isPlaceholder(i):this.placeholder?i!==this.placeholder:!!i}}/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Sr=s=>class extends s{static get properties(){return{pageSize:{type:Number,value:50,observer:"_pageSizeChanged",sync:!0},size:{type:Number,observer:"_sizeChanged",sync:!0},dataProvider:{type:Object,observer:"_dataProviderChanged",sync:!0}}}static get observers(){return["_dataProviderFilterChanged(filter)","_ensureFirstPage(opened)"]}constructor(){super(),this.__dataProviderInitialized=!1,this.__previousDataProviderFilter,this.__dataProviderController=new Ir(this,{placeholder:new fe,isPlaceholder:e=>e instanceof fe,dataProviderParams:()=>({filter:this.filter})}),this.__dataProviderController.addEventListener("page-requested",this.__onDataProviderPageRequested.bind(this)),this.__dataProviderController.addEventListener("page-loaded",this.__onDataProviderPageLoaded.bind(this))}ready(){super.ready(),this._scroller.addEventListener("index-requested",e=>{if(!this._shouldFetchData())return;const t=e.detail.index;t!==void 0&&this.__dataProviderController.ensureFlatIndexLoaded(t)}),this.__dataProviderInitialized=!0,this.dataProvider&&this.__synchronizeControllerState()}_dataProviderFilterChanged(e){if(this.__previousDataProviderFilter===void 0&&e===""){this.__previousDataProviderFilter=e;return}this.__previousDataProviderFilter!==e&&(this.__previousDataProviderFilter=e,this.__keepOverlayOpened=!0,this.size=void 0,this.clearCache(),this.__keepOverlayOpened=!1)}_shouldFetchData(){return this.dataProvider?this.opened||this.filter&&this.filter.length:!1}_ensureFirstPage(e){!this._shouldFetchData()||!e||(this._forceNextRequest||this.size===void 0?(this._forceNextRequest=!1,this.__dataProviderController.loadFirstPage()):this.size>0&&this.__dataProviderController.ensureFlatIndexLoaded(0))}__onDataProviderPageRequested(){this.loading=!0}__onDataProviderPageLoaded(){const{rootCache:e}=this.__dataProviderController;e.items=[...e.items],this.__synchronizeControllerState(),!this.opened&&!this._isInputFocused()&&this._commitValue()}clearCache(){this.dataProvider&&(this.__dataProviderController.clearCache(),this.__synchronizeControllerState(),this._shouldFetchData()?(this._forceNextRequest=!1,this.__dataProviderController.loadFirstPage()):this._forceNextRequest=!0)}_sizeChanged(e){const{rootCache:t}=this.__dataProviderController;t.size!==e&&(t.size=e,t.items=[...t.items],this.__synchronizeControllerState())}_filteredItemsChanged(e){if(super._filteredItemsChanged(e),this.dataProvider&&e){const{rootCache:t}=this.__dataProviderController;t.items!==e&&(t.items=e,this.__synchronizeControllerState())}}__synchronizeControllerState(){if(this.__dataProviderInitialized&&this.dataProvider){const{rootCache:e}=this.__dataProviderController;this.size=e.size,this.filteredItems=e.items,this.loading=this.__dataProviderController.isLoading()}}_pageSizeChanged(e,t){if(Math.floor(e)!==e||e<1)throw this.pageSize=t,new Error("`pageSize` value must be an integer > 0");this.__dataProviderController.setPageSize(e),this.clearCache()}_dataProviderChanged(e,t){this._ensureItemsOrDataProvider(()=>{this.dataProvider=t}),this.__dataProviderController.setDataProvider(e),this.clearCache()}_ensureItemsOrDataProvider(e){if(this.items!==void 0&&this.dataProvider!==void 0)throw e(),new Error("Using `items` and `dataProvider` together is not supported")}};/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function gc(s){return s!=null}function Ys(s,i){return s.findIndex(e=>e instanceof fe?!1:i(e))}const kr=s=>class extends hr(s){static get properties(){return{items:{type:Array,sync:!0,observer:"_itemsChanged"},filteredItems:{type:Array,observer:"_filteredItemsChanged",sync:!0},filter:{type:String,value:"",notify:!0,sync:!0},itemLabelGenerator:{type:Object},itemLabelPath:{type:String,value:"label",observer:"_itemLabelPathChanged",sync:!0},itemValuePath:{type:String,value:"value",sync:!0}}}updated(e){super.updated(e),e.has("filter")&&this._filterChanged(this.filter),e.has("itemLabelGenerator")&&this.requestContentUpdate()}_onInput(e){const t=this._inputElementValue,n={};this.filter===t?this._filterChanged(this.filter):n.filter=t,!this.opened&&!this._isClearButton(e)&&!this.autoOpenDisabled&&(n.opened=!0),this.setProperties(n)}_getItemLabel(e){if(typeof this.itemLabelGenerator=="function"&&e)return this.itemLabelGenerator(e)||"";let t=e&&this.itemLabelPath?Ee(this.itemLabelPath,e):void 0;return t==null&&(t=e?e.toString():""),t}_getItemValue(e){let t=e&&this.itemValuePath?Ee(this.itemValuePath,e):void 0;return t===void 0&&(t=e?e.toString():""),t}_itemLabelPathChanged(e){typeof e!="string"&&console.error("You should set itemLabelPath to a valid string")}_filterChanged(e){this._scrollIntoView(0),this._focusedIndex=-1,this.items?this.filteredItems=this._filterItems(this.items,e):this._filteredItemsChanged(this.filteredItems)}_itemsChanged(e,t){this._ensureItemsOrDataProvider(()=>{this.items=t}),e?this.filteredItems=e.slice(0):t&&(this.filteredItems=null)}_filteredItemsChanged(e){this._setDropdownItems(e)}_setDropdownItems(){}_filterItems(e,t){return e&&e.filter(r=>(t=t?t.toString().toLowerCase():"",this._getItemLabel(r).toString().toLowerCase().indexOf(t)>-1))}__getItemIndexByValue(e,t){return!e||!gc(t)?-1:Ys(e,n=>this._getItemValue(n)===t)}__getItemIndexByLabel(e,t){return!e||!t?-1:Ys(e,n=>this._getItemLabel(n).toString().toLowerCase()===t.toString().toLowerCase())}};/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function vc(s){return s!=null}const bc=s=>class extends Yi(kr(s)){static get properties(){return{renderer:{type:Object,sync:!0},allowCustomValue:{type:Boolean,value:!1},loading:{type:Boolean,value:!1,reflectToAttribute:!0,sync:!0},selectedItem:{type:Object,notify:!0,sync:!0},itemClassNameGenerator:{type:Object},itemIdPath:{type:String,sync:!0},__keepOverlayOpened:{type:Boolean,sync:!0}}}static get observers(){return["_openedOrItemsChanged(opened, _dropdownItems, loading, __keepOverlayOpened)","_selectedItemChanged(selectedItem, itemValuePath, itemLabelPath)","_updateScroller(opened, _dropdownItems, _focusedIndex, _theme)"]}ready(){super.ready(),this._lastCommittedValue=this.value}requestContentUpdate(){this._scroller&&(this._scroller.requestContentUpdate(),this._getItemElements().forEach(e=>{e.requestContentUpdate()}))}updated(e){super.updated(e),["loading","itemIdPath","itemClassNameGenerator","renderer","selectedItem"].forEach(t=>{e.has(t)&&(this._scroller[t]=this[t])})}_updateScroller(e,t,n,r){e&&(this._scroller.style.maxHeight=getComputedStyle(this).getPropertyValue(`--${this._tagNamePrefix}-overlay-max-height`)||"65vh"),this._scroller.setProperties({items:e?t:[],opened:e,focusedIndex:n,theme:r})}_openedOrItemsChanged(e,t,n,r){this._overlayOpened=e&&(r||n||!!(t&&t.length))}_onClearButtonClick(e){super._onClearButtonClick(e),this.opened&&this.requestContentUpdate()}_inputElementChanged(e){super._inputElementChanged(e),e&&this._revertInputValueToValue()}_closeOrCommit(){!this.opened&&!this.loading?this._commitValue():this.close()}_hasValidInputValue(){const e=this._focusedIndex<0&&this._inputElementValue!==""&&this._getItemLabel(this.selectedItem)!==this._inputElementValue;return this.allowCustomValue||!e}_onEscapeCancel(){this.cancel()}_onClearAction(){this.selectedItem=null,this.allowCustomValue&&(this.value=""),this._detectAndDispatchChange()}_clearFilter(){this.filter=""}cancel(){this._revertInputValueToValue(),this._lastCommittedValue=this.value,this._closeOrCommit()}_onOpened(){this.dispatchEvent(new CustomEvent("vaadin-combo-box-dropdown-opened",{bubbles:!0,composed:!0})),this._lastCommittedValue=this.value}_onOverlayClosed(){this.dispatchEvent(new CustomEvent("vaadin-combo-box-dropdown-closed",{bubbles:!0,composed:!0}))}_onClosed(){(!this.loading||this.allowCustomValue)&&this._commitValue()}_commitValue(){if(this._focusedIndex>-1){const e=this._dropdownItems[this._focusedIndex];this.selectedItem!==e&&(this.selectedItem=e),this._inputElementValue=this._getItemLabel(this.selectedItem),this._focusedIndex=-1}else if(this._inputElementValue===""||this._inputElementValue===void 0)this.selectedItem=null,this.allowCustomValue&&(this.value="");else{const e=[this.selectedItem,...this._dropdownItems||[]],t=e[this.__getItemIndexByLabel(e,this._inputElementValue)];if(this.allowCustomValue&&!t){const n=this._inputElementValue;this._lastCustomValue=n;const r=new CustomEvent("custom-value-set",{detail:n,composed:!0,cancelable:!0,bubbles:!0});this.dispatchEvent(r),r.defaultPrevented||(this.value=n)}else!this.allowCustomValue&&!this.opened&&t?this.value=this._getItemValue(t):this._revertInputValueToValue()}this._detectAndDispatchChange(),this._clearSelectionRange(),this._clearFilter()}_onChange(e){e.stopPropagation()}_revertInputValue(){this.filter!==""?this._inputElementValue=this.filter:this._revertInputValueToValue(),this._clearSelectionRange()}_revertInputValueToValue(){this.allowCustomValue&&!this.selectedItem?this._inputElementValue=this.value:this._inputElementValue=this._getItemLabel(this.selectedItem)}_selectedItemChanged(e){if(e==null)this.filteredItems&&(this.allowCustomValue||(this.value=""),this._toggleHasValue(this._hasValue),this._inputElementValue=this.value);else{const t=this._getItemValue(e);if(this.value!==t&&(this.value=t,this.value!==t))return;this._toggleHasValue(!0),this._inputElementValue=this._getItemLabel(e)}}_valueChanged(e,t){e===""&&t===void 0||(vc(e)?(this._getItemValue(this.selectedItem)!==e&&this._selectItemForValue(e),!this.selectedItem&&this.allowCustomValue&&(this._inputElementValue=e),this._toggleHasValue(this._hasValue)):this.selectedItem=null,this._clearFilter(),this._lastCommittedValue=void 0)}_detectAndDispatchChange(){document.hasFocus()&&this._requestValidation(),this.value!==this._lastCommittedValue&&(this.dispatchEvent(new CustomEvent("change",{bubbles:!0})),this._lastCommittedValue=this.value)}_selectItemForValue(e){const t=this.__getItemIndexByValue(this.filteredItems,e),n=this.selectedItem;t>=0?this.selectedItem=this.filteredItems[t]:this.dataProvider&&this.selectedItem===void 0?this.selectedItem=void 0:this.selectedItem=null,this.selectedItem===null&&n===null&&this._selectedItemChanged(this.selectedItem)}_setDropdownItems(e){const t=this._dropdownItems;this._dropdownItems=e;const n=t?t[this._focusedIndex]:null,r=this.__getItemIndexByValue(e,this.value);(this.selectedItem===null||this.selectedItem===void 0)&&r>=0&&(this.selectedItem=e[r]);const o=this.__getItemIndexByValue(e,this._getItemValue(n));o>-1?this._focusedIndex=o:this._focusedIndex=this.__getItemIndexByLabel(e,this.filter)}_handleFocusOut(){if(!this.opened&&this.allowCustomValue&&this._inputElementValue===this._lastCustomValue){delete this._lastCustomValue;return}super._handleFocusOut()}};/**
 * @license
 * Copyright (c) 2015 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class yc extends Sr(bc(cr(Ct(T(L(I(A(E)))))))){static get is(){return"vaadin-combo-box"}static get styles(){return[ke,wr]}static get properties(){return{_positionTarget:{type:Object}}}get clearElement(){return this.$.clearButton}render(){return y`
      <div class="vaadin-combo-box-container">
        <div part="label">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true" @click="${this.focus}"></span>
        </div>

        <vaadin-input-container
          part="input-field"
          .readonly="${this.readonly}"
          .disabled="${this.disabled}"
          .invalid="${this.invalid}"
          theme="${B(this._theme)}"
        >
          <slot name="prefix" slot="prefix"></slot>
          <slot name="input"></slot>
          <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
          <div id="toggleButton" part="field-button toggle-button" slot="suffix" aria-hidden="true"></div>
        </vaadin-input-container>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>

        <slot name="tooltip"></slot>
      </div>

      <vaadin-combo-box-overlay
        id="overlay"
        exportparts="overlay, content, loader"
        .owner="${this}"
        .dir="${this.dir}"
        .opened="${this._overlayOpened}"
        ?loading="${this.loading}"
        theme="${B(this._theme)}"
        .positionTarget="${this._positionTarget}"
        no-vertical-overlap
      >
        <slot name="overlay"></slot>
      </vaadin-combo-box-overlay>
    `}ready(){super.ready(),this.addController(new Te(this,i=>{this._setInputElement(i),this._setFocusElement(i),this.stateTarget=i,this.ariaTarget=i})),this.addController(new ve(this.inputElement,this._labelController)),this._tooltipController=new X(this),this.addController(this._tooltipController),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this._tooltipController.setShouldShow(i=>!i.opened),this._positionTarget=this.shadowRoot.querySelector('[part="input-field"]'),this._toggleElement=this.$.toggleButton}updated(i){super.updated(i),(i.has("dataProvider")||i.has("value"))&&this._warnDataProviderValue(this.dataProvider,this.value)}_onClearButtonClick(i){i.stopPropagation(),super._onClearButtonClick(i)}_onHostClick(i){const e=i.composedPath();(e.includes(this._labelNode)||e.includes(this._positionTarget))&&super._onHostClick(i)}_warnDataProviderValue(i,e){if(i&&e!==""&&(this.selectedItem===void 0||this.selectedItem===null)){const t=this.__getItemIndexByValue(this.filteredItems,e);(t<0||!this._getItemLabel(this.filteredItems[t]))&&console.warn("Warning: unable to determine the label for the provided `value`. Nothing to display in the text field. This usually happens when setting an initial `value` before any items are returned from the `dataProvider` callback. Consider setting `selectedItem` instead of `value`")}}}w(yc);window.Vaadin.Flow.comboBoxConnector={};window.Vaadin.Flow.comboBoxConnector.initLazy=s=>{if(s.$connector)return;s.$connector={};const i={};let e={},t="";const n=new window.Vaadin.ComboBoxPlaceholder,r=(()=>{let d="",h=!1;return{needsDataCommunicatorReset:()=>h=!0,getLastFilterSentToServer:()=>d,requestData:(v,x,b)=>{const k=x-v,u=b.filter;s.$server.setViewportRange(v,k,u),d=u,h&&(s.$server.resetDataCommunicator(),h=!1)}}})(),o=(d=Object.keys(i))=>{d.forEach(h=>{i[h]([],s.size),delete i[h];const c=parseInt(h)*s.pageSize,f=c+s.pageSize,m=Math.min(f,s.filteredItems.length);for(let v=c;v<m;v++)s.filteredItems[v]=n})};s.dataProvider=function(d,h){if(d.pageSize!=s.pageSize)throw"Invalid pageSize";if(s._clientSideFilter)if(e[0]){l(e[0],d.filter,h);return}else d.filter="";if(d.filter!==t){e={},t=d.filter,this._filterDebouncer=D.debounce(this._filterDebouncer,K.after(500),()=>{if(r.getLastFilterSentToServer()===d.filter&&r.needsDataCommunicatorReset(),d.filter!==t)throw new Error("Expected params.filter to be '"+t+"' but was '"+d.filter+"'");this._filterDebouncer=void 0,o(),s.dataProvider(d,h)});return}if(this._filterDebouncer){i[d.page]=h;return}if(e[d.page])a(d.page,h);else{i[d.page]=h;const f=Math.max(d.pageSize*2,500),m=Object.keys(i).map(b=>parseInt(b)),v=Math.min(...m),x=Math.max(...m);if(m.length*d.pageSize>f)d.page===v?o([String(x)]):o([String(v)]),s.dataProvider(d,h);else if(x-v+1!==m.length)o();else{const b=d.pageSize*v,k=d.pageSize*(x+1);r.requestData(b,k,d)}}},s.$connector.clear=(d,h)=>{const c=Math.floor(d/s.pageSize),f=Math.ceil(h/s.pageSize);for(let m=c;m<c+f;m++)delete e[m]},s.$connector.filter=(d,h)=>(h=h?h.toString().toLowerCase():"",s._getItemLabel(d,s.itemLabelPath).toString().toLowerCase().indexOf(h)>-1),s.$connector.set=(d,h,c)=>{if(c!=r.getLastFilterSentToServer())return;if(d%s.pageSize!=0)throw"Got new data to index "+d+" which is not aligned with the page size of "+s.pageSize;if(d===0&&h.length===0&&i[0]){e[0]=[];return}const f=d/s.pageSize,m=Math.ceil(h.length/s.pageSize);for(let v=0;v<m;v++){let x=f+v,b=h.slice(v*s.pageSize,(v+1)*s.pageSize);e[x]=b}},s.$connector.updateData=d=>{const h=new Map(d.map(c=>[c.key,c]));s.filteredItems=s.filteredItems.map(c=>h.get(c.key)||c)},s.$connector.updateSize=function(d){s._clientSideFilter||(s.size=d)},s.$connector.reset=function(){o(),e={},s.clearCache()},s.$connector.confirm=function(d,h){if(h!=r.getLastFilterSentToServer())return;let c=Object.getOwnPropertyNames(i);for(let f=0;f<c.length;f++){let m=c[f];e[m]&&a(m,i[m])}s.$server.confirmUpdate(d)};const a=function(d,h){let c=e[d];s._clientSideFilter?l(c,s.filter,h):(delete e[d],h(c,s.size))},l=function(d,h,c){let f=d;h&&(f=d.filter(m=>s.$connector.filter(m,h))),c(f,f.length)};s.addEventListener("custom-value-set",d=>d.preventDefault()),s.itemClassNameGenerator=function(d){return d.className||""}};window.Vaadin.ComboBoxPlaceholder=fe;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const wc=C`
  :host {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    box-sizing: border-box;
    gap: var(--vaadin-chip-gap, 0);
    background: var(--vaadin-chip-background, var(--vaadin-background-container));
    color: var(--vaadin-chip-text-color, var(--vaadin-text-color));
    font-size: max(11px, var(--vaadin-chip-font-size, 0.875em));
    font-weight: var(--vaadin-chip-font-weight, 500);
    line-height: var(--vaadin-input-field-value-line-height, inherit);
    padding: 0 var(--vaadin-chip-padding, 0.3em);
    height: var(--vaadin-chip-height, calc(1lh / 0.875));
    border-radius: var(--vaadin-chip-border-radius, var(--vaadin-radius-m));
    border: var(--vaadin-chip-border-width, 1px) solid
      var(--vaadin-chip-border-color, var(--vaadin-border-color-secondary));
    cursor: default;
  }

  :host(:not([slot='overflow'])) {
    min-width: min(max-content, var(--vaadin-multi-select-combo-box-chip-min-width, 48px));
  }

  :host([focused]) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--vaadin-chip-border-width, 1px) * -1);
  }

  [part='label'] {
    overflow: hidden;
    text-overflow: ellipsis;
    margin-block: calc(var(--vaadin-chip-border-width, 1px) * -1);
  }

  [part='remove-button'] {
    flex: none;
    display: block;
    margin-inline-start: auto;
    margin-block: calc(var(--vaadin-chip-border-width, 1px) * -1);
    color: var(--vaadin-chip-remove-button-text-color, var(--vaadin-text-color-secondary));
    cursor: var(--vaadin-clickable-cursor);
    translate: 25%;
  }

  [part='remove-button']::before {
    content: '';
    display: block;
    width: var(--vaadin-icon-size, 1lh);
    height: var(--vaadin-icon-size, 1lh);
    background: currentColor;
    mask-image: var(--_vaadin-icon-cross);
  }

  :host([disabled]) {
    cursor: var(--vaadin-disabled-cursor);
  }

  :host([disabled]) [part='label'] {
    --vaadin-chip-text-color: var(--vaadin-text-color-disabled);
  }

  :host([hidden]),
  :host(:is([readonly], [disabled], [slot='overflow'])) [part='remove-button'] {
    display: none !important;
  }

  :host([slot='overflow']) {
    position: relative;
    margin-inline-start: 8px;
    min-width: 1.5em;
  }

  :host([slot='overflow'])::before,
  :host([slot='overflow'])::after {
    content: '';
    position: absolute;
    inset: calc(var(--vaadin-chip-border-width, 1px) * -1);
    border-inline-start: 2px solid var(--vaadin-chip-border-color, var(--vaadin-border-color-secondary));
    border-radius: inherit;
  }

  :host([slot='overflow'])::before {
    left: calc(-4px - var(--vaadin-chip-border-width, 1px));
  }

  :host([slot='overflow'])::after {
    left: calc(-8px - var(--vaadin-chip-border-width, 1px));
  }

  :host([count='2']) {
    margin-inline-start: 4px;
  }

  :host([count='1']) {
    margin-inline-start: 0;
  }

  :host([count='2'])::after,
  :host([count='1'])::before,
  :host([count='1'])::after {
    display: none;
  }

  @media (forced-colors: active) {
    :host {
      border: 1px solid !important;
    }

    [part='remove-button']::before {
      background: CanvasText;
    }
  }
`;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Cc extends T(I(A(E))){static get is(){return"vaadin-multi-select-combo-box-chip"}static get styles(){return wc}static get properties(){return{disabled:{type:Boolean,reflectToAttribute:!0,sync:!0},readonly:{type:Boolean,reflectToAttribute:!0,sync:!0},label:{type:String,sync:!0},item:{type:Object}}}render(){return y`
      <div part="label">${this.label}</div>
      <div part="remove-button" @click="${this._onRemoveClick}"></div>
    `}_onRemoveClick(i){i.stopPropagation(),this.dispatchEvent(new CustomEvent("item-removed",{detail:{item:this.item},bubbles:!0,composed:!0}))}}w(Cc);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class xc extends En{static get is(){return"vaadin-multi-select-combo-box-container"}static get styles(){return[super.styles,C`
        #wrapper {
          display: flex;
          width: 100%;
          min-width: 0;
          gap: var(--_wrapper-gap);
          align-self: start;
        }

        :host([auto-expand-vertically]) #wrapper {
          flex-wrap: wrap;
        }
      `]}static get properties(){return{autoExpandVertically:{type:Boolean,reflectToAttribute:!0}}}render(){return y`
      <div id="wrapper">
        <slot name="prefix"></slot>
        <slot></slot>
      </div>
      <slot name="suffix"></slot>
    `}}w(xc);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ec extends ss(T(z(I(A(E))))){static get is(){return"vaadin-multi-select-combo-box-item"}static get styles(){return Et}render(){return y`
      <span part="checkmark" aria-hidden="true"></span>
      <div part="content">
        <slot></slot>
      </div>
    `}}w(Ec);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ic=[yr,C`
    #overlay {
      width: var(
        --vaadin-multi-select-combo-box-overlay-width,
        var(--_vaadin-multi-select-combo-box-overlay-default-width, auto)
      );
    }
  `];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Sc extends ns(ge(z(T(I(A(E)))))){static get is(){return"vaadin-multi-select-combo-box-overlay"}static get styles(){return[me,Ic]}render(){return y`
      <div part="overlay" id="overlay">
        <div part="loader"></div>
        <div part="content" id="content"><slot></slot></div>
      </div>
    `}}w(Sc);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const kc=os;/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Tc extends rs(I(E)){static get is(){return"vaadin-multi-select-combo-box-scroller"}static get styles(){return kc}render(){return y`
      <div id="selector">
        <slot></slot>
      </div>
    `}ready(){super.ready(),this.setAttribute("aria-multiselectable","true")}_isItemSelected(i,e,t){return i instanceof fe||this.owner.readonly?!1:this.owner._findIndex(i,this.owner.selectedItems,t)>-1}_updateElement(i,e){super._updateElement(i,e),i.toggleAttribute("readonly",this.owner.readonly)}}w(Tc);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ac=[wr,C`
    :host {
      max-width: 100%;
      --_input-min-width: var(--vaadin-multi-select-combo-box-input-min-width, 4rem);
      --_chip-min-width: var(--vaadin-multi-select-combo-box-chip-min-width, 48px);
      --_wrapper-gap: var(--vaadin-multi-select-combo-box-chips-gap, 2px);
    }

    #chips {
      display: flex;
      align-items: center;
      gap: var(--vaadin-multi-select-combo-box-chips-gap, 2px);
    }

    ::slotted(input) {
      box-sizing: border-box;
      flex: 1 0 var(--_input-min-width);
    }

    ::slotted([slot='chip']),
    ::slotted([slot='overflow']) {
      flex: 0 1 auto;
    }

    ::slotted([slot='chip']) {
      overflow: hidden;
    }

    :host(:is([readonly], [disabled])) ::slotted(input) {
      flex-grow: 0;
      flex-basis: 0;
      padding: 0;
    }

    :host([readonly]:not([disabled])) [part~='toggle-button'] {
      display: block;
      color: var(--vaadin-input-field-button-text-color, var(--vaadin-text-color-secondary));
    }

    :host([readonly]:not([disabled])) [part$='button'] {
      cursor: var(--vaadin-clickable-cursor);
    }

    :host([auto-expand-vertically]) #chips {
      display: contents;
    }

    :host([auto-expand-horizontally]) {
      --vaadin-field-default-width: auto;
    }
  `];/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Dc={cleared:"Selection cleared",focused:"focused. Press Backspace to remove",selected:"added to selection",deselected:"removed from selection",total:"{count} items selected"},Oc=s=>class extends ei(Dc,Sr(kr(Ct(Zt(s))))){static get properties(){return{autoExpandHorizontally:{type:Boolean,value:!1,reflectToAttribute:!0,sync:!0},autoExpandVertically:{type:Boolean,value:!1,reflectToAttribute:!0,sync:!0},itemClassNameGenerator:{type:Object,sync:!0},itemIdPath:{type:String,sync:!0},keepFilter:{type:Boolean,value:!1},loading:{type:Boolean,value:!1,reflectToAttribute:!0,sync:!0},readonly:{type:Boolean,value:!1,reflectToAttribute:!0,sync:!0},selectedItems:{type:Array,value:()=>[],notify:!0,sync:!0},allowCustomValue:{type:Boolean,value:!1},placeholder:{type:String,observer:"_placeholderChanged",reflectToAttribute:!0,sync:!0},renderer:{type:Function,sync:!0},selectedItemsOnTop:{type:Boolean,value:!1,sync:!0},value:{type:String},_overflowItems:{type:Array,value:()=>[],sync:!0},_focusedChipIndex:{type:Number,value:-1,observer:"_focusedChipIndexChanged"},_lastFilter:{type:String,sync:!0},_topGroup:{type:Array,observer:"_topGroupChanged",sync:!0},_inputField:{type:Object}}}static get observers(){return["_selectedItemsChanged(selectedItems)","__openedOrItemsChanged(opened, _dropdownItems, loading, __keepOverlayOpened)","__updateOverflowChip(_overflow, _overflowItems, disabled, readonly)","__updateScroller(opened, _dropdownItems, _focusedIndex, _theme)","__updateTopGroup(selectedItemsOnTop, selectedItems, opened)"]}get i18n(){return super.i18n}set i18n(e){super.i18n=e}get slotStyles(){const e=this.localName;return[...super.slotStyles,`
        ${e}[has-value] input::placeholder {
          color: transparent !important;
          forced-color-adjust: none;
        }
      `]}get clearElement(){return this.$.clearButton}get _chips(){return[...this.querySelectorAll('[slot="chip"]')]}get _hasValue(){return this.selectedItems&&this.selectedItems.length>0}get _tagNamePrefix(){return"vaadin-multi-select-combo-box"}ready(){super.ready(),this.addController(new Te(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new ve(this.inputElement,this._labelController)),this._tooltipController=new X(this),this.addController(this._tooltipController),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.inputElement),this._tooltipController.setShouldShow(e=>!e.opened),this._toggleElement=this.$.toggleButton,this._inputField=this.shadowRoot.querySelector('[part="input-field"]'),this._overflowController=new G(this,"overflow","vaadin-multi-select-combo-box-chip",{initializer:e=>{e.addEventListener("mousedown",t=>this._preventBlur(t)),this._overflow=e}}),this.addController(this._overflowController)}updated(e){super.updated(e),["loading","itemIdPath","itemClassNameGenerator","renderer"].forEach(n=>{e.has(n)&&(this._scroller[n]=this[n])}),e.has("selectedItems")&&this.opened&&this.$.overlay._updateOverlayWidth(),["autoExpandHorizontally","autoExpandVertically","disabled","readonly","clearButtonVisible","itemClassNameGenerator"].some(n=>e.has(n))&&this.__updateChips(),e.has("readonly")&&(this._setDropdownItems(this.filteredItems),this.dataProvider&&this.clearCache())}checkValidity(){return this.required&&!this.readonly?this._hasValue:!0}open(){!this.disabled&&!(this.readonly&&this.selectedItems.length===0)&&(this.opened=!0)}clear(){this.__updateSelection([]),Rt(this.__effectiveI18n.cleared)}__syncTopGroup(){this._topGroup=this.selectedItemsOnTop?[...this.selectedItems]:[]}clearCache(){this.readonly||(super.clearCache(),this.__syncTopGroup())}_itemsChanged(e,t){super._itemsChanged(e,t),this.__syncTopGroup()}requestContentUpdate(){this._scroller&&(this._scroller.requestContentUpdate(),this._getItemElements().forEach(e=>{e.requestContentUpdate()}))}_onClearAction(){this.clear()}_onClosed(){this._ignoreCommitValue=!0,(!this.loading||this.allowCustomValue)&&this._commitValue()}__updateScroller(e,t,n,r){e&&(this._scroller.style.maxHeight=getComputedStyle(this).getPropertyValue(`--${this._tagNamePrefix}-overlay-max-height`)||"65vh"),this._scroller.setProperties({items:e?t:[],opened:e,focusedIndex:n,theme:r})}__openedOrItemsChanged(e,t,n,r){this._overlayOpened=e&&(r||n||!!(t&&t.length))}_closeOrCommit(){this.opened?this.close():this._commitValue()}_commitValue(){this._lastFilter=this.filter,this._ignoreCommitValue?(this._inputElementValue="",this._focusedIndex=-1,this._ignoreCommitValue=!1):this.__commitUserInput(),(!this.keepFilter||!this.opened)&&(this.filter="")}__commitUserInput(){if(this._focusedIndex>-1){const e=this._dropdownItems[this._focusedIndex];this.__selectItem(e)}else if(this._inputElementValue){const e=[...this._dropdownItems],t=e[this.__getItemIndexByLabel(e,this._inputElementValue)];if(this.allowCustomValue&&!t){const n=this._inputElementValue;this._lastCustomValue=n,this.__clearInternalValue(!0),this.dispatchEvent(new CustomEvent("custom-value-set",{detail:n,composed:!0,bubbles:!0}))}else!this.allowCustomValue&&!this.opened&&t?this.__selectItem(t):this._inputElementValue=""}}_setFocused(e){e||(this._ignoreCommitValue=!0),super._setFocused(e),!e&&document.hasFocus()&&(this._focusedChipIndex=-1,this._requestValidation()),!e&&this.readonly&&!this._closeOnBlurIsPrevented&&this.close()}_onResize(){this.__updateChips()}_delegateAttribute(e,t){if(this.stateTarget){if(e==="required"){this._delegateAttribute("aria-required",t?"true":!1);return}super._delegateAttribute(e,t)}}_placeholderChanged(e){const t=this.__tmpA11yPlaceholder;t!==e&&(this.__savedPlaceholder=e,t&&(this.placeholder=t))}_selectedItemsChanged(e){if(this._toggleHasValue(this._hasValue),this._hasValue){const t=this._mergeItemLabels(e);this.__tmpA11yPlaceholder===void 0&&(this.__savedPlaceholder=this.placeholder),this.__tmpA11yPlaceholder=t,this.placeholder=t}else this.__tmpA11yPlaceholder!==void 0&&(delete this.__tmpA11yPlaceholder,this.placeholder=this.__savedPlaceholder);this.__updateChips(),this.requestContentUpdate()}_topGroupChanged(e){e&&this._setDropdownItems(this.filteredItems)}_hasValidInputValue(){const e=this._focusedIndex<0&&this._inputElementValue!=="";return this.allowCustomValue||!e}_shouldFetchData(){return this.readonly?!1:super._shouldFetchData()}_setDropdownItems(e){if(this.readonly){this.__setDropdownItems(this.selectedItems);return}if(this.filter||!this.selectedItemsOnTop){this.__setDropdownItems(e);return}if(e&&e.length&&this._topGroup&&this._topGroup.length){const t=e.filter(n=>this._findIndex(n,this._topGroup,this.itemIdPath)===-1);this.__setDropdownItems(this._topGroup.concat(t));return}this.__setDropdownItems(e)}__setDropdownItems(e){const t=this._dropdownItems;this._dropdownItems=e;const n=t?t[this._focusedIndex]:null,r=this.__getItemIndexByValue(e,this._getItemValue(n));r>-1?this._focusedIndex=r:this._focusedIndex=this.__getItemIndexByLabel(e,this.filter)}_mergeItemLabels(e){return e.map(t=>this._getItemLabel(t)).join(", ")}_findIndex(e,t,n){if(n&&e){for(let r=0;r<t.length;r++)if(t[r]&&t[r][n]===e[n])return r;return-1}return t.indexOf(e)}__clearInternalValue(e=!1){!this.keepFilter||e?(this.filter="",this._inputElementValue=""):this._inputElementValue=this.filter}__announceItem(e,t,n){const r=t?"selected":"deselected",o=this.__effectiveI18n.total.replace("{count}",n||0);Rt(`${e} ${this.__effectiveI18n[r]} ${o}`)}__removeItem(e){const t=[...this.selectedItems];t.splice(t.indexOf(e),1),this.__updateSelection(t);const n=this._getItemLabel(e);this.__announceItem(n,!1,t.length)}__selectItem(e){const t=[...this.selectedItems],n=this._findIndex(e,t,this.itemIdPath),r=this._getItemLabel(e);let o=!1;if(n!==-1){const a=this._lastFilter;if(a&&a.toLowerCase()===r.toLowerCase()){this.__clearInternalValue();return}t.splice(n,1)}else t.push(e),o=!0;this.__updateSelection(t),this.__clearInternalValue(),this.__announceItem(r,o,t.length)}__updateSelection(e){this.selectedItems=e,this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{bubbles:!0}))}__updateTopGroup(e,t,n){e?(!n||this.__needToSyncTopGroup())&&(this._topGroup=[...t]):this._topGroup=[]}__needToSyncTopGroup(){return this.itemIdPath?this._topGroup&&this._topGroup.some(e=>{const t=this.selectedItems[this._findIndex(e,this.selectedItems,this.itemIdPath)];return t&&e!==t}):!1}__createChip(e){const t=document.createElement("vaadin-multi-select-combo-box-chip");t.setAttribute("slot","chip"),t.item=e,t.disabled=this.disabled,t.readonly=this.readonly;const n=this._getItemLabel(e);return t.label=n,t.setAttribute("title",n),typeof this.itemClassNameGenerator=="function"&&(t.className=this.itemClassNameGenerator(e)),t.addEventListener("item-removed",r=>this._onItemRemoved(r)),t.addEventListener("mousedown",r=>this._preventBlur(r)),t}__getOverflowWidth(){const e=this._overflow;e.style.visibility="hidden",e.removeAttribute("hidden");const t=e.getAttribute("count");e.setAttribute("count","99");const n=getComputedStyle(e),r=e.clientWidth+parseInt(n.marginInlineStart);return e.setAttribute("count",t),e.setAttribute("hidden",""),e.style.visibility="",r}__updateChips(){if(!this._inputField||!this.inputElement)return;this._chips.forEach(a=>{a.remove()});const e=[...this.selectedItems],t=this._inputField.$.wrapper.clientWidth,n=parseInt(getComputedStyle(this.inputElement).flexBasis);let r=t-n;e.length>1&&(r-=this.__getOverflowWidth());const o=parseInt(getComputedStyle(this).getPropertyValue("--_chip-min-width"));if(this.autoExpandHorizontally){const a=[];for(let h=e.length-1,c=null;h>=0;h--){const f=this.__createChip(e[h]);this.insertBefore(f,c),c=f,a.unshift(f)}const l=[],d=this._inputField.$.wrapper.clientWidth-this.$.chips.clientWidth;if(!this.autoExpandVertically&&d<n){for(;a.length>1;){a.pop().remove(),l.unshift(e.pop());const c=l.length>0?n+this.__getOverflowWidth():n;if(this._inputField.$.wrapper.clientWidth-this.$.chips.clientWidth>=c)break}a.length===1&&(a[0].style.maxWidth=`${Math.max(o,r)}px`)}this._overflowItems=l;return}for(let a=e.length-1,l=null;a>=0;a--){const d=this.__createChip(e[a]);if(this.insertBefore(d,l),!this.autoExpandVertically){if(this.$.chips.clientWidth>r&&(r<o||l!==null)){d.remove();break}d.style.maxWidth=`${r}px`}e.pop(),l=d}this._overflowItems=e}__updateOverflowChip(e,t,n,r){if(e){const o=t.length;e.label=`${o}`,e.setAttribute("count",`${o}`),e.setAttribute("title",this._mergeItemLabels(t)),e.toggleAttribute("hidden",o===0),e.disabled=n,e.readonly=r}}_onClearButtonClick(e){e.stopPropagation(),super._onClearButtonClick(e),this.opened&&this.requestContentUpdate()}_onChange(e){e.stopPropagation()}_onEscape(e){if(this.readonly){e.stopPropagation(),this.opened&&this.close();return}this.clearButtonVisible&&!this.opened&&this.selectedItems&&this.selectedItems.length&&(e.stopPropagation(),this.selectedItems=[]),super._onEscape(e)}_onEscapeCancel(){this._closeOrCommit()}_onEnter(e){if(this.opened){if(e.preventDefault(),e.stopPropagation(),this.readonly)this.close();else if(this._hasValidInputValue()){const t=this._dropdownItems[this._focusedIndex];this._commitValue(),this._focusedIndex=this._dropdownItems.indexOf(t)}return}super._onEnter(e)}_onArrowDown(){this.readonly?this.opened||this.open():super._onArrowDown()}_onArrowUp(){this.readonly?this.opened||this.open():super._onArrowUp()}_onKeyDown(e){super._onKeyDown(e);const t=this._chips;if(!this.readonly&&t.length>0)switch(e.key){case"Backspace":this._onBackSpace(t);break;case"ArrowLeft":this._onArrowLeft(t,e);break;case"ArrowRight":this._onArrowRight(t,e);break;default:this._focusedChipIndex=-1;break}}_onArrowLeft(e,t){if(this.inputElement.selectionStart!==0)return;const n=this._focusedChipIndex;n!==-1&&t.preventDefault();let r;this.__isRTL?n===e.length-1?r=-1:n>-1&&(r=n+1):n===-1?r=e.length-1:n>0&&(r=n-1),r!==void 0&&(this._focusedChipIndex=r)}_onArrowRight(e,t){if(this.inputElement.selectionStart!==0)return;const n=this._focusedChipIndex;n!==-1&&t.preventDefault();let r;this.__isRTL?n===-1?r=e.length-1:n>0&&(r=n-1):n===e.length-1?r=-1:n>-1&&(r=n+1),r!==void 0&&(this._focusedChipIndex=r)}_onBackSpace(e){if(this.inputElement.selectionStart!==0)return;const t=this._focusedChipIndex;t===-1?this._focusedChipIndex=e.length-1:(this.__removeItem(e[t].item),this._focusedChipIndex=-1)}_focusedChipIndexChanged(e,t){if(e>-1||t>-1){const n=this._chips;if(n.forEach((r,o)=>{r.toggleAttribute("focused",o===e)}),e>-1){const r=n[e].item,o=this._getItemLabel(r);Rt(`${o} ${this.__effectiveI18n.focused}`)}}}_overlaySelectedItemChanged(e){e.stopPropagation(),!this.readonly&&(e.detail.item instanceof fe||this.opened&&(this._lastFilter=this._inputElementValue,this.__selectItem(e.detail.item)))}_onItemRemoved(e){this.__removeItem(e.detail.item)}_preventBlur(e){e.preventDefault()}};/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Pc extends Oc(T(L(I(A(E))))){static get is(){return"vaadin-multi-select-combo-box"}static get styles(){return[ke,Ac]}render(){return y`
      <div class="vaadin-multi-select-combo-box-container">
        <div part="label">
          <slot name="label"></slot>
          <span part="required-indicator" aria-hidden="true" @click="${this.focus}"></span>
        </div>

        <vaadin-multi-select-combo-box-container
          part="input-field"
          .autoExpandVertically="${this.autoExpandVertically}"
          .readonly="${this.readonly}"
          .disabled="${this.disabled}"
          .invalid="${this.invalid}"
          theme="${B(this._theme)}"
        >
          <slot name="overflow" slot="prefix"></slot>
          <div id="chips" part="chips" slot="prefix">
            <slot name="chip"></slot>
          </div>
          <slot name="input"></slot>
          <div id="clearButton" part="field-button clear-button" slot="suffix" aria-hidden="true"></div>
          <div id="toggleButton" part="field-button toggle-button" slot="suffix" aria-hidden="true"></div>
        </vaadin-multi-select-combo-box-container>

        <div part="helper-text">
          <slot name="helper"></slot>
        </div>

        <div part="error-message">
          <slot name="error-message"></slot>
        </div>

        <slot name="tooltip"></slot>
      </div>

      <vaadin-multi-select-combo-box-overlay
        id="overlay"
        exportparts="overlay, content, loader"
        .owner="${this}"
        .dir="${this.dir}"
        .opened="${this._overlayOpened}"
        ?loading="${this.loading}"
        theme="${B(this._theme)}"
        .positionTarget="${this._inputField}"
        no-vertical-overlap
      >
        <slot name="overlay"></slot>
      </vaadin-multi-select-combo-box-overlay>
    `}}w(Pc);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ti=s=>class extends Qt(oe(s)){static get properties(){return{_hasVaadinItemMixin:{value:!0},selected:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"_selectedChanged",sync:!0},_value:String}}get _activeKeys(){return["Enter"," "]}get value(){return this._value!==void 0?this._value:this.textContent.trim()}set value(e){this._value=e}ready(){super.ready();const e=this.getAttribute("value");e!==null&&(this.value=e)}focus(e){this.disabled||super.focus(e)}_shouldSetActive(e){return!this.disabled&&!(e.type==="keydown"&&e.defaultPrevented)}_selectedChanged(e){this.setAttribute("aria-selected",e)}_disabledChanged(e){super._disabledChanged(e),e&&(this.selected=!1,this.blur())}_onKeyDown(e){super._onKeyDown(e),this._activeKeys.includes(e.key)&&!e.defaultPrevented&&(e.preventDefault(),this.click())}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Mc extends ti(T(z(I(A(E))))){static get is(){return"vaadin-select-item"}static get styles(){return Et}static get properties(){return{role:{type:String,value:"option",reflectToAttribute:!0}}}render(){return y`
      <span part="checkmark" aria-hidden="true"></span>
      <div part="content">
        <slot></slot>
      </div>
    `}}w(Mc);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function ds(s,i){const{scrollLeft:e}=s;return i!=="rtl"?e:s.scrollWidth-s.clientWidth+e}function Rc(s,i,e){i!=="rtl"?s.scrollLeft=e:s.scrollLeft=s.clientWidth-s.scrollWidth+e}/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Tr=s=>class extends De(s){get focused(){return(this._getItems()||[]).find(Je)}get _vertical(){return!0}get _tabNavigation(){return!1}focus(e){const t=this._getFocusableIndex();t>=0&&this._focus(t,e)}_getFocusableIndex(){const e=this._getItems();return Array.isArray(e)?this._getAvailableIndex(e,0,null,t=>!se(t)):-1}_getItems(){return Array.from(this.children)}_onKeyDown(e){if(super._onKeyDown(e),e.metaKey||e.ctrlKey)return;const{key:t,shiftKey:n}=e,r=this._getItems()||[],o=r.indexOf(this.focused);let a,l;const h=!this._vertical&&this.getAttribute("dir")==="rtl"?-1:1;this.__isPrevKeyPressed(t,n)?(l=-h,a=o-h):this.__isNextKeyPressed(t,n)?(l=h,a=o+h):t==="Home"?(l=1,a=0):t==="End"&&(l=-1,a=r.length-1),a=this._getAvailableIndex(r,a,l,c=>!se(c)),!(this._tabNavigation&&t==="Tab"&&(a>o&&e.shiftKey||a<o&&!e.shiftKey||a===o))&&a>=0&&(e.preventDefault(),this._focus(a,{focusVisible:!0},!0))}__isPrevKeyPressed(e,t){return this._vertical?e==="ArrowUp":e==="ArrowLeft"||this._tabNavigation&&e==="Tab"&&t}__isNextKeyPressed(e,t){return this._vertical?e==="ArrowDown":e==="ArrowRight"||this._tabNavigation&&e==="Tab"&&!t}_focus(e,t,n=!1){const r=this._getItems();this._focusItem(r[e],t,n)}_focusItem(e,t){e&&e.focus(t)}_getAvailableIndex(e,t,n,r){const o=e.length;let a=t;for(let l=0;typeof a=="number"&&l<o;l+=1,a+=n||1){a<0?a=o-1:a>=o&&(a=0);const d=e[a];if(this._isItemFocusable(d)&&this.__isMatchingItem(d,r))return a}return-1}__isMatchingItem(e,t){return typeof t=="function"?t(e):!0}_isItemFocusable(e){return!e.hasAttribute("disabled")}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ii=s=>class extends Tr(s){static get properties(){return{disabled:{type:Boolean,value:!1,reflectToAttribute:!0},selected:{type:Number,reflectToAttribute:!0,notify:!0,sync:!0},orientation:{type:String,reflectToAttribute:!0,value:""},items:{type:Array,readOnly:!0,notify:!0},_searchBuf:{type:String,value:""}}}static get observers(){return["_enhanceItems(items, orientation, selected, disabled)"]}get _isRTL(){return!this._vertical&&this.getAttribute("dir")==="rtl"}get _scrollerElement(){return console.warn(`Please implement the '_scrollerElement' property in <${this.localName}>`),this}get _vertical(){return this.orientation!=="horizontal"}focus(e){this._observer&&this._observer.flush();const t=Array.isArray(this.items)?this.items:[],n=this._getAvailableIndex(t,0,null,r=>r.tabIndex===0&&!se(r));n>=0?this._focus(n,e):super.focus(e)}ready(){super.ready(),this.addEventListener("click",t=>this._onClick(t));const e=this.shadowRoot.querySelector("slot:not([name])");this._observer=new ce(e,()=>{this._setItems(this._filterItems([...this.children]))})}_getItems(){return this.items}_enhanceItems(e,t,n,r){if(!r&&e){this.setAttribute("aria-orientation",t||"vertical"),e.forEach(a=>{t?a.setAttribute("orientation",t):a.removeAttribute("orientation")}),this._setFocusable(n<0||!n?0:n);const o=e[n];e.forEach(a=>{a.selected=a===o}),o&&!o.disabled&&this._scrollToItem(n)}}_filterItems(e){return e.filter(t=>t._hasVaadinItemMixin)}_onClick(e){if(e.metaKey||e.shiftKey||e.ctrlKey||e.defaultPrevented)return;const t=this._filterItems(e.composedPath())[0];let n;t&&!t.disabled&&(n=this.items.indexOf(t))>=0&&(this.selected=n)}_searchKey(e,t){this._searchReset=D.debounce(this._searchReset,K.after(500),()=>{this._searchBuf=""}),this._searchBuf+=t.toLowerCase(),this.items.some(r=>this.__isMatchingKey(r))||(this._searchBuf=t.toLowerCase());const n=this._searchBuf.length===1?e+1:e;return this._getAvailableIndex(this.items,n,1,r=>this.__isMatchingKey(r)&&getComputedStyle(r).display!=="none")}__isMatchingKey(e){return e.textContent.replace(/[^\p{L}\p{Nd}]/gu,"").toLowerCase().startsWith(this._searchBuf)}_onKeyDown(e){if(e.metaKey||e.ctrlKey)return;const t=e.key,n=this.items.indexOf(this.focused);if(/[\p{L}\p{Nd}]/u.test(t)&&t.length===1){const r=this._searchKey(n,t);r>=0&&this._focus(r);return}super._onKeyDown(e)}_setFocusable(e){e=this._getAvailableIndex(this.items,e,1);const t=this.items[e];this.items.forEach(n=>{n.tabIndex=n===t?0:-1})}_focus(e,t){this.items.forEach((n,r)=>{n.focused=r===e}),this._setFocusable(e),this._scrollToItem(e),super._focus(e,t)}_scrollToItem(e){const t=this.items[e];if(!t)return;const n=this._vertical?["top","bottom"]:this._isRTL?["right","left"]:["left","right"],r=this._scrollerElement.getBoundingClientRect(),o=(this.items[e+1]||t).getBoundingClientRect(),a=(this.items[e-1]||t).getBoundingClientRect();let l=0;!this._isRTL&&o[n[1]]>=r[n[1]]||this._isRTL&&o[n[1]]<=r[n[1]]?l=o[n[1]]-r[n[1]]:(!this._isRTL&&a[n[0]]<=r[n[0]]||this._isRTL&&a[n[0]]>=r[n[0]])&&(l=a[n[0]]-r[n[0]]),this._scroll(l)}_scroll(e){if(this._vertical)this._scrollerElement.scrollTop+=e;else{const t=this.getAttribute("dir")||"ltr",n=ds(this._scrollerElement,t)+e;Rc(this._scrollerElement,t,n)}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const hs=C`
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
 */class Lc extends ii(T(z(I(A(E))))){static get is(){return"vaadin-select-list-box"}static get styles(){return hs}static get properties(){return{orientation:{readOnly:!0}}}get _scrollerElement(){return this.shadowRoot.querySelector('[part="items"]')}render(){return y`
      <div part="items">
        <slot></slot>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","listbox")}}w(Lc);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Fc=C`
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
 */const $c=s=>class extends xt(ge(z(s))){static get observers(){return["_updateOverlayWidth(opened, positionTarget)"]}ready(){super.ready(),this.restoreFocusOnClose=!0}get _contentRoot(){return this._rendererRoot}get _rendererRoot(){if(!this.__savedRoot){const e=document.createElement("div");e.setAttribute("slot","overlay"),this.owner.appendChild(e),this.__savedRoot=e}return this.__savedRoot}_shouldCloseOnOutsideClick(e){return!0}_mouseDownListener(e){super._mouseDownListener(e),e.preventDefault()}_getMenuElement(){return Array.from(this._rendererRoot.children).find(e=>e.localName!=="style")}_updateOverlayWidth(e,t){e&&t&&this.style.setProperty("--_vaadin-select-overlay-default-width",`${t.offsetWidth}px`)}requestContentUpdate(){if(super.requestContentUpdate(),this.owner){const e=this._getMenuElement();this.owner._assignMenuElement(e)}}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class zc extends $c(T(I(A(E)))){static get is(){return"vaadin-select-overlay"}static get styles(){return[me,Fc]}render(){return y`
      <div id="backdrop" part="backdrop" ?hidden="${!this.withBackdrop}"></div>
      <div part="overlay" id="overlay">
        <div part="content" id="content">
          <slot></slot>
        </div>
      </div>
    `}updated(i){super.updated(i),i.has("renderer")&&this.requestContentUpdate()}}w(zc);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Nc=C`
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
 */class Bc extends Zi(T(I(A(E)))){static get is(){return"vaadin-select-value-button"}static get styles(){return Nc}render(){return y`
      <div class="vaadin-button-container">
        <span part="label">
          <slot></slot>
        </span>
      </div>
    `}}w(Bc);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Vc=C`
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
 */const Hc=C`
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
 * Copyright (c) 2023 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Wc extends G{constructor(i){super(i,"value","vaadin-select-value-button",{initializer:(e,t)=>{t._setFocusElement(e),t.ariaTarget=e,t.stateTarget=e,e.setAttribute("aria-haspopup","listbox")}})}}/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const qc=s=>class extends bt(Kt(De(wt(s)))){static get properties(){return{items:{type:Array,observer:"__itemsChanged"},opened:{type:Boolean,value:!1,notify:!0,observer:"_openedChanged",reflectToAttribute:!0,sync:!0},renderer:{type:Object},value:{type:String,value:"",notify:!0,observer:"_valueChanged",sync:!0},name:{type:String},placeholder:{type:String},readonly:{type:Boolean,value:!1,reflectToAttribute:!0},noVerticalOverlap:{type:Boolean,value:!1},_phone:Boolean,_phoneMediaQuery:{value:"(max-width: 450px), (max-height: 450px)"},_inputContainer:Object,_items:Object}}static get delegateAttrs(){return[...super.delegateAttrs,"invalid"]}static get observers(){return["_updateAriaExpanded(opened, focusElement)","_updateSelectedItem(value, _items, placeholder)"]}constructor(){super(),this._itemId=`value-${this.localName}-${Se()}`,this._srLabelController=new kn(this),this._srLabelController.slotName="sr-label"}disconnectedCallback(){super.disconnectedCallback(),this.opened=!1}ready(){super.ready(),this._inputContainer=this.shadowRoot.querySelector('[part~="input-field"]'),this._overlayElement=this.$.overlay,this._valueButtonController=new Wc(this),this.addController(this._valueButtonController),this.addController(this._srLabelController),this.addController(new Jt(this._phoneMediaQuery,e=>{this._phone=e})),this._tooltipController=new X(this),this._tooltipController.setPosition("top"),this._tooltipController.setAriaTarget(this.focusElement),this.addController(this._tooltipController)}updated(e){super.updated(e),e.has("_phone")&&this.toggleAttribute("phone",this._phone)}requestContentUpdate(){this._overlayElement&&this._overlayElement.requestContentUpdate()}_requiredChanged(e){super._requiredChanged(e),e===!1&&this._requestValidation()}__itemsChanged(e,t){(e||t)&&this.requestContentUpdate()}_assignMenuElement(e){e&&e!==this.__lastMenuElement&&(this._menuElement=e,this.__initMenuItems(e),e.addEventListener("items-changed",()=>{this.__initMenuItems(e)}),e.addEventListener("selected-changed",()=>this.__updateValueButton()),e.addEventListener("keydown",t=>this._onKeyDownInside(t),!0),e.addEventListener("click",t=>{const n=t.composedPath().find(r=>r._hasVaadinItemMixin);this.__dispatchChangePending=!!(n&&n.value!==void 0&&n.value!==this.value),this.opened=!1},!0),this.__lastMenuElement=e),this._menuElement&&this._menuElement.items&&this._updateSelectedItem(this.value,this._menuElement.items)}__initMenuItems(e){e.items&&(this._items=e.items)}_valueChanged(e,t){this.toggleAttribute("has-value",!!e),t!==void 0&&!this.__dispatchChangePending&&this._requestValidation()}_onClick(e){this.disabled||(e.preventDefault(),this.opened=!this.readonly)}_onEscape(e){this.opened&&(e.stopPropagation(),this.opened=!1)}_onToggleMouseDown(e){e.preventDefault(),this.opened||this.focusElement.focus()}_onKeyDown(e){if(super._onKeyDown(e),!(e.altKey||e.shiftKey||e.ctrlKey||e.metaKey)&&e.target===this.focusElement&&!this.readonly&&!this.disabled&&!this.opened){if(/^(Enter|SpaceBar|\s|ArrowDown|Down|ArrowUp|Up)$/u.test(e.key))e.preventDefault(),this.opened=!0;else if(/[\p{L}\p{Nd}]/u.test(e.key)&&e.key.length===1){const t=this._menuElement.selected,n=t!==void 0?t:-1,r=this._menuElement._searchKey(n,e.key);r>=0&&(this.__dispatchChangePending=!0,this._updateAriaLive(!0),this._menuElement.selected=r)}}}_onKeyDownInside(e){e.key==="Tab"&&(this.focusElement.setAttribute("tabindex","-1"),this._overlayElement.restoreFocusOnClose=!1,this.opened=!1,setTimeout(()=>{this.focusElement.setAttribute("tabindex","0"),this._overlayElement.restoreFocusOnClose=!0}))}_openedChanged(e,t){if(e){if(this.disabled||this.readonly){this.opened=!1;return}this._updateAriaLive(!1);const n=this.hasAttribute("focus-ring");this._openedWithFocusRing=n,n&&this.removeAttribute("focus-ring")}else t&&(this._openedWithFocusRing&&this.setAttribute("focus-ring",""),!this.__dispatchChangePending&&!this._keyboardActive&&this._requestValidation())}_updateAriaExpanded(e,t){t&&t.setAttribute("aria-expanded",e?"true":"false")}_updateAriaLive(e){this.focusElement&&(e?this.focusElement.setAttribute("aria-live","polite"):this.focusElement.removeAttribute("aria-live"))}__attachSelectedItem(e){let t;const n=e.getAttribute("label");n?t=this.__createItemElement({label:n}):t=e.cloneNode(!0),t._sourceItem=e,this.__appendValueItemElement(t,this.focusElement),t.selected=!0}__createItemElement(e){const t=document.createElement(e.component||"vaadin-select-item");return e.label&&(t.textContent=e.label),e.value&&(t.value=e.value),e.disabled&&(t.disabled=e.disabled),e.className&&(t.className=e.className),t}__appendValueItemElement(e,t){t.appendChild(e),e.removeAttribute("tabindex"),e.removeAttribute("aria-selected"),e.removeAttribute("role"),e.removeAttribute("focused"),e.removeAttribute("focus-ring"),e.removeAttribute("active"),e.setAttribute("id",this._itemId)}_accessibleNameChanged(e){this._srLabelController.setLabel(e),this._setCustomAriaLabelledBy(e?this._srLabelController.defaultId:null)}_accessibleNameRefChanged(e){this._setCustomAriaLabelledBy(e)}_setCustomAriaLabelledBy(e){const t=this._getLabelIdWithItemId(e);this._fieldAriaController.setLabelId(t,!0)}_getLabelIdWithItemId(e){const n=(this._items?this._items[this._menuElement.selected]:!1)||this.placeholder?this._itemId:"";return e?`${e} ${n}`.trim():null}__updateValueButton(){const e=this.focusElement;if(!e)return;e.innerHTML="";const t=this._items[this._menuElement.selected];if(e.removeAttribute("placeholder"),this._hasContent(t))this.__attachSelectedItem(t);else if(this.placeholder){const r=this.__createItemElement({label:this.placeholder});this.__appendValueItemElement(r,e),e.setAttribute("placeholder","")}!this._valueChanging&&t&&(this._selectedChanging=!0,this.value=t.value||"",this.__dispatchChangePending&&this.__dispatchChange(),delete this._selectedChanging);const n=t||this.placeholder?{newId:this._itemId}:{oldId:this._itemId};Mt(e,"aria-labelledby",n),(this.accessibleName||this.accessibleNameRef)&&this._setCustomAriaLabelledBy(this.accessibleNameRef||this._srLabelController.defaultId)}_hasContent(e){if(!e)return!1;const t=!!(e.hasAttribute("label")?e.getAttribute("label"):e.textContent.trim()),n=e.childElementCount>0;return t||n}_updateSelectedItem(e,t){if(t){const n=e==null?e:e.toString();this._menuElement.selected=t.reduce((r,o,a)=>r===void 0&&o.value===n?a:r,void 0),this._selectedChanging||(this._valueChanging=!0,this.__updateValueButton(),delete this._valueChanging)}}_shouldRemoveFocus(e){return!this.contains(e.relatedTarget)}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}checkValidity(){return!this.required||this.readonly||!!this.value}__defaultRenderer(e,t){if(!this.items||this.items.length===0){e.textContent="";return}let n=e.firstElementChild;n||(n=document.createElement("vaadin-select-list-box"),e.appendChild(n)),n.textContent="",this.items.forEach(r=>{n.appendChild(this.__createItemElement(r))})}__dispatchChange(){this._requestValidation(),this.dispatchEvent(new CustomEvent("change",{bubbles:!0})),this.__dispatchChangePending=!1}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Uc extends qc(L(T(I(A(E))))){static get is(){return"vaadin-select"}static get styles(){return[ke,Vc,Hc]}render(){return y`
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
          theme="${B(this._theme)}"
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
        theme="${B(this._theme)}"
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
    `}_onOpenedChanged(i){this.opened=i.detail.value}_onOverlayOpen(){this._menuElement&&this._menuElement.focus({focusVisible:Q()})}}w(Uc);window.Vaadin.Flow.selectConnector={};window.Vaadin.Flow.selectConnector.initLazy=s=>{s.$connector||(s.$connector={},s.renderer=i=>{const e=s.querySelector("vaadin-select-list-box");e&&(i.firstChild&&i.removeChild(i.firstChild),i.appendChild(e))})};/**
 * @license
 * Copyright 2020 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Yc=Fi(class extends Li{constructor(s){if(super(s),s.type!==we.PROPERTY&&s.type!==we.ATTRIBUTE&&s.type!==we.BOOLEAN_ATTRIBUTE)throw Error("The `live` directive is not allowed on child or event bindings");if(!vn(s))throw Error("`live` bindings can only contain a single expression")}render(s){return s}update(s,[i]){if(i===Re||i===Ue)return i;const e=s.element,t=s.name;if(s.type===we.PROPERTY){if(i===e[t])return Re}else if(s.type===we.BOOLEAN_ATTRIBUTE){if(!!i===e.hasAttribute(t))return Re}else if(s.type===we.ATTRIBUTE&&e.getAttribute(t)===i+"")return Re;return Qo(s),i}}),Ht=window;Ht.Vaadin=Ht.Vaadin||{};Ht.Vaadin.setLitRenderer=(s,i,e,t,n,r,o)=>{const a=f=>n.map(m=>(...v)=>{f!==void 0&&t(m,f,v[0]instanceof Event?[]:[...v])}),l=["html","root","live","appId","itemKey","model","item","index",...n,`return html\`${e}\``],d=new Function(...l),h=(f,m,v)=>{const{item:x,index:b}=m;Ut(d(y,f,Yc,o,v,m,x,b,...a(v)),f)},c=(f,m,v)=>{const{item:x}=v;f.__litRenderer!==c&&(f.innerHTML="",delete f._$litPart$,f.__litRenderer=c);const b={};for(const k in x)k.startsWith(r)&&(b[k.replace(r,"")]=x[k]);h(f,{...v,item:b},x.key)};c.__rendererId=r,s[i]=c};Ht.Vaadin.unsetLitRenderer=(s,i,e)=>{s[i]?.__rendererId===e&&(s[i]=void 0)};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const jc=C`
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
`,Gc=[vt,gr("radio","radio-button"),jc];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Kc=s=>class extends gt(Tn(vr(bt(Qt(s))))){static get properties(){return{name:{type:String,value:""}}}static get delegateAttrs(){return[...super.delegateAttrs,"name"]}constructor(){super(),this._setType("radio"),this.value="on",this.tabindex=0}get slotStyles(){return[`
          ${this.localName} > input[slot='input'] {
            opacity: 0;
          }
        `]}ready(){super.ready(),this.addController(new Te(this,e=>{this._setInputElement(e),this._setFocusElement(e),this.stateTarget=e,this.ariaTarget=e})),this.addController(new ve(this.inputElement,this._labelController))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Xc extends Kc(L(T(I(A(E))))){static get is(){return"vaadin-radio-button"}static get styles(){return Gc}render(){return y`
      <div class="vaadin-radio-button-container">
        <div part="radio" aria-hidden="true"></div>
        <slot name="input"></slot>
        <slot name="label"></slot>
      </div>
    `}}w(Xc);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ar=C`
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
 */const Qc=[vt,Ar,C`
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
 */const Zc=s=>class extends wt(oe(Ae(De(s)))){static get properties(){return{name:{type:String,observer:"__nameChanged",sync:!0},value:{type:String,notify:!0,value:"",sync:!0,observer:"__valueChanged"},readonly:{type:Boolean,value:!1,reflectToAttribute:!0,sync:!0,observer:"__readonlyChanged"},_fieldName:{type:String}}}constructor(){super(),this.__registerRadioButton=this.__registerRadioButton.bind(this),this.__unregisterRadioButton=this.__unregisterRadioButton.bind(this),this.__onRadioButtonCheckedChange=this.__onRadioButtonCheckedChange.bind(this),this._tooltipController=new X(this),this._tooltipController.addEventListener("tooltip-changed",e=>{const t=e.detail.node;if(t&&t.isConnected){const n=this.__radioButtons.map(r=>r.inputElement);this._tooltipController.setAriaTarget(n)}else this._tooltipController.setAriaTarget([])})}get __radioButtons(){return this.__filterRadioButtons([...this.children])}get __selectedRadioButton(){return this.__radioButtons.find(e=>e.checked)}get isHorizontalRTL(){return this.__isRTL&&this._theme!=="vertical"}ready(){super.ready(),this.ariaTarget=this,this.setAttribute("role","radiogroup"),this._fieldName=`${this.localName}-${Se()}`;const e=this.shadowRoot.querySelector("slot:not([name])");this._observer=new ce(e,({addedNodes:t,removedNodes:n})=>{this.__filterRadioButtons(t).reverse().forEach(this.__registerRadioButton),this.__filterRadioButtons(n).forEach(this.__unregisterRadioButton);const r=this.__radioButtons.map(o=>o.inputElement);this._tooltipController.setAriaTarget(r)}),this.addController(this._tooltipController)}__filterRadioButtons(e){return e.filter(t=>t.nodeType===Node.ELEMENT_NODE&&t.localName==="vaadin-radio-button")}_onKeyDown(e){super._onKeyDown(e);const t=e.composedPath().find(n=>n.nodeType===Node.ELEMENT_NODE&&n.localName==="vaadin-radio-button");["ArrowLeft","ArrowUp"].includes(e.key)&&(e.preventDefault(),this.__selectNextRadioButton(t)),["ArrowRight","ArrowDown"].includes(e.key)&&(e.preventDefault(),this.__selectPrevRadioButton(t))}_invalidChanged(e){super._invalidChanged(e),e?this.setAttribute("aria-invalid","true"):this.removeAttribute("aria-invalid")}__nameChanged(e){this.__radioButtons.forEach(t=>{t.name=e||this._fieldName})}__selectNextRadioButton(e){const t=this.__radioButtons.indexOf(e);this.__selectIncRadioButton(t,this.isHorizontalRTL?1:-1)}__selectPrevRadioButton(e){const t=this.__radioButtons.indexOf(e);this.__selectIncRadioButton(t,this.isHorizontalRTL?-1:1)}__selectIncRadioButton(e,t){const n=(this.__radioButtons.length+e+t)%this.__radioButtons.length,r=this.__radioButtons[n];r.disabled?this.__selectIncRadioButton(n,t):(r.focusElement.focus(),r.focusElement.click())}__registerRadioButton(e){e.name=this.name||this._fieldName,e.addEventListener("checked-changed",this.__onRadioButtonCheckedChange),(this.disabled||this.readonly)&&(e.disabled=!0),e.checked&&this.__selectRadioButton(e)}__unregisterRadioButton(e){e.removeEventListener("checked-changed",this.__onRadioButtonCheckedChange),e.value===this.value&&this.__selectRadioButton(null)}__onRadioButtonCheckedChange(e){e.target.checked&&this.__selectRadioButton(e.target)}__valueChanged(e,t){if(!(t===void 0&&e==="")){if(e){const n=this.__radioButtons.find(r=>r.value===e);n?(this.__selectRadioButton(n),this.toggleAttribute("has-value",!0)):console.warn(`The radio button with the value "${e}" was not found.`)}else this.__selectRadioButton(null),this.removeAttribute("has-value");t!==void 0&&this._requestValidation()}}__readonlyChanged(e,t){!e&&t===void 0||t!==e&&this.__updateRadioButtonsDisabledProperty()}_disabledChanged(e,t){super._disabledChanged(e,t),!(!e&&t===void 0)&&t!==e&&this.__updateRadioButtonsDisabledProperty()}_shouldRemoveFocus(e){return!this.contains(e.relatedTarget)}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}__selectRadioButton(e){e?this.value=e.value:this.value="",this.__radioButtons.forEach(t=>{t.checked=t===e}),this.readonly&&this.__updateRadioButtonsDisabledProperty()}__updateRadioButtonsDisabledProperty(){this.__radioButtons.forEach(e=>{this.readonly?e.disabled=e!==this.__selectedRadioButton:e.disabled=this.disabled})}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Jc extends Zc(L(T(I(A(E))))){static get is(){return"vaadin-radio-group"}static get styles(){return Qc}render(){return y`
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
    `}}w(Jc);/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const eu=[vt,Ar];/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const tu=s=>class extends wt(oe(Ae(s))){static get properties(){return{value:{type:Array,value:()=>[],notify:!0,sync:!0,observer:"__valueChanged"},readonly:{type:Boolean,value:!1,reflectToAttribute:!0,observer:"__readonlyChanged"}}}constructor(){super(),this.__registerCheckbox=this.__registerCheckbox.bind(this),this.__unregisterCheckbox=this.__unregisterCheckbox.bind(this),this.__onCheckboxCheckedChanged=this.__onCheckboxCheckedChanged.bind(this),this._tooltipController=new X(this),this._tooltipController.addEventListener("tooltip-changed",e=>{const t=e.detail.node;if(t&&t.isConnected){const n=this.__checkboxes.map(r=>r.inputElement);this._tooltipController.setAriaTarget(n)}else this._tooltipController.setAriaTarget([])})}get __checkboxes(){return this.__filterCheckboxes([...this.children])}ready(){super.ready(),this.ariaTarget=this,this.setAttribute("role","group");const e=this.shadowRoot.querySelector("slot:not([name])");this._observer=new ce(e,({addedNodes:t,removedNodes:n})=>{const r=this.__filterCheckboxes(t),o=this.__filterCheckboxes(n);r.forEach(this.__registerCheckbox),o.forEach(this.__unregisterCheckbox);const a=this.__checkboxes.map(l=>l.inputElement);this._tooltipController.setAriaTarget(a),this.__warnOfCheckboxesWithoutValue(r)}),this.addController(this._tooltipController)}checkValidity(){return!this.required||!!(this.value&&this.value.length>0)}__filterCheckboxes(e){return e.filter(t=>t.nodeType===Node.ELEMENT_NODE&&t.localName==="vaadin-checkbox")}__warnOfCheckboxesWithoutValue(e){e.some(n=>{const{value:r}=n;return!n.hasAttribute("value")&&(!r||r==="on")})&&console.warn("Please provide the value attribute to all the checkboxes inside the checkbox group.")}__registerCheckbox(e){e.addEventListener("checked-changed",this.__onCheckboxCheckedChanged),this.disabled&&(e.disabled=!0),this.readonly&&(e.readonly=!0),e.checked?this.__addCheckboxToValue(e.value):this.value&&this.value.includes(e.value)&&(e.checked=!0)}__unregisterCheckbox(e){e.removeEventListener("checked-changed",this.__onCheckboxCheckedChanged),e.checked&&this.__removeCheckboxFromValue(e.value)}_disabledChanged(e,t){super._disabledChanged(e,t),!(!e&&t===void 0)&&t!==e&&this.__checkboxes.forEach(n=>{n.disabled=e})}__addCheckboxToValue(e){this.value?this.value.includes(e)||(this.value=[...this.value,e]):this.value=[e]}__removeCheckboxFromValue(e){this.value&&this.value.includes(e)&&(this.value=this.value.filter(t=>t!==e))}__onCheckboxCheckedChanged(e){const t=e.target;t.checked?this.__addCheckboxToValue(t.value):this.__removeCheckboxFromValue(t.value)}__valueChanged(e,t){e&&e.length===0&&t===void 0||(this.toggleAttribute("has-value",e&&e.length>0),this.__checkboxes.forEach(n=>{n.checked=e&&e.includes(n.value)}),t!==void 0&&this._requestValidation())}__readonlyChanged(e,t){(e||t)&&this.__checkboxes.forEach(n=>{n.readonly=e})}_shouldRemoveFocus(e){return!this.contains(e.relatedTarget)}_setFocused(e){super._setFocused(e),!e&&document.hasFocus()&&this._requestValidation()}};/**
 * @license
 * Copyright (c) 2018 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class iu extends tu(L(T(I(A(E))))){static get is(){return"vaadin-checkbox-group"}static get styles(){return eu}render(){return y`
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
    `}}w(iu);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const su=C`
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
 */const nu=s=>class extends s{static get properties(){return{value:{type:Number,observer:"_valueChanged"},min:{type:Number,value:0,observer:"_minChanged"},max:{type:Number,value:1,observer:"_maxChanged"},indeterminate:{type:Boolean,value:!1,reflectToAttribute:!0}}}static get observers(){return["_normalizedValueChanged(value, min, max)"]}ready(){super.ready(),this.setAttribute("role","progressbar")}_normalizedValueChanged(e,t,n){const r=this._normalizeValue(e,t,n);this.style.setProperty("--vaadin-progress-value",r)}_valueChanged(e){this.setAttribute("aria-valuenow",e)}_minChanged(e){this.setAttribute("aria-valuemin",e)}_maxChanged(e){this.setAttribute("aria-valuemax",e)}_normalizeValue(e,t,n){let r;return!e&&e!==0?r=0:t>=n?r=1:(r=(e-t)/(n-t),r=Math.min(Math.max(r,0),1)),r}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ru extends nu(L(T(I(A(E))))){static get is(){return"vaadin-progress-bar"}static get styles(){return su}render(){return y`
      <div part="bar">
        <div part="value"></div>
      </div>
    `}}w(ru);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ou=C`
  :host {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--vaadin-tab-gap, var(--vaadin-gap-s));
    padding: var(--vaadin-tab-padding, var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container));
    cursor: var(--vaadin-clickable-cursor);
    font-size: var(--vaadin-tab-font-size, 1em);
    font-weight: var(--vaadin-tab-font-weight, 500);
    line-height: var(--vaadin-tab-line-height, inherit);
    color: var(--vaadin-tab-text-color, var(--vaadin-text-color-secondary));
    background: var(--vaadin-tab-background, transparent);
    border-radius: var(--vaadin-tab-border-radius, var(--vaadin-radius-m));
    border: var(--vaadin-tab-border-width, 0) solid var(--vaadin-tab-border-color, var(--vaadin-border-color-secondary));
    -webkit-tap-highlight-color: transparent;
    -webkit-user-select: none;
    user-select: none;
    touch-action: manipulation;
    position: relative;
  }

  :host([hidden]) {
    display: none !important;
  }

  :host([orientation='vertical']) {
    justify-content: start;
  }

  :host([selected]) {
    --vaadin-tab-background: var(--vaadin-background-container);
    --vaadin-tab-text-color: var(--vaadin-text-color);
  }

  :host([disabled]) {
    cursor: var(--vaadin-disabled-cursor);
    opacity: 0.5;
  }

  :host(:is([focus-ring], :focus-visible)) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: calc(var(--vaadin-focus-ring-width) * -1);
  }

  slot {
    gap: inherit;
    align-items: inherit;
    justify-content: inherit;
  }

  ::slotted(a) {
    color: inherit !important;
    cursor: inherit !important;
    text-decoration: inherit !important;
    display: flex;
    align-items: inherit;
    justify-content: inherit;
    gap: inherit;
  }

  ::slotted(a)::before {
    content: '';
    position: absolute;
    inset: 0;
  }

  @media (forced-colors: active) {
    :host {
      border: 1px solid Canvas;
    }

    :host([selected]) {
      color: Highlight;
      border-color: Highlight;
    }

    :host([disabled]) {
      color: GrayText;
      opacity: 1;
    }
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class au extends ti(T(L(I(A(E))))){static get is(){return"vaadin-tab"}static get styles(){return ou}render(){return y`
      <slot></slot>
      <slot name="tooltip"></slot>
    `}ready(){super.ready(),this.setAttribute("role","tab"),this._tooltipController=new X(this),this.addController(this._tooltipController)}_onKeyUp(i){const e=this.hasAttribute("active");if(super._onKeyUp(i),e){const t=this.querySelector("a");t&&t.click()}}}w(au);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const lu=C`
  :host {
    display: flex;
    max-width: 100%;
    max-height: 100%;
    position: relative;
    box-sizing: border-box;
    padding: var(--vaadin-tabs-padding);
    background: var(--vaadin-tabs-background);
    border-radius: var(--vaadin-tabs-border-radius);
    border: var(--vaadin-tabs-border-width, 0) solid
      var(--vaadin-tabs-border-color, var(--vaadin-border-color-secondary));
  }

  :host([hidden]) {
    display: none !important;
  }

  :host([orientation='vertical']) {
    flex-direction: column;
  }

  [part='tabs'] {
    flex: 1;
    overflow: auto;
    overscroll-behavior: contain;
    display: flex;
    flex-direction: column;
    gap: var(--vaadin-tabs-gap, var(--vaadin-gap-s));
  }

  :host([orientation='horizontal']) [part='tabs'] {
    flex-direction: row;
    scrollbar-width: none;
  }

  /* scrollbar-width is supported in Safari 18.2, use the following for earlier */
  :host([orientation='horizontal']) [part='tabs']::-webkit-scrollbar {
    display: none;
  }

  [part$='button'] {
    position: absolute;
    z-index: 1;
    pointer-events: none;
    opacity: 0;
    cursor: var(--vaadin-clickable-cursor);
    box-sizing: border-box;
    height: 100%;
    padding: var(--vaadin-tab-padding, var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container));
    background: var(--vaadin-background-color);
    display: flex;
    align-items: center;
    justify-content: center;
    -webkit-tap-highlight-color: transparent;
    touch-action: manipulation;
  }

  [part='forward-button'] {
    inset-inline-end: 0;
  }

  :host([overflow~='start']) [part='back-button'],
  :host([overflow~='end']) [part='forward-button'] {
    pointer-events: auto;
    opacity: 1;
  }

  [part$='button']::before {
    content: '';
    display: block;
    width: var(--vaadin-icon-size, 1lh);
    height: var(--vaadin-icon-size, 1lh);
    background: currentColor;
    mask: var(--_vaadin-icon-chevron-down) 50% / var(--vaadin-icon-visual-size, 100%) no-repeat;
    rotate: 90deg;
  }

  [part='forward-button']::before {
    rotate: -90deg;
  }

  :host(:is([orientation='vertical'], [theme~='hide-scroll-buttons'])) [part$='button'] {
    display: none;
  }

  @media (pointer: coarse) {
    :host(:not([theme~='show-scroll-buttons'])) [part$='button'] {
      display: none;
    }
  }

  :host([dir='rtl']) [part$='button']::before {
    scale: 1 -1;
  }

  @media (forced-colors: active) {
    [part$='button']::before {
      background: CanvasText;
    }
  }
`;/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const du=s=>class extends Zt(ii(s)){static get properties(){return{orientation:{value:"horizontal",type:String,reflectToAttribute:!0,sync:!0},selected:{value:0,type:Number,reflectToAttribute:!0}}}static get observers(){return["__tabsItemsChanged(items)"]}constructor(){super(),this.__itemsResizeObserver=new ResizeObserver(()=>{setTimeout(()=>this._updateOverflow())})}get _scrollOffset(){return this._vertical?this._scrollerElement.offsetHeight:this._scrollerElement.offsetWidth}get _scrollerElement(){return this.$.scroll}get __direction(){return!this._vertical&&this.__isRTL?1:-1}ready(){super.ready(),this._scrollerElement.addEventListener("scroll",()=>this._updateOverflow()),this.setAttribute("role","tablist")}_onResize(){this._updateOverflow()}__tabsItemsChanged(e){this.__itemsResizeObserver.disconnect(),(e||[]).forEach(t=>{this.__itemsResizeObserver.observe(t)}),this._updateOverflow()}_scrollForward(){const e=this._getNavigationButtonVisibleWidth("forward-button"),t=this._getNavigationButtonVisibleWidth("back-button"),n=this._scrollerElement.getBoundingClientRect(),o=[...this.items].reverse().find(h=>this._isItemVisible(h,e,t,n)).getBoundingClientRect(),l=20+this.shadowRoot.querySelector('[part="back-button"]').clientWidth;let d;if(this.__isRTL){const h=n.right-l;d=o.right-h}else{const h=n.left+l;d=o.left-h}-this.__direction*d<1&&(d=-this.__direction*(this._scrollOffset-l)),this._scroll(d)}_scrollBack(){const e=this._getNavigationButtonVisibleWidth("forward-button"),t=this._getNavigationButtonVisibleWidth("back-button"),n=this._scrollerElement.getBoundingClientRect(),o=this.items.find(h=>this._isItemVisible(h,e,t,n)).getBoundingClientRect(),l=20+this.shadowRoot.querySelector('[part="forward-button"]').clientWidth;let d;if(this.__isRTL){const h=n.left+l;d=o.left-h}else{const h=n.right-l;d=o.right-h}this.__direction*d<1&&(d=this.__direction*(this._scrollOffset-l)),this._scroll(d)}_isItemVisible(e,t,n,r){if(this._vertical)throw new Error("Visibility check is only supported for horizontal tabs.");const o=this.__isRTL?n:t,a=this.__isRTL?t:n,l=r.right-o,d=r.left+a,h=e.getBoundingClientRect();return l>Math.floor(h.left)&&d<Math.ceil(h.right)}_getNavigationButtonVisibleWidth(e){const t=this.shadowRoot.querySelector(`[part="${e}"]`);return window.getComputedStyle(t).opacity==="0"?0:t.clientWidth}_updateOverflow(){const e=this._vertical?this._scrollerElement.scrollTop:ds(this._scrollerElement,this.getAttribute("dir")),t=this._vertical?this._scrollerElement.scrollHeight:this._scrollerElement.scrollWidth;let n=Math.floor(e)>1?"start":"";Math.ceil(e)<Math.ceil(t-this._scrollOffset)&&(n+=" end"),this.__direction===1&&(n=n.replace(/start|end/giu,r=>r==="start"?"end":"start")),n?this.setAttribute("overflow",n.trim()):this.removeAttribute("overflow")}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class hu extends du(L(T(I(A(E))))){static get is(){return"vaadin-tabs"}static get styles(){return lu}render(){return y`
      <div @click="${this._scrollBack}" part="back-button" aria-hidden="true"></div>

      <div id="scroll" part="tabs">
        <slot></slot>
      </div>

      <div @click="${this._scrollForward}" part="forward-button" aria-hidden="true"></div>
    `}}w(hu);/**
 * @license
 * Copyright (c) 2021 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class cs{constructor(i,e){this.host=i,this.scrollTarget=e||i,this.__boundOnScroll=this.__onScroll.bind(this)}hostConnected(){this.initialized||(this.initialized=!0,this.observe())}observe(){const{host:i}=this;this.__resizeObserver=new ResizeObserver(()=>{this.__debounceOverflow=D.debounce(this.__debounceOverflow,ue,()=>{this.__updateOverflow()})}),this.__resizeObserver.observe(i),[...i.children].forEach(e=>{this.__resizeObserver.observe(e)}),this.__childObserver=new MutationObserver(e=>{e.forEach(({addedNodes:t,removedNodes:n})=>{t.forEach(r=>{r.nodeType===Node.ELEMENT_NODE&&this.__resizeObserver.observe(r)}),n.forEach(r=>{r.nodeType===Node.ELEMENT_NODE&&this.__resizeObserver.unobserve(r)})}),this.__updateOverflow()}),this.__childObserver.observe(i,{childList:!0}),this.scrollTarget.addEventListener("scroll",this.__boundOnScroll),this.__updateOverflow()}__onScroll(){this.__updateOverflow()}__updateOverflow(){const i=this.scrollTarget;let e="";i.scrollTop>0&&(e+=" top"),Math.ceil(i.scrollTop)<Math.ceil(i.scrollHeight-i.clientHeight)&&(e+=" bottom");const t=Math.abs(i.scrollLeft);t>0&&(e+=" start"),Math.ceil(t)<Math.ceil(i.scrollWidth-i.clientWidth)&&(e+=" end"),e=e.trim(),e.length>0&&this.host.getAttribute("overflow")!==e?this.host.setAttribute("overflow",e):e.length===0&&this.host.hasAttribute("overflow")&&this.host.removeAttribute("overflow")}}/**
 * @license
 * Copyright (c) 2020 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const cu=C`
  :host {
    --_indicator-height: var(--vaadin-scroller-overflow-indicator-height, 1px);
    /* Don't let these properties inherit */
    --vaadin-scroller-padding-block: 0px;
    --vaadin-scroller-padding-inline: 0px;
    --vaadin-scroller-overflow-indicator-top-opacity: 0;
    --vaadin-scroller-overflow-indicator-bottom-opacity: 0;
    display: block;
    overflow: auto;
    outline: none;
    flex: 1;
    box-sizing: border-box;
    padding: var(--vaadin-scroller-padding-block) var(--vaadin-scroller-padding-inline);
  }

  :host([focus-ring]) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
  }

  :host([hidden]) {
    display: none !important;
  }

  :host([scroll-direction='vertical']) {
    overflow-x: hidden;
  }

  :host([scroll-direction='horizontal']) {
    overflow-y: hidden;
  }

  :host([scroll-direction='none']) {
    overflow: hidden;
  }

  :host::before,
  :host::after {
    content: '';
    display: block;
    opacity: 0;
    position: sticky;
    inset: 0 calc(var(--vaadin-scroller-padding-inline) * -1);
    z-index: 9999;
    pointer-events: none;
    box-sizing: border-box;
    height: var(--_indicator-height);
    margin-inline: calc(var(--vaadin-scroller-padding-inline) * -1);
    background: var(--vaadin-border-color-secondary);
  }

  :host::before {
    top: 0;
    margin-bottom: calc(var(--_indicator-height) * -1);
    translate: 0 calc(var(--vaadin-scroller-padding-block) * -1);
  }

  :host::after {
    bottom: 0;
    margin-top: calc(var(--_indicator-height) * -1);
    translate: 0 calc(var(--vaadin-scroller-padding-block) * 1);
  }

  :host([overflow~='top'])::before {
    opacity: var(--vaadin-scroller-overflow-indicator-top-opacity);
  }

  :host([overflow~='bottom'])::after {
    opacity: var(--vaadin-scroller-overflow-indicator-bottom-opacity);
  }

  :host([theme~='overflow-indicator-top'][overflow~='top']),
  :host([theme~='overflow-indicators'][overflow~='top']) {
    --vaadin-scroller-overflow-indicator-top-opacity: 1;
  }

  :host([theme~='overflow-indicators'][overflow~='bottom']),
  :host([theme~='overflow-indicator-bottom'][overflow~='bottom']) {
    --vaadin-scroller-overflow-indicator-bottom-opacity: 1;
  }
`;/**
 * @license
 * Copyright (c) 2020 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const uu=s=>class extends oe(s){static get properties(){return{scrollDirection:{type:String,reflectToAttribute:!0},tabindex:{type:Number,value:0,reflectToAttribute:!0}}}_shouldSetFocus(e){return e.target===this}};/**
 * @license
 * Copyright (c) 2020 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Dr extends uu(L(T(I(A(E))))){static get is(){return"vaadin-scroller"}static get styles(){return cu}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return y`<slot></slot>`}ready(){super.ready(),this.__overflowController=new cs(this),this.addController(this.__overflowController)}}w(Dr);/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class _u extends Dr{static get is(){return"vaadin-tabsheet-scroller"}}w(_u);/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const pu=[br,C`
    :host {
      display: flex;
      flex-direction: column;
      border: var(--vaadin-tabsheet-border-width, 1px) solid
        var(--vaadin-tabsheet-border-color, var(--vaadin-border-color-secondary));
      border-radius: var(--vaadin-tabsheet-border-radius, var(--vaadin-radius-l));
      overflow: hidden;
    }

    :host([hidden]) {
      display: none !important;
    }

    [part='tabs-container'] {
      position: relative;
      display: flex;
      align-items: center;
      gap: var(--vaadin-tabsheet-gap, var(--vaadin-gap-s));
      padding: var(--vaadin-tabsheet-padding, var(--vaadin-padding-m));
      box-sizing: border-box;
    }

    ::slotted([slot='tabs']) {
      flex: 1;
      align-self: stretch;
      min-width: 128px;
    }

    ::slotted([hidden]) {
      display: none !important;
    }

    [part='content'] {
      position: relative;
      flex: 1;
      box-sizing: border-box;
      --vaadin-scroller-padding-block: var(--vaadin-tabsheet-padding, var(--vaadin-padding-m));
      --vaadin-scroller-padding-inline: var(--vaadin-tabsheet-padding, var(--vaadin-padding-m));
      --vaadin-scroller-overflow-indicator-top-opacity: 1;
    }

    [part='content'][focus-ring] {
      border-bottom-left-radius: inherit;
      border-bottom-right-radius: inherit;
      outline-offset: calc(var(--vaadin-focus-ring-width) * -1);
    }

    :host([loading]) [part='content'] {
      align-content: center;
    }

    [part='loader'] {
      margin: auto;
    }

    :host([theme~='no-border']) {
      border: 0;
      border-radius: 0;
    }

    :host([theme~='no-padding']) [part='content'] {
      padding: 0 !important;
      --vaadin-scroller-padding-block: 0px !important;
      --vaadin-scroller-padding-inline: 0px !important;
    }
  `];/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class fu extends G{constructor(i){super(i,"tabs"),this.__tabsItemsChangedListener=this.__tabsItemsChangedListener.bind(this),this.__tabsSelectedChangedListener=this.__tabsSelectedChangedListener.bind(this),this.__tabIdObserver=new MutationObserver(e=>{e.forEach(t=>{const n=t.target;i.__linkTabAndPanel(n),n.selected&&i.__togglePanels(n)})})}__tabsItemsChangedListener(){this.__tabIdObserver.disconnect();const i=this.tabs.items||[];i.forEach(e=>{this.__tabIdObserver.observe(e,{attributeFilter:["id"]})}),this.host._setItems(i)}__tabsSelectedChangedListener(){this.host.selected=this.tabs.selected}initCustomNode(i){if(!(i instanceof customElements.get("vaadin-tabs")))throw Error('The "tabs" slot of a <vaadin-tabsheet> must only contain a <vaadin-tabs> element!');this.tabs=i,i.addEventListener("items-changed",this.__tabsItemsChangedListener),i.addEventListener("selected-changed",this.__tabsSelectedChangedListener),this.host.__tabs=i,this.host.stateTarget=i,this.__tabsItemsChangedListener()}teardownNode(i){this.tabs=null,i.removeEventListener("items-changed",this.__tabsItemsChangedListener),i.removeEventListener("selected-changed",this.__tabsSelectedChangedListener),this.host.__tabs=null,this.host._setItems([]),this.host.stateTarget=void 0}}const mu=s=>class extends Kt(s){static get properties(){return{items:{type:Array,readOnly:!0,notify:!0},selected:{value:0,type:Number,notify:!0},__tabs:{type:Object,value:()=>[]},__panels:{type:Array,value:()=>[]}}}static get observers(){return["__itemsOrPanelsChanged(items, __panels)","__selectedTabItemChanged(selected, items, __panels)"]}static get delegateProps(){return["selected","_theme"]}ready(){super.ready(),this.__overflowController=new cs(this,this.shadowRoot.querySelector('[part="content"]')),this.addController(this.__overflowController),this._tabsSlotController=new fu(this),this.addController(this._tabsSlotController);const i=this.shadowRoot.querySelector("#panel-slot");this.__panelsObserver=new ce(i,({addedNodes:e,removedNodes:t})=>{e.length&&e.forEach(n=>{n.nodeType===Node.ELEMENT_NODE&&n.hidden&&(n.__customHidden=!0)}),t.length&&t.forEach(n=>{n.nodeType===Node.ELEMENT_NODE&&n.hidden&&(n.__customHidden?delete n.__customHidden:n.hidden=!1)}),this.__panels=Array.from(i.assignedNodes({flatten:!0})).filter(n=>n.nodeType===Node.ELEMENT_NODE)})}_delegateProperty(i,e){if(this.stateTarget){if(i==="_theme"){this._delegateAttribute("theme",e);return}super._delegateProperty(i,e)}}__itemsOrPanelsChanged(i,e){i&&i.forEach(t=>{this.__linkTabAndPanel(t,e)})}__selectedTabItemChanged(i,e,t){!e||i===void 0||this.__togglePanels(e[i],t)}__togglePanels(i,e=this.__panels){const t=i?i.id:"",n=e.find(a=>a.getAttribute("tab")===t),r=this.shadowRoot.querySelector('[part="content"]');this.toggleAttribute("loading",!n);const o=e.filter(a=>!a.hidden).length===1;n?r.style.minHeight="":o&&(r.style.minHeight=`${r.offsetHeight}px`),e.forEach(a=>{a.hidden=a!==n})}__linkTabAndPanel(i,e=this.__panels){const t=e.find(n=>n.getAttribute("tab")===i.id);t&&(t.role="tabpanel",t.id||(t.id=`tabsheet-panel-${Se()}`),t.setAttribute("aria-labelledby",i.id),i.setAttribute("aria-controls",t.id))}};/**
 * @license
 * Copyright (c) 2022 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class gu extends mu(T(L(I(A(E))))){static get is(){return"vaadin-tabsheet"}static get styles(){return pu}render(){return y`
      <div part="tabs-container">
        <slot name="prefix"></slot>
        <slot name="tabs"></slot>
        <slot name="suffix"></slot>
      </div>

      <vaadin-tabsheet-scroller part="content">
        <div part="loader"></div>
        <slot id="panel-slot"></slot>
      </vaadin-tabsheet-scroller>
    `}}w(gu);function vu(s,i){try{return window.Vaadin.Flow.clients[s].getByNodeId(i)}catch(e){console.error("Could not get node %s from app %s",i,s),console.error(e)}}function bu(s,i){s.$connector||(s.$connector={generateItems(e){const t=us(i,e);s.items=t}})}function us(s,i){const e=vu(s,i);if(e)return Array.from(e.children).map(t=>{const n={component:t,checked:t._checked,keepOpen:t._keepOpen,className:t.className,theme:t.__theme};return t._hasVaadinItemMixin&&t._containerNodeId&&(n.children=us(s,t._containerNodeId)),t._item=n,n})}function yu(s,i){s._item&&(s._item.checked=i,s._item.keepOpen&&s.toggleAttribute("menu-item-checked",i))}function wu(s,i){s._item&&(s._item.keepOpen=i)}function Cu(s,i){s._item&&(s._item.theme=i)}window.Vaadin.Flow.contextMenuConnector={initLazy:bu,generateItemsTree:us,setChecked:yu,setKeepOpen:wu,setTheme:Cu};function xu(s,i){if(s.$connector)return;const e=new MutationObserver(t=>{t.some(r=>{const o=r.oldValue,a=r.target.getAttribute(r.attributeName);return o!==a})&&s.$connector.generateItems()});s.$connector={generateItems(t){if(!s.shadowRoot){setTimeout(()=>s.$connector.generateItems(t));return}if(!s._container){queueMicrotask(()=>s.$connector.generateItems(t));return}t&&(s.__generatedItems=window.Vaadin.Flow.contextMenuConnector.generateItemsTree(i,t));let n=s.__generatedItems||[];n.forEach(r=>{r.disabled=r.component.disabled,r.component._rootItem=r}),n.forEach(r=>{e.observe(r.component,{attributeFilter:["hidden","disabled"],attributeOldValue:!0})}),n=n.filter(r=>!r.component.hidden),s.items=n}}}function Eu(s){const i=s._rootItem||s._item;i&&(i.className=s.className)}window.Vaadin.Flow.menubarConnector={initLazy:xu,setClassName:Eu};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Iu=C`
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
`,Or=[Et,Iu];/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Su=Or;/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class ku extends ti(T(z(I(A(E))))){static get is(){return"vaadin-menu-bar-item"}static get styles(){return Su}render(){return y`
      <span part="checkmark" aria-hidden="true"></span>
      <div part="content">
        <slot></slot>
      </div>
    `}connectedCallback(){super.connectedCallback(),this.setAttribute("role","menuitem")}}w(ku);/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Tu extends ii(T(z(I(A(E))))){static get is(){return"vaadin-menu-bar-list-box"}static get styles(){return hs}static get properties(){return{orientation:{type:String,readOnly:!0}}}get _scrollerElement(){return this.shadowRoot.querySelector('[part="items"]')}render(){return y`
      <div part="items">
        <slot></slot>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","menu")}}w(Tu);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Pr=s=>class extends fn(xt(s)){static get properties(){return{parentOverlay:{type:Object,readOnly:!0},_theme:{type:String,readOnly:!0,sync:!0}}}static get observers(){return["_themeChanged(_theme)"]}get _contentRoot(){return this._rendererRoot}get _rendererRoot(){if(!this.__savedRoot){const e=document.createElement("div");e.setAttribute("slot","overlay"),e.style.display="contents",this.owner.appendChild(e),this.__savedRoot=e}return this.__savedRoot}ready(){super.ready(),this.restoreFocusOnClose=!0,this.addEventListener("keydown",e=>{if(!e.defaultPrevented&&e.composedPath()[0]===this.$.overlay&&[38,40].indexOf(e.keyCode)>-1){const t=this._contentRoot.firstElementChild;t&&Array.isArray(t.items)&&t.items.length&&(e.preventDefault(),e.keyCode===38?t.items[t.items.length-1].focus():t.focus())}})}_themeChanged(){this.close()}getBoundaries(){const e=this.getBoundingClientRect(),t=this.$.overlay.getBoundingClientRect();let n=e.bottom-t.height;const r=this.parentOverlay;if(r&&r.hasAttribute("bottom-aligned")){const o=getComputedStyle(r);n=n-parseFloat(o.bottom)-parseFloat(o.height)}return{xMax:e.right-t.width,xMin:e.left+t.width,yMax:n}}_updatePosition(){if(super._updatePosition(),this.positionTarget&&this.parentOverlay&&this.opened){const e=this.$.content,t=getComputedStyle(e);!!this.style.left?this.style.left=`${parseFloat(this.style.left)+parseFloat(t.paddingLeft)}px`:this.style.right=`${parseFloat(this.style.right)+parseFloat(t.paddingRight)}px`,!!this.style.bottom?this.style.bottom=`${parseFloat(this.style.bottom)-parseFloat(t.paddingBottom)}px`:this.style.top=`${parseFloat(this.style.top)-parseFloat(t.paddingTop)}px`}}_shouldRestoreFocus(){return this.parentOverlay?!1:super._shouldRestoreFocus()}_deepContains(e){return this.owner.contains(e)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Mr=C`
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
 */const Au=[me,Mr];/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Du extends Pr(ge(z(T(I(A(E)))))){static get is(){return"vaadin-menu-bar-overlay"}static get styles(){return Au}render(){return y`
      <div id="backdrop" part="backdrop" ?hidden="${!this.withBackdrop}"></div>
      <div part="overlay" id="overlay" tabindex="0">
        <div part="content" id="content">
          <slot></slot>
          <slot name="submenu"></slot>
        </div>
      </div>
    `}}w(Du);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Ou=s=>class extends s{static get properties(){return{items:{type:Array,sync:!0},_positionTarget:{type:Object,sync:!0}}}constructor(){super(),this.__itemsOutsideClickListener=e=>{this._shouldCloseOnOutsideClick(e)&&this.dispatchEvent(new CustomEvent("items-outside-click"))},this.addEventListener("items-outside-click",()=>{this.items&&this.close()})}get _tagNamePrefix(){return"vaadin-context-menu"}connectedCallback(){super.connectedCallback(),document.documentElement.addEventListener("click",this.__itemsOutsideClickListener)}disconnectedCallback(){super.disconnectedCallback(),document.documentElement.removeEventListener("click",this.__itemsOutsideClickListener)}_shouldCloseOnOutsideClick(e){return!e.composedPath().some(t=>t.localName===`${this._tagNamePrefix}-overlay`)}__forwardFocus(){const e=this._overlayElement,t=e._contentRoot.firstElementChild;if(e.parentOverlay){const n=e.parentOverlay._contentRoot.querySelector("[expanded]");n&&n.hasAttribute("focused")&&t?t.focus():e.$.overlay.focus()}else t&&t.focus()}__openSubMenu(e,t){this.__updateSubMenuForItem(e,t);const n=this._overlayElement,r=e._overlayElement;r._setParentOverlay(n),n.hasAttribute("theme")?e.setAttribute("theme",n.getAttribute("theme")):e.removeAttribute("theme");const o=r.$.content;o.style.minWidth="",t.dispatchEvent(new CustomEvent("opensubmenu",{detail:{children:t._item.children}}))}__updateSubMenuForItem(e,t){e.items=t._item.children,e.listenOn=t,e._positionTarget=t,e._overlayElement.requestContentUpdate()}__createComponent(e){let t;return e.component instanceof HTMLElement?t=e.component:t=document.createElement(e.component||`${this._tagNamePrefix}-item`),t._hasVaadinItemMixin&&(t.setAttribute("role","menuitem"),t.tabIndex=-1),t.localName==="hr"?t.setAttribute("role","separator"):t.setAttribute("aria-haspopup","false"),this._setMenuItemTheme(t,e,this._theme),t._item=e,e.text&&(t.textContent=e.text),e.className&&t.setAttribute("class",e.className),this.__toggleMenuComponentAttribute(t,"menu-item-checked",e.checked),this.__toggleMenuComponentAttribute(t,"disabled",e.disabled),e.children&&e.children.length&&(this.__updateExpanded(t,!1),t.setAttribute("aria-haspopup","true")),t}__initListBox(){const e=document.createElement(`${this._tagNamePrefix}-list-box`);return this._theme&&e.setAttribute("theme",this._theme),e.addEventListener("selected-changed",t=>{const{value:n}=t.detail;if(typeof n=="number"){const r=e.items[n]._item;e.selected=null,r.children||this.dispatchEvent(new CustomEvent("item-selected",{detail:{value:r}}))}}),e}__initOverlay(){const e=this._overlayElement;e.$.backdrop.addEventListener("click",()=>{this.close()}),e.addEventListener(Ne?"click":"mouseover",t=>{t.composedPath().includes(this._subMenu)||this.__showSubMenu(t)}),e.addEventListener("keydown",t=>{if(t.composedPath().includes(this._subMenu))return;const{key:n}=t,r=this.__isRTL,o=n==="ArrowRight",a=n==="ArrowLeft";!r&&o||r&&a||n==="Enter"||n===" "?this.__showSubMenu(t):!r&&a||r&&o||n==="Escape"?(n==="Escape"&&t.stopPropagation(),this.close(),this.listenOn.focus()):n==="Tab"&&!t.defaultPrevented&&this.dispatchEvent(new CustomEvent("close-all-menus"))})}__initSubMenu(){const e=document.createElement(this.constructor.is);return e._modeless=!0,e.openOn="opensubmenu",this.addEventListener("opened-changed",t=>{t.detail.value||this._subMenu.close()}),e.addEventListener("close-all-menus",()=>{this.dispatchEvent(new CustomEvent("close-all-menus"))}),e.addEventListener("item-selected",t=>{const{detail:n}=t;this.dispatchEvent(new CustomEvent("item-selected",{detail:n}))}),this.addEventListener("close-all-menus",()=>{this._overlayElement.close()}),this.addEventListener("item-selected",t=>{const n=t.target,r=t.detail.value,o=n.items.indexOf(r);r.keepOpen&&o>-1&&n.opened?(n.__selectedIndex=o,n.requestContentUpdate()):r.keepOpen||this.close()}),e.addEventListener("opened-changed",t=>{if(!t.detail.value){const n=this._listBox.querySelector("[expanded]");n&&this.__updateExpanded(n,!1)}}),e}__showSubMenu(e,t=e.composedPath().find(n=>n.localName===`${this._tagNamePrefix}-item`)){if(!this.__openListenerActive)return;if(this._overlayElement.hasAttribute("opening")){requestAnimationFrame(()=>{this.__showSubMenu(e,t)});return}const n=this._subMenu,r=this._listBox.querySelector("[expanded]");if(t&&t!==r){const{children:o}=t._item,a=n._overlayElement._contentRoot.firstElementChild,l=a&&a.focused;if(r&&this.__updateExpanded(r,!1),(!o||!o.length)&&n.close(),!this.opened)return;o&&o.length?(this.__updateExpanded(t,!0),this.__openSubMenu(n,t)):l?n.listenOn.focus():this._listBox.focused||this._overlayElement.$.overlay.focus()}}__getListBox(){return this._overlayElement._contentRoot.querySelector(`${this._tagNamePrefix}-list-box`)}__itemsRenderer(e,t){this.__initMenu(e,t),this._subMenu.closeOn=t.closeOn,this._listBox.innerHTML="",t.items.forEach(n=>{const r=this.__createComponent(n);this._listBox.appendChild(r)})}_setMenuItemTheme(e,t,n){let r=e.getAttribute("theme")||n;t.theme!=null&&(r=Array.isArray(t.theme)?t.theme.join(" "):t.theme),this.__updateTheme(e,r)}__toggleMenuComponentAttribute(e,t,n){n?(e.setAttribute(t,""),e[`__has-${t}`]=!0):e[`__has-${t}`]&&(e.removeAttribute(t),e[`__has-${t}`]=!1)}__initMenu(e,t){if(e.firstElementChild)this.__updateTheme(this._listBox,this._theme);else{this.__initOverlay();const n=this.__initListBox();this._listBox=n,e.appendChild(n);const r=this.__initSubMenu();r.slot="submenu",this._subMenu=r,this.appendChild(r),requestAnimationFrame(()=>{this.__openListenerActive=!0})}}__updateExpanded(e,t){e.setAttribute("aria-expanded",t.toString()),e.toggleAttribute("expanded",t)}__updateTheme(e,t){t?e.setAttribute("theme",t):e.removeAttribute("theme")}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Rr=s=>class extends Ou(s){static get properties(){return{selector:{type:String},opened:{type:Boolean,reflectToAttribute:!0,observer:"_openedChanged",value:!1,notify:!0,readOnly:!0},openOn:{type:String,value:"vaadin-contextmenu",sync:!0},listenOn:{type:Object,sync:!0,value(){return this}},closeOn:{type:String,value:"click",observer:"_closeOnChanged",sync:!0},renderer:{type:Function,sync:!0},_modeless:{type:Boolean,sync:!0},_context:{type:Object,sync:!0},_phone:{type:Boolean},_fullscreen:{type:Boolean},_fullscreenMediaQuery:{type:String,value:"(max-width: 450px), (max-height: 450px)"}}}static get observers(){return["_targetOrOpenOnChanged(listenOn, openOn)","_rendererChanged(renderer, items)","_fullscreenChanged(_fullscreen)"]}constructor(){super(),this._boundOpen=this.open.bind(this),this._boundClose=this.close.bind(this),this._boundPreventDefault=this._preventDefault.bind(this),this._boundOnGlobalContextMenu=this._onGlobalContextMenu.bind(this)}connectedCallback(){super.connectedCallback(),this.__boundOnScroll=this.__onScroll.bind(this),window.addEventListener("scroll",this.__boundOnScroll,!0),this.__restoreOpened&&this._setOpened(!0)}disconnectedCallback(){super.disconnectedCallback(),window.removeEventListener("scroll",this.__boundOnScroll,!0),this.__restoreOpened=this.opened,this.close()}firstUpdated(){super.firstUpdated(),this._overlayElement=this.$.overlay,this.addController(new Jt(this._fullscreenMediaQuery,e=>{this._fullscreen=e}))}_onOverlayOpened(e){if(e.target!==this._overlayElement)return;const t=e.detail.value;this._setOpened(t),t&&this.__alignOverlayPosition()}_onVaadinOverlayOpen(e){e.target===this._overlayElement&&(this.__alignOverlayPosition(),this._overlayElement.style.visibility="",this.__forwardFocus())}_onVaadinOverlayClosed(){this.dispatchEvent(new CustomEvent("closed"))}_targetOrOpenOnChanged(e,t){this._oldListenOn&&this._oldOpenOn&&(this._unlisten(this._oldListenOn,this._oldOpenOn,this._boundOpen),this._oldListenOn.style.webkitTouchCallout="",this._oldListenOn.style.webkitUserSelect="",this._oldListenOn.style.userSelect="",this._oldListenOn=null,this._oldOpenOn=null),e&&t&&(this._listen(e,t,this._boundOpen),this._oldListenOn=e,this._oldOpenOn=t)}_fullscreenChanged(e){this._phone=e}__setListenOnUserSelect(e){const t=e?"none":"";this.listenOn.style.webkitTouchCallout=t,this.listenOn.style.webkitUserSelect=t,this.listenOn.style.userSelect=t,e&&document.getSelection().removeAllRanges()}_closeOnChanged(e,t){const n="vaadin-overlay-outside-click",r=this._overlayElement;t&&this._unlisten(r,t,this._boundClose),e?(this._listen(r,e,this._boundClose),r.removeEventListener(n,this._boundPreventDefault)):r.addEventListener(n,this._boundPreventDefault)}_preventDefault(e){e.preventDefault()}_openedChanged(e,t){e?document.documentElement.addEventListener("contextmenu",this._boundOnGlobalContextMenu,!0):t&&document.documentElement.removeEventListener("contextmenu",this._boundOnGlobalContextMenu,!0),this.__setListenOnUserSelect(e)}requestContentUpdate(){this._overlayElement&&(this.__preserveMenuState(),this._overlayElement.requestContentUpdate(),this.__restoreMenuState())}_rendererChanged(e,t){if(t){if(e)throw new Error("The items API cannot be used together with a renderer");this.closeOn==="click"&&(this.closeOn="")}}close(){this._setOpened(!1)}_contextTarget(e){if(this.selector){const t=this.listenOn.querySelectorAll(this.selector);return Array.prototype.filter.call(t,n=>e.composedPath().indexOf(n)>-1)[0]}else if(this.listenOn&&this.listenOn!==this&&this.position)return this.listenOn;return e.target}open(e){this._overlayElement&&e.composedPath().includes(this._overlayElement)||e&&!this.opened&&(this._context={detail:e.detail,target:this._contextTarget(e)},this._context.target&&(e.preventDefault(),e.stopPropagation(),this.__x=this._getEventCoordinate(e,"x"),this.__pageXOffset=window.pageXOffset,this.__y=this._getEventCoordinate(e,"y"),this.__pageYOffset=window.pageYOffset,this._overlayElement.style.visibility="hidden",this._setOpened(!0)))}__preserveMenuState(){const e=this.__getListBox();e&&(this.__focusedIndex=e.items.indexOf(e.focused),this._subMenu&&this._subMenu.opened&&(this.__subMenuIndex=e.items.indexOf(this._subMenu.listenOn)))}__restoreMenuState(){const e=this.__focusedIndex,t=this.__subMenuIndex,n=this.__selectedIndex,r=this.__getListBox();if(r){if(r._observer.flush(),t>-1){const o=r.items[t];o?Array.isArray(o._item.children)&&o._item.children.length?(this.__updateSubMenuForItem(this._subMenu,o),this._subMenu.requestContentUpdate()):(this._subMenu.close(),this.__focusItem(o)):r.focus()}this.__focusItem(n>-1?r.children[n]:r.items[e])}this.__focusedIndex=void 0,this.__subMenuIndex=void 0,this.__selectedIndex=void 0}__focusItem(e){e&&e.focus({focusVisible:Q()})}__onScroll(){if(!this.opened||this.position)return;const e=window.pageYOffset-this.__pageYOffset,t=window.pageXOffset-this.__pageXOffset;this.__adjustPosition("left",-t),this.__adjustPosition("right",t),this.__adjustPosition("top",-e),this.__adjustPosition("bottom",e),this.__pageYOffset+=e,this.__pageXOffset+=t}__adjustPosition(e,t){const r=this._overlayElement.style;r[e]=`${(parseInt(r[e])||0)+t}px`}__alignOverlayPosition(){const e=this._overlayElement;if(e.positionTarget)return;const t=e.style;["top","right","bottom","left"].forEach(c=>t.removeProperty(c)),["right-aligned","end-aligned","bottom-aligned"].forEach(c=>e.removeAttribute(c));const{xMax:n,xMin:r,yMax:o}=e.getBoundaries(),a=this.__x,l=this.__y,d=document.documentElement.clientWidth,h=document.documentElement.clientHeight;this.__isRTL?a>d/2||a>r?t.right=`${Math.max(0,d-a)}px`:(t.left=`${a}px`,this._setEndAligned(e)):a<d/2||a<n?t.left=`${a}px`:(t.right=`${Math.max(0,d-a)}px`,this._setEndAligned(e)),l<h/2||l<o?t.top=`${l}px`:(t.bottom=`${Math.max(0,h-l)}px`,e.setAttribute("bottom-aligned",""))}_setEndAligned(e){e.setAttribute("end-aligned",""),this.__isRTL||e.setAttribute("right-aligned","")}_getEventCoordinate(e,t){if(e.detail instanceof Object){if(e.detail[t])return e.detail[t];if(e.detail.sourceEvent)return this._getEventCoordinate(e.detail.sourceEvent,t)}else{const n=`client${t.toUpperCase()}`,r=e.changedTouches?e.changedTouches[0][n]:e[n];if(r===0){const o=e.target.getBoundingClientRect();return t==="x"?o.left:o.top+o.height}return r}}_listen(e,t,n){_e[t]?pe(e,t,n):e.addEventListener(t,n)}_unlisten(e,t,n){_e[t]?zn(e,t,n):e.removeEventListener(t,n)}__createMouseEvent(e,t,n){return new MouseEvent(e,{bubbles:!0,composed:!0,cancelable:!0,clientX:t,clientY:n})}__focusClosestFocusable(e){let t=e;for(;t;){if(t instanceof HTMLElement&&mt(t)){t.focus();return}t=t.parentNode||t.host}}__contextMenuAt(e,t){const n=Fn(e,t);n&&queueMicrotask(()=>{n.dispatchEvent(this.__createMouseEvent("mousedown",e,t)),n.dispatchEvent(this.__createMouseEvent("mouseup",e,t)),this.__focusClosestFocusable(n),n.dispatchEvent(this.__createMouseEvent("contextmenu",e,t))})}_onGlobalContextMenu(e){e.shiftKey||(Si||ze||(e.stopPropagation(),this._overlayElement.__focusRestorationController.focusNode=null,this._overlayElement.addEventListener("vaadin-overlay-closed",n=>{n.target===this._overlayElement&&this.__contextMenuAt(e.clientX,e.clientY)},{once:!0})),e.preventDefault(),this.close())}};/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Pu extends Rr(st(I(E))){static get is(){return"vaadin-menu-bar-submenu"}static get styles(){return C`
      :host {
        display: block;
      }

      :host([hidden]) {
        display: none !important;
      }
    `}static get properties(){return{isRoot:{type:Boolean,reflectToAttribute:!0,sync:!0}}}constructor(){super(),this.openOn="opensubmenu"}get _tagNamePrefix(){return"vaadin-menu-bar"}render(){return y`
      <vaadin-menu-bar-overlay
        id="overlay"
        .owner="${this}"
        .opened="${this.opened}"
        .model="${this._context}"
        .modeless="${this._modeless}"
        .renderer="${this.__itemsRenderer}"
        .withBackdrop="${this._phone}"
        .positionTarget="${this._positionTarget}"
        ?no-horizontal-overlap="${!this.isRoot}"
        ?phone="${this._phone}"
        theme="${B(this._theme)}"
        exportparts="backdrop, overlay, content"
        @opened-changed="${this._onOverlayOpened}"
        @vaadin-overlay-open="${this._onVaadinOverlayOpen}"
      >
        <slot name="overlay"></slot>
        <slot name="submenu" slot="submenu"></slot>
      </vaadin-menu-bar-overlay>
    `}_openedChanged(){}close(){super.close(),this.hasAttribute("is-root")&&this.parentElement._close()}_shouldCloseOnOutsideClick(i){return this.hasAttribute("is-root")&&i.composedPath().includes(this.listenOn)?!1:super._shouldCloseOnOutsideClick(i)}}w(Pu);/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Mu=C`
  :host {
    flex-shrink: 0;
  }

  :host([focus-ring]) {
    z-index: 1;
  }

  :host([slot='overflow']) {
    margin-inline-end: 0;
  }

  .vaadin-button-container {
    gap: inherit;
  }

  :host(:not([slot='overflow'])[aria-haspopup]) [part='suffix'] {
    display: flex;
    align-items: center;
    gap: inherit;
  }

  :host(:not([slot='overflow'])[aria-haspopup]) [part='suffix']::after {
    background: currentColor;
    content: '';
    height: var(--vaadin-icon-size, 1lh);
    mask: var(--_vaadin-icon-chevron-down) 50% / var(--vaadin-icon-visual-size, 100%) no-repeat;
    width: var(--vaadin-icon-size, 1lh);
  }

  ::slotted(vaadin-menu-bar-item) {
    padding: 0;
    gap: 0;
  }

  ::slotted(vaadin-menu-bar-item)::after {
    display: none;
  }
`;/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Ru extends Vn{static get is(){return"vaadin-menu-bar-button"}static get styles(){return[super.styles,Mu]}_onKeyDown(i){this.__triggeredWithActiveKeys=this._activeKeys.includes(i.key),super._onKeyDown(i),this.__triggeredWithActiveKeys=null}__shouldSuppressInteractionEvent(i){return i.type==="keydown"&&["ArrowLeft","ArrowRight"].includes(i.key)?!1:super.__shouldSuppressInteractionEvent(i)}}w(Ru);/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Lu=C`
  :host {
    display: block;
  }

  :host([hidden]) {
    display: none !important;
  }

  [part='container'] {
    display: flex;
    flex-wrap: nowrap;
    contain: layout;
    position: relative;
    width: 100%;
    --_gap: var(--vaadin-menu-bar-gap, 0px);
    --_bw: var(--vaadin-button-border-width, 1px);
    gap: var(--_gap);
    --_rad-button: var(--vaadin-button-border-radius, var(--vaadin-radius-m));
  }

  :host(:not([has-single-button])) ::slotted(vaadin-menu-bar-button:not(:first-of-type)) {
    margin-inline-start: min(var(--_bw) * -1 + var(--_gap) * 1000, 0px);
  }

  ::slotted(vaadin-menu-bar-button) {
    border-radius: 0;
  }

  ::slotted([first-visible]),
  :host([has-single-button]) ::slotted([slot='overflow']),
  ::slotted(vaadin-menu-bar-button[theme~='tertiary']) {
    border-start-start-radius: var(--_rad-button);
    border-end-start-radius: var(--_rad-button);
  }

  ::slotted(:is([last-visible], [slot='overflow'])),
  ::slotted(vaadin-menu-bar-button[theme~='tertiary']) {
    border-start-end-radius: var(--_rad-button);
    border-end-end-radius: var(--_rad-button);
  }

  :host([theme~='end-aligned']) ::slotted(vaadin-menu-bar-button[first-visible]),
  :host([theme~='end-aligned'][has-single-button]) ::slotted(vaadin-menu-bar-button) {
    margin-inline-start: auto;
  }
`;/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Fu extends Li{update(i,[{component:e,text:t}]){const{parentNode:n,startNode:r}=i,o=e||(t?document.createTextNode(t):null),a=this.getOldNode(i);return a===o?Re:(a&&o?n.replaceChild(o,a):a?n.removeChild(a):o&&r.after(o),Re)}getOldNode(i){const{startNode:e,endNode:t}=i;return e.nextSibling===t?null:e.nextSibling}}const $u=Fi(Fu),zu={moreOptions:"More options"},Nu=s=>class extends ei(zu,Tr(Zt(oe(Ae(s))))){static get properties(){return{items:{type:Array,sync:!0,value:()=>[]},openOnHover:{type:Boolean},reverseCollapse:{type:Boolean,sync:!0},tabNavigation:{type:Boolean,sync:!0}}}get i18n(){return super.i18n}set i18n(e){super.i18n=e}constructor(){super(),this.__boundOnContextMenuKeydown=this.__onContextMenuKeydown.bind(this),this.__boundOnTooltipMouseLeave=this.__onTooltipOverlayMouseLeave.bind(this)}get focused(){return(this._getItems()||[]).find(Je)||this._expandedButton}get _vertical(){return!1}get _tabNavigation(){return this.tabNavigation}get _observeParent(){return!0}get _buttons(){return Array.from(this.querySelectorAll("vaadin-menu-bar-button"))}get _hasOverflow(){return this._overflow&&!this._overflow.hasAttribute("hidden")}set _hasOverflow(e){this._overflow&&this._overflow.toggleAttribute("hidden",!e)}ready(){super.ready(),this.setAttribute("role","menubar"),this._subMenuController=new G(this,"submenu","vaadin-menu-bar-submenu",{initializer:e=>{e.setAttribute("is-root",""),e.addEventListener("item-selected",this.__onItemSelected.bind(this)),e.addEventListener("close-all-menus",this.__onEscapeClose.bind(this)),e._overlayElement._contentRoot.addEventListener("keydown",this.__boundOnContextMenuKeydown),this._subMenu=e}}),this._overflowController=new G(this,"overflow","vaadin-menu-bar-button",{initializer:e=>{e.setAttribute("hidden","");const t=document.createElement("div");t.setAttribute("aria-hidden","true"),t.innerHTML="&centerdot;".repeat(3),e.appendChild(t),e.setAttribute("aria-haspopup","true"),e.setAttribute("aria-expanded","false"),e.setAttribute("role",this.tabNavigation?"button":"menuitem"),this._overflow=e}}),this.addController(this._subMenuController),this.addController(this._overflowController),this.addEventListener("mousedown",()=>this._hideTooltip(!0)),this.addEventListener("mouseleave",()=>this._hideTooltip()),this._container=this.shadowRoot.querySelector('[part="container"]')}updated(e){super.updated(e),(e.has("items")||e.has("_theme")||e.has("disabled"))&&this.__renderButtons(this.items),(e.has("items")||e.has("_theme")||e.has("reverseCollapse"))&&this.__scheduleOverflow(),e.has("items")&&this.__updateSubMenu(),e.has("_theme")&&this._themeChanged(this._theme),e.has("disabled")&&this._overflow.toggleAttribute("disabled",this.disabled),e.has("tabNavigation")&&this._tabNavigationChanged(this.tabNavigation),e.has("__effectiveI18n")&&this.__i18nChanged(this.__effectiveI18n)}_getItems(){return this._buttons}disconnectedCallback(){super.disconnectedCallback(),this._hideTooltip(!0)}_onResize(){this.__scheduleOverflow()}_themeChanged(e){e?(this._overflow.setAttribute("theme",e),this._subMenu.setAttribute("theme",e)):(this._overflow.removeAttribute("theme"),this._subMenu.removeAttribute("theme"))}_tabNavigationChanged(e){const t=this.querySelector('[tabindex="0"]');this._buttons.forEach(n=>{t?this._setTabindex(n,n===t):this._setTabindex(n,!1),n.setAttribute("role",e?"button":"menuitem")}),this.setAttribute("role",e?"group":"menubar")}__updateSubMenu(){const e=this._subMenu;if(e&&e.opened){const t=e._positionTarget;(!t.isConnected||!Array.isArray(t.item.children)||t.item.children.length===0)&&e.close()}}__i18nChanged(e){e&&e.moreOptions!==void 0&&(e.moreOptions?this._overflow.setAttribute("aria-label",e.moreOptions):this._overflow.removeAttribute("aria-label"))}__getOverflowCount(e){return e.item&&e.item.children&&e.item.children.length||0}__restoreButtons(e){e.forEach(t=>{t.style.visibility="",t.style.position="",t.style.width="";const n=t.item&&t.item.component;n instanceof HTMLElement&&n.getAttribute("role")==="menuitem"&&this.__restoreItem(t,n)}),this.__updateOverflow([])}__restoreItem(e,t){e.appendChild(t),t.removeAttribute("role"),t.removeAttribute("aria-expanded"),t.removeAttribute("aria-haspopup"),t.removeAttribute("tabindex")}__updateOverflow(e){this._overflow.item={children:e},this._hasOverflow=e.length>0}__setOverflowItems(e,t){const n=this._container;if(n.offsetWidth<n.scrollWidth){this._hasOverflow=!0;const r=this.__isRTL,o=n.offsetLeft,a=[...e];for(;a.length;){const d=a[a.length-1],h=d.offsetLeft-o;if(!r&&h+d.offsetWidth<n.offsetWidth-t.offsetWidth||r&&h>=t.offsetWidth)break;const c=this.reverseCollapse?a.shift():a.pop();c.style.width=getComputedStyle(c).width,c.style.visibility="hidden",c.style.position="absolute"}const l=e.filter(d=>!a.includes(d)).map(d=>d.item);this.__updateOverflow(l)}}__scheduleOverflow(){this._overflowDebouncer=D.debounce(this._overflowDebouncer,te,()=>{this.__detectOverflow()})}__detectOverflow(){const e=this._overflow,t=this._buttons.filter(l=>l!==e),n=this.__getOverflowCount(e);this.__restoreButtons(t),this.__setOverflowItems(t,e);const r=this.__getOverflowCount(e);n!==r&&this._subMenu.opened&&this._subMenu.close();const o=r===t.length||r===0&&t.length===1;this.toggleAttribute("has-single-button",o);const a=t.filter(l=>l.style.visibility!=="hidden");a.length?a.some(l=>l.getAttribute("tabindex")==="0")||this._setTabindex(a[a.length-1],!0):this._overflow.setAttribute("tabindex","0"),a.forEach((l,d,h)=>{l.toggleAttribute("first-visible",d===0),l.toggleAttribute("last-visible",!this._hasOverflow&&d===h.length-1)})}__getButtonTheme(e,t){let n=t;const r=e&&e.theme;return r!=null&&(n=Array.isArray(r)?r.join(" "):r),n}__getComponent(e){const t=e.component;let n;const r=t instanceof HTMLElement;if(r&&t.localName==="vaadin-menu-bar-item"?n=t:(n=document.createElement("vaadin-menu-bar-item"),n.appendChild(r?t:document.createElement(t))),e.text){const o=n.firstChild||n;o.textContent=e.text}return n}__renderButtons(e=[]){Ut(y`
          ${e.map(t=>{const n={...t},r=!!(t&&t.children);if(n.component){const o=this.__getComponent(n);n.component=o,o.item=n}return y`
              <vaadin-menu-bar-button
                .item="${n}"
                .disabled="${this.disabled||t.disabled}"
                role="${this.tabNavigation?"button":"menuitem"}"
                aria-haspopup="${B(r?"true":Ue)}"
                aria-expanded="${B(r?"false":Ue)}"
                class="${B(t.className||Ue)}"
                theme="${B(this.__getButtonTheme(t,this._theme)||Ue)}"
                @click="${this.__onRootButtonClick}"
                >${$u(n)}</vaadin-menu-bar-button
              >
            `})}
        `,this,{renderBefore:this._overflow})}__onRootButtonClick(e){const t=e.target;t.item&&t.item.component&&!e.composedPath().includes(t.item.component)&&(e.stopPropagation(),t.item.component.click())}_showTooltip(e,t){const n=this._tooltipController.node;n&&n.isConnected&&(n.generator===void 0&&(n.generator=({item:r})=>r&&r.tooltip),n._mouseLeaveListenerAdded||(n._overlayElement.addEventListener("mouseleave",this.__boundOnTooltipMouseLeave),n._mouseLeaveListenerAdded=!0),this._subMenu.opened||(this._tooltipController.setTarget(e),this._tooltipController.setContext({item:e.item}),n._stateController.open({hover:t,focus:!t})))}_hideTooltip(e){const t=this._tooltipController&&this._tooltipController.node;t&&(this._tooltipController.setContext({item:null}),t._stateController.close(e))}__onTooltipOverlayMouseLeave(e){e.relatedTarget!==this._tooltipController.target&&this._hideTooltip()}_setExpanded(e,t){e.toggleAttribute("expanded",t),e.toggleAttribute("active",t),e.setAttribute("aria-expanded",t?"true":"false")}_setTabindex(e,t){this.tabNavigation&&this._isItemFocusable(e)?e.setAttribute("tabindex","0"):e.setAttribute("tabindex",t?"0":"-1")}_focusItem(e,t,n){const r=n&&this.focused===this._expandedButton;r&&this._close(),super._focusItem(e,t,n),this._buttons.forEach(o=>{this._setTabindex(o,o===e)}),r&&e.item&&e.item.children?this.__openSubMenu(e,!0,{keepFocus:!0}):e===this._overflow?this._hideTooltip():this._showTooltip(e)}_getButtonFromEvent(e){return Array.from(e.composedPath()).find(t=>t.localName==="vaadin-menu-bar-button")}_shouldSetFocus(e){return e.composedPath().includes(this._subMenu)?!1:super._shouldSetFocus(e)}_shouldRemoveFocus(e){return e.composedPath().includes(this._subMenu)?!1:super._shouldRemoveFocus(e)}_setFocused(e){if(e){const t=this.__getFocusTarget();t&&this._buttons.forEach(n=>{this._setTabindex(n,n===t),n===t&&n!==this._overflow&&Q()&&this._showTooltip(n)})}else this._hideTooltip()}__getFocusTarget(){let e=this._buttons.find(t=>Je(t));if(!e){const t=this.tabNavigation?"[focused]":'[tabindex="0"]';e=this.querySelector(`vaadin-menu-bar-button${t}`),se(e)&&(e=this._buttons[this._getFocusableIndex()])}return e}_onArrowDown(e){e.preventDefault();const t=this._getButtonFromEvent(e);t===this._expandedButton?this._focusFirstItem():this.__openSubMenu(t,!0)}_onArrowUp(e){e.preventDefault();const t=this._getButtonFromEvent(e);t===this._expandedButton?this._focusLastItem():this.__openSubMenu(t,!0,{focusLast:!0})}_onEscape(e){e.composedPath().includes(this._expandedButton)&&this._close(!0),this._hideTooltip(!0)}_onKeyDown(e){e.composedPath().includes(this._subMenu)||this._handleKeyDown(e)}_handleKeyDown(e){switch(e.key){case"ArrowDown":this._onArrowDown(e);break;case"ArrowUp":this._onArrowUp(e);break;default:super._onKeyDown(e);break}}_onMouseOver(e){if(e.composedPath().includes(this._subMenu))return;const t=this._getButtonFromEvent(e);t?t!==this._expandedButton&&(t.item.children&&(this.openOnHover||this._subMenu.opened)&&this.__openSubMenu(t,!1),t===this._overflow||this.openOnHover&&t.item.children?this._hideTooltip():this._showTooltip(t,!0)):this._hideTooltip()}__onContextMenuKeydown(e){const t=Array.from(e.composedPath()).find(n=>n._item);if(t){const n=t.parentNode;e.keyCode===38&&t===n.items[0]&&this._close(!0),(e.keyCode===37||e.keyCode===39&&!t._item.children)&&(e.stopImmediatePropagation(),this._handleKeyDown(e)),e.key==="Tab"&&this.tabNavigation&&this._handleKeyDown(e)}}__fireItemSelected(e){this.dispatchEvent(new CustomEvent("item-selected",{detail:{value:e}}))}__onButtonClick(e){const t=this._getButtonFromEvent(e);t&&this.__openSubMenu(t,t.__triggeredWithActiveKeys)}__openSubMenu(e,t,n={}){if(e.disabled)return;const r=this._subMenu,o=e.item;if(r.opened&&(this._close(),r.listenOn===e))return;const a=o&&o.children;if(!a||a.length===0){this.__fireItemSelected(o);return}r.items=a,r.listenOn=e,r._positionTarget=e;const l=r._overlayElement;l.noVerticalOverlap=!0,this._hideTooltip(!0),this._expandedButton=e,this._setExpanded(e,!0),this.style.pointerEvents="auto",e.dispatchEvent(new CustomEvent("opensubmenu",{detail:{children:a}})),l.addEventListener("vaadin-overlay-open",()=>{if(n.focusLast&&this._focusLastItem(),n.keepFocus){const d={focusVisible:Q()};this._focusItem(this._expandedButton,d,!1)}t||l.$.overlay.focus()},{once:!0})}_focusFirstItem(){this._subMenu._overlayElement._contentRoot.firstElementChild.focus()}_focusLastItem(){const e=this._subMenu._overlayElement._contentRoot.firstElementChild,t=e.items[e.items.length-1];t&&t.focus()}__onItemSelected(e){e.stopPropagation(),this.__fireItemSelected(e.detail.value)}__onEscapeClose(){this.__deactivateButton(!0)}__deactivateButton(e){const t=this._expandedButton;if(t&&t.hasAttribute("expanded")){if(this._setExpanded(t,!1),e){const n={focusVisible:Q()};this._focusItem(t,n,!1)}this._expandedButton=null}}_close(e=!1){this.style.pointerEvents="",this.__deactivateButton(e),this._subMenu.opened&&this._subMenu.close()}close(){this._close()}_isItemFocusable(e){return e.disabled&&e.__shouldAllowFocusWhenDisabled?e.__shouldAllowFocusWhenDisabled():super._isItemFocusable(e)}};/**
 * @license
 * Copyright (c) 2019 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Bu extends Nu(L(T(I(A(E))))){static get is(){return"vaadin-menu-bar"}static get styles(){return Lu}render(){return y`
      <div part="container" @click="${this.__onButtonClick}" @mouseover="${this._onMouseOver}">
        <slot></slot>
        <slot name="overflow"></slot>
      </div>

      <slot name="submenu"></slot>

      <slot name="tooltip"></slot>
    `}ready(){super.ready(),this._tooltipController=new X(this),this._tooltipController.setManual(!0),this.addController(this._tooltipController)}}w(Bu);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */Xt({name:"vaadin-contextmenu",deps:["touchstart","touchmove","touchend","contextmenu"],flow:{start:["touchstart","contextmenu"],end:["contextmenu"]},emits:["vaadin-contextmenu"],info:{sourceEvent:null},reset(){this.info.sourceEvent=null,this._cancelTimer(),this.info.touchJob=null,this.info.touchStartCoords=null},_cancelTimer(){this._timerId&&(clearTimeout(this._timerId),delete this._fired)},_setSourceEvent(s){this.info.sourceEvent=s;const i=s.composedPath();this.info.sourceEvent.__composedPath=i},touchstart(s){this._setSourceEvent(s),this.info.touchStartCoords={x:s.changedTouches[0].clientX,y:s.changedTouches[0].clientY};const i=s.composedPath()[0]||s.target;this._timerId=setTimeout(()=>{const e=s.changedTouches[0];s.shiftKey||(ze&&(this._fired=!0,this.fire(i,e.clientX,e.clientY)),et("tap"))},500)},touchmove(s){const e=this.info.touchStartCoords;(Math.abs(e.x-s.changedTouches[0].clientX)>15||Math.abs(e.y-s.changedTouches[0].clientY)>15)&&this._cancelTimer()},touchend(s){this._fired&&s.preventDefault(),this._cancelTimer()},contextmenu(s){if(!s.shiftKey){if(this._setSourceEvent(s),un&&Q()){const i=s.composedPath()[0],e=i.getBoundingClientRect();this.fire(i,e.left,e.bottom)}else this.fire(s.target,s.clientX,s.clientY);et("tap")}},fire(s,i,e){const t=this.info.sourceEvent,n=new Event("vaadin-contextmenu",{bubbles:!0,cancelable:!0,composed:!0});n.detail={x:i,y:e,sourceEvent:t},s.dispatchEvent(n),n.defaultPrevented&&t&&t.preventDefault&&t.preventDefault()}});/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Vu extends ti(T(z(I(A(E))))){static get is(){return"vaadin-context-menu-item"}static get styles(){return Or}render(){return y`
      <span part="checkmark" aria-hidden="true"></span>
      <div part="content">
        <slot></slot>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","menuitem")}}w(Vu);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Hu extends ii(T(z(I(A(E))))){static get is(){return"vaadin-context-menu-list-box"}static get styles(){return hs}static get properties(){return{orientation:{type:String,readOnly:!0}}}get _scrollerElement(){return this.shadowRoot.querySelector('[part="items"]')}render(){return y`
      <div part="items">
        <slot></slot>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","menu")}}w(Hu);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Wu=C`
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
`,qu=[me,Mr,Wu];/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Uu extends Pr(ge(z(T(I(A(E)))))){static get is(){return"vaadin-context-menu-overlay"}static get properties(){return{position:{type:String,reflectToAttribute:!0}}}static get styles(){return qu}_updatePosition(){if(super._updatePosition(),this.parentOverlay==null&&this.positionTarget&&this.position&&this.opened){if(this.position==="bottom"||this.position==="top"){const i=this.positionTarget.getBoundingClientRect(),e=this.$.overlay.getBoundingClientRect(),t=i.width/2-e.width/2;if(this.style.left){const n=e.left+t;n>0&&(this.style.left=`${n}px`)}if(this.style.right){const n=parseFloat(this.style.right)+t;n>0&&(this.style.right=`${n}px`)}}if(this.position==="start"||this.position==="end"){const i=this.positionTarget.getBoundingClientRect(),e=this.$.overlay.getBoundingClientRect(),t=i.height/2-e.height/2;this.style.top=`${e.top+t}px`}}}render(){return y`
      <div id="backdrop" part="backdrop" ?hidden="${!this.withBackdrop}"></div>
      <div part="overlay" id="overlay" tabindex="0">
        <div part="content" id="content">
          <slot></slot>
          <slot name="submenu"></slot>
        </div>
      </div>
    `}}w(Uu);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class Yu extends Rr(L(st(I(E)))){static get is(){return"vaadin-context-menu"}static get styles(){return C`
      :host {
        display: block;
      }

      :host([hidden]) {
        display: none !important;
      }
    `}static get properties(){return{position:{type:String}}}render(){const{_context:i,position:e}=this;return y`
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
        theme="${B(this._theme)}"
        exportparts="backdrop, overlay, content"
        @opened-changed="${this._onOverlayOpened}"
        @vaadin-overlay-open="${this._onVaadinOverlayOpen}"
        @vaadin-overlay-closed="${this._onVaadinOverlayClosed}"
      >
        <slot name="overlay"></slot>
        <slot name="submenu" slot="submenu"></slot>
      </vaadin-context-menu-overlay>
    `}__computeHorizontalAlign(i){return i&&["top-end","bottom-end","start-top","start","start-bottom"].includes(i)?"end":"start"}__computeNoHorizontalOverlap(i){return i?["start-top","start","start-bottom","end-top","end","end-bottom"].includes(i):!!this._positionTarget}__computeNoVerticalOverlap(i){return i?["top-start","top-end","top","bottom-start","bottom","bottom-end"].includes(i):!1}__computeVerticalAlign(i){return i&&["top-start","top-end","top","start-bottom","end-bottom"].includes(i)?"bottom":"top"}}w(Yu);function ju(s){s.$contextMenuTargetConnector||(s.$contextMenuTargetConnector={openOnHandler(i){if(s.preventContextMenu&&s.preventContextMenu(i))return;i.preventDefault(),i.stopPropagation(),this.$contextMenuTargetConnector.openEvent=i;let e={};s.getContextMenuBeforeOpenDetail&&(e=s.getContextMenuBeforeOpenDetail(i)),s.dispatchEvent(new CustomEvent("vaadin-context-menu-before-open",{detail:e}))},updateOpenOn(i){this.removeListener(),this.openOnEventType=i,customElements.whenDefined("vaadin-context-menu").then(()=>{_e[i]?pe(s,i,this.openOnHandler):s.addEventListener(i,this.openOnHandler)})},removeListener(){this.openOnEventType&&(_e[this.openOnEventType]?zn(s,this.openOnEventType,this.openOnHandler):s.removeEventListener(this.openOnEventType,this.openOnHandler))},openMenu(i){i.open(this.openEvent)},removeConnector(){this.removeListener(),s.$contextMenuTargetConnector=void 0}})}window.Vaadin.Flow.contextMenuTargetConnector={init:ju};document.addEventListener("click",s=>{const i=s.composedPath().find(e=>e.hasAttribute&&e.hasAttribute("disableonclick"));i&&(i.disabled=!0)});/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function it(s){return s.__cells||Array.from(s.querySelectorAll('[part~="cell"]:not([part~="details-cell"])'))}function Z(s,i){[...s.children].forEach(i)}function ft(s,i){it(s).forEach(i),s.__detailsCell&&i(s.__detailsCell)}function Lr(s,i,e){let t=1;s.forEach(n=>{t%10===0&&(t+=1),n._order=e+t*i,t+=1})}function si(s,i,e){switch(typeof e){case"boolean":s.toggleAttribute(i,e);break;case"string":s.setAttribute(i,e);break;default:s.removeAttribute(i);break}}function $(s,i,e){s.classList.toggle(i,e||e===""),s.part.toggle(i,e||e===""),s.part.length===0&&s.removeAttribute("part")}function Wt(s,i,e){s.forEach(t=>{$(t,i,e)})}function je(s,i){const e=it(s);Object.entries(i).forEach(([t,n])=>{si(s,t,n);const r=`${t}-row`;$(s,r,n),Wt(e,`${r}-cell`,n)})}function js(s,i){const e=it(s);Object.entries(i).forEach(([t,n])=>{const r=s.getAttribute(t);if(si(s,t,n),r){const o=`${t}-${r}-row`;$(s,o,!1),Wt(e,`${o}-cell`,!1)}if(n){const o=`${t}-${n}-row`;$(s,o,n),Wt(e,`${o}-cell`,n)}})}function Me(s,i,e,t,n){si(s,i,e),n&&$(s,n,!1),$(s,t||`${i}-cell`,e)}function Gu(s){return it(s).find(i=>i._content.querySelector("vaadin-grid-tree-toggle"))}class xe{constructor(i,e){this.__host=i,this.__callback=e,this.__currentSlots=[],this.__onMutation=this.__onMutation.bind(this),this.__observer=new MutationObserver(this.__onMutation),this.__observer.observe(i,{childList:!0}),this.__initialCallDebouncer=D.debounce(this.__initialCallDebouncer,te,()=>this.__onMutation())}disconnect(){this.__observer.disconnect(),this.__initialCallDebouncer.cancel(),this.__toggleSlotChangeListeners(!1)}flush(){this.__onMutation()}__toggleSlotChangeListeners(i){this.__currentSlots.forEach(e=>{i?e.addEventListener("slotchange",this.__onMutation):e.removeEventListener("slotchange",this.__onMutation)})}__onMutation(){const i=!this.__currentColumns;this.__currentColumns=this.__currentColumns||[];const e=xe.getColumns(this.__host),t=e.filter(a=>!this.__currentColumns.includes(a)),n=this.__currentColumns.filter(a=>!e.includes(a)),r=this.__currentColumns.some((a,l)=>a!==e[l]);this.__currentColumns=e,this.__toggleSlotChangeListeners(!1),this.__currentSlots=[...this.__host.children].filter(a=>a instanceof HTMLSlotElement),this.__toggleSlotChangeListeners(!0),(i||t.length||n.length||r)&&this.__callback(t,n)}static __isColumnElement(i){return i.nodeType===Node.ELEMENT_NODE&&/\bcolumn\b/u.test(i.localName)}static getColumns(i){const e=[],t=i._isColumnElement||xe.__isColumnElement;return[...i.children].forEach(n=>{t(n)?e.push(n):n instanceof HTMLSlotElement&&[...n.assignedElements({flatten:!0})].filter(r=>t(r)).forEach(r=>e.push(r))}),e}}/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Fr=s=>class extends s{static get properties(){return{resizable:{type:Boolean,sync:!0,value(){if(this.localName==="vaadin-grid-column-group")return;const e=this.parentNode;return e&&e.localName==="vaadin-grid-column-group"&&e.resizable||!1}},frozen:{type:Boolean,value:!1,sync:!0},frozenToEnd:{type:Boolean,value:!1,sync:!0},rowHeader:{type:Boolean,value:!1,sync:!0},hidden:{type:Boolean,value:!1,sync:!0},header:{type:String,sync:!0},textAlign:{type:String,sync:!0},headerPartName:{type:String,sync:!0},footerPartName:{type:String,sync:!0},_lastFrozen:{type:Boolean,value:!1,sync:!0},_bodyContentHidden:{type:Boolean,value:!1,sync:!0},_firstFrozenToEnd:{type:Boolean,value:!1,sync:!0},_order:{type:Number,sync:!0},_reorderStatus:{type:Boolean,sync:!0},_emptyCells:Array,_headerCell:{type:Object,sync:!0},_footerCell:{type:Object,sync:!0},_grid:Object,__initialized:{type:Boolean,value:!0},headerRenderer:{type:Function,sync:!0},_headerRenderer:{type:Function,computed:"_computeHeaderRenderer(headerRenderer, header, __initialized)"},footerRenderer:{type:Function,sync:!0},_footerRenderer:{type:Function,computed:"_computeFooterRenderer(footerRenderer, __initialized)"},__gridColumnElement:{type:Boolean,value:!0}}}static get observers(){return["_widthChanged(width, _headerCell, _footerCell, _cells)","_frozenChanged(frozen, _headerCell, _footerCell, _cells)","_frozenToEndChanged(frozenToEnd, _headerCell, _footerCell, _cells)","_flexGrowChanged(flexGrow, _headerCell, _footerCell, _cells)","_textAlignChanged(textAlign, _cells, _headerCell, _footerCell)","_orderChanged(_order, _headerCell, _footerCell, _cells)","_lastFrozenChanged(_lastFrozen)","_firstFrozenToEndChanged(_firstFrozenToEnd)","_onRendererOrBindingChanged(_renderer, _cells, _bodyContentHidden, path)","_onHeaderRendererOrBindingChanged(_headerRenderer, _headerCell, path, header)","_onFooterRendererOrBindingChanged(_footerRenderer, _footerCell)","_resizableChanged(resizable, _headerCell)","_reorderStatusChanged(_reorderStatus, _headerCell, _footerCell, _cells)","_hiddenChanged(hidden, _headerCell, _footerCell, _cells)","_rowHeaderChanged(rowHeader, _cells)","__headerFooterPartNameChanged(_headerCell, _footerCell, headerPartName, footerPartName)"]}get _grid(){return this._gridValue||(this._gridValue=this._findHostGrid()),this._gridValue}get _allCells(){return[].concat(this._cells||[]).concat(this._emptyCells||[]).concat(this._headerCell).concat(this._footerCell).filter(e=>e)}connectedCallback(){super.connectedCallback(),requestAnimationFrame(()=>{this._grid&&this._allCells.forEach(e=>{e._content.parentNode||this._grid.appendChild(e._content)})})}disconnectedCallback(){super.disconnectedCallback(),requestAnimationFrame(()=>{this._grid||this._allCells.forEach(e=>{e._content.parentNode&&e._content.parentNode.removeChild(e._content)})}),this._gridValue=void 0}_findHostGrid(){let e=this;for(;e&&!/^vaadin.*grid(-pro)?$/u.test(e.localName);)e=e.assignedSlot?e.assignedSlot.parentNode:e.parentNode;return e||void 0}_renderHeaderAndFooter(){this._renderHeaderCellContent(this._headerRenderer,this._headerCell),this._renderFooterCellContent(this._footerRenderer,this._footerCell)}_flexGrowChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("flexGrow"),this._allCells.forEach(t=>{t.style.flexGrow=e})}_orderChanged(e){this._allCells.forEach(t=>{t.style.order=e})}_widthChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("width"),this._allCells.forEach(t=>{t.style.width=e})}_frozenChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("frozen",e),this._allCells.forEach(t=>{Me(t,"frozen",e)}),this._grid&&this._grid._frozenCellsChanged&&this._grid._frozenCellsChanged()}_frozenToEndChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("frozenToEnd",e),this._allCells.forEach(t=>{this._grid&&t.parentElement===this._grid.$.sizer||Me(t,"frozen-to-end",e)}),this._grid&&this._grid._frozenCellsChanged&&this._grid._frozenCellsChanged()}_lastFrozenChanged(e){this._allCells.forEach(t=>{Me(t,"last-frozen",e)}),this.parentElement&&this.parentElement._columnPropChanged&&(this.parentElement._lastFrozen=e)}_firstFrozenToEndChanged(e){this._allCells.forEach(t=>{this._grid&&t.parentElement===this._grid.$.sizer||Me(t,"first-frozen-to-end",e)}),this.parentElement&&this.parentElement._columnPropChanged&&(this.parentElement._firstFrozenToEnd=e)}_rowHeaderChanged(e,t){t&&t.forEach(n=>{n.setAttribute("role",e?"rowheader":"gridcell")})}_generateHeader(e){return e.substr(e.lastIndexOf(".")+1).replace(/([A-Z])/gu,"-$1").toLowerCase().replace(/-/gu," ").replace(/^./u,t=>t.toUpperCase())}_reorderStatusChanged(e){const t=this.__previousReorderStatus,n=t?`reorder-${t}-cell`:"",r=`reorder-${e}-cell`;this._allCells.forEach(o=>{Me(o,"reorder-status",e,r,n)}),this.__previousReorderStatus=e}_resizableChanged(e,t){e===void 0||t===void 0||t&&[t].concat(this._emptyCells).forEach(n=>{if(n){const r=n.querySelector('[part~="resize-handle"]');if(r&&n.removeChild(r),e){const o=document.createElement("div");$(o,"resize-handle",!0),n.appendChild(o)}}})}_textAlignChanged(e){if(!(e===void 0||this._grid===void 0)){if(["start","end","center"].indexOf(e)===-1){console.warn('textAlign can only be set as "start", "end" or "center"');return}this._allCells.forEach(t=>{t._content.style.textAlign=e})}}_hiddenChanged(e){this.parentElement&&this.parentElement._columnPropChanged&&this.parentElement._columnPropChanged("hidden",e),!!e!=!!this._previousHidden&&this._grid&&(e===!0&&this._allCells.forEach(t=>{t._content.parentNode&&t._content.parentNode.removeChild(t._content)}),this._grid._debouncerHiddenChanged=D.debounce(this._grid._debouncerHiddenChanged,ue,()=>{this._grid&&this._grid._renderColumnTree&&this._grid._renderColumnTree(this._grid._columnTree)}),this._grid._debounceUpdateFrozenColumn&&this._grid._debounceUpdateFrozenColumn(),this._grid._resetKeyboardNavigation&&this._grid._resetKeyboardNavigation()),this._previousHidden=e}_runRenderer(e,t,n){const r=n&&n.item&&!t.parentElement.hidden;if(!(r||e===this._headerRenderer||e===this._footerRenderer))return;const a=[t._content,this];r&&a.push(n),e.apply(this,a)}__renderCellsContent(e,t){this.hidden||!this._grid||t.forEach(n=>{if(!n.parentElement)return;const r=this._grid.__getRowModel(n.parentElement);e&&(n._renderer!==e&&this._clearCellContent(n),n._renderer=e,this._runRenderer(e,n,r))})}_clearCellContent(e){e._content.innerHTML="",delete e._content._$litPart$}_renderHeaderCellContent(e,t){!t||!e||(this.__renderCellsContent(e,[t]),this._grid&&t.parentElement&&this._grid.__debounceUpdateHeaderFooterRowVisibility(t.parentElement))}_onHeaderRendererOrBindingChanged(e,t,...n){this._renderHeaderCellContent(e,t)}__headerFooterPartNameChanged(e,t,n,r){[{cell:e,partName:n},{cell:t,partName:r}].forEach(({cell:o,partName:a})=>{if(o){const l=o.__customParts||[];o.part.remove(...l),o.__customParts=a?a.trim().split(" "):[],o.part.add(...o.__customParts)}})}_renderBodyCellsContent(e,t){!t||!e||this.__renderCellsContent(e,t)}_onRendererOrBindingChanged(e,t,...n){this._renderBodyCellsContent(e,t)}_renderFooterCellContent(e,t){!t||!e||(this.__renderCellsContent(e,[t]),this._grid&&t.parentElement&&this._grid.__debounceUpdateHeaderFooterRowVisibility(t.parentElement))}_onFooterRendererOrBindingChanged(e,t){this._renderFooterCellContent(e,t)}__setTextContent(e,t){e.textContent!==t&&(e.textContent=t)}__textHeaderRenderer(){this.__setTextContent(this._headerCell._content,this.header)}_defaultHeaderRenderer(){this.path&&this.__setTextContent(this._headerCell._content,this._generateHeader(this.path))}_defaultRenderer(e,t,{item:n}){this.path&&this.__setTextContent(e,Ee(this.path,n))}_defaultFooterRenderer(){}_computeHeaderRenderer(e,t){return e||(t!=null?this.__textHeaderRenderer:this._defaultHeaderRenderer)}_computeRenderer(e){return e||this._defaultRenderer}_computeFooterRenderer(e){return e||this._defaultFooterRenderer}},Ku=s=>class extends Fr(z(s)){static get properties(){return{width:{type:String,value:"100px",sync:!0},flexGrow:{type:Number,value:1,sync:!0},renderer:{type:Function,sync:!0},_renderer:{type:Function,computed:"_computeRenderer(renderer, __initialized)"},path:{type:String,sync:!0},autoWidth:{type:Boolean,value:!1},_focusButtonMode:{type:Boolean,value:!1},_cells:{type:Array,sync:!0}}}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class $r extends Ku(I(E)){static get is(){return"vaadin-grid-column"}}w($r);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Xu=C`
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
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Qu=s=>class extends s{static get properties(){return{accessibleName:{type:String}}}static get observers(){return["__a11yUpdateGridSize(size, _columnTree, __emptyState)"]}__a11yGetHeaderRowCount(e){return e.filter(t=>t.some(n=>n.headerRenderer||n.path&&n.header!==null||n.header)).length}__a11yGetFooterRowCount(e){return e.filter(t=>t.some(n=>n.footerRenderer)).length}__a11yUpdateGridSize(e,t,n){if(e===void 0||t===void 0)return;const r=this.__a11yGetHeaderRowCount(t),o=this.__a11yGetFooterRowCount(t),l=(n?1:e)+r+o;this.$.table.setAttribute("aria-rowcount",l);const d=t[t.length-1],h=n?1:l&&d&&d.length||0;this.$.table.setAttribute("aria-colcount",h),this.__a11yUpdateHeaderRows(),this.__a11yUpdateFooterRows()}__a11yUpdateHeaderRows(){Z(this.$.header,(e,t)=>{e.setAttribute("aria-rowindex",t+1)})}__a11yUpdateFooterRows(){Z(this.$.footer,(e,t)=>{e.setAttribute("aria-rowindex",this.__a11yGetHeaderRowCount(this._columnTree)+this.size+t+1)})}__a11yUpdateRowRowindex(e){e.setAttribute("aria-rowindex",e.index+this.__a11yGetHeaderRowCount(this._columnTree)+1)}__a11yUpdateRowSelected(e,t){e.setAttribute("aria-selected",!!t),ft(e,n=>{n.setAttribute("aria-selected",!!t)})}__a11yUpdateRowExpanded(e){const t=Gu(e);this.__isRowExpandable(e)?(e.setAttribute("aria-expanded","false"),t&&t.setAttribute("aria-expanded","false")):this.__isRowCollapsible(e)?(e.setAttribute("aria-expanded","true"),t&&t.setAttribute("aria-expanded","true")):(e.removeAttribute("aria-expanded"),t&&t.removeAttribute("aria-expanded"))}__a11yUpdateRowLevel(e,t){t>0||this.__isRowCollapsible(e)||this.__isRowExpandable(e)?e.setAttribute("aria-level",t+1):e.removeAttribute("aria-level")}__a11ySetRowDetailsCell(e,t){ft(e,n=>{n!==t&&n.setAttribute("aria-controls",t.id)})}__a11yUpdateCellColspan(e,t){e.setAttribute("aria-colspan",Number(t))}__a11yUpdateSorters(){Array.from(this.querySelectorAll("vaadin-grid-sorter")).forEach(e=>{let t=e.parentNode;for(;t&&t.localName!=="vaadin-grid-cell-content";)t=t.parentNode;t&&t.assignedSlot&&t.assignedSlot.parentNode.setAttribute("aria-sort",{asc:"ascending",desc:"descending"}[String(e.direction)]||"none")})}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const zr=s=>s.offsetParent&&!s.part.contains("body-cell")&&mt(s)&&getComputedStyle(s).visibility!=="hidden",Zu=s=>class extends s{static get properties(){return{activeItem:{type:Object,notify:!0,value:null,sync:!0}}}ready(){super.ready(),this.$.scroller.addEventListener("click",this._onClick.bind(this)),this.addEventListener("cell-activate",this._activateItem.bind(this)),this.addEventListener("row-activate",this._activateItem.bind(this))}_activateItem(e){const t=e.detail.model,n=t?t.item:null;n&&(this.activeItem=this._itemsEqual(this.activeItem,n)?null:n)}_shouldPreventCellActivationOnClick(e){const{cell:t}=this._getGridEventLocation(e);return e.defaultPrevented||!t||t.part.contains("details-cell")||t===this.$.emptystatecell||t._content.contains(this.getRootNode().activeElement)||this._isFocusable(e.target)||e.target instanceof HTMLLabelElement}_onClick(e){if(this._shouldPreventCellActivationOnClick(e))return;const{cell:t}=this._getGridEventLocation(e);t&&this.dispatchEvent(new CustomEvent("cell-activate",{detail:{model:this.__getRowModel(t.parentElement)}}))}_isFocusable(e){return zr(e)}};/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Ge(s,i){return s.split(".").reduce((e,t)=>e[t],i)}function Gs(s,i,e){if(e.length===0)return!1;let t=!0;return s.forEach(({path:n})=>{if(!n||n.indexOf(".")===-1)return;const r=n.replace(/\.[^.]*$/u,"");Ge(r,e[0])===void 0&&(console.warn(`Path "${n}" used for ${i} does not exist in all of the items, ${i} is disabled.`),t=!1)}),t}function qt(s){return[void 0,null].indexOf(s)>=0?"":isNaN(s)?s.toString():s}function Ks(s,i){return s=qt(s),i=qt(i),s<i?-1:s>i?1:0}function Ju(s,i){return s.sort((e,t)=>i.map(n=>n.direction==="asc"?Ks(Ge(n.path,e),Ge(n.path,t)):n.direction==="desc"?Ks(Ge(n.path,t),Ge(n.path,e)):0).reduce((n,r)=>n!==0?n:r,0))}function e_(s,i){return s.filter(e=>i.every(t=>{const n=qt(Ge(t.path,e)),r=qt(t.value).toString().toLowerCase();return n.toString().toLowerCase().includes(r)}))}const t_=s=>(i,e)=>{let t=s?[...s]:[];i.filters&&Gs(i.filters,"filtering",t)&&(t=e_(t,i.filters)),Array.isArray(i.sortOrders)&&i.sortOrders.length&&Gs(i.sortOrders,"sorting",t)&&(t=Ju(t,i.sortOrders));const n=Math.min(t.length,i.pageSize),r=i.page*n,o=r+n,a=t.slice(r,o);e(a,t.length)};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const i_=s=>class extends s{static get properties(){return{items:{type:Array,sync:!0}}}static get observers(){return["__dataProviderOrItemsChanged(dataProvider, items, isAttached, items.*)"]}__setArrayDataProvider(e){const t=t_(this.items);t.__items=e,this._arrayDataProvider=t,this.size=e.length,this.dataProvider=t}_onDataProviderPageReceived(){super._onDataProviderPageReceived(),this._arrayDataProvider&&(this.size=this._flatSize)}__dataProviderOrItemsChanged(e,t,n){n&&(this._arrayDataProvider?e!==this._arrayDataProvider?(this._arrayDataProvider=void 0,this.items=void 0):t?this._arrayDataProvider.__items===t?this.clearCache():this.__setArrayDataProvider(t):(this._arrayDataProvider=void 0,this.dataProvider=void 0,this.size=0,this.clearCache()):t&&this.__setArrayDataProvider(t))}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const s_=s=>class extends s{static get properties(){return{__pendingRecalculateColumnWidths:{type:Boolean,value:!0}}}static get observers(){return["__dataProviderChangedAutoWidth(dataProvider)","__columnTreeChangedAutoWidth(_columnTree)","__flatSizeChangedAutoWidth(_flatSize)"]}updated(i){super.updated(i),i.has("__hostVisible")&&!i.get("__hostVisible")&&this.__tryToRecalculateColumnWidthsIfPending()}__dataProviderChangedAutoWidth(i){this.__hasHadRenderedRowsForColumnWidthCalculation||this.recalculateColumnWidths()}__columnTreeChangedAutoWidth(i){queueMicrotask(()=>this.recalculateColumnWidths())}__flatSizeChangedAutoWidth(i){requestAnimationFrame(()=>{i&&!this.__hasHadRenderedRowsForColumnWidthCalculation?this.recalculateColumnWidths():this.__tryToRecalculateColumnWidthsIfPending()})}_onDataProviderPageLoaded(){super._onDataProviderPageLoaded(),this.__tryToRecalculateColumnWidthsIfPending()}_updateFrozenColumn(){super._updateFrozenColumn(),this.__tryToRecalculateColumnWidthsIfPending()}__getIntrinsicWidth(i){return this.__intrinsicWidthCache.has(i)||this.__calculateAndCacheIntrinsicWidths([i]),this.__intrinsicWidthCache.get(i)}__getDistributedWidth(i,e){if(i==null||i===this)return 0;const t=Math.max(this.__getIntrinsicWidth(i),this.__getDistributedWidth(this.__getParentColumnGroup(i),i));if(!e)return t;const n=i,r=t,o=n._visibleChildColumns.map(h=>this.__getIntrinsicWidth(h)).reduce((h,c)=>h+c,0),a=Math.max(0,r-o),d=this.__getIntrinsicWidth(e)/o*a;return this.__getIntrinsicWidth(e)+d}_recalculateColumnWidths(){this.__virtualizer.flush(),[...this.$.header.children,...this.$.footer.children].forEach(r=>{r.__debounceUpdateHeaderFooterRowVisibility&&r.__debounceUpdateHeaderFooterRowVisibility.flush()}),this.__hasHadRenderedRowsForColumnWidthCalculation=this.__hasHadRenderedRowsForColumnWidthCalculation||this._getRenderedRows().length>0,this.__intrinsicWidthCache=new Map;const i=this._firstVisibleIndex,e=this._lastVisibleIndex;this.__viewportRowsCache=this._getRenderedRows().filter(r=>r.index>=i&&r.index<=e);const t=this.__getAutoWidthColumns(),n=new Set;for(const r of t){let o=this.__getParentColumnGroup(r);for(;o&&!n.has(o);)n.add(o),o=this.__getParentColumnGroup(o)}this.__calculateAndCacheIntrinsicWidths([...t,...n]),t.forEach(r=>{r.width=`${this.__getDistributedWidth(r)}px`}),this.__intrinsicWidthCache.clear()}__getParentColumnGroup(i){const e=(i.assignedSlot||i).parentElement;return e&&e!==this?e:null}__setVisibleCellContentAutoWidth(i,e){i._allCells.filter(t=>this.$.items.contains(t)?this.__viewportRowsCache.includes(t.parentElement):!0).forEach(t=>{t.__measuringAutoWidth=e,t.__measuringAutoWidth?(t.__originalWidth=t.style.width,t.style.width="auto",t.style.position="absolute"):(t.style.width=t.__originalWidth,delete t.__originalWidth,t.style.position="")}),e?this.$.scroller.setAttribute("measuring-auto-width",""):this.$.scroller.removeAttribute("measuring-auto-width")}__getAutoWidthCellsMaxWidth(i){return i._allCells.reduce((e,t)=>t.__measuringAutoWidth?Math.max(e,t.offsetWidth+1):e,0)}__calculateAndCacheIntrinsicWidths(i){i.forEach(e=>this.__setVisibleCellContentAutoWidth(e,!0)),i.forEach(e=>{const t=this.__getAutoWidthCellsMaxWidth(e);this.__intrinsicWidthCache.set(e,t)}),i.forEach(e=>this.__setVisibleCellContentAutoWidth(e,!1))}recalculateColumnWidths(){if(!this.__isReadyForColumnWidthCalculation()){this.__pendingRecalculateColumnWidths=!0;return}this._recalculateColumnWidths()}__tryToRecalculateColumnWidthsIfPending(){this.__pendingRecalculateColumnWidths&&(this.__pendingRecalculateColumnWidths=!1,this.recalculateColumnWidths())}__getAutoWidthColumns(){return this._getColumns().filter(i=>!i.hidden&&i.autoWidth)}__isReadyForColumnWidthCalculation(){if(!this._columnTree)return!1;const i=this.__getAutoWidthColumns().filter(o=>!customElements.get(o.localName));if(i.length)return Promise.all(i.map(o=>customElements.whenDefined(o.localName))).then(()=>{this.__tryToRecalculateColumnWidthsIfPending()}),!1;const e=[...this.$.items.children].some(o=>o.index===void 0),t=this._debouncerHiddenChanged&&this._debouncerHiddenChanged.isActive(),n=this.__debounceUpdateFrozenColumn&&this.__debounceUpdateFrozenColumn.isActive(),r=this.clientHeight>0;return!this._dataProviderController.isLoading()&&!e&&!se(this)&&!t&&!n&&r}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const n_=s=>class extends s{static get properties(){return{columnReorderingAllowed:{type:Boolean,value:!1},_orderBaseScope:{type:Number,value:1e7}}}static get observers(){return["_updateOrders(_columnTree)"]}ready(){super.ready(),pe(this,"track",this._onTrackEvent),this._reorderGhost=this.shadowRoot.querySelector('[part="reorder-ghost"]'),this.addEventListener("touchstart",this._onTouchStart.bind(this)),this.addEventListener("touchmove",this._onTouchMove.bind(this)),this.addEventListener("touchend",this._onTouchEnd.bind(this)),this.addEventListener("contextmenu",this._onContextMenu.bind(this))}_onContextMenu(e){this.hasAttribute("reordering")&&(e.preventDefault(),Ne||this._onTrackEnd())}_onTouchStart(e){this._startTouchReorderTimeout=setTimeout(()=>{this._onTrackStart({detail:{x:e.touches[0].clientX,y:e.touches[0].clientY}})},100)}_onTouchMove(e){this._draggedColumn&&e.preventDefault(),clearTimeout(this._startTouchReorderTimeout)}_onTouchEnd(){clearTimeout(this._startTouchReorderTimeout),this._onTrackEnd()}_onTrackEvent(e){if(e.detail.state==="start"){const t=e.composedPath(),n=t[t.indexOf(this.$.header)-2];if(!n||!n._content||n._content.contains(this.getRootNode().activeElement)||this.$.scroller.hasAttribute("column-resizing"))return;this._touchDevice||this._onTrackStart(e)}else e.detail.state==="track"?this._onTrack(e):e.detail.state==="end"&&this._onTrackEnd(e)}_onTrackStart(e){if(!this.columnReorderingAllowed)return;const t=e.composedPath&&e.composedPath();if(t&&t.slice(0,Math.max(0,t.indexOf(this))).some(r=>r.draggable))return;const n=this._cellFromPoint(e.detail.x,e.detail.y);if(!(!n||!n.part.contains("header-cell"))){for(this.toggleAttribute("reordering",!0),this._draggedColumn=n._column;this._draggedColumn.parentElement.childElementCount===1;)this._draggedColumn=this._draggedColumn.parentElement;this._setSiblingsReorderStatus(this._draggedColumn,"allowed"),this._draggedColumn._reorderStatus="dragging",this._updateGhost(n),this._reorderGhost.style.visibility="visible",this._updateGhostPosition(e.detail.x,this._touchDevice?e.detail.y-50:e.detail.y),this._autoScroller()}}_onTrack(e){if(!this._draggedColumn)return;const t=this._cellFromPoint(e.detail.x,e.detail.y);if(!t)return;const n=this._getTargetColumn(t,this._draggedColumn);if(this._isSwapAllowed(this._draggedColumn,n)&&this._isSwappableByPosition(n,e.detail.x)){const r=this._columnTree.findIndex(h=>h.includes(n)),o=this._getColumnsInOrder(r),a=o.indexOf(this._draggedColumn),l=o.indexOf(n),d=a<l?1:-1;for(let h=a;h!==l;h+=d)this._swapColumnOrders(this._draggedColumn,o[h+d])}this._updateGhostPosition(e.detail.x,this._touchDevice?e.detail.y-50:e.detail.y),this._lastDragClientX=e.detail.x}_onTrackEnd(){this._draggedColumn&&(this.toggleAttribute("reordering",!1),this._draggedColumn._reorderStatus="",this._setSiblingsReorderStatus(this._draggedColumn,""),this._draggedColumn=null,this._lastDragClientX=null,this._reorderGhost.style.visibility="hidden",this.dispatchEvent(new CustomEvent("column-reorder",{detail:{columns:this._getColumnsInOrder()}})))}_getColumnsInOrder(e=this._columnTree.length-1){return this._columnTree[e].filter(t=>!t.hidden).sort((t,n)=>t._order-n._order)}_cellFromPoint(e=0,t=0){this._draggedColumn||this.$.scroller.toggleAttribute("no-content-pointer-events",!0);const n=this.shadowRoot.elementFromPoint(e,t);return this.$.scroller.toggleAttribute("no-content-pointer-events",!1),this._getCellFromElement(n)}_getCellFromElement(e){if(e){if(e._column)return e;const{parentElement:t}=e;if(t&&t._focusButton===e)return t}return null}_updateGhostPosition(e,t){const n=this._reorderGhost.getBoundingClientRect(),r=e-n.width/2,o=t-n.height/2,a=parseInt(this._reorderGhost._left||0),l=parseInt(this._reorderGhost._top||0);this._reorderGhost._left=a-(n.left-r),this._reorderGhost._top=l-(n.top-o),this._reorderGhost.style.transform=`translate(${this._reorderGhost._left}px, ${this._reorderGhost._top}px)`}_updateGhost(e){const t=this._reorderGhost;t.textContent=e._content.innerText;const n=window.getComputedStyle(e);return["boxSizing","display","width","height","background","alignItems","padding","border","flex-direction","overflow"].forEach(r=>{t.style[r]=n[r]}),t}_updateOrders(e){e!==void 0&&(e[0].forEach(t=>{t._order=0}),Lr(e[0],this._orderBaseScope,0))}_setSiblingsReorderStatus(e,t){Z(e.parentNode,n=>{/column/u.test(n.localName)&&this._isSwapAllowed(n,e)&&(n._reorderStatus=t)})}_autoScroller(){if(this._lastDragClientX){const e=this._lastDragClientX-this.getBoundingClientRect().right+50,t=this.getBoundingClientRect().left-this._lastDragClientX+50;e>0?this.$.table.scrollLeft+=e/10:t>0&&(this.$.table.scrollLeft-=t/10)}this._draggedColumn&&setTimeout(()=>this._autoScroller(),10)}_isSwapAllowed(e,t){if(e&&t){const n=e!==t,r=e.parentElement===t.parentElement,o=e.frozen&&t.frozen||e.frozenToEnd&&t.frozenToEnd||!e.frozen&&!e.frozenToEnd&&!t.frozen&&!t.frozenToEnd;return n&&r&&o}}_isSwappableByPosition(e,t){const n=Array.from(this.$.header.querySelectorAll('tr:not([hidden]) [part~="cell"]')).find(a=>e.contains(a._column)),r=this.$.header.querySelector("tr:not([hidden]) [reorder-status=dragging]").getBoundingClientRect(),o=n.getBoundingClientRect();return o.left>r.left?t>o.right-r.width:t<o.left+r.width}_swapColumnOrders(e,t){[e._order,t._order]=[t._order,e._order],this._debounceUpdateFrozenColumn(),this._updateFirstAndLastColumn()}_getTargetColumn(e,t){if(e&&t){let n=e._column;for(;n.parentElement!==t.parentElement&&n!==this;)n=n.parentElement;return n.parentElement===t.parentElement?n:e._column}}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const r_=s=>class extends s{ready(){super.ready();const e=this.$.scroller;pe(e,"track",this._onHeaderTrack.bind(this)),e.addEventListener("touchmove",t=>e.hasAttribute("column-resizing")&&t.preventDefault()),e.addEventListener("contextmenu",t=>t.target.part.contains("resize-handle")&&t.preventDefault()),e.addEventListener("mousedown",t=>t.target.part.contains("resize-handle")&&t.preventDefault())}_onHeaderTrack(e){const t=e.target;if(t.part.contains("resize-handle")){let r=t.parentElement._column;for(this.$.scroller.toggleAttribute("column-resizing",!0);r.localName==="vaadin-grid-column-group";)r=r._childColumns.slice(0).sort((c,f)=>c._order-f._order).filter(c=>!c.hidden).pop();const o=this.__isRTL,a=e.detail.x,l=Array.from(this.$.header.querySelectorAll('[part~="row"]:last-child [part~="cell"]')),d=l.find(c=>c._column===r);if(d.offsetWidth){const c=getComputedStyle(d._content),f=10+parseInt(c.paddingLeft)+parseInt(c.paddingRight)+parseInt(c.borderLeftWidth)+parseInt(c.borderRightWidth)+parseInt(c.marginLeft)+parseInt(c.marginRight);let m;const v=d.offsetWidth,x=d.getBoundingClientRect();d.hasAttribute("frozen-to-end")?m=v+(o?a-x.right:x.left-a):m=v+(o?x.left-a:a-x.right),r.width=`${Math.max(f,m)}px`,r.flexGrow=0}l.sort((c,f)=>c._column._order-f._column._order).forEach((c,f,m)=>{f<m.indexOf(d)&&(c._column.width=`${c.offsetWidth}px`,c._column.flexGrow=0)});const h=this._frozenToEndCells[0];if(h&&this.$.table.scrollWidth>this.$.table.offsetWidth){const c=h.getBoundingClientRect(),f=a-(o?c.right:c.left);(o&&f<=0||!o&&f>=0)&&(this.$.table.scrollLeft+=f)}e.detail.state==="end"&&(this.$.scroller.toggleAttribute("column-resizing",!1),this.dispatchEvent(new CustomEvent("column-resize",{detail:{resizedColumn:r}}))),this._resizeHandler()}}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const o_=s=>class extends s{static get properties(){return{size:{type:Number,notify:!0,sync:!0},_flatSize:{type:Number,sync:!0},pageSize:{type:Number,value:50,observer:"_pageSizeChanged",sync:!0},dataProvider:{type:Object,notify:!0,observer:"_dataProviderChanged",sync:!0},loading:{type:Boolean,notify:!0,readOnly:!0,reflectToAttribute:!0},_hasData:{type:Boolean,value:!1,sync:!0},itemHasChildrenPath:{type:String,value:"children",observer:"__itemHasChildrenPathChanged",sync:!0},itemIdPath:{type:String,value:null,sync:!0},expandedItems:{type:Object,notify:!0,value:()=>[],sync:!0},__expandedKeys:{type:Object,computed:"__computeExpandedKeys(itemIdPath, expandedItems)"}}}static get observers(){return["_sizeChanged(size)","_expandedItemsChanged(expandedItems)"]}constructor(){super(),this._dataProviderController=new Ir(this,{size:this.size||0,pageSize:this.pageSize,getItemId:this.getItemId.bind(this),isExpanded:this._isExpanded.bind(this),dataProvider:this.dataProvider?this.dataProvider.bind(this):null,dataProviderParams:()=>({sortOrders:this._mapSorters(),filters:this._mapFilters()})}),this._dataProviderController.addEventListener("page-requested",this._onDataProviderPageRequested.bind(this)),this._dataProviderController.addEventListener("page-received",this._onDataProviderPageReceived.bind(this)),this._dataProviderController.addEventListener("page-loaded",this._onDataProviderPageLoaded.bind(this))}_sizeChanged(e){this._dataProviderController.rootCache.size=e,this._dataProviderController.recalculateFlatSize(),this._flatSize=this._dataProviderController.flatSize}__itemHasChildrenPathChanged(e,t){!t&&e==="children"||this.requestContentUpdate()}__getRowLevel(e){const{level:t}=this._dataProviderController.getFlatIndexContext(e.index);return t}__getRowItem(e){const{item:t}=this._dataProviderController.getFlatIndexContext(e.index);return t}__ensureRowItem(e){this._dataProviderController.ensureFlatIndexLoaded(e.index)}__ensureRowHierarchy(e){this._dataProviderController.ensureFlatIndexHierarchy(e.index)}getItemId(e){return this.itemIdPath?Ee(this.itemIdPath,e):e}_isExpanded(e){return this.__expandedKeys&&this.__expandedKeys.has(this.getItemId(e))}_hasChildren(e){return this.itemHasChildrenPath&&e&&!!Ee(this.itemHasChildrenPath,e)}_expandedItemsChanged(){this._dataProviderController.recalculateFlatSize(),this._flatSize=this._dataProviderController.flatSize,this.__updateVisibleRows()}__computeExpandedKeys(e,t){const n=t||[],r=new Set;return n.forEach(o=>{r.add(this.getItemId(o))}),r}expandItem(e){this._isExpanded(e)||(this.expandedItems=[...this.expandedItems,e])}collapseItem(e){this._isExpanded(e)&&(this.expandedItems=this.expandedItems.filter(t=>!this._itemsEqual(t,e)))}_onDataProviderPageRequested(){this._setLoading(!0)}_onDataProviderPageReceived(){this._flatSize!==this._dataProviderController.flatSize&&(this._shouldLoadAllRenderedRowsAfterPageLoad=!0,this._flatSize=this._dataProviderController.flatSize),this._getRenderedRows().forEach(e=>this.__ensureRowHierarchy(e)),this._hasData=!0}_onDataProviderPageLoaded(){this._debouncerApplyCachedData=D.debounce(this._debouncerApplyCachedData,K.after(0),()=>{this._setLoading(!1);const e=this._shouldLoadAllRenderedRowsAfterPageLoad;this._shouldLoadAllRenderedRowsAfterPageLoad=!1,this._getRenderedRows().forEach(t=>{this.__updateRow(t),e&&this.__ensureRowItem(t)}),this.__scrollToPendingIndexes(),this.__dispatchPendingBodyCellFocus()}),this._dataProviderController.isLoading()||this._debouncerApplyCachedData.flush()}__debounceClearCache(){this.__clearCacheDebouncer=D.debounce(this.__clearCacheDebouncer,te,()=>this.clearCache())}clearCache(){this._dataProviderController.clearCache(),this._dataProviderController.rootCache.size=this.size||0,this._dataProviderController.recalculateFlatSize(),this._hasData=!1,this.__updateVisibleRows(),(!this.__virtualizer||!this.__virtualizer.size)&&this._dataProviderController.loadFirstPage()}_pageSizeChanged(e,t){this._dataProviderController.setPageSize(e),t!==void 0&&e!==t&&this.clearCache()}_checkSize(){this.size===void 0&&this._flatSize===0&&console.warn("The <vaadin-grid> needs the total number of items in order to display rows, which you can specify either by setting the `size` property, or by providing it to the second argument of the `dataProvider` function `callback` call.")}_dataProviderChanged(e,t){this._dataProviderController.setDataProvider(e?e.bind(this):null),t!==void 0&&this.clearCache(),this._ensureFirstPageLoaded(),this._debouncerCheckSize=D.debounce(this._debouncerCheckSize,K.after(2e3),this._checkSize.bind(this))}_ensureFirstPageLoaded(){this._hasData||this._dataProviderController.loadFirstPage()}_itemsEqual(e,t){return this.getItemId(e)===this.getItemId(t)}_getItemIndexInArray(e,t){let n=-1;return t.forEach((r,o)=>{this._itemsEqual(r,e)&&(n=o)}),n}scrollToIndex(...e){if(!this.__virtualizer||!this.clientHeight||!this._columnTree){this.__pendingScrollToIndexes=e;return}let t;for(;t!==(t=this._dataProviderController.getFlatIndexByPath(e));)this._scrollToFlatIndex(t);this._dataProviderController.isLoading()&&(this.__pendingScrollToIndexes=e)}__scrollToPendingIndexes(){if(this.__pendingScrollToIndexes&&this.$.items.children.length){const e=this.__pendingScrollToIndexes;delete this.__pendingScrollToIndexes,this.scrollToIndex(...e)}}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const ct={BETWEEN:"between",ON_TOP_OR_BETWEEN:"on-top-or-between",ON_GRID:"on-grid"},ye={ON_TOP:"on-top",ABOVE:"above",BELOW:"below",EMPTY:"empty"},a_=s=>class extends s{static get properties(){return{dropMode:{type:String,sync:!0},rowsDraggable:{type:Boolean,sync:!0},dragFilter:{type:Function,sync:!0},dropFilter:{type:Function,sync:!0},__dndAutoScrollThreshold:{value:50},__draggedItems:{value:()=>[]}}}static get observers(){return["_dragDropAccessChanged(rowsDraggable, dropMode, dragFilter, dropFilter, loading)"]}constructor(){super(),this.__onDocumentDragStart=this.__onDocumentDragStart.bind(this)}ready(){super.ready(),this.$.table.addEventListener("dragstart",this._onDragStart.bind(this)),this.$.table.addEventListener("dragend",this._onDragEnd.bind(this)),this.$.table.addEventListener("dragover",this._onDragOver.bind(this)),this.$.table.addEventListener("dragleave",this._onDragLeave.bind(this)),this.$.table.addEventListener("drop",this._onDrop.bind(this)),this.$.table.addEventListener("dragenter",e=>{this.dropMode&&(e.preventDefault(),e.stopPropagation())})}connectedCallback(){super.connectedCallback(),document.addEventListener("dragstart",this.__onDocumentDragStart,{capture:!0})}disconnectedCallback(){super.disconnectedCallback(),document.removeEventListener("dragstart",this.__onDocumentDragStart,{capture:!0})}_onDragStart(e){if(this.rowsDraggable){let t=e.target;if(t.localName==="vaadin-grid-cell-content"&&(t=t.assignedSlot.parentNode.parentNode),t.parentNode!==this.$.items)return;if(e.stopPropagation(),this.toggleAttribute("dragging-rows",!0),this._safari){const a=t.style.transform;t.style.top=/translateY\((.*)\)/u.exec(a)[1],t.style.transform="none",requestAnimationFrame(()=>{t.style.top="",t.style.transform=a})}const n=t.getBoundingClientRect();e.dataTransfer.setDragImage(t,e.clientX-n.left,e.clientY-n.top);let r=[t];this._isSelected(t._item)&&(r=this.__getViewportRows().filter(a=>this._isSelected(a._item)).filter(a=>!this.dragFilter||this.dragFilter(this.__getRowModel(a)))),this.__draggedItems=r.map(a=>a._item),e.dataTransfer.setData("text",this.__formatDefaultTransferData(r)),je(t,{dragstart:r.length>1?`${r.length}`:""}),this.style.setProperty("--_grid-drag-start-x",`${e.clientX-n.left+20}px`),this.style.setProperty("--_grid-drag-start-y",`${e.clientY-n.top+10}px`),requestAnimationFrame(()=>{je(t,{dragstart:!1}),this.style.setProperty("--_grid-drag-start-x",""),this.style.setProperty("--_grid-drag-start-y",""),this.requestContentUpdate()});const o=new CustomEvent("grid-dragstart",{detail:{draggedItems:[...this.__draggedItems],setDragData:(a,l)=>e.dataTransfer.setData(a,l),setDraggedItemsCount:a=>t.setAttribute("dragstart",a)}});o.originalEvent=e,this.dispatchEvent(o)}}_onDragEnd(e){this.toggleAttribute("dragging-rows",!1),e.stopPropagation();const t=new CustomEvent("grid-dragend");t.originalEvent=e,this.dispatchEvent(t),this.__draggedItems=[],this.requestContentUpdate()}_onDragLeave(e){this.dropMode&&(e.stopPropagation(),this._clearDragStyles())}_onDragOver(e){if(this.dropMode){if(this._dropLocation=void 0,this._dragOverItem=void 0,this.__dndAutoScroll(e.clientY)){this._clearDragStyles();return}let t=e.composedPath().find(n=>n.localName==="tr");if(this.__updateRowScrollPositionProperty(t),!this._flatSize||this.dropMode===ct.ON_GRID)this._dropLocation=ye.EMPTY;else if(!t||t.parentNode!==this.$.items){if(t)return;if(this.dropMode===ct.BETWEEN||this.dropMode===ct.ON_TOP_OR_BETWEEN)t=Array.from(this.$.items.children).filter(n=>!n.hidden).pop(),this._dropLocation=ye.BELOW;else return}else{const n=t.getBoundingClientRect();if(this._dropLocation=ye.ON_TOP,this.dropMode===ct.BETWEEN){const r=e.clientY-n.top<n.bottom-e.clientY;this._dropLocation=r?ye.ABOVE:ye.BELOW}else this.dropMode===ct.ON_TOP_OR_BETWEEN&&(e.clientY-n.top<n.height/3?this._dropLocation=ye.ABOVE:e.clientY-n.top>n.height/3*2&&(this._dropLocation=ye.BELOW))}if(t&&t.hasAttribute("drop-disabled")){this._dropLocation=void 0;return}e.stopPropagation(),e.preventDefault(),this._dropLocation===ye.EMPTY?this.toggleAttribute("dragover",!0):t?(this._dragOverItem=t._item,t.getAttribute("dragover")!==this._dropLocation&&js(t,{dragover:this._dropLocation})):this._clearDragStyles()}}__onDocumentDragStart(e){if(e.target.contains(this)){const t=[e.target,this.$.items,this.$.scroller],n=t.map(r=>r.style.cssText);this.$.table.scrollHeight>2e4&&(this.$.scroller.style.display="none"),cn&&(e.target.style.willChange="transform"),Ni&&(this.$.items.style.flexShrink=1),requestAnimationFrame(()=>{t.forEach((r,o)=>{r.style.cssText=n[o]})})}}__dndAutoScroll(e){if(this.__dndAutoScrolling)return!0;const t=this.$.header.getBoundingClientRect().bottom,n=this.$.footer.getBoundingClientRect().top,r=t-e+this.__dndAutoScrollThreshold,o=e-n+this.__dndAutoScrollThreshold;let a=0;if(o>0?a=o*2:r>0&&(a=-r*2),a){const l=this.$.table.scrollTop;if(this.$.table.scrollTop+=a,l!==this.$.table.scrollTop)return this.__dndAutoScrolling=!0,setTimeout(()=>{this.__dndAutoScrolling=!1},20),!0}}__getViewportRows(){const e=this.$.header.getBoundingClientRect().bottom,t=this.$.footer.getBoundingClientRect().top;return Array.from(this.$.items.children).filter(n=>{const r=n.getBoundingClientRect();return r.bottom>e&&r.top<t})}_clearDragStyles(){this.removeAttribute("dragover"),Z(this.$.items,e=>{js(e,{dragover:null})})}__updateDragSourceParts(e,t){je(e,{"drag-source":this.__draggedItems.includes(t.item)})}_onDrop(e){if(this.dropMode&&this._dropLocation){e.stopPropagation(),e.preventDefault();const t=e.dataTransfer.types&&Array.from(e.dataTransfer.types).map(r=>({type:r,data:e.dataTransfer.getData(r)}));this._clearDragStyles();const n=new CustomEvent("grid-drop",{bubbles:e.bubbles,cancelable:e.cancelable,detail:{dropTargetItem:this._dragOverItem,dropLocation:this._dropLocation,dragData:t}});n.originalEvent=e,this.dispatchEvent(n)}}__formatDefaultTransferData(e){return e.map(t=>Array.from(t.children).filter(n=>!n.hidden&&!n.part.contains("details-cell")).sort((n,r)=>n._column._order>r._column._order?1:-1).map(n=>n._content.textContent.trim()).filter(n=>n).join("	")).join(`
`)}_dragDropAccessChanged(){this.filterDragAndDrop()}filterDragAndDrop(){Z(this.$.items,e=>{e.hidden||this._filterDragAndDrop(e,this.__getRowModel(e))})}_filterDragAndDrop(e,t){const n=this.loading||e.hasAttribute("loading"),r=!this.rowsDraggable||n||this.dragFilter&&!this.dragFilter(t),o=!this.dropMode||n||this.dropFilter&&!this.dropFilter(t);ft(e,a=>{r?a._content.removeAttribute("draggable"):a._content.setAttribute("draggable",!0)}),je(e,{"drag-disabled":!!r,"drop-disabled":!!o})}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function Nr(s,i){if(!s||!i||s.length!==i.length)return!1;for(let e=0,t=s.length;e<t;e++)if(s[e]instanceof Array&&i[e]instanceof Array){if(!Nr(s[e],i[e]))return!1}else if(s[e]!==i[e])return!1;return!0}const l_=s=>class extends s{static get properties(){return{_columnTree:{type:Object,sync:!0}}}ready(){super.ready(),this._addNodeObserver()}_hasColumnGroups(e){return e.some(t=>t.localName==="vaadin-grid-column-group")}_getChildColumns(e){return xe.getColumns(e)}_flattenColumnGroups(e){return e.map(t=>t.localName==="vaadin-grid-column-group"?this._getChildColumns(t):[t]).reduce((t,n)=>t.concat(n),[])}_getColumnTree(){const e=xe.getColumns(this),t=[e];let n=e;for(;this._hasColumnGroups(n);)n=this._flattenColumnGroups(n),t.push(n);return t}_debounceUpdateColumnTree(){this.__updateColumnTreeDebouncer=D.debounce(this.__updateColumnTreeDebouncer,te,()=>this._updateColumnTree())}_updateColumnTree(){const e=this._getColumnTree();Nr(e,this._columnTree)||(this._columnTree=e)}_addNodeObserver(){this._observer=new xe(this,(e,t)=>{const n=t.flatMap(o=>o._allCells),r=o=>n.filter(a=>a&&a._content.contains(o)).length;this.__removeSorters(this._sorters.filter(r)),this.__removeFilters(this._filters.filter(r)),this._debounceUpdateColumnTree(),this._debouncerCheckImports=D.debounce(this._debouncerCheckImports,K.after(2e3),this._checkImports.bind(this)),this._ensureFirstPageLoaded()})}_checkImports(){["vaadin-grid-column-group","vaadin-grid-filter","vaadin-grid-filter-column","vaadin-grid-tree-toggle","vaadin-grid-selection-column","vaadin-grid-sort-column","vaadin-grid-sorter"].forEach(e=>{this.querySelector(e)&&!customElements.get(e)&&console.warn(`Make sure you have imported the required module for <${e}> element.`)})}_updateFirstAndLastColumn(){Array.from(this.shadowRoot.querySelectorAll("tr")).forEach(e=>this._updateFirstAndLastColumnForRow(e))}_updateFirstAndLastColumnForRow(e){Array.from(e.querySelectorAll('[part~="cell"]:not([part~="details-cell"])')).sort((t,n)=>t._column._order-n._column._order).forEach((t,n,r)=>{Me(t,"first-column",n===0),Me(t,"last-column",n===r.length-1)})}_isColumnElement(e){return e.nodeType===Node.ELEMENT_NODE&&/\bcolumn\b/u.test(e.localName)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const d_=s=>class extends s{getEventContext(e){const t={},{cell:n}=this._getGridEventLocation(e);return n&&(t.section=["body","header","footer","details"].find(r=>n.part.contains(`${r}-cell`)),n._column&&(t.column=n._column),(t.section==="body"||t.section==="details")&&Object.assign(t,this.__getRowModel(n.parentElement))),t}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const h_=s=>class extends s{static get properties(){return{_filters:{type:Array,value:()=>[]}}}constructor(){super(),this._filterChanged=this._filterChanged.bind(this),this.addEventListener("filter-changed",this._filterChanged)}_filterChanged(e){e.stopPropagation(),this.__addFilter(e.target),this.__applyFilters()}__removeFilters(e){e.length!==0&&(this._filters=this._filters.filter(t=>e.indexOf(t)<0),this.__applyFilters())}__addFilter(e){this._filters.indexOf(e)===-1&&this._filters.push(e)}__applyFilters(){this.dataProvider&&this.isAttached&&this.clearCache()}_mapFilters(){return this._filters.map(e=>({path:e.path,value:e.value}))}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */function At(s){return s instanceof HTMLTableRowElement}function Dt(s){return s instanceof HTMLTableCellElement}function Oe(s){return s.matches('[part~="details-cell"]')}const c_=s=>class extends s{static get properties(){return{_headerFocusable:{type:Object,observer:"_focusableChanged",sync:!0},_itemsFocusable:{type:Object,observer:"_focusableChanged",sync:!0},_footerFocusable:{type:Object,observer:"_focusableChanged",sync:!0},_navigatingIsHidden:Boolean,_focusedItemIndex:{type:Number,value:0},_focusedColumnOrder:Number,_focusedCell:{type:Object,observer:"_focusedCellChanged",sync:!0},interacting:{type:Boolean,value:!1,reflectToAttribute:!0,readOnly:!0,observer:"_interactingChanged"}}}get __rowFocusMode(){return[this._headerFocusable,this._itemsFocusable,this._footerFocusable].some(At)}set __rowFocusMode(e){["_itemsFocusable","_footerFocusable","_headerFocusable"].forEach(t=>{const n=this[t];if(e){const r=n&&n.parentElement;Dt(n)?this[t]=r:Dt(r)&&(this[t]=r.parentElement)}else if(!e&&At(n)){const r=n.firstElementChild;this[t]=r._focusButton||r}})}get _visibleItemsCount(){return this._lastVisibleIndex-this._firstVisibleIndex-1}ready(){super.ready(),!(this._ios||this._android)&&(this.addEventListener("keydown",this._onKeyDown),this.addEventListener("keyup",this._onKeyUp),this.addEventListener("focusin",this._onFocusIn),this.addEventListener("focusout",this._onFocusOut),this.$.table.addEventListener("focusin",this._onContentFocusIn.bind(this)),this.addEventListener("mousedown",()=>{this.toggleAttribute("navigating",!1),this._isMousedown=!0,this._focusedColumnOrder=void 0}),this.addEventListener("mouseup",()=>{this._isMousedown=!1}))}_focusableChanged(e,t){t&&t.setAttribute("tabindex","-1"),e&&this._updateGridSectionFocusTarget(e)}_focusedCellChanged(e,t){t&&$(t,"focused-cell",!1),e&&$(e,"focused-cell",!0)}_interactingChanged(){this._updateGridSectionFocusTarget(this._headerFocusable),this._updateGridSectionFocusTarget(this._itemsFocusable),this._updateGridSectionFocusTarget(this._footerFocusable)}__updateItemsFocusable(){if(!this._itemsFocusable)return;const e=this.shadowRoot.activeElement===this._itemsFocusable;this._getRenderedRows().forEach(t=>{if(t.index===this._focusedItemIndex)if(this.__rowFocusMode)this._itemsFocusable=t;else{let n=this._itemsFocusable.parentElement,r=this._itemsFocusable;if(n){Dt(n)&&(r=n,n=n.parentElement);const o=[...n.children].indexOf(r);this._itemsFocusable=this.__getFocusable(t,t.children[o])}}}),e&&this._itemsFocusable.focus()}_onKeyDown(e){const t=e.key;let n;switch(t){case"ArrowUp":case"ArrowDown":case"ArrowLeft":case"ArrowRight":case"PageUp":case"PageDown":case"Home":case"End":n="Navigation";break;case"Enter":case"Escape":case"F2":n="Interaction";break;case"Tab":n="Tab";break;case" ":n="Space";break}this._detectInteracting(e),this.interacting&&n!=="Interaction"&&(n=void 0),n&&this[`_on${n}KeyDown`](e,t)}__ensureFlatIndexInViewport(e){const t=[...this.$.items.children].find(n=>n.index===e);t?this.__scrollIntoViewport(t):this._scrollToFlatIndex(e)}__isRowExpandable(e){return this._hasChildren(e._item)&&!this._isExpanded(e._item)}__isRowCollapsible(e){return this._isExpanded(e._item)}_onNavigationKeyDown(e,t){e.preventDefault();const n=this.__isRTL,r=e.composedPath().find(At),o=e.composedPath().find(Dt);let a=0,l=0;switch(t){case"ArrowRight":a=n?-1:1;break;case"ArrowLeft":a=n?1:-1;break;case"Home":this.__rowFocusMode||e.ctrlKey?l=-1/0:a=-1/0;break;case"End":this.__rowFocusMode||e.ctrlKey?l=1/0:a=1/0;break;case"ArrowDown":l=1;break;case"ArrowUp":l=-1;break;case"PageDown":if(this.$.items.contains(r)){const c=this.__getIndexInGroup(r,this._focusedItemIndex);this._scrollToFlatIndex(c)}l=this._visibleItemsCount;break;case"PageUp":l=-this._visibleItemsCount;break}if(this.__rowFocusMode&&!r||!this.__rowFocusMode&&!o)return;const d=n?"ArrowLeft":"ArrowRight",h=n?"ArrowRight":"ArrowLeft";if(t===d){if(this.__rowFocusMode){if(this.__isRowExpandable(r)){this.expandItem(r._item);return}this.__rowFocusMode=!1,this._onCellNavigation(r.firstElementChild,0,0);return}}else if(t===h)if(this.__rowFocusMode){if(this.__isRowCollapsible(r)){this.collapseItem(r._item);return}}else{const c=[...r.children].sort((f,m)=>f._order-m._order);if(o===c[0]||Oe(o)){this.__rowFocusMode=!0,this._onRowNavigation(r,0);return}}this.__rowFocusMode?this._onRowNavigation(r,l):this._onCellNavigation(o,a,l)}_onRowNavigation(e,t){const{dstRow:n}=this.__navigateRows(t,e);n&&n.focus()}__getIndexInGroup(e,t){const n=e.parentNode;return n===this.$.items?t!==void 0?t:e.index:[...n.children].indexOf(e)}__navigateRows(e,t,n){const r=this.__getIndexInGroup(t,this._focusedItemIndex),o=t.parentNode,a=(o===this.$.items?this._flatSize:o.children.length)-1;let l=Math.max(0,Math.min(r+e,a));if(o!==this.$.items){if(l>r)for(;l<a&&o.children[l].hidden;)l+=1;else if(l<r)for(;l>0&&o.children[l].hidden;)l-=1;return this.toggleAttribute("navigating",!0),{dstRow:o.children[l]}}let d=!1;if(n){const h=Oe(n);if(o===this.$.items){const c=t._item,{item:f}=this._dataProviderController.getFlatIndexContext(l);h?d=e===0:d=e===1&&this._isDetailsOpened(c)||e===-1&&l!==r&&this._isDetailsOpened(f),d!==h&&(e===1&&d||e===-1&&!d)&&(l=r)}}return this.__ensureFlatIndexInViewport(l),this._focusedItemIndex=l,this.toggleAttribute("navigating",!0),{dstRow:[...o.children].find(h=>!h.hidden&&h.index===l),dstIsRowDetails:d}}_onCellNavigation(e,t,n){const r=e.parentNode,{dstRow:o,dstIsRowDetails:a}=this.__navigateRows(n,r,e);if(!o)return;let l=[...r.children].indexOf(e);this.$.items.contains(e)&&(l=[...this.$.sizer.children].findIndex(f=>f._column===e._column));const d=Oe(e),h=r.parentNode,c=this.__getIndexInGroup(r,this._focusedItemIndex);if(this._focusedColumnOrder===void 0&&(d?this._focusedColumnOrder=0:this._focusedColumnOrder=this._getColumns(h,c).filter(f=>!f.hidden)[l]._order),a)[...o.children].find(Oe).focus();else{const f=this.__getIndexInGroup(o,this._focusedItemIndex),m=this._getColumns(h,f).filter(g=>!g.hidden),v=m.map(g=>g._order).sort((g,S)=>g-S),x=v.length-1,b=v.indexOf(v.slice(0).sort((g,S)=>Math.abs(g-this._focusedColumnOrder)-Math.abs(S-this._focusedColumnOrder))[0]),k=n===0&&d?b:Math.max(0,Math.min(b+t,x));k!==b&&(this._focusedColumnOrder=void 0);const _=m.reduce((g,S,F)=>(g[S._order]=F,g),{})[v[k]];let p;if(this.$.items.contains(e)){const g=this.$.sizer.children[_];this._lazyColumns&&(this.__isColumnInViewport(g._column)||g.scrollIntoView(),this.__updateColumnsBodyContentHidden(),this.__updateHorizontalScrollPosition()),p=[...o.children].find(S=>S._column===g._column),this._scrollHorizontallyToCell(p)}else p=o.children[_],this._scrollHorizontallyToCell(p);p.focus({preventScroll:!0})}}_onInteractionKeyDown(e,t){const n=e.composedPath()[0],r=n.localName==="input"&&!/^(button|checkbox|color|file|image|radio|range|reset|submit)$/iu.test(n.type);let o;switch(t){case"Enter":o=this.interacting?!r:!0;break;case"Escape":o=!1;break;case"F2":o=!this.interacting;break}const{cell:a}=this._getGridEventLocation(e);if(this.interacting!==o&&a!==null)if(o){const l=a._content.querySelector("[focus-target]")||[...a._content.querySelectorAll("*")].find(d=>this._isFocusable(d));l&&(e.preventDefault(),l.focus(),this._setInteracting(!0),this.toggleAttribute("navigating",!1))}else e.preventDefault(),this._focusedColumnOrder=void 0,a.focus(),this._setInteracting(!1),this.toggleAttribute("navigating",!0);t==="Escape"&&this._hideTooltip(!0)}_predictFocusStepTarget(e,t){const n=[this.$.table,this._headerFocusable,this.__emptyState?this.$.emptystatecell:this._itemsFocusable,this._footerFocusable,this.$.focusexit];let r=n.indexOf(e);for(r+=t;r>=0&&r<=n.length-1;){let a=n[r];if(a&&!this.__rowFocusMode&&(a=n[r].parentNode),!a||a.hidden)r+=t;else break}let o=n[r];if(o&&!this.__isHorizontallyInViewport(o)){const a=this._getColumnsInOrder().find(l=>this.__isColumnInViewport(l));if(a)if(o===this._headerFocusable)o=a._headerCell;else if(o===this._itemsFocusable){const l=o._column._cells.indexOf(o);o=a._cells[l]}else o===this._footerFocusable&&(o=a._footerCell)}return o}_onTabKeyDown(e){let t=this._predictFocusStepTarget(e.composedPath()[0],e.shiftKey?-1:1);t&&(e.stopPropagation(),t===this._itemsFocusable&&(this.__ensureFlatIndexInViewport(this._focusedItemIndex),this.__updateItemsFocusable(),t=this._itemsFocusable),t.focus(),t!==this.$.table&&t!==this.$.focusexit&&e.preventDefault(),this.toggleAttribute("navigating",!0))}_onSpaceKeyDown(e){e.preventDefault();const t=e.composedPath()[0],n=At(t);(n||!t._content||!t._content.firstElementChild)&&this.dispatchEvent(new CustomEvent(n?"row-activate":"cell-activate",{detail:{model:this.__getRowModel(n?t:t.parentElement)}}))}_onKeyUp(e){if(!/^( |SpaceBar)$/u.test(e.key)||this.interacting)return;e.preventDefault();const t=e.composedPath()[0];if(t._content&&t._content.firstElementChild){const n=this.hasAttribute("navigating");t._content.firstElementChild.dispatchEvent(new MouseEvent("click",{shiftKey:e.shiftKey,bubbles:!0,composed:!0,cancelable:!0})),this.toggleAttribute("navigating",n)}}_onFocusIn(e){this._isMousedown||this.toggleAttribute("navigating",!0);const t=e.composedPath()[0];t===this.$.table||t===this.$.focusexit?(this._isMousedown||this._predictFocusStepTarget(t,t===this.$.table?1:-1).focus(),this._setInteracting(!1)):this._detectInteracting(e)}_onFocusOut(e){this.toggleAttribute("navigating",!1),this._detectInteracting(e),this._hideTooltip(),this._focusedCell=null}_onContentFocusIn(e){const{section:t,cell:n,row:r}=this._getGridEventLocation(e);if(!(!n&&!this.__rowFocusMode)&&(this._detectInteracting(e),t&&(n||r)))if(this._activeRowGroup=t,t===this.$.header?this._headerFocusable=this.__getFocusable(r,n):t===this.$.items?(this._itemsFocusable=this.__getFocusable(r,n),this._focusedItemIndex=r.index):t===this.$.footer&&(this._footerFocusable=this.__getFocusable(r,n)),n){const o=this.getEventContext(e);this.__pendingBodyCellFocus=this.loading&&o.section==="body",!this.__pendingBodyCellFocus&&n!==this.$.emptystatecell&&n.dispatchEvent(new CustomEvent("cell-focus",{bubbles:!0,composed:!0,detail:{context:o}})),this._focusedCell=n._focusButton||n,Q()&&e.target===n&&this._showTooltip(e)}else this._focusedCell=null}__dispatchPendingBodyCellFocus(){this.__pendingBodyCellFocus&&this.shadowRoot.activeElement===this._itemsFocusable&&this._itemsFocusable.dispatchEvent(new Event("focusin",{bubbles:!0,composed:!0}))}__getFocusable(e,t){return this.__rowFocusMode?e:t._focusButton||t}_detectInteracting(e){const t=e.composedPath().some(n=>n.localName==="slot"&&this.shadowRoot.contains(n));this._setInteracting(t),this.__updateHorizontalScrollPosition()}_updateGridSectionFocusTarget(e){if(!e)return;const t=this._getGridSectionFromFocusTarget(e),n=this.interacting&&t===this._activeRowGroup;e.tabIndex=n?-1:0}_preventScrollerRotatingCellFocus(){this._activeRowGroup===this.$.items&&(this.__preventScrollerRotatingCellFocusDebouncer=D.debounce(this.__preventScrollerRotatingCellFocusDebouncer,ue,()=>{const e=this._activeRowGroup===this.$.items;this._getRenderedRows().some(n=>n.index===this._focusedItemIndex)?(this.__updateItemsFocusable(),e&&!this.__rowFocusMode&&(this._focusedCell=this._itemsFocusable),this._navigatingIsHidden&&(this.toggleAttribute("navigating",!0),this._navigatingIsHidden=!1)):e&&(this._focusedCell=null,this.hasAttribute("navigating")&&(this._navigatingIsHidden=!0,this.toggleAttribute("navigating",!1)))}))}_getColumns(e,t){let n=this._columnTree.length-1;return e===this.$.header?n=t:e===this.$.footer&&(n=this._columnTree.length-1-t),this._columnTree[n]}__isValidFocusable(e){return this.$.table.contains(e)&&e.offsetHeight}_resetKeyboardNavigation(){if(!this.$&&this.performUpdate&&this.performUpdate(),["header","footer"].forEach(e=>{if(!this.__isValidFocusable(this[`_${e}Focusable`])){const t=[...this.$[e].children].find(r=>r.offsetHeight),n=t?[...t.children].find(r=>!r.hidden):null;t&&n&&(this[`_${e}Focusable`]=this.__getFocusable(t,n))}}),!this.__isValidFocusable(this._itemsFocusable)&&this.$.items.firstElementChild){const e=this.__getFirstVisibleItem(),t=e?[...e.children].find(n=>!n.hidden):null;t&&e&&(this._focusedColumnOrder=void 0,this._itemsFocusable=this.__getFocusable(e,t))}else this.__updateItemsFocusable()}_scrollHorizontallyToCell(e){if(e.hasAttribute("frozen")||e.hasAttribute("frozen-to-end")||Oe(e))return;const t=e.getBoundingClientRect(),n=e.parentNode,r=Array.from(n.children).indexOf(e),o=this.$.table.getBoundingClientRect(),a=this.$.table.clientWidth-this.$.table.offsetWidth;let l=o.left-(this.__isRTL?a:0),d=o.right+(this.__isRTL?0:a);for(let h=r-1;h>=0;h--){const c=n.children[h];if(!(c.hasAttribute("hidden")||Oe(c))&&(c.hasAttribute("frozen")||c.hasAttribute("frozen-to-end"))){l=c.getBoundingClientRect().right;break}}for(let h=r+1;h<n.children.length;h++){const c=n.children[h];if(!(c.hasAttribute("hidden")||Oe(c))&&(c.hasAttribute("frozen")||c.hasAttribute("frozen-to-end"))){d=c.getBoundingClientRect().left;break}}t.left<l&&(this.$.table.scrollLeft+=t.left-l),t.right>d&&(this.$.table.scrollLeft+=t.right-d)}_getGridEventLocation(e){const t=e.__composedPath||e.composedPath(),n=t.indexOf(this.$.table),r=n>=1?t[n-1]:null,o=n>=2?t[n-2]:null,a=n>=3?t[n-3]:null;return{section:r,row:o,cell:a}}_getGridSectionFromFocusTarget(e){return e===this._headerFocusable?this.$.header:e===this._itemsFocusable?this.$.items:e===this._footerFocusable?this.$.footer:null}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const u_=s=>class extends s{static get properties(){return{__hostVisible:{type:Boolean,value:!1},__tableRect:Object,__headerRect:Object,__itemsRect:Object,__footerRect:Object}}ready(){super.ready();const i=new ResizeObserver(e=>{e.findLast(({target:l})=>l===this)&&(this.__hostVisible=this.checkVisibility());const n=e.findLast(({target:l})=>l===this.$.table);n&&(this.__tableRect=n.contentRect);const r=e.findLast(({target:l})=>l===this.$.header);r&&(this.__headerRect=r.contentRect);const o=e.findLast(({target:l})=>l===this.$.items);o&&(this.__itemsRect=o.contentRect);const a=e.findLast(({target:l})=>l===this.$.footer);a&&(this.__footerRect=a.contentRect)});i.observe(this),i.observe(this.$.table),i.observe(this.$.header),i.observe(this.$.items),i.observe(this.$.footer)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const __=s=>class extends s{static get properties(){return{detailsOpenedItems:{type:Array,value:()=>[],sync:!0},rowDetailsRenderer:{type:Function,sync:!0},_detailsCells:{type:Array}}}static get observers(){return["_detailsOpenedItemsChanged(detailsOpenedItems, rowDetailsRenderer)","_rowDetailsRendererChanged(rowDetailsRenderer)"]}ready(){super.ready(),this._detailsCellResizeObserver=new ResizeObserver(e=>{e.forEach(({target:t})=>{this._updateDetailsCellHeight(t.parentElement)})})}_rowDetailsRendererChanged(e){e&&this._columnTree&&Z(this.$.items,t=>{t.querySelector("[part~=details-cell]")||(this.__initRow(t,this._columnTree[this._columnTree.length-1]),this.__updateRow(t))})}_detailsOpenedItemsChanged(e,t){Z(this.$.items,n=>{if(n.hasAttribute("details-opened")){this.__updateRow(n);return}t&&this._isDetailsOpened(n._item)&&this.__updateRow(n)})}_configureDetailsCell(e){$(e,"cell",!0),$(e,"details-cell",!0),e.toggleAttribute("frozen",!0),this._detailsCellResizeObserver.observe(e)}_toggleDetailsCell(e,t){const n=e.querySelector('[part~="details-cell"]');n&&(n.hidden=!t,!n.hidden&&this.rowDetailsRenderer&&(n._renderer=this.rowDetailsRenderer))}_updateDetailsCellHeight(e){const t=e.querySelector('[part~="details-cell"]');t&&(this.__updateDetailsRowPadding(e,t),requestAnimationFrame(()=>this.__updateDetailsRowPadding(e,t)))}__updateDetailsRowPadding(e,t){t.hidden?e.style.removeProperty("padding-bottom"):e.style.setProperty("padding-bottom",`${t.offsetHeight}px`)}_updateDetailsCellHeights(){Z(this.$.items,e=>{this._updateDetailsCellHeight(e)})}_isDetailsOpened(e){return this.detailsOpenedItems&&this._getItemIndexInArray(e,this.detailsOpenedItems)!==-1}openItemDetails(e){this._isDetailsOpened(e)||(this.detailsOpenedItems=[...this.detailsOpenedItems,e])}closeItemDetails(e){this._isDetailsOpened(e)&&(this.detailsOpenedItems=this.detailsOpenedItems.filter(t=>!this._itemsEqual(t,e)))}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Xs={SCROLLING:500,UPDATE_CONTENT_VISIBILITY:100},p_=s=>class extends s{static get properties(){return{columnRendering:{type:String,value:"eager",sync:!0},_frozenCells:{type:Array,value:()=>[]},_frozenToEndCells:{type:Array,value:()=>[]}}}static get observers(){return["__columnRenderingChanged(_columnTree, columnRendering)"]}get _scrollLeft(){return this.$.table.scrollLeft}get _scrollTop(){return this.$.table.scrollTop}set _scrollTop(e){this.$.table.scrollTop=e}get _lazyColumns(){return this.columnRendering==="lazy"}ready(){super.ready(),this.scrollTarget=this.$.table,this.$.items.addEventListener("focusin",e=>{const t=e.composedPath(),n=t[t.indexOf(this.$.items)-1];if(n){if(!this._isMousedown){const r=this.$.table.clientHeight,o=this.$.header.clientHeight,a=this.$.footer.clientHeight,l=r-o-a,h=n.clientHeight>l?e.target:n;this.__scrollIntoViewport(h)}this.$.table.contains(e.relatedTarget)||this.$.table.dispatchEvent(new CustomEvent("virtualizer-element-focused",{detail:{element:n}}))}}),this.$.table.addEventListener("scroll",()=>this._afterScroll()),this.__overflowController=new cs(this,this.$.table),this.addController(this.__overflowController)}_scrollToFlatIndex(e){e=Math.min(this._flatSize-1,Math.max(0,e)),this.__virtualizer.scrollToIndex(e);const t=[...this.$.items.children].find(n=>n.index===e);this.__scrollIntoViewport(t)}__scrollIntoViewport(e){if(!e)return;const t=e.getBoundingClientRect(),n=getComputedStyle(e),r=t.top+parseInt(n.scrollMarginTop||0),o=t.bottom+parseInt(n.scrollMarginBottom||0),a=this.$.footer.getBoundingClientRect().top,l=this.$.header.getBoundingClientRect().bottom;o>a?this.$.table.scrollTop+=o-a:r<l&&(this.$.table.scrollTop-=l-r)}_scheduleScrolling(){this._scrollingFrame||(this._scrollingFrame=requestAnimationFrame(()=>this.$.scroller.toggleAttribute("scrolling",!0))),this._debounceScrolling=D.debounce(this._debounceScrolling,K.after(Xs.SCROLLING),()=>{cancelAnimationFrame(this._scrollingFrame),delete this._scrollingFrame,this.$.scroller.toggleAttribute("scrolling",!1)})}_afterScroll(){this.__updateHorizontalScrollPosition(),this.hasAttribute("reordering")||this._scheduleScrolling(),this.hasAttribute("navigating")||this._hideTooltip(!0),this._debounceColumnContentVisibility=D.debounce(this._debounceColumnContentVisibility,K.after(Xs.UPDATE_CONTENT_VISIBILITY),()=>{this._lazyColumns&&this.__cachedScrollLeft!==this._scrollLeft&&(this.__cachedScrollLeft=this._scrollLeft,this.__updateColumnsBodyContentHidden())})}__updateColumnsBodyContentHidden(){if(!this._columnTree||!this._areSizerCellsAssigned())return;const e=this._getColumnsInOrder();let t=!1;if(e.forEach(n=>{const r=this._lazyColumns&&!this.__isColumnInViewport(n);n._bodyContentHidden!==r&&(t=!0,n._cells.forEach(o=>{if(o!==n._sizerCell){if(r)o.remove();else if(o.__parentRow){const a=[...o.__parentRow.children].find(l=>e.indexOf(l._column)>e.indexOf(n));o.__parentRow.insertBefore(o,a)}}})),n._bodyContentHidden=r}),t&&this._frozenCellsChanged(),this._lazyColumns){const n=[...e].reverse().find(a=>a.frozen),r=this.__getColumnEnd(n),o=e.find(a=>!a.frozen&&!a._bodyContentHidden);this.__lazyColumnsStart=this.__getColumnStart(o)-r,this.$.items.style.setProperty("--_grid-lazy-columns-start",`${this.__lazyColumnsStart}px`),this._resetKeyboardNavigation()}}__getColumnEnd(e){return e?e._sizerCell.offsetLeft+(this.__isRTL?0:e._sizerCell.offsetWidth):this.__isRTL?this.$.table.clientWidth:0}__getColumnStart(e){return e?e._sizerCell.offsetLeft+(this.__isRTL?e._sizerCell.offsetWidth:0):this.__isRTL?this.$.table.clientWidth:0}__isColumnInViewport(e){return e.frozen||e.frozenToEnd?!0:this.__isHorizontallyInViewport(e._sizerCell)}__isHorizontallyInViewport(e){return e.offsetLeft+e.offsetWidth>=this._scrollLeft&&e.offsetLeft<=this._scrollLeft+this.clientWidth}__columnRenderingChanged(e,t){t==="eager"?this.$.scroller.removeAttribute("column-rendering"):this.$.scroller.setAttribute("column-rendering",t),this.__updateColumnsBodyContentHidden()}_frozenCellsChanged(){this._debouncerCacheElements=D.debounce(this._debouncerCacheElements,te,()=>{Array.from(this.shadowRoot.querySelectorAll('[part~="cell"]')).forEach(e=>{e.style.transform=""}),this._frozenCells=Array.prototype.slice.call(this.$.table.querySelectorAll("[frozen]")),this._frozenToEndCells=Array.prototype.slice.call(this.$.table.querySelectorAll("[frozen-to-end]")),this.__updateHorizontalScrollPosition()}),this._debounceUpdateFrozenColumn()}_debounceUpdateFrozenColumn(){this.__debounceUpdateFrozenColumn=D.debounce(this.__debounceUpdateFrozenColumn,te,()=>this._updateFrozenColumn())}_updateFrozenColumn(){if(!this._columnTree)return;const e=this._columnTree[this._columnTree.length-1].slice(0);e.sort((r,o)=>r._order-o._order);let t,n;for(let r=0;r<e.length;r++){const o=e[r];o._lastFrozen=!1,o._firstFrozenToEnd=!1,n===void 0&&o.frozenToEnd&&!o.hidden&&(n=r),o.frozen&&!o.hidden&&(t=r)}t!==void 0&&(e[t]._lastFrozen=!0),n!==void 0&&(e[n]._firstFrozenToEnd=!0),this.__updateColumnsBodyContentHidden()}__updateHorizontalScrollPosition(){if(!this._columnTree)return;const e=this.$.table.scrollWidth,t=this.$.table.clientWidth,n=Math.max(0,this.$.table.scrollLeft),r=ds(this.$.table,this.getAttribute("dir")),o=`translate(${-n}px, 0)`;this.$.header.style.transform=o,this.$.footer.style.transform=o,this.$.items.style.transform=o;const a=this.__isRTL?r+t-e:n;this.__horizontalScrollPosition=a;const l=`translate(${a}px, 0)`;this._frozenCells.forEach(x=>{x.style.transform=l});const d=this.__isRTL?r:n+t-e,h=`translate(${d}px, 0)`;let c=h;if(this._lazyColumns&&this._areSizerCellsAssigned()){const x=this._getColumnsInOrder(),b=[...x].reverse().find(g=>!g.frozenToEnd&&!g._bodyContentHidden),k=this.__getColumnEnd(b),u=x.find(g=>g.frozenToEnd),_=this.__getColumnStart(u);c=`translate(${d+(_-k)+this.__lazyColumnsStart}px, 0)`}this._frozenToEndCells.forEach(x=>{this.$.items.contains(x)?x.style.transform=c:x.style.transform=h});const f=this.shadowRoot.querySelector("[part~='row']:focus");f&&this.__updateRowScrollPositionProperty(f);const m=this.$.header.querySelector("[part~='last-header-row']");m&&this.__updateRowScrollPositionProperty(m);const v=this.$.footer.querySelector("[part~='first-footer-row']");v&&this.__updateRowScrollPositionProperty(v)}__updateRowScrollPositionProperty(e){if(!(e instanceof HTMLTableRowElement))return;const t=`${this.__horizontalScrollPosition}px`;e.style.getPropertyValue("--_grid-horizontal-scroll-position")!==t&&e.style.setProperty("--_grid-horizontal-scroll-position",t)}_areSizerCellsAssigned(){return this._getColumnsInOrder().every(e=>e._sizerCell)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const f_=s=>class extends s{static get properties(){return{selectedItems:{type:Object,notify:!0,value:()=>[],sync:!0},isItemSelectable:{type:Function,notify:!0},__selectedKeys:{type:Object,computed:"__computeSelectedKeys(itemIdPath, selectedItems)"}}}static get observers(){return["__selectedItemsChanged(itemIdPath, selectedItems, isItemSelectable)"]}_isSelected(e){return this.__selectedKeys.has(this.getItemId(e))}__isItemSelectable(e){return!this.isItemSelectable||!e?!0:this.isItemSelectable(e)}selectItem(e){this._isSelected(e)||(this.selectedItems=[...this.selectedItems,e])}deselectItem(e){this._isSelected(e)&&(this.selectedItems=this.selectedItems.filter(t=>!this._itemsEqual(t,e)))}__selectedItemsChanged(){this.requestContentUpdate()}__computeSelectedKeys(e,t){const n=t||[],r=new Set;return n.forEach(o=>{r.add(this.getItemId(o))}),r}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */let Qs="prepend";const m_=s=>class extends s{static get properties(){return{multiSort:{type:Boolean,value:!1},multiSortPriority:{type:String,value:()=>Qs},multiSortOnShiftClick:{type:Boolean,value:!1},_sorters:{type:Array,value:()=>[]},_previousSorters:{type:Array,value:()=>[]}}}static setDefaultMultiSortPriority(e){Qs=["append","prepend"].includes(e)?e:"prepend"}ready(){super.ready(),this.addEventListener("sorter-changed",this._onSorterChanged)}_onSorterChanged(e){const t=e.target;e.stopPropagation(),t._grid=this,this.__updateSorter(t,e.detail.shiftClick,e.detail.fromSorterClick),this.__applySorters()}__removeSorters(e){e.length!==0&&(this._sorters=this._sorters.filter(t=>!e.includes(t)),this.__applySorters())}__updateSortOrders(){this._sorters.forEach(t=>{t._order=null});const e=this._getActiveSorters();e.length>1&&e.forEach((t,n)=>{t._order=n})}__updateSorter(e,t,n){if(!e.direction&&!this._sorters.includes(e))return;e._order=null;const r=this._sorters.filter(o=>o!==e);this.multiSort&&(!this.multiSortOnShiftClick||!n)||this.multiSortOnShiftClick&&t?this.multiSortPriority==="append"?this._sorters=[...r,e]:this._sorters=[e,...r]:(e.direction||this.multiSortOnShiftClick)&&(this._sorters=e.direction?[e]:[],r.forEach(o=>{o._order=null,o.direction=null}))}__applySorters(){this.__updateSortOrders(),this.dataProvider&&this.isAttached&&JSON.stringify(this._previousSorters)!==JSON.stringify(this._mapSorters())&&this.__debounceClearCache(),this.__a11yUpdateSorters(),this._previousSorters=this._mapSorters()}_getActiveSorters(){return this._sorters.filter(e=>e.direction&&e.isConnected)}_mapSorters(){return this._getActiveSorters().map(e=>({path:e.path,direction:e.direction}))}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const g_=s=>class extends s{static get properties(){return{cellPartNameGenerator:{type:Function,sync:!0}}}static get observers(){return["__cellPartNameGeneratorChanged(cellPartNameGenerator)"]}__cellPartNameGeneratorChanged(){this.generateCellPartNames()}generateCellPartNames(){Z(this.$.items,e=>{e.hidden||this._generateCellPartNames(e,this.__getRowModel(e))})}_generateCellPartNames(e,t){ft(e,n=>{if(n.__generatedParts&&n.__generatedParts.forEach(r=>{$(n,r,null)}),this.cellPartNameGenerator&&!e.hasAttribute("loading")){const r=this.cellPartNameGenerator(n._column,t);n.__generatedParts=r&&r.split(" ").filter(o=>o.length>0),n.__generatedParts&&n.__generatedParts.forEach(o=>{$(n,o,!0)})}})}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const v_=s=>class extends s_(i_(o_(l_(Zu(p_(f_(m_(__(c_(Qu(h_(n_(r_(d_(a_(g_(Wi(u_(s))))))))))))))))))){static get observers(){return["_columnTreeChanged(_columnTree)","_flatSizeChanged(_flatSize, __virtualizer, _hasData, _columnTree)"]}static get properties(){return{_safari:{type:Boolean,value:Ni},_ios:{type:Boolean,value:ze},_firefox:{type:Boolean,value:un},_android:{type:Boolean,value:Si},_touchDevice:{type:Boolean,value:Ne},allRowsVisible:{type:Boolean,value:!1,reflectToAttribute:!0},isAttached:{value:!1},__gridElement:{type:Boolean,value:!0},__hasEmptyStateContent:{type:Boolean,value:!1},__emptyState:{type:Boolean,computed:"__computeEmptyState(_flatSize, __hasEmptyStateContent)"}}}get _firstVisibleIndex(){const i=this.__getFirstVisibleItem();return i?i.index:void 0}get _lastVisibleIndex(){const i=this.__getLastVisibleItem();return i?i.index:void 0}connectedCallback(){super.connectedCallback(),this.isAttached=!0,this.__virtualizer.hostConnected()}disconnectedCallback(){super.disconnectedCallback(),this.isAttached=!1,this._hideTooltip(!0)}__getFirstVisibleItem(){return this._getRenderedRows().find(i=>this._isInViewport(i))}__getLastVisibleItem(){return this._getRenderedRows().reverse().find(i=>this._isInViewport(i))}_isInViewport(i){const e=this.$.table.getBoundingClientRect(),t=i.getBoundingClientRect(),n=this.$.header.getBoundingClientRect().height,r=this.$.footer.getBoundingClientRect().height;return t.bottom>e.top+n&&t.top<e.bottom-r}_getRenderedRows(){return Array.from(this.$.items.children).filter(i=>!i.hidden).sort((i,e)=>i.index-e.index)}_getRowContainingNode(i){const e=Cn("vaadin-grid-cell-content",i);return e?e.assignedSlot.parentElement.parentElement:void 0}_isItemAssignedToRow(i,e){const t=this.__getRowModel(e);return this.getItemId(i)===this.getItemId(t.item)}ready(){super.ready(),this.__virtualizer=new dr({createElements:this._createScrollerRows.bind(this),updateElement:this._updateScrollerItem.bind(this),scrollContainer:this.$.items,scrollTarget:this.$.table,reorderElements:!0,__disableHeightPlaceholder:!0}),this._tooltipController=new X(this),this.addController(this._tooltipController),this._tooltipController.setManual(!0),this.__emptyStateContentObserver=new ce(this.$.emptystateslot,({currentNodes:i})=>{this.$.emptystatecell._content=i[0],this.__hasEmptyStateContent=!!this.$.emptystatecell._content})}updated(i){super.updated(i),i.has("__hostVisible")&&!i.get("__hostVisible")&&(this._resetKeyboardNavigation(),requestAnimationFrame(()=>this.__scrollToPendingIndexes())),(i.has("__headerRect")||i.has("__footerRect")||i.has("__itemsRect"))&&setTimeout(()=>this.__updateMinHeight()),i.has("__tableRect")&&(setTimeout(()=>this.__updateColumnsBodyContentHidden()),this.__updateHorizontalScrollPosition())}__getBodyCellCoordinates(i){if(this.$.items.contains(i)&&i.localName==="td")return{item:i.parentElement._item,column:i._column}}__focusBodyCell({item:i,column:e}){const t=this._getRenderedRows().find(r=>r._item===i),n=t&&[...t.children].find(r=>r._column===e);n&&n.focus()}_focusFirstVisibleRow(){const i=this.__getFirstVisibleItem();this.__rowFocusMode=!0,i.focus()}_flatSizeChanged(i,e,t,n){if(e&&t&&n){const r=this.shadowRoot.activeElement,o=this.__getBodyCellCoordinates(r),a=e.size||0;e.size=i,e.update(a-1,a-1),i<a&&e.update(i-1,i-1),o&&r.parentElement.hidden&&this.__focusBodyCell(o),this._resetKeyboardNavigation()}}_createScrollerRows(i){const e=[];for(let t=0;t<i;t++){const n=document.createElement("tr");n.setAttribute("role","row"),n.setAttribute("tabindex","-1"),$(n,"row",!0),$(n,"body-row",!0),this._columnTree&&this.__initRow(n,this._columnTree[this._columnTree.length-1],"body",!1,!0),e.push(n)}return this._columnTree&&this._columnTree[this._columnTree.length-1].forEach(t=>{t.isConnected&&t._cells&&(t._cells=[...t._cells])}),this.__afterCreateScrollerRowsDebouncer=D.debounce(this.__afterCreateScrollerRowsDebouncer,ue,()=>{this._afterScroll()}),e}_createCell(i,e){const n=`vaadin-grid-cell-content-${this._contentIndex=this._contentIndex+1||0}`,r=document.createElement("vaadin-grid-cell-content");r.setAttribute("slot",n);const o=document.createElement(i);o.id=n.replace("-content-","-"),o.setAttribute("role",i==="td"?"gridcell":"columnheader"),!Si&&!ze&&(o.addEventListener("mouseenter",l=>{this.$.scroller.hasAttribute("scrolling")||this._showTooltip(l)}),o.addEventListener("mouseleave",()=>{this._hideTooltip()}),o.addEventListener("mousedown",()=>{this._hideTooltip(!0)}));const a=document.createElement("slot");if(a.setAttribute("name",n),e&&e._focusButtonMode){const l=document.createElement("div");l.setAttribute("role","button"),l.setAttribute("tabindex","-1"),o.appendChild(l),o._focusButton=l,o.focus=function(d){o._focusButton.focus(d)},l.appendChild(a)}else o.setAttribute("tabindex","-1"),o.appendChild(a);return o._content=r,r.addEventListener("mousedown",()=>{if(cn){const l=d=>{const h=r.contains(this.getRootNode().activeElement),c=d.composedPath().includes(r);!h&&c&&o.focus({preventScroll:!0}),document.removeEventListener("mouseup",l,!0)};document.addEventListener("mouseup",l,!0)}else setTimeout(()=>{r.contains(this.getRootNode().activeElement)||o.focus({preventScroll:!0})})}),o}__initRow(i,e,t="body",n=!1,r=!1){const o=document.createDocumentFragment();ft(i,a=>{a._vacant=!0}),i.innerHTML="",t==="body"&&(i.__cells=[],i.__detailsCell=null),e.filter(a=>!a.hidden).forEach((a,l,d)=>{let h;if(t==="body"){a._cells||(a._cells=[]),h=a._cells.find(f=>f._vacant),h||(h=this._createCell("td",a),a._onCellKeyDown&&h.addEventListener("keydown",a._onCellKeyDown.bind(a)),a._cells.push(h)),$(h,"cell",!0),$(h,"body-cell",!0),h.__parentRow=i,i.__cells.push(h);const c=i===this.$.sizer;if((!a._bodyContentHidden||c)&&i.appendChild(h),c&&(a._sizerCell=h),l===d.length-1&&this.rowDetailsRenderer){this._detailsCells||(this._detailsCells=[]);const f=this._detailsCells.find(m=>m._vacant)||this._createCell("td");this._detailsCells.indexOf(f)===-1&&this._detailsCells.push(f),f._content.parentElement||o.appendChild(f._content),this._configureDetailsCell(f),i.appendChild(f),i.__detailsCell=f,this.__a11ySetRowDetailsCell(i,f),f._vacant=!1}r||(a._cells=[...a._cells])}else{const c=t==="header"?"th":"td";n||a.localName==="vaadin-grid-column-group"?(h=a[`_${t}Cell`],h||(h=this._createCell(c),a._onCellKeyDown&&h.addEventListener("keydown",a._onCellKeyDown.bind(a))),h._column=a,i.appendChild(h),a[`_${t}Cell`]=h):(a._emptyCells||(a._emptyCells=[]),h=a._emptyCells.find(f=>f._vacant)||this._createCell(c),h._column=a,i.appendChild(h),a._emptyCells.indexOf(h)===-1&&a._emptyCells.push(h)),$(h,"cell",!0),$(h,`${t}-cell`,!0)}h._content.parentElement||o.appendChild(h._content),h._vacant=!1,h._column=a}),t!=="body"&&this.__debounceUpdateHeaderFooterRowVisibility(i),this.appendChild(o),this._frozenCellsChanged(),this._updateFirstAndLastColumnForRow(i)}__debounceUpdateHeaderFooterRowVisibility(i){i.__debounceUpdateHeaderFooterRowVisibility=D.debounce(i.__debounceUpdateHeaderFooterRowVisibility,te,()=>this.__updateHeaderFooterRowVisibility(i))}__updateHeaderFooterRowVisibility(i){if(!i)return;const e=Array.from(i.children).filter(t=>{const n=t._column;if(n._emptyCells&&n._emptyCells.indexOf(t)>-1)return!1;if(i.parentElement===this.$.header){if(n.headerRenderer)return!0;if(n.header===null)return!1;if(n.path||n.header!==void 0)return!0}else if(n.footerRenderer)return!0;return!1});i.hidden!==!e.length&&(i.hidden=!e.length),i.parentElement===this.$.header&&(this.$.table.toggleAttribute("has-header",this.$.header.querySelector("tr:not([hidden])")),this.__updateHeaderFooterRowParts("header")),i.parentElement===this.$.footer&&(this.$.table.toggleAttribute("has-footer",this.$.footer.querySelector("tr:not([hidden])")),this.__updateHeaderFooterRowParts("footer")),this._resetKeyboardNavigation(),this.__a11yUpdateGridSize(this.size,this._columnTree,this.__emptyState)}_updateScrollerItem(i,e){this._preventScrollerRotatingCellFocus(i,e),this._columnTree&&(i.index=e,this.__ensureRowItem(i),this.__ensureRowHierarchy(i),this.__updateRow(i))}_columnTreeChanged(i){this._renderColumnTree(i),this.__updateColumnsBodyContentHidden()}__updateRowOrderParts(i){je(i,{first:i.index===0,last:i.index===this._flatSize-1,odd:i.index%2!==0,even:i.index%2===0})}__updateRowStateParts(i,{item:e,expanded:t,selected:n,detailsOpened:r}){je(i,{expanded:t,collapsed:this.__isRowExpandable(i),selected:n,nonselectable:this.__isItemSelectable(e)===!1,"details-opened":r})}__computeEmptyState(i,e){return i===0&&e}_renderColumnTree(i){for(Z(this.$.items,e=>{this.__initRow(e,i[i.length-1],"body",!1,!0),this.__updateRow(e)});this.$.header.children.length<i.length;){const e=document.createElement("tr");e.setAttribute("role","row"),e.setAttribute("tabindex","-1"),$(e,"row",!0),$(e,"header-row",!0),this.$.header.appendChild(e);const t=document.createElement("tr");t.setAttribute("role","row"),t.setAttribute("tabindex","-1"),$(t,"row",!0),$(t,"footer-row",!0),this.$.footer.appendChild(t)}for(;this.$.header.children.length>i.length;)this.$.header.removeChild(this.$.header.firstElementChild),this.$.footer.removeChild(this.$.footer.firstElementChild);Z(this.$.header,(e,t)=>{this.__initRow(e,i[t],"header",t===i.length-1)}),Z(this.$.footer,(e,t)=>{this.__initRow(e,i[i.length-1-t],"footer",t===0)}),this.__initRow(this.$.sizer,i[i.length-1]),this.__updateHeaderFooterRowParts("header"),this.__updateHeaderFooterRowParts("footer"),this._resizeHandler(),this._frozenCellsChanged(),this._updateFirstAndLastColumn(),this._resetKeyboardNavigation(),this.__a11yUpdateHeaderRows(),this.__a11yUpdateFooterRows(),this.generateCellPartNames(),this.__updateHeaderAndFooter()}__updateHeaderFooterRowParts(i){const e=[...this.$[i].querySelectorAll("tr:not([hidden])")];[...this.$[i].children].forEach(t=>{$(t,`first-${i}-row`,t===e.at(0)),$(t,`last-${i}-row`,t===e.at(-1)),it(t).forEach(n=>{$(n,`first-${i}-row-cell`,t===e.at(0)),$(n,`last-${i}-row-cell`,t===e.at(-1))})})}__updateRowLoading(i,e){const t=it(i);si(i,"loading",e),Wt(t,"loading-row-cell",e),e&&this._generateCellPartNames(i)}__updateRow(i){this.__a11yUpdateRowRowindex(i),this.__updateRowOrderParts(i);const e=this.__getRowItem(i);if(e)this.__updateRowLoading(i,!1);else{this.__updateRowLoading(i,!0);return}i._item=e;const t=this.__getRowModel(i);this._toggleDetailsCell(i,t.detailsOpened),this.__a11yUpdateRowLevel(i,t.level),this.__a11yUpdateRowSelected(i,t.selected),this.__updateRowStateParts(i,t),this._generateCellPartNames(i,t),this._filterDragAndDrop(i,t),this.__updateDragSourceParts(i,t),Z(i,n=>{if(!(n._column&&!n._column.isConnected)&&n._renderer){const r=n._column||this;n._renderer.call(r,n._content,r,t)}}),this._updateDetailsCellHeight(i),this.__a11yUpdateRowExpanded(i,t.expanded)}_resizeHandler(){this._updateDetailsCellHeights(),this.__updateHorizontalScrollPosition()}__getRowModel(i){return{index:i.index,item:i._item,level:this.__getRowLevel(i),expanded:this._isExpanded(i._item),selected:this._isSelected(i._item),hasChildren:this._hasChildren(i._item),detailsOpened:!!this.rowDetailsRenderer&&this._isDetailsOpened(i._item)}}_showTooltip(i){const e=this._tooltipController.node;if(e&&e.isConnected){const t=i.target;if(!this.__isCellFullyVisible(t))return;this._tooltipController.setTarget(t),this._tooltipController.setContext(this.getEventContext(i)),e._stateController.open({focus:i.type==="focusin",hover:i.type==="mouseenter"})}}__isCellFullyVisible(i){if(i.hasAttribute("frozen")||i.hasAttribute("frozen-to-end"))return!0;let{left:e,right:t}=this.getBoundingClientRect();const n=[...i.parentNode.children].find(a=>a.hasAttribute("last-frozen"));if(n){const a=n.getBoundingClientRect();e=this.__isRTL?e:a.right,t=this.__isRTL?a.left:t}const r=[...i.parentNode.children].find(a=>a.hasAttribute("first-frozen-to-end"));if(r){const a=r.getBoundingClientRect();e=this.__isRTL?a.right:e,t=this.__isRTL?t:a.left}const o=i.getBoundingClientRect();return o.left>=e&&o.right<=t}_hideTooltip(i){const e=this._tooltipController&&this._tooltipController.node;e&&e._stateController.close(i)}requestContentUpdate(){this.__updateHeaderAndFooter(),this.__updateVisibleRows()}__updateHeaderAndFooter(){(this._columnTree||[]).forEach(i=>{i.forEach(e=>{e._renderHeaderAndFooter&&e._renderHeaderAndFooter()})})}__updateVisibleRows(i,e){this.__virtualizer&&this.__virtualizer.update(i,e)}__updateMinHeight(){const e=this.$.header.clientHeight,t=this.$.footer.clientHeight,n=this.$.table.offsetHeight-this.$.table.clientHeight,r=e+36+t+n;this.__minHeightStyleSheet||(this.__minHeightStyleSheet=new CSSStyleSheet,this.shadowRoot.adoptedStyleSheets.push(this.__minHeightStyleSheet)),this.__minHeightStyleSheet.replaceSync(`:host { --_grid-min-height: ${r}px; }`)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class b_ extends v_(L(T(I(A(E))))){static get is(){return"vaadin-grid"}static get styles(){return Xu}render(){return y`
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
          aria-label="${B(this.accessibleName)}"
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
    `}}w(b_);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const y_=C`
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
 */const w_=s=>class extends s{static get properties(){return{path:String,direction:{type:String,reflectToAttribute:!0,notify:!0,value:null,sync:!0},_order:{type:Number,value:null,sync:!0}}}static get observers(){return["_pathOrDirectionChanged(path, direction)"]}ready(){super.ready(),this.addEventListener("click",this._onClick.bind(this))}connectedCallback(){super.connectedCallback(),this._grid?this._grid.__applySorters():this.__dispatchSorterChangedEvenIfPossible()}disconnectedCallback(){super.disconnectedCallback(),!this.parentNode&&this._grid?this._grid.__removeSorters([this]):this._grid&&this._grid.__applySorters()}_pathOrDirectionChanged(){this.__dispatchSorterChangedEvenIfPossible()}__dispatchSorterChangedEvenIfPossible(){this.path===void 0||this.direction===void 0||!this.isConnected||(this.dispatchEvent(new CustomEvent("sorter-changed",{detail:{shiftClick:!!this._shiftClick,fromSorterClick:!!this._fromSorterClick},bubbles:!0,composed:!0})),this._fromSorterClick=!1,this._shiftClick=!1)}_getDisplayOrder(e){return e===null?"":e+1}_onClick(e){if(e.defaultPrevented)return;const t=this.getRootNode().activeElement;this!==t&&this.contains(t)||(e.preventDefault(),this._shiftClick=e.shiftKey,this._fromSorterClick=!0,this.direction==="asc"?this.direction="desc":this.direction==="desc"?this.direction=null:this.direction="asc")}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class C_ extends w_(T(z(I(A(E))))){static get is(){return"vaadin-grid-sorter"}static get styles(){return y_}render(){return y`
      <div part="content">
        <slot></slot>
      </div>
      <div part="indicators">
        <span part="order">${this._getDisplayOrder(this._order)}</span>
      </div>
    `}}w(C_);/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const x_=s=>class extends s{static get properties(){return{width:{type:String,value:"58px",sync:!0},autoWidth:{type:Boolean,value:!0},flexGrow:{type:Number,value:0,sync:!0},selectAll:{type:Boolean,value:!1,notify:!0,sync:!0},autoSelect:{type:Boolean,value:!1,sync:!0},dragSelect:{type:Boolean,value:!1,sync:!0},_indeterminate:{type:Boolean,sync:!0},_selectAllHidden:Boolean,_shiftKeyDown:{type:Boolean,value:!1}}}static get observers(){return["_onHeaderRendererOrBindingChanged(_headerRenderer, _headerCell, path, header, selectAll, _indeterminate, _selectAllHidden)"]}constructor(){super(),this.__onCellTrack=this.__onCellTrack.bind(this),this.__onCellClick=this.__onCellClick.bind(this),this.__onCellMouseDown=this.__onCellMouseDown.bind(this),this.__onGridInteraction=this.__onGridInteraction.bind(this),this.__onActiveItemChanged=this.__onActiveItemChanged.bind(this),this.__onSelectRowCheckboxChange=this.__onSelectRowCheckboxChange.bind(this),this.__onSelectAllCheckboxChange=this.__onSelectAllCheckboxChange.bind(this)}connectedCallback(){super.connectedCallback(),this._grid&&(this._grid.addEventListener("keyup",this.__onGridInteraction),this._grid.addEventListener("keydown",this.__onGridInteraction,{capture:!0}),this._grid.addEventListener("mousedown",this.__onGridInteraction),this._grid.addEventListener("active-item-changed",this.__onActiveItemChanged))}disconnectedCallback(){super.disconnectedCallback(),this._grid&&(this._grid.removeEventListener("keyup",this.__onGridInteraction),this._grid.removeEventListener("keydown",this.__onGridInteraction,{capture:!0}),this._grid.removeEventListener("mousedown",this.__onGridInteraction),this._grid.removeEventListener("active-item-changed",this.__onActiveItemChanged))}_defaultHeaderRenderer(e,t){let n=e.firstElementChild;n||(n=document.createElement("vaadin-checkbox"),n.accessibleName="Select All",n.classList.add("vaadin-grid-select-all-checkbox"),n.addEventListener("change",this.__onSelectAllCheckboxChange),e.appendChild(n));const r=this.__isChecked(this.selectAll,this._indeterminate);n.checked=r,n.indeterminate=this._indeterminate,n.style.visibility=this._selectAllHidden?"hidden":""}_defaultRenderer(e,t,{item:n,selected:r}){let o=e.firstElementChild;o||(o=document.createElement("vaadin-checkbox"),o.accessibleName="Select Row",o.addEventListener("change",this.__onSelectRowCheckboxChange),e.appendChild(o),pe(e,"track",this.__onCellTrack),e.addEventListener("mousedown",this.__onCellMouseDown),e.addEventListener("click",this.__onCellClick)),o.__item=n,o.checked=r;const a=this._grid.__isItemSelectable(n);o.readonly=!a;const l=!a&&!r;o.style.visibility=l?"hidden":""}__onSelectAllCheckboxChange(e){this._indeterminate||e.currentTarget.checked?this._selectAll():this._deselectAll()}__onGridInteraction(e){this._shiftKeyDown=e.shiftKey,this.autoSelect&&this._grid.$.scroller.toggleAttribute("range-selecting",this._shiftKeyDown)}__onSelectRowCheckboxChange(e){this.__toggleItem(e.currentTarget.__item,e.currentTarget.checked)}__onCellTrack(e){if(this.dragSelect)if(this.__dragCurrentY=e.detail.y,this.__dragDy=e.detail.dy,e.detail.state==="start"){const n=this._grid._getRenderedRows().find(r=>r.contains(e.currentTarget.assignedSlot));this.__selectOnDrag=!this._grid._isSelected(n._item),this.__dragStartIndex=n.index,this.__dragStartItem=n._item,this.__dragAutoScroller()}else e.detail.state==="end"&&(this.__dragStartItem&&this.__toggleItem(this.__dragStartItem,this.__selectOnDrag),setTimeout(()=>{this.__dragStartIndex=void 0}))}__onCellMouseDown(e){this.dragSelect&&e.preventDefault()}__onCellClick(e){this.__dragStartIndex!==void 0&&e.preventDefault()}_onCellKeyDown(e){const t=e.composedPath()[0];if(e.keyCode===32){if(t===this._headerCell)this.selectAll?this._deselectAll():this._selectAll();else if(this._cells.includes(t)&&!this.autoSelect){const n=t._content.firstElementChild;this.__toggleItem(n.__item)}}}__onActiveItemChanged(e){const t=e.detail.value;if(this.autoSelect){const n=t||this.__previousActiveItem;n&&this.__toggleItem(n)}this.__previousActiveItem=t}__dragAutoScroller(){if(this.__dragStartIndex===void 0)return;const e=this._grid._getRenderedRows(),t=e.find(l=>{const d=l.getBoundingClientRect();return this.__dragCurrentY>=d.top&&this.__dragCurrentY<=d.bottom});let n=t?t.index:void 0;const r=this.__getScrollableArea();this.__dragCurrentY<r.top?n=this._grid._firstVisibleIndex:this.__dragCurrentY>r.bottom&&(n=this._grid._lastVisibleIndex),n!==void 0&&e.forEach(l=>{(n>this.__dragStartIndex&&l.index>=this.__dragStartIndex&&l.index<=n||n<this.__dragStartIndex&&l.index<=this.__dragStartIndex&&l.index>=n)&&(this.__toggleItem(l._item,this.__selectOnDrag),this.__dragStartItem=void 0)});const o=r.height*.15,a=10;if(this.__dragDy<0&&this.__dragCurrentY<r.top+o){const l=r.top+o-this.__dragCurrentY,d=Math.min(1,l/o);this._grid.$.table.scrollTop-=d*a}if(this.__dragDy>0&&this.__dragCurrentY>r.bottom-o){const l=this.__dragCurrentY-(r.bottom-o),d=Math.min(1,l/o);this._grid.$.table.scrollTop+=d*a}setTimeout(()=>this.__dragAutoScroller(),10)}__getScrollableArea(){const e=this._grid.$.table.getBoundingClientRect(),t=this._grid.$.header.getBoundingClientRect(),n=this._grid.$.footer.getBoundingClientRect();return{top:e.top+t.height,bottom:e.bottom-n.height,left:e.left,right:e.right,height:e.height-t.height-n.height,width:e.width}}_selectAll(){}_deselectAll(){}_selectItem(e){}_deselectItem(e){}__toggleItem(e,t=!this._grid._isSelected(e)){t!==this._grid._isSelected(e)&&(t?this._selectItem(e):this._deselectItem(e))}__isChecked(e,t){return t||e}};class Ri extends x_($r){static get is(){return"vaadin-grid-flow-selection-column"}static get properties(){return{autoWidth:{type:Boolean,value:!0},width:{type:String,value:"56px"}}}_defaultHeaderRenderer(i,e){super._defaultHeaderRenderer(i,e);const t=i.firstElementChild;t&&(t.id="selectAllCheckbox")}_selectAll(){this.selectAll=!0,this.$server.selectAll()}_deselectAll(){this.selectAll=!1,this.$server.deselectAll()}_selectItem(i){this.$server.setShiftKeyDown(this._shiftKeyDown),this._grid.$connector.doSelection([i],!0)}_deselectItem(i){this.$server.setShiftKeyDown(this._shiftKeyDown),this._grid.$connector.doDeselection([i],!0),this.selectAll=!1}}customElements.define(Ri.is,Ri);window.Vaadin.Flow.gridConnector={};window.Vaadin.Flow.gridConnector.initLazy=s=>{if(s.$connector)return;const i=s._dataProviderController;let e={};const t=150;let n,r=[0,0];const o=["SINGLE","NONE","MULTI"];let a={},l="SINGLE",d=!1;s.size=0,s.itemIdPath="key",s.$connector={},s.$connector.hasRootRequestQueue=()=>{const{pendingRequests:u}=i.rootCache;return Object.keys(u).length>0||!!n?.isActive()},s.$connector.doSelection=function(u,_){if(l==="NONE"||!u.length||_&&s.hasAttribute("disabled"))return;l==="SINGLE"&&(a={});let p=!1;u.forEach(g=>{const S=!_||s.isItemSelectable(g);p=p||S,g&&S&&(a[g.key]=g,g.selected=!0,_&&s.$server.select(g.key));const F=!s.activeItem||!g||g.key!=s.activeItem.key;!_&&l==="SINGLE"&&F&&(s.activeItem=g)}),p&&(s.selectedItems=Object.values(a))},s.$connector.doDeselection=function(u,_){if(l==="NONE"||!u.length||_&&s.hasAttribute("disabled"))return;const p=s.selectedItems.slice();for(;u.length;){const g=u.shift();if(!_||s.isItemSelectable(g)){for(let F=0;F<p.length;F++){const R=p[F];if(g?.key===R.key){p.splice(F,1);break}}g&&(delete a[g.key],delete g.selected,_&&s.$server.deselect(g.key))}}s.selectedItems=p},s.__activeItemChanged=function(u,_){l=="SINGLE"&&(u?a[u.key]||s.$connector.doSelection([u],!0):_&&a[_.key]&&(s.__deselectDisallowed?s.activeItem=_:(_=i.getItemContext(_).item,s.$connector.doDeselection([_],!0))))},s._createPropertyObserver("activeItem","__activeItemChanged",!0),s.__activeItemChangedDetails=function(u,_){s.__disallowDetailsOnClick||u==null&&_===void 0||(u&&!u.detailsOpened?s.$server.setDetailsVisible(u.key):s.$server.setDetailsVisible(null))},s._createPropertyObserver("activeItem","__activeItemChangedDetails",!0),s.$connector.debounceRootRequest=function(u){const _=s._hasData?t:0;n=D.debounce(n,K.after(_),()=>{s.$connector.fetchPage((p,g)=>s.$server.setViewportRange(p,g),u)})},s.$connector.fetchPage=function(u,_){_=Math.min(_,Math.floor((s.size-1)/s.pageSize));const p=s._getRenderedRows();let g=p.length>0?p[0].index:0,S=p.length>0?p[p.length-1].index:0,F=S-g;g=Math.max(0,g-F),S=Math.min(S+F,s.size);let R=[Math.floor(g/s.pageSize),Math.floor(S/s.pageSize)];if((_<R[0]||_>R[1])&&(R=[_,_]),r[0]!=R[0]||r[1]!=R[1]){r=R;let j=R[1]-R[0]+1;u(R[0]*s.pageSize,j*s.pageSize)}},s.dataProvider=function(u,_){if(u.pageSize!=s.pageSize)throw"Invalid pageSize";let p=u.page;if(s.size===0){_([],0);return}e[p]?_(e[p]):s.$connector.debounceRootRequest(p)},s.$connector.setSorterDirections=function(u){d=!0,setTimeout(()=>{try{const _=Array.from(s.querySelectorAll("vaadin-grid-sorter"));s._sorters.forEach(p=>{_.includes(p)||_.push(p)}),_.forEach(p=>{p.direction=null}),s.multiSortPriority!=="append"&&(u=u.reverse()),u.forEach(({column:p,direction:g})=>{_.forEach(S=>{S.getAttribute("path")===p&&(S.direction=g)})}),s.__applySorters()}finally{d=!1}})};let h=0;function c(u){try{h++,u()}finally{h--}}s.__updateVisibleRows=function(...u){h===0&&Object.getPrototypeOf(this).__updateVisibleRows.call(this,...u)},s.__updateRow=function(u,..._){Object.getPrototypeOf(this).__updateRow.call(this,u,..._),l===o[1]&&(u.removeAttribute("aria-selected"),Array.from(u.children).forEach(p=>p.removeAttribute("aria-selected")))};const f=function(u){if(!u||!Array.isArray(u))throw"Attempted to call itemsUpdated with an invalid value: "+JSON.stringify(u);let _=Array.from(s.detailsOpenedItems);for(let p=0;p<u.length;++p){const g=u[p];g&&(g.detailsOpened?s._getItemIndexInArray(g,_)<0&&_.push(g):s._getItemIndexInArray(g,_)>=0&&_.splice(s._getItemIndexInArray(g,_),1))}s.detailsOpenedItems=_},m=function(u){const{rootCache:_}=i;if(!(e[u]&&_.pendingRequests[u]))for(let p=0;p<s.pageSize;p++){const g=u*s.pageSize+p,S=e[u]?.[p];_.items[g]=S}};s.$connector.set=function(u,_){_.forEach((S,F)=>{const R=u+F,j=Math.floor(R/s.pageSize);e[j]??=[],e[j][R%s.pageSize]=S});const p=Math.floor(u/s.pageSize),g=Math.ceil(_.length/s.pageSize);for(let S=0;S<g;S++)m(p+S);c(()=>{s.$connector.doSelection(_.filter(S=>S.selected)),s.$connector.doDeselection(_.filter(S=>!S.selected&&a[S.key])),f(_)}),s.__updateVisibleRows(u,u+_.length-1)};const v=function(u){for(let _ in e)for(let p in e[_])if(s.getItemId(e[_][p])===s.getItemId(u))return{page:_,index:p};return null};s.$connector.updateFlatData=function(u){const _=[];for(let p=0;p<u.length;p++){let g=v(u[p]);if(g){e[g.page][g.index]=u[p];const S=parseInt(g.page)*s.pageSize+parseInt(g.index),{rootCache:F}=i;F.items[S]&&(F.items[S]=u[p]),_.push(S)}}c(()=>{f(u)}),_.forEach(p=>s.__updateVisibleRows(p,p))},s.$connector.clear=function(u,_){if(!e||Object.keys(e).length===0)return;if(u%s.pageSize!=0)throw"Got cleared data for index "+u+" which is not aligned with the page size of "+s.pageSize;let p=Math.floor(u/s.pageSize),g=Math.ceil(_/s.pageSize);for(let S=0;S<g;S++){let F=p+S,R=e[F];R&&(c(()=>{s.$connector.doDeselection(R.filter(j=>a[j.key])),R.forEach(j=>s.closeItemDetails(j))}),delete e[F],m(F))}s.__updateVisibleRows(u,u+_-1)},s.$connector.reset=function(){e={},i.clearCache(),r=[-1,-1],n?.cancel(),s.__updateVisibleRows()},s.$connector.updateSize=u=>s.size=u,s.$connector.updateUniqueItemIdPath=u=>s.itemIdPath=u,s.$connector.confirm=function(u){const{pendingRequests:_}=i.rootCache;Object.entries(_).forEach(([p,g])=>{const S=s.size?Math.ceil(s.size/s.pageSize)-1:0,F=Math.min(r[1],S);e[p]?g(e[p]):p<r[0]||+p>F?(g(new Array(s.pageSize)),s.requestContentUpdate()):g&&s.size===0&&g([])}),Object.keys(_).length===0&&(n?.cancel(),r=[-1,-1]),s.$server.confirmUpdate(u)},s.$connector.setSelectionMode=function(u){if((typeof u=="string"||u instanceof String)&&o.indexOf(u)>=0)l=u,a={},s.selectedItems=[],s.$connector.updateMultiSelectable();else throw"Attempted to set an invalid selection mode"},s.$connector.updateMultiSelectable=function(){s.$&&(l===o[0]?s.$.table.setAttribute("aria-multiselectable",!1):l===o[1]?s.$.table.removeAttribute("aria-multiselectable"):s.$.table.setAttribute("aria-multiselectable",!0))},s._createPropertyObserver("isAttached",()=>s.$connector.updateMultiSelectable());const x=u=>_=>{u&&(u(_),u=null)};s.$connector.setHeaderRenderer=function(u,_){const{content:p,showSorter:g,sorterPath:S}=_;if(p===null){u.headerRenderer=null;return}u.headerRenderer=x(F=>{F.innerHTML="";let R=F;if(g){const j=document.createElement("vaadin-grid-sorter");j.setAttribute("path",S);const ae=p instanceof Node?p.textContent:p;ae&&j.setAttribute("aria-label",`Sort by ${ae}`),F.appendChild(j),R=j}p instanceof Node?R.appendChild(p):R.textContent=p})},s._getActiveSorters=function(){return this._sorters.filter(u=>u.direction)},s.__applySorters=function(...u){const _=s._mapSorters(),p=JSON.stringify(s._previousSorters)!==JSON.stringify(_);s._previousSorters=_,Object.getPrototypeOf(this).__applySorters.call(this,...u),p&&!d&&s.$server.sortersChanged(_)},s.$connector.setFooterRenderer=function(u,_){const{content:p}=_;if(p===null){u.footerRenderer=null;return}u.footerRenderer=x(g=>{g.innerHTML="",p instanceof Node?g.appendChild(p):g.textContent=p})},s.addEventListener("vaadin-context-menu-before-open",function(u){const{key:_,columnId:p}=u.detail;s.$server.updateContextMenuTargetItem(_,p)}),s.getContextMenuBeforeOpenDetail=function(u){const _=u.detail.sourceEvent||u,p=s.getEventContext(_),g=p.item?.key||"",S=p.column?.id||"";return{key:g,columnId:S}},s.preventContextMenu=function(u){const _=u.type==="click",{column:p}=s.getEventContext(u);return _&&p instanceof Ri},s.addEventListener("click",u=>b(u,"item-click")),s.addEventListener("dblclick",u=>b(u,"item-double-click")),s.addEventListener("column-resize",u=>{s._getColumnsInOrder().filter(p=>!p.hidden).forEach(p=>{p.dispatchEvent(new CustomEvent("column-drag-resize"))}),s.dispatchEvent(new CustomEvent("column-drag-resize",{detail:{resizedColumnKey:u.detail.resizedColumn._flowId}}))}),s.addEventListener("column-reorder",u=>{const _=s._columnTree.slice(0).pop().filter(p=>p._flowId).sort((p,g)=>p._order-g._order).map(p=>p._flowId);s.dispatchEvent(new CustomEvent("column-reorder-all-columns",{detail:{columns:_}}))}),s.addEventListener("cell-focus",u=>{const _=s.getEventContext(u);["header","body","footer"].indexOf(_.section)!==-1&&s.dispatchEvent(new CustomEvent("grid-cell-focus",{detail:{itemKey:_.item?_.item.key:null,internalColumnId:_.column?_.column._flowId:null,section:_.section}}))});function b(u,_){if(u.defaultPrevented)return;const p=u.composedPath(),g=p.findIndex(ae=>ae.localName==="td"||ae.localName==="th"),S=p[g];if(p.slice(0,g).some(ae=>S?._focusButton!==ae&&zr(ae)||ae instanceof HTMLLabelElement))return;const R=s.getEventContext(u),j=R.section;R.item&&j!=="details"&&(u.itemKey=R.item.key,R.column&&(u.internalColumnId=R.column._flowId),s.dispatchEvent(new CustomEvent(_,{detail:u})))}s.cellPartNameGenerator=function(u,_){const p=_.item.part;if(p)return(p.row||"")+" "+(u&&p[u._flowId]||"")},s.dropFilter=u=>u.item&&!u.item.dropDisabled,s.dragFilter=u=>u.item&&!u.item.dragDisabled,s.addEventListener("grid-dragstart",u=>{s._isSelected(u.detail.draggedItems[0])?(s.__selectionDragData?Object.keys(s.__selectionDragData).forEach(_=>{u.detail.setDragData(_,s.__selectionDragData[_])}):(s.__dragDataTypes||[]).forEach(_=>{u.detail.setDragData(_,u.detail.draggedItems.map(p=>p.dragData[_]).join(`
`))}),s.__selectionDraggedItemsCount>1&&u.detail.setDraggedItemsCount(s.__selectionDraggedItemsCount)):(s.__dragDataTypes||[]).forEach(_=>{u.detail.setDragData(_,u.detail.draggedItems[0].dragData[_])})}),s.isItemSelectable=u=>u?.selectable===void 0||u.selectable;function k(u){const _=u.getBoundingClientRect(),p=s.$.table.getBoundingClientRect(),g=s.$.header.getBoundingClientRect(),S=s.$.footer.getBoundingClientRect();return _.top>=p.top+g.height&&_.bottom<=p.bottom-S.height}s.$connector.scrollToItem=function(u,..._){const p=s._getRenderedRows().find(g=>{const{item:S}=s.__getRowModel(g);return s.getItemId(S)===u});p&&k(p)||s.scrollToIndex(..._)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const E_=s=>class extends Fr(s){static get properties(){return{_childColumns:{value(){return this._getChildColumns(this)}},flexGrow:{type:Number,readOnly:!0,sync:!0},width:{type:String,readOnly:!0,sync:!0},_visibleChildColumns:Array,_colSpan:Number,_rootColumns:Array}}static get observers(){return["_groupFrozenChanged(frozen, _rootColumns)","_groupFrozenToEndChanged(frozenToEnd, _rootColumns)","_groupHiddenChanged(hidden)","_colSpanChanged(_colSpan, _headerCell, _footerCell)","_groupOrderChanged(_order, _rootColumns)","_groupReorderStatusChanged(_reorderStatus, _rootColumns)","_groupResizableChanged(resizable, _rootColumns)"]}connectedCallback(){super.connectedCallback(),this._addNodeObserver(),this._updateFlexAndWidth()}disconnectedCallback(){super.disconnectedCallback(),this._observer&&this._observer.disconnect()}_columnPropChanged(i,e){i==="hidden"&&(this._preventHiddenSynchronization=!0,this._updateVisibleChildColumns(this._childColumns),this._preventHiddenSynchronization=!1),/flexGrow|width|hidden|_childColumns/u.test(i)&&this._updateFlexAndWidth(),i==="frozen"&&!this.frozen&&(this.frozen=e),i==="lastFrozen"&&!this._lastFrozen&&(this._lastFrozen=e),i==="frozenToEnd"&&!this.frozenToEnd&&(this.frozenToEnd=e),i==="firstFrozenToEnd"&&!this._firstFrozenToEnd&&(this._firstFrozenToEnd=e)}_groupOrderChanged(i,e){if(e){const t=e.slice(0);if(!i){t.forEach(a=>{a._order=0});return}const n=/(0+)$/u.exec(i).pop().length,r=~~(Math.log(e.length)/Math.LN10)+1,o=10**(n-r);t[0]&&t[0]._order&&t.sort((a,l)=>a._order-l._order),Lr(t,o,i)}}_groupReorderStatusChanged(i,e){i===void 0||e===void 0||e.forEach(t=>{t._reorderStatus=i})}_groupResizableChanged(i,e){i===void 0||e===void 0||e.forEach(t=>{t.resizable=i})}_updateVisibleChildColumns(i){this._visibleChildColumns=Array.prototype.filter.call(i,e=>!e.hidden),this._colSpan=this._visibleChildColumns.length,this._updateAutoHidden()}_updateFlexAndWidth(){if(this._visibleChildColumns){if(this._visibleChildColumns.length>0){const i=this._visibleChildColumns.reduce((e,t)=>(e+=` + ${(t.width||"0px").replace("calc","")}`,e),"").substring(3);this._setWidth(`calc(${i})`)}else this._setWidth("0px");this._setFlexGrow(Array.prototype.reduce.call(this._visibleChildColumns,(i,e)=>i+e.flexGrow,0))}}__scheduleAutoFreezeWarning(i,e){if(this._grid){const t=e.replace(/([A-Z])/gu,"-$1").toLowerCase(),n=i[0][e]||i[0].hasAttribute(t);i.every(o=>(o[e]||o.hasAttribute(t))===n)||(this._grid.__autoFreezeWarningDebouncer=D.debounce(this._grid.__autoFreezeWarningDebouncer,ue,()=>{console.warn(`WARNING: Joining ${e} and non-${e} Grid columns inside the same column group! This will automatically freeze all the joined columns to avoid rendering issues. If this was intentional, consider marking each joined column explicitly as ${e}. Otherwise, exclude the ${e} columns from the joined group.`)}))}}_groupFrozenChanged(i,e){e===void 0||i===void 0||i!==!1&&(this.__scheduleAutoFreezeWarning(e,"frozen"),Array.from(e).forEach(t=>{t.frozen=i}))}_groupFrozenToEndChanged(i,e){e===void 0||i===void 0||i!==!1&&(this.__scheduleAutoFreezeWarning(e,"frozenToEnd"),Array.from(e).forEach(t=>{t.frozenToEnd=i}))}_groupHiddenChanged(i){(i||this.__groupHiddenInitialized)&&this._synchronizeHidden(),this.__groupHiddenInitialized=!0}_updateAutoHidden(){const i=this._autoHidden;this._autoHidden=(this._visibleChildColumns||[]).length===0,(i||this._autoHidden)&&(this.hidden=this._autoHidden)}_synchronizeHidden(){this._childColumns&&!this._preventHiddenSynchronization&&this._childColumns.forEach(i=>{i.hidden=this.hidden})}_colSpanChanged(i,e,t){e&&(e.setAttribute("colspan",i),this._grid&&this._grid.__a11yUpdateCellColspan(e,i)),t&&(t.setAttribute("colspan",i),this._grid&&this._grid.__a11yUpdateCellColspan(t,i))}_getChildColumns(i){return xe.getColumns(i)}_addNodeObserver(){this._observer=new xe(this,()=>{this._preventHiddenSynchronization=!0,this._rootColumns=this._getChildColumns(this),this._childColumns=this._rootColumns,this._updateVisibleChildColumns(this._childColumns),this._preventHiddenSynchronization=!1,this._grid&&this._grid._debounceUpdateColumnTree&&this._grid._debounceUpdateColumnTree()}),this._observer.flush()}_isColumnElement(i){return i.nodeType===Node.ELEMENT_NODE&&/\bcolumn\b/u.test(i.localName)}};/**
 * @license
 * Copyright (c) 2016 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class I_ extends E_(I(E)){static get is(){return"vaadin-grid-column-group"}}w(I_);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const Zs=C`
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
`,S_=window.Vaadin.featureFlags.layoutComponentImprovements,k_=C`
  ::slotted([data-width-full]) {
    flex: 1;
  }

  ::slotted(vaadin-horizontal-layout[data-width-full]),
  ::slotted(vaadin-vertical-layout[data-width-full]) {
    min-width: 0;
  }
`,T_=S_?[Zs,k_]:[Zs];/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const A_=s=>class extends s{ready(){super.ready();const i=this.shadowRoot.querySelector("slot:not([name])");this.__startSlotObserver=new ce(i,({currentNodes:n,removedNodes:r})=>{r.length&&this.__clearAttribute(r,"last-start-child");const o=n.filter(l=>l.nodeType===Node.ELEMENT_NODE);this.__updateAttributes(o,"start",!1,!0);const a=n.filter(l=>!xn(l));this.toggleAttribute("has-start",a.length>0)});const e=this.shadowRoot.querySelector('[name="end"]');this.__endSlotObserver=new ce(e,({currentNodes:n,removedNodes:r})=>{r.length&&this.__clearAttribute(r,"first-end-child"),this.__updateAttributes(n,"end",!0,!1),this.toggleAttribute("has-end",n.length>0)});const t=this.shadowRoot.querySelector('[name="middle"]');this.__middleSlotObserver=new ce(t,({currentNodes:n,removedNodes:r})=>{r.length&&(this.__clearAttribute(r,"first-middle-child"),this.__clearAttribute(r,"last-middle-child")),this.__updateAttributes(n,"middle",!0,!0),this.toggleAttribute("has-middle",n.length>0)})}__clearAttribute(i,e){const t=i.find(n=>n.nodeType===Node.ELEMENT_NODE&&n.hasAttribute(e));t&&t.removeAttribute(e)}__updateAttributes(i,e,t,n){i.forEach((r,o)=>{if(t){const a=`first-${e}-child`;o===0?r.setAttribute(a,""):r.hasAttribute(a)&&r.removeAttribute(a)}if(n){const a=`last-${e}-child`;o===i.length-1?r.setAttribute(a,""):r.hasAttribute(a)&&r.removeAttribute(a)}})}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class D_ extends A_(T(L(I(A(E))))){static get is(){return"vaadin-horizontal-layout"}static get styles(){return T_}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return y`
      <slot></slot>
      <slot name="middle"></slot>
      <slot name="end"></slot>
    `}}w(D_);/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const O_=C`
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
 */const P_=C`
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
 */const M_=s=>class extends s{static get properties(){return{overlayClass:{type:String},_overlayElement:{type:Object}}}static get observers(){return["__updateOverlayClassNames(overlayClass, _overlayElement)"]}__updateOverlayClassNames(e,t){if(!t||e===void 0)return;const{classList:n}=t;if(this.__initialClasses||(this.__initialClasses=new Set(n)),Array.isArray(this.__previousClasses)){const o=this.__previousClasses.filter(a=>!this.__initialClasses.has(a));o.length>0&&n.remove(...o)}const r=typeof e=="string"?e.split(" ").filter(Boolean):[];r.length>0&&n.add(...r),this.__previousClasses=r}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */const R_=s=>class extends s{static get properties(){return{opened:{type:Boolean,value:!1,sync:!0,observer:"_openedChanged"}}}constructor(){super(),this._boundVaadinOverlayClose=this._onVaadinOverlayClose.bind(this),ze&&(this._boundIosResizeListener=()=>this._detectIosNavbar())}firstUpdated(i){super.firstUpdated(i),this.popover="manual"}bringToFront(){this.matches(":popover-open")&&(this.hidePopover(),this.showPopover())}_openedChanged(i){i?(document.body.appendChild(this),this.showPopover(),document.addEventListener("vaadin-overlay-close",this._boundVaadinOverlayClose),this._boundIosResizeListener&&(this._detectIosNavbar(),window.addEventListener("resize",this._boundIosResizeListener))):(document.body.removeChild(this),this.hidePopover(),document.removeEventListener("vaadin-overlay-close",this._boundVaadinOverlayClose),this._boundIosResizeListener&&window.removeEventListener("resize",this._boundIosResizeListener))}_detectIosNavbar(){const i=window.innerHeight,t=window.innerWidth>i,n=document.documentElement.clientHeight;t&&n>i?this.style.bottom=`${n-i}px`:this.style.bottom="0"}_onVaadinOverlayClose(i){const e=i.detail.sourceEvent;e&&e.composedPath().indexOf(this)>=0&&i.preventDefault()}},L_=s=>class extends st(M_(s)){static get properties(){return{assertive:{type:Boolean,value:!1,sync:!0},duration:{type:Number,value:5e3,sync:!0},opened:{type:Boolean,value:!1,notify:!0,sync:!0,observer:"_openedChanged"},position:{type:String,value:"bottom-start",observer:"_positionChanged",sync:!0},renderer:{type:Function,sync:!0}}}static get observers(){return["_durationChanged(duration, opened)","_rendererChanged(renderer, opened, _overlayElement)"]}static show(i,e){const t=customElements.get("vaadin-notification");return Ko(i)?t._createAndShowNotification(n=>{Ut(i,n)},e):t._createAndShowNotification(n=>{n.innerText=i},e)}static _createAndShowNotification(i,e){const t=document.createElement("vaadin-notification");return e&&Number.isFinite(e.duration)&&(t.duration=e.duration),e&&e.position&&(t.position=e.position),e&&e.assertive&&(t.assertive=e.assertive),e&&e.theme&&t.setAttribute("theme",e.theme),t.renderer=i,document.body.appendChild(t),t.opened=!0,t.addEventListener("opened-changed",n=>{n.detail.value||t.remove()}),t}get _container(){const i=customElements.get("vaadin-notification");return i._container||(i._container=document.createElement("vaadin-notification-container"),document.body.appendChild(i._container)),i._container}get _card(){return this._overlayElement}ready(){super.ready(),this._overlayElement=this.shadowRoot.querySelector("vaadin-notification-card")}disconnectedCallback(){super.disconnectedCallback(),queueMicrotask(()=>{this.isConnected||(this.opened=!1)})}requestContentUpdate(){!this.renderer||!this._card||this.renderer(this._card,this)}__computeAriaLive(i){return i?"assertive":"polite"}_rendererChanged(i,e,t){if(!t)return;const n=this._oldRenderer!==i;this._oldRenderer=i,n&&(t.innerHTML="",delete t._$litPart$),e&&(this._didAnimateNotificationAppend||this._animatedAppendNotificationCard(),this.requestContentUpdate())}open(){this.opened=!0}close(){this.opened=!1}_openedChanged(i){i?(this._container.opened=!0,this._animatedAppendNotificationCard()):this._card&&this._closeNotificationCard()}__cleanUpOpeningClosingState(){this._card.removeAttribute("opening"),this._card.removeAttribute("closing"),this._card.removeEventListener("animationend",this.__animationEndListener)}_animatedAppendNotificationCard(){this._card?(this.__cleanUpOpeningClosingState(),this._card.setAttribute("opening",""),this._appendNotificationCard(),this.__animationEndListener=()=>this.__cleanUpOpeningClosingState(),this._card.addEventListener("animationend",this.__animationEndListener),this._didAnimateNotificationAppend=!0):this._didAnimateNotificationAppend=!1}_appendNotificationCard(){if(this._card){if(!this._container.shadowRoot.querySelector(`slot[name="${this.position}"]`)){console.warn(`Invalid alignment parameter provided: position=${this.position}`);return}this._container.firstElementChild&&this._container.bringToFront(),this._card.slot=this.position,this._container.firstElementChild&&/top/u.test(this.position)?this._container.insertBefore(this._card,this._container.firstElementChild):this._container.appendChild(this._card)}}_removeNotificationCard(){this._card&&(this._card.parentNode&&this._card.parentNode.removeChild(this._card),this._card.removeAttribute("closing"),this._container.opened=!!this._container.firstElementChild,this.dispatchEvent(new CustomEvent("closed")))}_closeNotificationCard(){this._durationTimeoutId&&clearTimeout(this._durationTimeoutId),this._animatedRemoveNotificationCard()}_animatedRemoveNotificationCard(){this.__cleanUpOpeningClosingState(),this._card.setAttribute("closing","");const i=getComputedStyle(this._card).getPropertyValue("animation-name");i&&i!=="none"?(this.__animationEndListener=()=>{this._removeNotificationCard(),this.__cleanUpOpeningClosingState()},this._card.addEventListener("animationend",this.__animationEndListener)):this._removeNotificationCard()}_positionChanged(){this.opened&&this._animatedAppendNotificationCard()}_durationChanged(i,e){e&&(clearTimeout(this._durationTimeoutId),i>0&&(this._durationTimeoutId=setTimeout(()=>this.close(),i)))}};/**
 * @license
 * Copyright (c) 2017 - 2026 Vaadin Ltd.
 * This program is available under Apache License Version 2.0, available at https://vaadin.com/license/
 */class F_ extends R_(T(L(I(A(E))))){static get is(){return"vaadin-notification-container"}static get styles(){return P_}render(){return y`
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
    `}}class $_ extends T(I(A(E))){static get is(){return"vaadin-notification-card"}static get styles(){return O_}render(){return y`
      <div part="overlay">
        <div part="content">
          <slot></slot>
        </div>
      </div>
    `}ready(){super.ready(),this.setAttribute("role","alert")}}class z_ extends L_(L(T(I(E)))){static get is(){return"vaadin-notification"}static get styles(){return C`
      :host {
        display: none !important;
      }
    `}render(){return y`
      <vaadin-notification-card
        theme="${B(this._theme)}"
        aria-live="${this.__computeAriaLive(this.assertive)}"
      ></vaadin-notification-card>
    `}}w(F_);w($_);w(z_);function N_(s,i){if(i.type==="stateKeyChanged"){const{value:e}=i;return{...s,key:e}}else return s}const B_=()=>{};class V_ extends HTMLElement{#e=void 0;#i=!1;#t=void 0;#s=Object.create(null);#r=new Map;#n=new Map;#o=B_;#d=new Map;#h;#a;#l;constructor(){super(),this.#h={useState:this.useState.bind(this),useCustomEvent:this.useCustomEvent.bind(this),useContent:this.useContent.bind(this)},this.#a=this.#u.bind(this),this.#_()}async connectedCallback(){this.#t=rt.createElement(this.#a),!(!this.dispatchEvent(new CustomEvent("flow-portal-add",{bubbles:!0,cancelable:!0,composed:!0,detail:{children:this.#t,domNode:this}}))||this.#e)&&(await this.#l,this.#e=Wr.createRoot(this),this.#c(),this.#e.render(this.#t))}addReadyCallback(i,e){this.#d.set(i,e)}async disconnectedCallback(){this.#e?(this.#l=Promise.resolve(),await this.#l,this.#e.unmount(),this.#e=void 0):this.dispatchEvent(new CustomEvent("flow-portal-remove",{bubbles:!0,cancelable:!0,composed:!0,detail:{children:this.#t,domNode:this}})),this.#i=!1,this.#t=void 0}useState(i,e){if(this.#r.has(i))return[this.#s[i],this.#r.get(i)];const t=this[i]??e;this.#s[i]=t,Object.defineProperty(this,i,{enumerable:!0,get(){return this.#s[i]},set(o){this.#s[i]=o,this.#o({type:"stateKeyChanged",key:i,value:t})}});const n=this.useCustomEvent(`${i}-changed`,{detail:{value:t}}),r=o=>{this.#s[i]=o,n({value:o}),this.#o({type:"stateKeyChanged",key:i,value:o})};return this.#r.set(i,r),[t,r]}useCustomEvent(i,e={}){if(!this.#n.has(i)){const t=(n=>{const r=n===void 0?e:{...e,detail:n},o=new CustomEvent(i,r);return this.dispatchEvent(o)});return this.#n.set(i,t),t}return this.#n.get(i)}useContent(i){return rt.useEffect(()=>{this.#d.get(i)?.()},[]),rt.createElement("flow-content-container",{name:i,style:{display:"contents"}})}#c(){this.#i||!this.#e||(this.#e.render(rt.createElement(this.#a)),this.#i=!0)}#u(){const[i,e]=rt.useReducer(N_,this.#s);return this.#s=i,this.#o=e,this.render(this.#h)}#_(){let i=window.Vaadin||{};i.developmentMode&&(i.registrations=i.registrations||[],i.registrations.push({is:"ReactAdapterElement",version:"25.0.5"}))}}class H_ extends V_{async connectedCallback(){await super.connectedCallback(),this.style.display="contents"}render(){return qr.jsx(Ur,{})}}customElements.define("react-router-outlet",H_);const W_=s=>Promise.resolve(0);window.Vaadin=window.Vaadin||{};window.Vaadin.Flow=window.Vaadin.Flow||{};window.Vaadin.Flow.loadOnDemand=W_;window.Vaadin.Flow.resetFocus=()=>{let s=document.activeElement;for(;s&&s.shadowRoot;)s=s.shadowRoot.activeElement;return!s||s.blur()||s.focus()||!0};
