import{o as fe,P as ne,d as ie,a as ge,O as pe,D as me,T as ae,L as ce,b as be,c as se,t as oe,i as ue,E as ve}from"./generated-flow-imports-BNGvL9My.js";import{i as Xt,a as re,b as Zt,D as de}from"./indexhtml-GL0WLVAv.js";import"./commonjsHelpers-CqkleIqs.js";/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 *
 * This program is available under Vaadin Commercial License and Service Terms.
 *
 *
 * See https://vaadin.com/commercial-license-and-service-terms for the full
 * license.
 */const ye=Xt`
  [part='overlay'] {
    padding: var(
      --vaadin-rich-text-editor-overlay-padding,
      var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container)
    );
  }

  [part='content'] {
    display: grid;
    gap: var(--vaadin-rich-text-editor-overlay-gap, var(--vaadin-gap-s));
    grid-template-columns: repeat(7, minmax(0, 1fr));
  }

  [part='content'] ::slotted(button) {
    background-color: var(--_btn-background);
    border: var(--vaadin-rich-text-editor-overlay-color-option-border-width, 1px) solid
      var(--vaadin-rich-text-editor-overlay-color-option-border-color, transparent);
    border-radius: var(--vaadin-rich-text-editor-overlay-color-option-border-radius, 9999px);
    cursor: var(--vaadin-clickable-cursor);
    font: inherit;
    height: var(--vaadin-rich-text-editor-overlay-color-option-height, 1lh);
    padding: 0;
    width: var(--vaadin-rich-text-editor-overlay-color-option-width, 1lh);
  }

  [part='content'] ::slotted(button:first-of-type) {
    background-color: transparent;
    border-color: var(--vaadin-border-color-secondary);
    background-image: repeating-linear-gradient(
      135deg,
      transparent 0%,
      transparent 47%,
      red 50%,
      transparent 53%,
      transparent 100%
    );
  }

  [part='content'] ::slotted(button:focus-visible) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: 1px;
  }
`,Ae=[fe,ye];/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 *
 * This program is available under Vaadin Commercial License and Service Terms.
 *
 *
 * See https://vaadin.com/commercial-license-and-service-terms for the full
 * license.
 */class ke extends ne(re){static get is(){return"vaadin-rich-text-editor-popup"}static get styles(){return Xt`
      :host([opened]),
      :host([opening]),
      :host([closing]) {
        display: block !important;
        position: fixed;
      }

      :host,
      :host([hidden]) {
        display: none !important;
      }
    `}static get properties(){return{target:{type:Object},opened:{type:Boolean,reflectToAttribute:!0,notify:!0},colors:{type:Array}}}static get observers(){return["__openedOrTargetChanged(opened, target)","__colorsChanged(colors)"]}render(){return Zt`
      <vaadin-rich-text-editor-popup-overlay
        id="overlay"
        .owner="${this}"
        .opened="${this.opened}"
        .positionTarget="${this.target}"
        no-vertical-overlap
        horizontal-align="start"
        vertical-align="top"
        focus-trap
        exportparts="overlay, content"
        @opened-changed="${this._onOpenedChanged}"
        @vaadin-overlay-escape-press="${this._onOverlayEscapePress}"
      >
        <slot></slot>
      </vaadin-rich-text-editor-popup-overlay>
    `}_onOpenedChanged(ct){this.opened=ct.detail.value}_onOverlayEscapePress(){this.target.focus()}_onColorClick(ct){const{color:E}=ct.target.dataset;this.dispatchEvent(new CustomEvent("color-selected",{detail:{color:E}}))}__colorsChanged(ct){de(Zt`
        ${ct.map(E=>Zt`
            <button data-color="${E}" style="--_btn-background: ${E}" @click="${this._onColorClick}"></button>
          `)}
      `,this,{host:this})}__openedOrTargetChanged(ct,E){E&&E.setAttribute("aria-expanded",ct?"true":"false")}}ie(ke);class xe extends ge(pe(me(ae(ne(ce(re)))))){static get is(){return"vaadin-rich-text-editor-popup-overlay"}static get styles(){return Ae}render(){return Zt`
      <div part="overlay" id="overlay">
        <div part="content" id="content">
          <slot></slot>
        </div>
      </div>
    `}get _contentRoot(){return this.owner}get _focusTrapRoot(){return this.owner}}ie(xe);/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 *
 * This program is available under Vaadin Commercial License and Service Terms.
 *
 *
 * See https://vaadin.com/commercial-license-and-service-terms for the full
 * license.
 */const Ne=Xt`
  :host {
    --_vaadin-icon-align-center: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 5H3"/><path d="M17 12H7"/><path d="M19 19H5"/></svg>');
    --_vaadin-icon-align-left: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 5H3"/><path d="M15 12H3"/><path d="M17 19H3"/></svg>');
    --_vaadin-icon-align-right: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 5H3"/><path d="M21 12H9"/><path d="M21 19H7"/></svg>');
    --_vaadin-icon-background: url('data:image/svg+xml,<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.6 12L12 9.4L8 13.4L10.575 16L14.6 12ZM13.425 8L16 10.575L20 6.6L17.4 4L13.425 8ZM11.325 7.275L16.725 12.675L12 17.425C11.6 17.825 11.1292 18.025 10.5875 18.025C10.0458 18.025 9.575 17.825 9.175 17.425L8.5 18H3.5L6.65 14.875C6.25 14.475 6.04167 13.9958 6.025 13.4375C6.00833 12.8792 6.2 12.4 6.6 12L11.325 7.275ZM11.325 7.275L16 2.6C16.4 2.2 16.8708 2 17.4125 2C17.9542 2 18.425 2.2 18.825 2.6L21.425 5.175C21.825 5.575 22.025 6.04583 22.025 6.5875C22.025 7.12917 21.825 7.6 21.425 8L16.725 12.675L11.325 7.275Z" fill="currentColor"/></svg>');
    --_vaadin-icon-bold: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linejoin="round" d="M6.75 3.744h-.753v8.25h7.125a4.125 4.125 0 0 0 0-8.25H6.75Zm0 0v.38m0 16.122h6.747a4.5 4.5 0 0 0 0-9.001h-7.5v9h.753Zm0 0v-.37m0-15.751h6a3.75 3.75 0 1 1 0 7.5h-6m0-7.5v7.5m0 0v8.25m0-8.25h6.375a4.125 4.125 0 0 1 0 8.25H6.75m.747-15.38h4.875a3.375 3.375 0 0 1 0 6.75H7.497v-6.75Zm0 7.5h5.25a3.75 3.75 0 0 1 0 7.5h-5.25v-7.5Z" /></svg>');
    --_vaadin-icon-clear: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" fill="currentColor"><path d="m528-546-93-93-121-121h486v120H568l-40 94ZM792-56 460-388l-80 188H249l119-280L56-792l56-56 736 736-56 56Z"/></svg>');
    --_vaadin-icon-code: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/></svg>');
    --_vaadin-icon-color: url('data:image/svg+xml,<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5.5 17L10.75 3H13.25L18.5 17H16.1L14.85 13.4H9.2L7.9 17H5.5ZM9.9 11.4H14.1L12.05 5.6H11.95L9.9 11.4Z" fill="currentColor"/></svg>');
    --_vaadin-icon-color-underline: url('data:image/svg+xml,<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2 24V20H22V24H2Z" fill="currentColor"/></svg>');
    --_vaadin-icon-h1: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h8"/><path d="M4 18V6"/><path d="M12 18V6"/><path d="m17 12 3-2v8"/></svg>');
    --_vaadin-icon-h2: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h8"/><path d="M4 18V6"/><path d="M12 18V6"/><path d="M21 18h-4c0-4 4-3 4-6 0-1.5-2-2.5-4-1"/></svg>');
    --_vaadin-icon-h3: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h8"/><path d="M4 18V6"/><path d="M12 18V6"/><path d="M17.5 10.5c1.7-1 3.5 0 3.5 1.5a2 2 0 0 1-2 2"/><path d="M17 17.5c2 1.5 4 .3 4-1.5a2 2 0 0 0-2-2"/></svg>');
    --_vaadin-icon-indent: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 5H11"/><path d="M21 12H11"/><path d="M21 19H11"/><path d="m3 8 4 4-4 4"/></svg>');
    --_vaadin-icon-italic: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" x2="10" y1="4" y2="4"/><line x1="14" x2="5" y1="20" y2="20"/><line x1="15" x2="9" y1="4" y2="20"/></svg>');
    --_vaadin-icon-list-number: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5h10"/><path d="M11 12h10"/><path d="M11 19h10"/><path d="M4 4h1v5"/><path d="M4 9h2"/><path d="M6.5 20H3.4c0-1 2.6-1.925 2.6-3.5a1.5 1.5 0 0 0-2.6-1.02"/></svg>');
    --_vaadin-icon-list-bullet: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 5h.01"/><path d="M3 12h.01"/><path d="M3 19h.01"/><path d="M8 5h13"/><path d="M8 12h13"/><path d="M8 19h13"/></svg>');
    --_vaadin-icon-outdent: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 5H11"/><path d="M21 12H11"/><path d="M21 19H11"/><path d="m7 8-4 4 4 4"/></svg>');
    --_vaadin-icon-quote: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 5H3"/><path d="M21 12H8"/><path d="M21 19H8"/><path d="M3 12v7"/></svg>');
    --_vaadin-icon-strikethrough: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4H9a3 3 0 0 0-2.83 4"/><path d="M14 12a4 4 0 0 1 0 8H6"/><line x1="4" x2="20" y1="12" y2="12"/></svg>');
    --_vaadin-icon-subscript: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m4 5 8 8"/><path d="m12 5-8 8"/><path d="M20 19h-4c0-1.5.44-2 1.5-2.5S20 15.33 20 14c0-.47-.17-.93-.48-1.29a2.11 2.11 0 0 0-2.62-.44c-.42.24-.74.62-.9 1.07"/></svg>');
    --_vaadin-icon-superscript: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m4 19 8-8"/><path d="m12 19-8-8"/><path d="M20 12h-4c0-1.5.442-2 1.5-2.5S20 8.334 20 7.002c0-.472-.17-.93-.484-1.29a2.105 2.105 0 0 0-2.617-.436c-.42.239-.738.614-.899 1.06"/></svg>');
    --_vaadin-icon-underline: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4v6a6 6 0 0 0 12 0V4"/><line x1="4" x2="20" y1="20" y2="20"/></svg>');
  }
`;/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 *
 * This program is available under Vaadin Commercial License and Service Terms.
 *
 *
 * See https://vaadin.com/commercial-license-and-service-terms for the full
 * license.
 */const Ee=Xt`
  :host {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
  }

  :host([hidden]) {
    display: none !important;
  }

  .announcer {
    clip: rect(0, 0, 0, 0);
    position: fixed;
  }

  input[type='file'] {
    display: none;
  }

  .vaadin-rich-text-editor-container {
    display: flex;
    flex: auto;
    flex-direction: column;
    max-height: inherit;
    min-height: inherit;
    background: var(--vaadin-rich-text-editor-background, var(--vaadin-background-color));
    border: var(--vaadin-input-field-border-width, 1px) solid
      var(--vaadin-input-field-border-color, var(--vaadin-border-color));
    border-radius: var(--vaadin-input-field-border-radius, var(--vaadin-radius-m));
    outline-offset: calc(var(--vaadin-input-field-border-width, 1px) * -1);
    contain: paint;
  }

  .vaadin-rich-text-editor-container:has([part='content']:focus-within),
  .vaadin-rich-text-editor-container:has([part~='toolbar-button']:active) {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
  }
`,_e=Xt`
  :host {
    --_item-indent: var(--vaadin-padding-s);
    --_marker-indent: var(--vaadin-gap-s);
    --_list-indent: var(--_item-indent);
  }

  [part='content'] {
    box-sizing: border-box;
    display: flex;
    flex: auto;
    flex-direction: column;
    overflow: hidden;
    position: relative;
    cursor: text;
  }

  /*
    Quill core styles.
    CSS selectors removed: margin & padding reset, check list, indentation, video, colors, ordered & unordered list, h1-6, anchor
  */
  .ql-clipboard {
    height: 1px;
    left: -100000px;
    overflow-y: hidden;
    position: absolute;
    top: 50%;
  }

  .ql-clipboard p {
    margin: 0;
    padding: 0;
  }

  .ql-editor {
    box-sizing: border-box;
    color: var(--vaadin-rich-text-editor-content-color, var(--vaadin-text-color));
    flex: 1;
    font-size: var(--vaadin-rich-text-editor-content-font-size, var(--vaadin-input-field-value-font-size, inherit));
    height: 100%;
    line-height: var(--vaadin-rich-text-editor-content-line-height, inherit);
    outline: none;
    overflow-y: auto;
    padding: var(
      --vaadin-rich-text-editor-content-padding,
      var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container)
    );
    tab-size: calc(var(--_item-indent) * 2);
    text-align: left;
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .ql-editor > * {
    cursor: text;
  }

  .ql-align-left {
    text-align: left;
  }

  .ql-direction-rtl {
    direction: rtl;
    text-align: inherit;
  }

  .ql-align-center {
    text-align: center;
  }

  .ql-align-justify {
    text-align: justify;
  }

  .ql-align-right {
    text-align: right;
  }

  .ql-code-block-container {
    font-family: monospace;
    background-color: var(--vaadin-background-container);
    border-radius: var(--vaadin-radius-s);
    white-space: pre-wrap;
    margin-block: var(--vaadin-padding-s);
    padding: var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container);
  }

  /* lists */
  .ql-editor ol {
    padding-inline-start: var(--_list-indent);
  }

  .ql-editor li {
    list-style-type: none;
    position: relative;
    padding-inline-start: var(--_item-indent);
  }

  .ql-editor li > .ql-ui::before {
    display: inline-block;
    width: var(--_item-indent);
    margin-inline: calc(var(--_item-indent) * -1) var(--_marker-indent);
    text-align: end;
    white-space: nowrap;
  }

  .ql-editor li[data-list='bullet'] > .ql-ui::before {
    content: '\\2022';
    font-size: 1.5rem;
    line-height: 1rem;
    align-self: baseline;
    vertical-align: text-top;
  }

  .ql-editor p,
  .ql-editor h1,
  .ql-editor h2,
  .ql-editor h3,
  .ql-editor h4,
  .ql-editor h5,
  .ql-editor h6 {
    counter-set: list-0 list-1 list-2 list-3 list-4 list-5 list-6 list-7 list-8 list-9;
  }

  /* 0 */
  .ql-editor li[data-list='ordered'] {
    counter-increment: list-0;
  }

  .ql-editor li[data-list='ordered'] > .ql-ui::before {
    content: counter(list-0, decimal) '. ';
  }

  /* 1 */
  .ql-editor li[data-list='ordered'].ql-indent-1 {
    counter-increment: list-1;
  }

  .ql-editor li[data-list='ordered'].ql-indent-1 > .ql-ui::before {
    content: counter(list-1, lower-alpha) '. ';
  }

  .ql-editor li[data-list].ql-indent-1 {
    counter-set: list-2 list-3 list-4 list-5 list-6 list-7 list-8 list-9;
  }

  /* 2 */
  .ql-editor li[data-list='ordered'].ql-indent-2 {
    counter-increment: list-2;
  }

  .ql-editor li[data-list='ordered'].ql-indent-2 > .ql-ui::before {
    content: counter(list-2, lower-roman) '. ';
  }

  .ql-editor li[data-list].ql-indent-2 {
    counter-set: list-3 list-4 list-5 list-6 list-7 list-8 list-9;
  }

  /* 3 */
  .ql-editor li[data-list='ordered'].ql-indent-3 {
    counter-increment: list-3;
  }

  .ql-editor li[data-list='ordered'].ql-indent-3 > .ql-ui::before {
    content: counter(list-3, decimal) '. ';
  }

  .ql-editor li[data-list].ql-indent-3 {
    counter-set: list-4 list-5 list-6 list-7 list-8 list-9;
  }

  /* 4 */
  .ql-editor li[data-list='ordered'].ql-indent-4 {
    counter-increment: list-4;
  }

  .ql-editor li[data-list='ordered'].ql-indent-4 > .ql-ui::before {
    content: counter(list-4, lower-alpha) '. ';
  }

  .ql-editor li[data-list].ql-indent-4 {
    counter-set: list-5 list-6 list-7 list-8 list-9;
  }

  /* 5 */
  .ql-editor li[data-list='ordered'].ql-indent-5 {
    counter-increment: list-5;
  }

  .ql-editor li[data-list='ordered'].ql-indent-5 > .ql-ui::before {
    content: counter(list-5, lower-roman) '. ';
  }

  .ql-editor li[data-list].ql-indent-5 {
    counter-set: list-6 list-7 list-8 list-9;
  }

  /* 6 */
  .ql-editor li[data-list='ordered'].ql-indent-6 {
    counter-increment: list-6;
  }

  .ql-editor li[data-list='ordered'].ql-indent-6 > .ql-ui::before {
    content: counter(list-6, decimal) '. ';
  }

  .ql-editor li[data-list].ql-indent-6 {
    counter-set: list-7 list-8 list-9;
  }

  /* 7 */
  .ql-editor li[data-list='ordered'].ql-indent-7 {
    counter-increment: list-7;
  }

  .ql-editor li[data-list='ordered'].ql-indent-7 > .ql-ui::before {
    content: counter(list-7, lower-alpha) '. ';
  }

  .ql-editor li[data-list].ql-indent-7 {
    counter-set: list-8 list-9;
  }

  /* 8 */
  .ql-editor li[data-list='ordered'].ql-indent-8 {
    counter-increment: list-8;
  }

  .ql-editor li[data-list='ordered'].ql-indent-8 > .ql-ui::before {
    content: counter(list-8, lower-roman) '. ';
  }

  .ql-editor li[data-list].ql-indent-8 {
    counter-set: list-9;
  }

  /* indent 1 */
  .ql-editor .ql-indent-1 {
    padding-inline-start: calc(var(--_item-indent) * 2);
  }

  .ql-editor li.ql-indent-1 {
    padding-inline-start: calc(var(--_list-indent) + var(--_item-indent) * 2);
  }

  /* indent 2 */
  .ql-editor .ql-indent-2 {
    padding-inline-start: calc(var(--_item-indent) * 4);
  }

  .ql-editor li.ql-indent-2 {
    padding-inline-start: calc(var(--_list-indent) * 2 + var(--_item-indent) * 3);
  }

  /* indent 3 */
  .ql-editor .ql-indent-3 {
    padding-inline-start: calc(var(--_item-indent) * 6);
  }

  .ql-editor li.ql-indent-3 {
    padding-inline-start: calc(var(--_list-indent) * 3 + var(--_item-indent) * 4);
  }

  /* indent 4 */
  .ql-editor .ql-indent-4 {
    padding-inline-start: calc(var(--_item-indent) * 8);
  }

  .ql-editor li.ql-indent-4 {
    padding-inline-start: calc(var(--_list-indent) * 4 + var(--_item-indent) * 5);
  }

  /* indent 5 */
  .ql-editor .ql-indent-5 {
    padding-inline-start: calc(var(--_item-indent) * 10);
  }

  .ql-editor li.ql-indent-5 {
    padding-inline-start: calc(var(--_list-indent) * 5 + var(--_item-indent) * 6);
  }

  /* indent 6 */
  .ql-editor .ql-indent-6 {
    padding-inline-start: calc(var(--_item-indent) * 12);
  }

  .ql-editor li.ql-indent-6 {
    padding-inline-start: calc(var(--_list-indent) * 6 + var(--_item-indent) * 7);
  }

  /* indent 7 */
  .ql-editor .ql-indent-7 {
    padding-inline-start: calc(var(--_item-indent) * 14);
  }

  .ql-editor li.ql-indent-7 {
    padding-inline-start: calc(var(--_list-indent) * 7 + var(--_item-indent) * 8);
  }

  /* indent 8 */
  .ql-editor .ql-indent-8 {
    padding-inline-start: calc(var(--_item-indent) * 16);
  }

  .ql-editor li.ql-indent-8 {
    padding-inline-start: calc(var(--_list-indent) * 8 + var(--_item-indent) * 9);
  }
  /* quill core end */

  blockquote {
    border-inline-start: 4px solid var(--vaadin-border-color-secondary);
    margin: var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container);
    padding-inline-start: var(--vaadin-padding-s);
  }

  code {
    background-color: var(--vaadin-background-container);
    border-radius: var(--vaadin-radius-s);
    padding: 0.125rem 0.25rem;
  }

  img {
    max-width: 100%;
  }

  .ql-editor > :is(p, ol, ul, blockquote, .ql-code-block-container):first-child {
    margin-top: 0;
  }

  .ql-editor > :is(p, ol, ul, blockquote, .ql-code-block-container):last-child {
    margin-bottom: 0;
  }

  /* RTL specific styles */
  :host([dir='rtl']) .ql-editor {
    direction: rtl;
    text-align: right;
  }
`,we=Xt`
  [part='toolbar'] {
    background-color: var(--vaadin-rich-text-editor-toolbar-background, var(--vaadin-background-container));
    display: flex;
    flex-shrink: 0;
    flex-wrap: wrap;
    gap: var(--vaadin-rich-text-editor-toolbar-gap, var(--vaadin-gap-s));
    padding: var(--vaadin-rich-text-editor-toolbar-padding, var(--vaadin-padding-s));
  }

  [part~='toolbar-group'] {
    display: flex;
  }

  [part~='toolbar-button'] {
    background: var(--vaadin-rich-text-editor-toolbar-button-background, var(--vaadin-background-container));
    border: var(--vaadin-rich-text-editor-toolbar-button-border-width, 1px) solid
      var(--vaadin-rich-text-editor-toolbar-button-border-color, transparent);
    border-radius: var(--vaadin-rich-text-editor-toolbar-button-border-radius, var(--vaadin-radius-m));
    color: var(--vaadin-rich-text-editor-toolbar-button-text-color, var(--vaadin-text-color));
    cursor: var(--vaadin-clickable-cursor);
    flex-shrink: 0;
    font: inherit;
    padding: var(
      --vaadin-rich-text-editor-toolbar-button-padding,
      var(--vaadin-padding-block-container) var(--vaadin-padding-inline-container)
    );
    position: relative;
  }

  [part~='toolbar-button']::before {
    background: currentColor;
    content: '';
    display: block;
    height: var(--vaadin-icon-size, 1lh);
    width: var(--vaadin-icon-size, 1lh);
    mask-size: var(--vaadin-icon-visual-size, 100%);
    mask-repeat: no-repeat;
    mask-position: 50%;
  }

  [part~='toolbar-button']:focus-visible {
    outline: var(--vaadin-focus-ring-width) solid var(--vaadin-focus-ring-color);
    outline-offset: 1px;
    z-index: 1;
  }

  [part~='toolbar-button-pressed'],
  [part~='toolbar-button'][aria-expanded='true'] {
    --vaadin-rich-text-editor-toolbar-button-background: var(--vaadin-background-container-strong);
  }

  [part~='toolbar-button-undo']::before {
    mask-image: var(--_vaadin-icon-undo);
  }

  [part~='toolbar-button-redo']::before {
    mask-image: var(--_vaadin-icon-redo);
  }

  [part~='toolbar-button-bold']::before {
    mask-image: var(--_vaadin-icon-bold);
  }

  [part~='toolbar-button-italic']::before {
    mask-image: var(--_vaadin-icon-italic);
  }

  [part~='toolbar-button-underline']::before {
    mask-image: var(--_vaadin-icon-underline);
  }

  [part~='toolbar-button-strike']::before {
    mask-image: var(--_vaadin-icon-strikethrough);
  }

  [part~='toolbar-button-color']::before {
    mask-image: var(--_vaadin-icon-color);
  }

  [part~='toolbar-button-color']::after {
    background-color: var(--_color-value, currentColor);
  }

  [part~='toolbar-button-background']::before {
    mask-image: var(--_vaadin-icon-background);
  }

  [part~='toolbar-button-background']::after {
    background-color: var(--_background-value, currentColor);
  }

  [part~='toolbar-button-color']::after,
  [part~='toolbar-button-background']::after {
    bottom: 50%;
    content: '';
    display: block;
    height: var(--vaadin-icon-size, 1lh);
    mask-image: var(--_vaadin-icon-color-underline);
    position: absolute;
    transform: translateY(50%);
    width: var(--vaadin-icon-size, 1lh);
  }

  [part~='toolbar-button-h1']::before {
    mask-image: var(--_vaadin-icon-h1);
  }

  [part~='toolbar-button-h2']::before {
    mask-image: var(--_vaadin-icon-h2);
  }

  [part~='toolbar-button-h3']::before {
    mask-image: var(--_vaadin-icon-h3);
  }

  [part~='toolbar-button-subscript']::before {
    mask-image: var(--_vaadin-icon-subscript);
  }

  [part~='toolbar-button-superscript']::before {
    mask-image: var(--_vaadin-icon-superscript);
  }

  [part~='toolbar-button-list-ordered']::before {
    mask-image: var(--_vaadin-icon-list-number);
  }

  [part~='toolbar-button-list-bullet']::before {
    mask-image: var(--_vaadin-icon-list-bullet);
  }

  [part~='toolbar-button-outdent']::before {
    mask-image: var(--_vaadin-icon-outdent);
  }

  [part~='toolbar-button-indent']::before {
    mask-image: var(--_vaadin-icon-indent);
  }

  [part~='toolbar-button-align-left']::before {
    mask-image: var(--_vaadin-icon-align-left);
  }

  [part~='toolbar-button-align-center']::before {
    mask-image: var(--_vaadin-icon-align-center);
  }

  [part~='toolbar-button-align-right']::before {
    mask-image: var(--_vaadin-icon-align-right);
  }

  [part~='toolbar-button-image']::before {
    mask-image: var(--_vaadin-icon-image);
  }

  [part~='toolbar-button-link']::before {
    mask-image: var(--_vaadin-icon-link);
  }

  [part~='toolbar-button-blockquote']::before {
    mask-image: var(--_vaadin-icon-quote);
  }

  [part~='toolbar-button-code-block']::before {
    mask-image: var(--_vaadin-icon-code);
  }

  [part~='toolbar-button-clean']::before {
    mask-image: var(--_vaadin-icon-clear);
  }

  @media (forced-colors: active) {
    [part~='toolbar-button']::before {
      background: CanvasText;
    }

    [part~='toolbar-button-pressed'] {
      background: Highlight;
    }

    [part~='toolbar-button-pressed']::before {
      background: HighlightText;
    }
  }
`,Ce=Xt`
  :host([readonly]) [part='toolbar'] {
    display: none;
  }

  :host([disabled]) {
    pointer-events: none;
    opacity: 0.5;
    -webkit-user-select: none;
    user-select: none;
  }
`,qe=[Ne,Ee,_e,we,Ce];var Yt={exports:{}};/*!
 * Quill Editor v2.0.3
 * https://quilljs.com
 * Copyright (c) 2017-2026, Slab
 * Copyright (c) 2014, Jason Chen
 * Copyright (c) 2013, salesforce.com
 */var le;function Le(){return le||(le=1,(function(Wt){(function(ct,E){ct.Quill=E()})(window,(function(){return(function(){var ct={698:function(j,U,p){p.d(U,{Ay:function(){return B},Ji:function(){return q},zo:function(){return C}});var m=p(3),v=p(398),w=p(36),Y=p(850),et=p(508);class B extends m.BlockBlot{cache={};delta(){return this.cache.delta==null&&(this.cache.delta=(function(f){let T=!(arguments.length>1&&arguments[1]!==void 0)||arguments[1];return f.descendants(m.LeafBlot).reduce(((_,L)=>L.length()===0?_:_.insert(L.value(),q(L,{},T))),new v.Ay).insert(`
`,q(f))})(this)),this.cache.delta}deleteAt(f,T){super.deleteAt(f,T),this.cache={}}formatAt(f,T,_,L){T<=0||(this.scroll.query(_,m.Scope.BLOCK)?f+T===this.length()&&this.format(_,L):super.formatAt(f,Math.min(T,this.length()-f-1),_,L),this.cache={})}insertAt(f,T,_){if(_!=null)return super.insertAt(f,T,_),void(this.cache={});if(T.length===0)return;const L=T.split(`
`),H=L.shift();H.length>0&&(f<this.length()-1||this.children.tail==null?super.insertAt(Math.min(f,this.length()-1),H):this.children.tail.insertAt(this.children.tail.length(),H),this.cache={});let G=this;L.reduce(((I,k)=>(G=G.split(I,!0),G.insertAt(0,k),k.length)),f+H.length)}insertBefore(f,T){const{head:_}=this.children;super.insertBefore(f,T),_ instanceof w.A&&_.remove(),this.cache={}}length(){return this.cache.length==null&&(this.cache.length=super.length()+1),this.cache.length}moveChildren(f,T){super.moveChildren(f,T),this.cache={}}optimize(f){super.optimize(f),this.cache={}}path(f){return super.path(f,!0)}removeChild(f){super.removeChild(f),this.cache={}}split(f){let T=arguments.length>1&&arguments[1]!==void 0&&arguments[1];if(T&&(f===0||f>=this.length()-1)){const L=this.clone();return f===0?(this.parent.insertBefore(L,this),this):(this.parent.insertBefore(L,this.next),L)}const _=super.split(f,T);return this.cache={},_}}B.blotName="block",B.tagName="P",B.defaultChild=w.A,B.allowedChildren=[w.A,Y.A,m.EmbedBlot,et.A];class C extends m.EmbedBlot{attach(){super.attach(),this.attributes=new m.AttributorStore(this.domNode)}delta(){return new v.Ay().insert(this.value(),{...this.formats(),...this.attributes.values()})}format(f,T){const _=this.scroll.query(f,m.Scope.BLOCK_ATTRIBUTE);_!=null&&this.attributes.attribute(_,T)}formatAt(f,T,_,L){this.format(_,L)}insertAt(f,T,_){if(_!=null)return void super.insertAt(f,T,_);const L=T.split(`
`),H=L.pop(),G=L.map((k=>{const N=this.scroll.create(B.blotName);return N.insertAt(0,k),N})),I=this.split(f);G.forEach((k=>{this.parent.insertBefore(k,I)})),H&&this.parent.insertBefore(this.scroll.create("text",H),I)}}function q(R){let f=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},T=!(arguments.length>2&&arguments[2]!==void 0)||arguments[2];return R==null?f:("formats"in R&&typeof R.formats=="function"&&(f={...f,...R.formats()},T&&delete f["code-token"]),R.parent==null||R.parent.statics.blotName==="scroll"||R.parent.statics.scope!==R.statics.scope?f:q(R.parent,f,T))}C.scope=m.Scope.BLOCK_BLOT},36:function(j,U,p){var m=p(3);class v extends m.EmbedBlot{static value(){}optimize(){(this.prev||this.next)&&this.remove()}length(){return 0}value(){return""}}v.blotName="break",v.tagName="BR",U.A=v},580:function(j,U,p){var m=p(3);class v extends m.ContainerBlot{}U.A=v},541:function(j,U,p){var m=p(3),v=p(508);class w extends m.EmbedBlot{static blotName="cursor";static className="ql-cursor";static tagName="span";static CONTENTS="\uFEFF";static value(){}constructor(et,B,C){super(et,B),this.selection=C,this.textNode=document.createTextNode(w.CONTENTS),this.domNode.appendChild(this.textNode),this.savedLength=0}detach(){this.parent!=null&&this.parent.removeChild(this)}format(et,B){if(this.savedLength!==0)return void super.format(et,B);let C=this,q=0;for(;C!=null&&C.statics.scope!==m.Scope.BLOCK_BLOT;)q+=C.offset(C.parent),C=C.parent;C!=null&&(this.savedLength=w.CONTENTS.length,C.optimize(),C.formatAt(q,w.CONTENTS.length,et,B),this.savedLength=0)}index(et,B){return et===this.textNode?0:super.index(et,B)}length(){return this.savedLength}position(){return[this.textNode,this.textNode.data.length]}remove(){super.remove(),this.parent=null}restore(){if(this.selection.composing||this.parent==null)return null;const et=this.selection.getNativeRange();for(;this.domNode.lastChild!=null&&this.domNode.lastChild!==this.textNode;)this.domNode.parentNode.insertBefore(this.domNode.lastChild,this.domNode);const B=this.prev instanceof v.A?this.prev:null,C=B?B.length():0,q=this.next instanceof v.A?this.next:null,R=q?q.text:"",{textNode:f}=this,T=f.data.split(w.CONTENTS).join("");let _;if(f.data=w.CONTENTS,B)_=B,(T||q)&&(B.insertAt(B.length(),T+R),q&&q.remove());else if(q)_=q,q.insertAt(0,T);else{const L=document.createTextNode(T);_=this.scroll.create(L),this.parent.insertBefore(_,this)}if(this.remove(),et){const L=(I,k)=>B&&I===B.domNode?k:I===f?C+k-1:q&&I===q.domNode?C+T.length+k:null,H=L(et.start.node,et.start.offset),G=L(et.end.node,et.end.offset);if(H!==null&&G!==null)return{startNode:_.domNode,startOffset:H,endNode:_.domNode,endOffset:G}}return null}update(et,B){if(et.some((C=>C.type==="characterData"&&C.target===this.textNode))){const C=this.restore();C&&(B.range=C)}}optimize(et){super.optimize(et);let{parent:B}=this;for(;B;){if(B.domNode.tagName==="A"){this.savedLength=w.CONTENTS.length,B.isolate(this.offset(B),this.length()).unwrap(),this.savedLength=0;break}B=B.parent}}value(){return""}}U.A=w},746:function(j,U,p){var m=p(3),v=p(508);const w="\uFEFF";class Y extends m.EmbedBlot{constructor(B,C){super(B,C),this.contentNode=document.createElement("span"),this.contentNode.setAttribute("contenteditable","false"),Array.from(this.domNode.childNodes).forEach((q=>{this.contentNode.appendChild(q)})),this.leftGuard=document.createTextNode(w),this.rightGuard=document.createTextNode(w),this.domNode.appendChild(this.leftGuard),this.domNode.appendChild(this.contentNode),this.domNode.appendChild(this.rightGuard)}index(B,C){return B===this.leftGuard?0:B===this.rightGuard?1:super.index(B,C)}restore(B){let C,q=null;const R=B.data.split(w).join("");if(B===this.leftGuard)if(this.prev instanceof v.A){const f=this.prev.length();this.prev.insertAt(f,R),q={startNode:this.prev.domNode,startOffset:f+R.length}}else C=document.createTextNode(R),this.parent.insertBefore(this.scroll.create(C),this),q={startNode:C,startOffset:R.length};else B===this.rightGuard&&(this.next instanceof v.A?(this.next.insertAt(0,R),q={startNode:this.next.domNode,startOffset:R.length}):(C=document.createTextNode(R),this.parent.insertBefore(this.scroll.create(C),this.next),q={startNode:C,startOffset:R.length}));return B.data=w,q}update(B,C){B.forEach((q=>{if(q.type==="characterData"&&(q.target===this.leftGuard||q.target===this.rightGuard)){const R=this.restore(q.target);R&&(C.range=R)}}))}}U.A=Y},850:function(j,U,p){var m=p(3),v=p(36),w=p(508);class Y extends m.InlineBlot{static allowedChildren=[Y,v.A,m.EmbedBlot,w.A];static order=["cursor","inline","link","underline","strike","italic","bold","script","code"];static compare(B,C){const q=Y.order.indexOf(B),R=Y.order.indexOf(C);return q>=0||R>=0?q-R:B===C?0:B<C?-1:1}formatAt(B,C,q,R){if(Y.compare(this.statics.blotName,q)<0&&this.scroll.query(q,m.Scope.BLOT)){const f=this.isolate(B,C);R&&f.wrap(q,R)}else super.formatAt(B,C,q,R)}optimize(B){if(super.optimize(B),this.parent instanceof Y&&Y.compare(this.statics.blotName,this.parent.statics.blotName)>0){const C=this.parent.isolate(this.offset(),this.length());this.moveChildren(C),C.wrap(this)}}}U.A=Y},508:function(j,U,p){p.d(U,{A:function(){return v},X:function(){return Y}});var m=p(3);class v extends m.TextBlot{}const w={"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"};function Y(et){return et.replace(/[&<>"']/g,(B=>w[B]))}},729:function(j,U,p){p.d(U,{default:function(){return d}});var m=p(543),v=p(698),w=p(36),Y=p(580),et=p(541),B=p(746),C=p(850),q=p(3),R=p(398),f=p(200);function T(e){return e instanceof v.Ay||e instanceof v.zo}function _(e){return typeof e.updateContent=="function"}class L extends q.ScrollBlot{static blotName="scroll";static className="ql-editor";static tagName="DIV";static defaultChild=v.Ay;static allowedChildren=[v.Ay,v.zo,Y.A];constructor(t,s,r){let{emitter:c}=r;super(t,s),this.emitter=c,this.batch=!1,this.optimize(),this.enable(),this.domNode.addEventListener("dragstart",(h=>this.handleDragStart(h)))}batchStart(){Array.isArray(this.batch)||(this.batch=[])}batchEnd(){if(!this.batch)return;const t=this.batch;this.batch=!1,this.update(t)}emitMount(t){this.emitter.emit(f.A.events.SCROLL_BLOT_MOUNT,t)}emitUnmount(t){this.emitter.emit(f.A.events.SCROLL_BLOT_UNMOUNT,t)}emitEmbedUpdate(t,s){this.emitter.emit(f.A.events.SCROLL_EMBED_UPDATE,t,s)}deleteAt(t,s){const[r,c]=this.line(t),[h]=this.line(t+s);if(super.deleteAt(t,s),h!=null&&r!==h&&c>0){if(r instanceof v.zo||h instanceof v.zo)return void this.optimize();const i=h.children.head instanceof w.A?null:h.children.head;r.moveChildren(h,i),r.remove()}this.optimize()}enable(){let t=!(arguments.length>0&&arguments[0]!==void 0)||arguments[0];this.domNode.setAttribute("contenteditable",t?"true":"false")}formatAt(t,s,r,c){super.formatAt(t,s,r,c),this.optimize()}insertAt(t,s,r){if(t>=this.length())if(r==null||this.scroll.query(s,q.Scope.BLOCK)==null){const c=this.scroll.create(this.statics.defaultChild.blotName);this.appendChild(c),r==null&&s.endsWith(`
`)?c.insertAt(0,s.slice(0,-1),r):c.insertAt(0,s,r)}else{const c=this.scroll.create(s,r);this.appendChild(c)}else super.insertAt(t,s,r);this.optimize()}insertBefore(t,s){if(t.statics.scope===q.Scope.INLINE_BLOT){const r=this.scroll.create(this.statics.defaultChild.blotName);r.appendChild(t),super.insertBefore(r,s)}else super.insertBefore(t,s)}insertContents(t,s){const r=this.deltaToRenderBlocks(s.concat(new R.Ay().insert(`
`))),c=r.pop();if(c==null)return;this.batchStart();const h=r.shift();if(h){const l=h.type==="block"&&(h.delta.length()===0||!this.descendant(v.zo,t)[0]&&t<this.length()),o=h.type==="block"?h.delta:new R.Ay().insert({[h.key]:h.value});H(this,t,o);const u=h.type==="block"?1:0,a=t+o.length()+u;l&&this.insertAt(a-1,`
`);const A=(0,v.Ji)(this.line(t)[0]),x=R.xb.diff(A,h.attributes)||{};Object.keys(x).forEach((b=>{this.formatAt(a-1,1,b,x[b])})),t=a}let[i,n]=this.children.find(t);r.length&&(i&&(i=i.split(n),n=0),r.forEach((l=>{if(l.type==="block")H(this.createBlock(l.attributes,i||void 0),0,l.delta);else{const o=this.create(l.key,l.value);this.insertBefore(o,i||void 0),Object.keys(l.attributes).forEach((u=>{o.format(u,l.attributes[u])}))}}))),c.type==="block"&&c.delta.length()&&H(this,i?i.offset(i.scroll)+n:this.length(),c.delta),this.batchEnd(),this.optimize()}isEnabled(){return this.domNode.getAttribute("contenteditable")==="true"}leaf(t){const s=this.path(t).pop();if(!s)return[null,-1];const[r,c]=s;return r instanceof q.LeafBlot?[r,c]:[null,-1]}line(t){return t===this.length()?this.line(t-1):this.descendant(T,t)}lines(){let t=arguments.length>0&&arguments[0]!==void 0?arguments[0]:0,s=arguments.length>1&&arguments[1]!==void 0?arguments[1]:Number.MAX_VALUE;const r=(c,h,i)=>{let n=[],l=i;return c.children.forEachAt(h,i,((o,u,a)=>{T(o)?n.push(o):o instanceof q.ContainerBlot&&(n=n.concat(r(o,u,l))),l-=a})),n};return r(this,t,s)}optimize(){let t=arguments.length>0&&arguments[0]!==void 0?arguments[0]:[],s=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};this.batch||(super.optimize(t,s),t.length>0&&this.emitter.emit(f.A.events.SCROLL_OPTIMIZE,t,s))}path(t){return super.path(t).slice(1)}remove(){}update(t){if(this.batch)return void(Array.isArray(t)&&(this.batch=this.batch.concat(t)));let s=f.A.sources.USER;typeof t=="string"&&(s=t),Array.isArray(t)||(t=this.observer.takeRecords()),(t=t.filter((r=>{let{target:c}=r;const h=this.find(c,!0);return h&&!_(h)}))).length>0&&this.emitter.emit(f.A.events.SCROLL_BEFORE_UPDATE,s,t),super.update(t.concat([])),t.length>0&&this.emitter.emit(f.A.events.SCROLL_UPDATE,s,t)}updateEmbedAt(t,s,r){const[c]=this.descendant((h=>h instanceof v.zo),t);c&&c.statics.blotName===s&&_(c)&&c.updateContent(r)}handleDragStart(t){t.preventDefault()}deltaToRenderBlocks(t){const s=[];let r=new R.Ay;return t.forEach((c=>{const h=c?.insert;if(h)if(typeof h=="string"){const i=h.split(`
`);i.slice(0,-1).forEach((l=>{r.insert(l,c.attributes),s.push({type:"block",delta:r,attributes:c.attributes??{}}),r=new R.Ay}));const n=i[i.length-1];n&&r.insert(n,c.attributes)}else{const i=Object.keys(h)[0];if(!i)return;this.query(i,q.Scope.INLINE)?r.push(c):(r.length()&&s.push({type:"block",delta:r,attributes:{}}),r=new R.Ay,s.push({type:"blockEmbed",key:i,value:h[i],attributes:c.attributes??{}}))}})),r.length()&&s.push({type:"block",delta:r,attributes:{}}),s}createBlock(t,s){let r;const c={};Object.entries(t).forEach((n=>{let[l,o]=n;this.query(l,q.Scope.BLOCK&q.Scope.BLOT)!=null?r=l:c[l]=o}));const h=this.create(r||this.statics.defaultChild.blotName,r?t[r]:void 0);this.insertBefore(h,s||void 0);const i=h.length();return Object.entries(c).forEach((n=>{let[l,o]=n;h.formatAt(0,i,l,o)})),h}}function H(e,t,s){s.reduce(((r,c)=>{const h=R.Op.length(c);let i=c.attributes||{};if(c.insert!=null){if(typeof c.insert=="string"){const n=c.insert;e.insertAt(r,n);const[l]=e.descendant(q.LeafBlot,r),o=(0,v.Ji)(l);i=R.xb.diff(o,i)||{}}else if(typeof c.insert=="object"){const n=Object.keys(c.insert)[0];if(n==null)return r;if(e.insertAt(r,n,c.insert[n]),e.scroll.query(n,q.Scope.INLINE)!=null){const[l]=e.descendant(q.LeafBlot,r),o=(0,v.Ji)(l);i=R.xb.diff(o,i)||{}}}}return Object.keys(i).forEach((n=>{e.formatAt(r,h,n,i[n])})),r+h}),t)}var G=L,I=p(508),k=p(584),N=p(266);class F extends N.A{static DEFAULTS={delay:1e3,maxStack:100,userOnly:!1};lastRecorded=0;ignoreChange=!1;stack={undo:[],redo:[]};currentRange=null;constructor(t,s){super(t,s),this.quill.on(m.Ay.events.EDITOR_CHANGE,((r,c,h,i)=>{r===m.Ay.events.SELECTION_CHANGE?c&&i!==m.Ay.sources.SILENT&&(this.currentRange=c):r===m.Ay.events.TEXT_CHANGE&&(this.ignoreChange||(this.options.userOnly&&i!==m.Ay.sources.USER?this.transform(c):this.record(c,h)),this.currentRange=K(this.currentRange,c))})),this.quill.keyboard.addBinding({key:"z",shortKey:!0},this.undo.bind(this)),this.quill.keyboard.addBinding({key:["z","Z"],shortKey:!0,shiftKey:!0},this.redo.bind(this)),/Win/i.test(navigator.platform)&&this.quill.keyboard.addBinding({key:"y",shortKey:!0},this.redo.bind(this)),this.quill.root.addEventListener("beforeinput",(r=>{r.inputType==="historyUndo"?(this.undo(),r.preventDefault()):r.inputType==="historyRedo"&&(this.redo(),r.preventDefault())}))}change(t,s){if(this.stack[t].length===0)return;const r=this.stack[t].pop();if(!r)return;const c=this.quill.getContents(),h=r.delta.invert(c);this.stack[s].push({delta:h,range:K(r.range,h)}),this.lastRecorded=0,this.ignoreChange=!0,this.quill.updateContents(r.delta,m.Ay.sources.USER),this.ignoreChange=!1,this.restoreSelection(r)}clear(){this.stack={undo:[],redo:[]}}cutoff(){this.lastRecorded=0}record(t,s){if(t.ops.length===0)return;this.stack.redo=[];let r=t.invert(s),c=this.currentRange;const h=Date.now();if(this.lastRecorded+this.options.delay>h&&this.stack.undo.length>0){const i=this.stack.undo.pop();i&&(r=r.compose(i.delta),c=i.range)}else this.lastRecorded=h;r.length()!==0&&(this.stack.undo.push({delta:r,range:c}),this.stack.undo.length>this.options.maxStack&&this.stack.undo.shift())}redo(){this.change("redo","undo")}transform(t){z(this.stack.undo,t),z(this.stack.redo,t)}undo(){this.change("undo","redo")}restoreSelection(t){if(t.range)this.quill.setSelection(t.range,m.Ay.sources.USER);else{const s=(function(r,c){const h=c.reduce(((n,l)=>n+(l.delete||0)),0);let i=c.length()-h;return(function(n,l){const o=l.ops[l.ops.length-1];return o!=null&&(o.insert!=null?typeof o.insert=="string"&&o.insert.endsWith(`
`):o.attributes!=null&&Object.keys(o.attributes).some((u=>n.query(u,q.Scope.BLOCK)!=null)))})(r,c)&&(i-=1),i})(this.quill.scroll,t.delta);this.quill.setSelection(s,m.Ay.sources.USER)}}}function z(e,t){let s=t;for(let r=e.length-1;r>=0;r-=1){const c=e[r];e[r]={delta:s.transform(c.delta,!0),range:c.range&&K(c.range,s)},s=c.delta.transform(s),e[r].delta.length()===0&&e.splice(r,1)}}function K(e,t){if(!e)return e;const s=t.transformPosition(e.index);return{index:s,length:t.transformPosition(e.index+e.length)-s}}var nt=p(123);class M extends N.A{constructor(t,s){super(t,s),t.root.addEventListener("drop",(r=>{r.preventDefault();let c=null;if(document.caretRangeFromPoint)c=document.caretRangeFromPoint(r.clientX,r.clientY);else if(document.caretPositionFromPoint){const i=document.caretPositionFromPoint(r.clientX,r.clientY);c=document.createRange(),c.setStart(i.offsetNode,i.offset),c.setEnd(i.offsetNode,i.offset)}const h=c&&t.selection.normalizeNative(c);if(h){const i=t.selection.normalizedToRange(h);r.dataTransfer?.files&&this.upload(i,r.dataTransfer.files)}}))}upload(t,s){const r=[];Array.from(s).forEach((c=>{c&&this.options.mimetypes?.includes(c.type)&&r.push(c)})),r.length>0&&this.options.handler.call(this,t,r)}}M.DEFAULTS={mimetypes:["image/png","image/jpeg"],handler(e,t){if(!this.quill.scroll.query("image"))return;const s=t.map((r=>new Promise((c=>{const h=new FileReader;h.onload=()=>{c(h.result)},h.readAsDataURL(r)}))));Promise.all(s).then((r=>{const c=r.reduce(((h,i)=>h.insert({image:i})),new R.Ay().retain(e.index).delete(e.length));this.quill.updateContents(c,f.A.sources.USER),this.quill.setSelection(e.index+r.length,f.A.sources.SILENT)}))}};var g=M;const y=["insertText","insertReplacementText"];class S extends N.A{constructor(t,s){super(t,s),t.root.addEventListener("beforeinput",(r=>{this.handleBeforeInput(r)})),/Android/i.test(navigator.userAgent)||t.on(m.Ay.events.COMPOSITION_BEFORE_START,(()=>{this.handleCompositionStart()}))}deleteRange(t){(0,nt.Xo)({range:t,quill:this.quill})}replaceText(t){let s=arguments.length>1&&arguments[1]!==void 0?arguments[1]:"";if(t.length===0)return!1;if(s){const r=this.quill.getFormat(t.index,1);this.deleteRange(t),this.quill.updateContents(new R.Ay().retain(t.index).insert(s,r),m.Ay.sources.USER)}else this.deleteRange(t);return this.quill.setSelection(t.index+s.length,0,m.Ay.sources.SILENT),!0}handleBeforeInput(t){if(this.quill.composition.isComposing||t.defaultPrevented||!y.includes(t.inputType))return;const s=t.getTargetRanges?t.getTargetRanges()[0]:null;if(!s||s.collapsed===!0)return;const r=(function(i){return typeof i.data=="string"?i.data:i.dataTransfer?.types.includes("text/plain")?i.dataTransfer.getData("text/plain"):null})(t);if(r==null)return;const c=this.quill.selection.normalizeNative(s),h=c?this.quill.selection.normalizedToRange(c):null;h&&this.replaceText(h,r)&&t.preventDefault()}handleCompositionStart(){const t=this.quill.getSelection();t&&this.replaceText(t)}}var O=S;const tt=/Mac/i.test(navigator.platform);class P extends N.A{isListening=!1;selectionChangeDeadline=0;constructor(t,s){super(t,s),this.handleArrowKeys(),this.handleNavigationShortcuts()}handleArrowKeys(){this.quill.keyboard.addBinding({key:["ArrowLeft","ArrowRight"],offset:0,shiftKey:null,handler(t,s){let{line:r,event:c}=s;if(!(r instanceof q.ParentBlot&&r.uiNode))return!0;const h=getComputedStyle(r.domNode).direction==="rtl";return!!(h&&c.key!=="ArrowRight"||!h&&c.key!=="ArrowLeft")||(this.quill.setSelection(t.index-1,t.length+(c.shiftKey?1:0),m.Ay.sources.USER),!1)}})}handleNavigationShortcuts(){this.quill.root.addEventListener("keydown",(t=>{!t.defaultPrevented&&(s=>s.key==="ArrowLeft"||s.key==="ArrowRight"||s.key==="ArrowUp"||s.key==="ArrowDown"||s.key==="Home"||!(!tt||s.key!=="a"||s.ctrlKey!==!0))(t)&&this.ensureListeningToSelectionChange()}))}ensureListeningToSelectionChange(){this.selectionChangeDeadline=Date.now()+100,this.isListening||(this.isListening=!0,document.addEventListener("selectionchange",(()=>{this.isListening=!1,Date.now()<=this.selectionChangeDeadline&&this.handleSelectionChange()}),{once:!0}))}handleSelectionChange(){const t=document.getSelection();if(!t)return;const s=t.getRangeAt(0);if(s.collapsed!==!0||s.startOffset!==0)return;const r=this.quill.scroll.find(s.startContainer);if(!(r instanceof q.ParentBlot&&r.uiNode))return;const c=document.createRange();c.setStartAfter(r.uiNode),c.setEndAfter(r.uiNode),t.removeAllRanges(),t.addRange(c)}}var V=P;m.Ay.register({"blots/block":v.Ay,"blots/block/embed":v.zo,"blots/break":w.A,"blots/container":Y.A,"blots/cursor":et.A,"blots/embed":B.A,"blots/inline":C.A,"blots/scroll":G,"blots/text":I.A,"modules/clipboard":k.Ay,"modules/history":F,"modules/keyboard":nt.Ay,"modules/uploader":g,"modules/input":O,"modules/uiNode":V});var d=m.Ay},200:function(j,U,p){p.d(U,{A:function(){return et}});class m{listener;context;once;constructor(C,q,R=!1){this.listener=C,this.context=q,this.once=R}}class v{static prefixed=!1;_events=Object.create(null);_eventsCount=0;#t(C,q,R,f){if(typeof q!="function")throw new TypeError("The listener must be a function");const T=new m(q,R||this,f),_=this._events[C];return Array.isArray(_)?_.push(T):_?this._events[C]=[_,T]:(this._events[C]=T,this._eventsCount++),this}clearEvent(C){--this._eventsCount==0?this._events=Object.create(null):delete this._events[C]}eventNames(){return this._eventsCount===0?[]:Reflect.ownKeys(this._events)}listeners(C){const q=this._events[C];return q?Array.isArray(q)?q.map((R=>R.listener)):[q.listener]:[]}listenerCount(C){const q=this._events[C];return q?Array.isArray(q)?q.length:1:0}emit(C,...q){const R=this._events[C];return!!R&&(Array.isArray(R)?R.slice(0).forEach((f=>{f.once&&this.removeListener(C,f.listener,void 0,!0),f.listener.call(f.context,...q)})):(R.once&&this.removeListener(C,R.listener,void 0,!0),R.listener.call(R.context,...q)),!0)}on(C,q,R){return this.#t(C,q,R,!1)}once(C,q,R){return this.#t(C,q,R,!0)}removeListener(C,q,R,f){const T=this._events[C];if(!T)return this;if(!q)return this.clearEvent(C),this;if(Array.isArray(T)){const _=[];T.forEach((L=>{(L.listener!==q||f&&!L.once||R&&L.context!==R)&&_.push(L)})),_.length?this._events[C]=_.length===1?_[0]:_:this.clearEvent(C)}else T.listener!==q||f&&!T.once||R&&T.context!==R||this.clearEvent(C);return this}removeAllListeners(C){return C?this._events[C]&&this.clearEvent(C):(this._events=Object.create(null),this._eventsCount=0),this}off(C,q,R,f){return this.removeListener(C,q,R,f)}addListener(C,q,R){return this.on(C,q,R)}}const w=(0,p(78).A)("quill:events"),Y=[];["selectionchange","mousedown","mouseup","click"].forEach((B=>{document.addEventListener(B,(function(){for(var C=arguments.length,q=new Array(C),R=0;R<C;R++)q[R]=arguments[R];Y.forEach((f=>{f.handleDOM(...q)}))}))}));var et=class extends v{static events={EDITOR_CHANGE:"editor-change",SCROLL_BEFORE_UPDATE:"scroll-before-update",SCROLL_BLOT_MOUNT:"scroll-blot-mount",SCROLL_BLOT_UNMOUNT:"scroll-blot-unmount",SCROLL_OPTIMIZE:"scroll-optimize",SCROLL_UPDATE:"scroll-update",SCROLL_EMBED_UPDATE:"scroll-embed-update",SELECTION_CHANGE:"selection-change",TEXT_CHANGE:"text-change",COMPOSITION_BEFORE_START:"composition-before-start",COMPOSITION_START:"composition-start",COMPOSITION_BEFORE_END:"composition-before-end",COMPOSITION_END:"composition-end"};static sources={API:"api",SILENT:"silent",USER:"user"};constructor(){super(),this.domListeners={},this.on("error",w.error)}connect(){Y.push(this)}disconnect(){Y.splice(Y.indexOf(this),1)}emit(){for(var B=arguments.length,C=new Array(B),q=0;q<B;q++)C[q]=arguments[q];return w.log.call(w,...C),super.emit(...C)}handleDOM(B){for(var C=arguments.length,q=new Array(C>1?C-1:0),R=1;R<C;R++)q[R-1]=arguments[R];const f=B.composedPath()[0];(this.domListeners[B.type]||[]).forEach((T=>{let{node:_,handler:L}=T;(f===_||((H,G)=>{if(G.getRootNode()===document)return H.contains(G);for(;!H.contains(G);){const I=G.getRootNode();if(!I)return!1;const k=I.host;if(!k)return!1;G=k}return!0})(_,f))&&L(B,...q)}))}listenDOM(B,C,q){this.domListeners[B]||(this.domListeners[B]=[]),this.domListeners[B].push({node:C,handler:q})}}},78:function(j,U){const p=["error","warn","log","info"];let m="warn";function v(Y){if(m&&p.indexOf(Y)<=p.indexOf(m)){for(var et=arguments.length,B=new Array(et>1?et-1:0),C=1;C<et;C++)B[C-1]=arguments[C];console[Y](...B)}}function w(Y){return p.reduce(((et,B)=>(et[B]=v.bind(console,B,Y),et)),{})}w.level=Y=>{m=Y},v.level=w.level,U.A=w},266:function(j,U){U.A=class{static DEFAULTS={};constructor(p){let m=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};this.quill=p,this.options=m}}},543:function(j,U,p){p.d(U,{Ay:function(){return d}});var m=p(3),v=p(398),w=p(698),Y=p(36),et=p(541),B=p(508),C=p(298),q=p(857),R=p(697);const f=/^[ -~]*$/;function T(i,n,l){if(i.length===0){const[rt]=H(l.pop());return n<=0?`</li></${rt}>`:`</li></${rt}>${T([],n-1,l)}`}const[{child:o,offset:u,length:a,indent:A,type:x},...b]=i,[$,X]=H(x);if(A>n)return l.push(x),A===n+1?`<${$}><li${X}>${_(o,u,a)}${T(b,A,l)}`:`<${$}><li>${T(i,n+1,l)}`;const W=l[l.length-1];if(A===n&&x===W)return`</li><li${X}>${_(o,u,a)}${T(b,A,l)}`;const[J]=H(l.pop());return`</li></${J}>${T(i,n-1,l)}`}function _(i,n,l){let o=arguments.length>3&&arguments[3]!==void 0&&arguments[3];if("html"in i&&typeof i.html=="function")return i.html(n,l);if(i instanceof B.A)return(0,B.X)(i.value().slice(n,n+l)).replaceAll(/  +/g,(u=>"&nbsp;".repeat(u.length-1)+" "));if(i instanceof m.ParentBlot){if(i.statics.blotName==="list-container"){const $=[];return i.children.forEachAt(n,l,((X,W,J)=>{const rt="formats"in X&&typeof X.formats=="function"?X.formats():{};$.push({child:X,offset:W,length:J,indent:rt.indent||0,type:rt.list})})),T($,-1,[])}const u=[];if(i.children.forEachAt(n,l,(($,X,W)=>{u.push(_($,X,W))})),o||i.statics.blotName==="list")return u.join("");const{outerHTML:a,innerHTML:A}=i.domNode,[x,b]=a.split(`>${A}<`);return x==="<table"?`<table style="border: 1px solid #000;">${u.join("")}<${b}`:`${x}>${u.join("")}<${b}`}return i.domNode instanceof Element?i.domNode.outerHTML:""}function L(i,n){return Object.keys(n).reduce(((l,o)=>{if(i[o]==null)return l;const u=n[o];return u===i[o]?l[o]=u:Array.isArray(u)?u.indexOf(i[o])<0?l[o]=u.concat([i[o]]):l[o]=u:l[o]=[u,i[o]],l}),{})}function H(i){const n=i==="ordered"?"ol":"ul";switch(i){case"checked":return[n,' data-list="checked"'];case"unchecked":return[n,' data-list="unchecked"'];default:return[n,""]}}function G(i){return i.reduce(((n,l)=>{if(typeof l.insert=="string"){const o=l.insert.replace(/\r\n/g,`
`).replace(/\r/g,`
`);return n.insert(o,l.attributes)}return n.push(l)}),new v.Ay)}function I(i,n){let{index:l,length:o}=i;return new C.Q(l+n,o)}var k=class{constructor(i){this.scroll=i,this.delta=this.getDelta()}applyDelta(i){this.scroll.update();let n=this.scroll.length();this.scroll.batchStart();const l=G(i),o=new v.Ay;return(function(u){const a=[];return u.forEach((A=>{typeof A.insert=="string"?A.insert.split(`
`).forEach(((x,b)=>{b&&a.push({insert:`
`,attributes:A.attributes}),x&&a.push({insert:x,attributes:A.attributes})})):a.push(A)})),a})(l.ops.slice()).reduce(((u,a)=>{const A=v.Op.length(a);let x=a.attributes||{},b=!1,$=!1;if(a.insert!=null){if(o.retain(A),typeof a.insert=="string"){const J=a.insert;$=!J.endsWith(`
`)&&(n<=u||!!this.scroll.descendant(w.zo,u)[0]),this.scroll.insertAt(u,J);const[rt,lt]=this.scroll.line(u);let Z=Object.assign({},(0,w.Ji)(rt));if(rt instanceof w.Ay){const[it]=rt.descendant(m.LeafBlot,lt);it&&(Z=Object.assign(Z,(0,w.Ji)(it)))}x=v.xb.diff(Z,x)||{}}else if(typeof a.insert=="object"){const J=Object.keys(a.insert)[0];if(J==null)return u;const rt=this.scroll.query(J,m.Scope.INLINE)!=null;if(rt)(n<=u||this.scroll.descendant(w.zo,u)[0])&&($=!0);else if(u>0){const[lt,Z]=this.scroll.descendant(m.LeafBlot,u-1);lt instanceof B.A?lt.value()[Z]!==`
`&&(b=!0):lt instanceof m.EmbedBlot&&lt.statics.scope===m.Scope.INLINE_BLOT&&(b=!0)}if(this.scroll.insertAt(u,J,a.insert[J]),rt){const[lt]=this.scroll.descendant(m.LeafBlot,u);if(lt){const Z=Object.assign({},(0,w.Ji)(lt));x=v.xb.diff(Z,x)||{}}}}n+=A}else if(o.push(a),a.retain!==null&&typeof a.retain=="object"){const J=Object.keys(a.retain)[0];if(J==null)return u;this.scroll.updateEmbedAt(u,J,a.retain[J])}Object.keys(x).forEach((J=>{this.scroll.formatAt(u,A,J,x[J])}));const X=b?1:0,W=$?1:0;return n+=X+W,o.retain(X),o.delete(W),u+A+X+W}),0),o.reduce(((u,a)=>typeof a.delete=="number"?(this.scroll.deleteAt(u,a.delete),u):u+v.Op.length(a)),0),this.scroll.batchEnd(),this.scroll.optimize(),this.update(l)}deleteText(i,n){return this.scroll.deleteAt(i,n),this.update(new v.Ay().retain(i).delete(n))}formatLine(i,n){let l=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{};this.scroll.update(),Object.keys(l).forEach((u=>{this.scroll.lines(i,Math.max(n,1)).forEach((a=>{a.format(u,l[u])}))})),this.scroll.optimize();const o=new v.Ay().retain(i).retain(n,(0,q.A)(l));return this.update(o)}formatText(i,n){let l=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{};Object.keys(l).forEach((u=>{this.scroll.formatAt(i,n,u,l[u])}));const o=new v.Ay().retain(i).retain(n,(0,q.A)(l));return this.update(o)}getContents(i,n){return this.delta.slice(i,i+n)}getDelta(){return this.scroll.lines().reduce(((i,n)=>i.concat(n.delta())),new v.Ay)}getFormat(i){let n=arguments.length>1&&arguments[1]!==void 0?arguments[1]:0,l=[],o=[];n===0?this.scroll.path(i).forEach((A=>{const[x]=A;x instanceof w.Ay?l.push(x):x instanceof m.LeafBlot&&o.push(x)})):(l=this.scroll.lines(i,n),o=this.scroll.descendants(m.LeafBlot,i,n));const[u,a]=[l,o].map((A=>{const x=A.shift();if(x==null)return{};let b=(0,w.Ji)(x);for(;Object.keys(b).length>0;){const $=A.shift();if($==null)return b;b=L((0,w.Ji)($),b)}return b}));return{...u,...a}}getHTML(i,n){const[l,o]=this.scroll.line(i);if(l){const u=l.length();return l.length()>=o+n&&(o!==0||n!==u)?_(l,o,n,!0):_(this.scroll,i,n,!0)}return""}getText(i,n){return this.getContents(i,n).filter((l=>typeof l.insert=="string")).map((l=>l.insert)).join("")}insertContents(i,n){const l=G(n),o=new v.Ay().retain(i).concat(l);return this.scroll.insertContents(i,l),this.update(o)}insertEmbed(i,n,l){return this.scroll.insertAt(i,n,l),this.update(new v.Ay().retain(i).insert({[n]:l}))}insertText(i,n){let l=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{};return n=n.replace(/\r\n/g,`
`).replace(/\r/g,`
`),this.scroll.insertAt(i,n),Object.keys(l).forEach((o=>{this.scroll.formatAt(i,n.length,o,l[o])})),this.update(new v.Ay().retain(i).insert(n,(0,q.A)(l)))}isBlank(){if(this.scroll.children.length===0)return!0;if(this.scroll.children.length>1)return!1;const i=this.scroll.children.head;if(i?.statics.blotName!==w.Ay.blotName)return!1;const n=i;return!(n.children.length>1)&&n.children.head instanceof Y.A}removeFormat(i,n){const l=this.getText(i,n),[o,u]=this.scroll.line(i+n);let a=0,A=new v.Ay;o!=null&&(a=o.length()-u,A=o.delta().slice(u,u+a-1).insert(`
`));const x=this.getContents(i,n+a).diff(new v.Ay().insert(l).concat(A)),b=new v.Ay().retain(i).concat(x);return this.applyDelta(b)}update(i){let n=arguments.length>1&&arguments[1]!==void 0?arguments[1]:[],l=arguments.length>2&&arguments[2]!==void 0?arguments[2]:void 0;const o=this.delta;if(n.length===1&&n[0].type==="characterData"&&n[0].target.data.match(f)&&this.scroll.find(n[0].target)){const u=this.scroll.find(n[0].target),a=(0,w.Ji)(u),A=u.offset(this.scroll),x=n[0].oldValue.replace(et.A.CONTENTS,""),b=new v.Ay().insert(x),$=new v.Ay().insert(u.value()),X=l&&{oldRange:I(l.oldRange,-A),newRange:I(l.newRange,-A)};i=new v.Ay().retain(A).concat(b.diff($,X)).reduce(((W,J)=>J.insert?W.insert(J.insert,a):W.push(J)),new v.Ay),this.delta=o.compose(i)}else this.delta=this.getDelta(),i&&(0,R.A)(o.compose(i),this.delta)||(i=o.diff(this.delta,l));return i}},N=p(200),F=new WeakMap,z=p(78),K=p(266),nt=p(746),M=class{isComposing=!1;constructor(i,n){this.scroll=i,this.emitter=n,this.setupListeners()}setupListeners(){this.scroll.domNode.addEventListener("compositionstart",(i=>{this.isComposing||this.handleCompositionStart(i)})),this.scroll.domNode.addEventListener("compositionend",(i=>{this.isComposing&&queueMicrotask((()=>{this.handleCompositionEnd(i)}))}))}handleCompositionStart(i){const n=i.target instanceof Node?this.scroll.find(i.target,!0):null;!n||n instanceof nt.A||(this.emitter.emit(N.A.events.COMPOSITION_BEFORE_START,i),this.scroll.batchStart(),this.emitter.emit(N.A.events.COMPOSITION_START,i),this.isComposing=!0)}handleCompositionEnd(i){this.emitter.emit(N.A.events.COMPOSITION_BEFORE_END,i),this.scroll.batchEnd(),this.emitter.emit(N.A.events.COMPOSITION_END,i),this.isComposing=!1}},g=p(609);const y=i=>{const n=i.getBoundingClientRect(),l="offsetWidth"in i&&Math.abs(n.width)/i.offsetWidth||1,o="offsetHeight"in i&&Math.abs(n.height)/i.offsetHeight||1;return{top:n.top,right:n.left+i.clientWidth*l,bottom:n.top+i.clientHeight*o,left:n.left}},S=i=>{const n=parseInt(i,10);return Number.isNaN(n)?0:n},O=(i,n,l,o,u,a)=>i<l&&n>o?0:i<l?-(l-i+u):n>o?n-i>o-l?i+u-l:n-o+a:0,tt=["block","break","cursor","inline","scroll","text"],P=(0,z.A)("quill"),V=new m.Registry;m.ParentBlot.uiClass="ql-ui";class d{static DEFAULTS={bounds:null,modules:{clipboard:!0,keyboard:!0,history:!0,uploader:!0},placeholder:"",readOnly:!1,registry:V,theme:"default"};static events=N.A.events;static sources=N.A.sources;static version="2.0.3";static imports={delta:v.Ay,parchment:m,"core/module":K.A,"core/theme":g.A};static debug(n){n===!0&&(n="log"),z.A.level(n)}static find(n){let l=arguments.length>1&&arguments[1]!==void 0&&arguments[1];return F.get(n)||V.find(n,l)}static import(n){return this.imports[n]==null&&P.error(`Cannot import ${n}. Are you sure it was registered?`),this.imports[n]}static register(){if(typeof(arguments.length<=0?void 0:arguments[0])!="string"){const n=arguments.length<=0?void 0:arguments[0],l=!!(!(arguments.length<=1)&&arguments[1]),o="attrName"in n?n.attrName:n.blotName;typeof o=="string"?this.register(`formats/${o}`,n,l):Object.keys(n).forEach((u=>{this.register(u,n[u],l)}))}else{const n=arguments.length<=0?void 0:arguments[0],l=arguments.length<=1?void 0:arguments[1],o=!!(!(arguments.length<=2)&&arguments[2]);this.imports[n]==null||o||P.warn(`Overwriting ${n} with`,l),this.imports[n]=l,(n.startsWith("blots/")||n.startsWith("formats/"))&&l&&typeof l!="boolean"&&l.blotName!=="abstract"&&V.register(l),typeof l.register=="function"&&l.register(V)}}constructor(n){let l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};if(this.options=(function(A,x){const b=e(A);if(!b)throw new Error("Invalid Quill container");const $=!x.theme||x.theme===d.DEFAULTS.theme?g.A:d.import(`themes/${x.theme}`);if(!$)throw new Error(`Invalid theme ${x.theme}. Did you register it?`);const{modules:X,...W}=d.DEFAULTS,{modules:J,...rt}=$.DEFAULTS;let lt=t(x.modules);lt!=null&&lt.toolbar&&lt.toolbar.constructor!==Object&&(lt={...lt,toolbar:{container:lt.toolbar}});const Z={...t(X),...t(J),...lt},it={...W,...s(rt),...s(x)};let gt=x.registry;return gt?x.formats&&P.warn('Ignoring "formats" option because "registry" is specified'):gt=x.formats?((ht,mt,st)=>{const pt=new m.Registry;return tt.forEach((At=>{const vt=mt.query(At);vt&&pt.register(vt)})),ht.forEach((At=>{let vt=mt.query(At);vt||st.error(`Cannot register "${At}" specified in "formats" config. Are you sure it was registered?`);let xt=0;for(;vt;)if(pt.register(vt),vt="blotName"in vt?vt.requiredContainer??null:null,xt+=1,xt>100){st.error(`Cycle detected in registering blot requiredContainer: "${At}"`);break}})),pt})(x.formats,it.registry,P):it.registry,{...it,registry:gt,container:b,theme:$,modules:Object.entries(Z).reduce(((ht,mt)=>{let[st,pt]=mt;if(!pt)return ht;const At=d.import(`modules/${st}`);return At==null?(P.error(`Cannot load ${st} module. Are you sure you registered it?`),ht):{...ht,[st]:{...At.DEFAULTS||{},...pt}}}),{}),bounds:e(it.bounds)}})(n,l),this.container=this.options.container,this.container==null)return void P.error("Invalid Quill container",n);this.options.debug&&d.debug(this.options.debug);const o=this.container.innerHTML.trim();this.container.classList.add("ql-container"),this.container.innerHTML="",F.set(this.container,this),this.root=this.addContainer("ql-editor"),this.root.classList.add("ql-blank"),this.emitter=new N.A;const u=m.ScrollBlot.blotName,a=this.options.registry.query(u);if(!a||!("blotName"in a))throw new Error(`Cannot initialize Quill without "${u}" blot`);if(this.scroll=new a(this.options.registry,this.root,{emitter:this.emitter}),this.editor=new k(this.scroll),this.selection=new C.A(this.scroll,this.emitter),this.composition=new M(this.scroll,this.emitter),this.theme=new this.options.theme(this,this.options),this.keyboard=this.theme.addModule("keyboard"),this.clipboard=this.theme.addModule("clipboard"),this.history=this.theme.addModule("history"),this.uploader=this.theme.addModule("uploader"),this.theme.addModule("input"),this.theme.addModule("uiNode"),this.theme.init(),this.emitter.on(N.A.events.EDITOR_CHANGE,(A=>{A===N.A.events.TEXT_CHANGE&&this.root.classList.toggle("ql-blank",this.editor.isBlank())})),this.emitter.on(N.A.events.SCROLL_UPDATE,((A,x)=>{const b=this.selection.lastRange,[$]=this.selection.getRange(),X=b&&$?{oldRange:b,newRange:$}:void 0;r.call(this,(()=>this.editor.update(null,x,X)),A)})),this.emitter.on(N.A.events.SCROLL_EMBED_UPDATE,((A,x)=>{const b=this.selection.lastRange,[$]=this.selection.getRange(),X=b&&$?{oldRange:b,newRange:$}:void 0;r.call(this,(()=>{const W=new v.Ay().retain(A.offset(this)).retain({[A.statics.blotName]:x});return this.editor.update(W,[],X)}),d.sources.USER)})),o){const A=this.clipboard.convert({html:`${o}<p><br></p>`,text:`
`});this.setContents(A)}this.history.clear(),this.options.placeholder&&this.root.setAttribute("data-placeholder",this.options.placeholder),this.options.readOnly&&this.disable(),this.allowReadOnlyEdits=!1}addContainer(n){let l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:null;if(typeof n=="string"){const o=n;(n=document.createElement("div")).classList.add(o)}return this.container.insertBefore(n,l),n}blur(){this.selection.setRange(null)}deleteText(n,l,o){return[n,l,,o]=c(n,l,o),r.call(this,(()=>this.editor.deleteText(n,l)),o,n,-1*l)}disable(){this.enable(!1)}editReadOnly(n){this.allowReadOnlyEdits=!0;const l=n();return this.allowReadOnlyEdits=!1,l}enable(){let n=!(arguments.length>0&&arguments[0]!==void 0)||arguments[0];this.scroll.enable(n),this.container.classList.toggle("ql-disabled",!n)}focus(){let n=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{};this.selection.focus(),n.preventScroll||this.scrollSelectionIntoView()}format(n,l){let o=arguments.length>2&&arguments[2]!==void 0?arguments[2]:N.A.sources.API;return r.call(this,(()=>{if(!this.hasFocus()){this.root.focus({preventScroll:!0});const A=this.selection.rangeToNative(this.selection.savedRange);this.selection.setNativeRange(...A)}const[u]=this.selection.getRange();let a=new v.Ay;if(u==null)return a;if(this.scroll.query(n,m.Scope.BLOCK))a=this.editor.formatLine(u.index,u.length,{[n]:l});else{if(u.length===0)return this.selection.format(n,l),a;a=this.editor.formatText(u.index,u.length,{[n]:l})}return this.setSelection(u,N.A.sources.SILENT),a}),o)}formatLine(n,l,o,u,a){let A;return[n,l,A,a]=c(n,l,o,u,a),r.call(this,(()=>this.editor.formatLine(n,l,A)),a,n,0)}formatText(n,l,o,u,a){let A;return[n,l,A,a]=c(n,l,o,u,a),r.call(this,(()=>this.editor.formatText(n,l,A)),a,n,0)}getBounds(n){let l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:0,o=null;if(o=typeof n=="number"?this.selection.getBounds(n,l):this.selection.getBounds(n.index,n.length),!o)return null;const u=this.container.getBoundingClientRect();return{bottom:o.bottom-u.top,height:o.height,left:o.left-u.left,right:o.right-u.left,top:o.top-u.top,width:o.width}}getContents(){let n=arguments.length>0&&arguments[0]!==void 0?arguments[0]:0,l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:this.getLength()-n;return[n,l]=c(n,l),this.editor.getContents(n,l)}getFormat(){let n=arguments.length>0&&arguments[0]!==void 0?arguments[0]:this.getSelection(!0),l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:0;return typeof n=="number"?this.editor.getFormat(n,l):this.editor.getFormat(n.index,n.length)}getIndex(n){return n.offset(this.scroll)}getLength(){return this.scroll.length()}getLeaf(n){return this.scroll.leaf(n)}getLine(n){return this.scroll.line(n)}getLines(){let n=arguments.length>0&&arguments[0]!==void 0?arguments[0]:0,l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:Number.MAX_VALUE;return typeof n!="number"?this.scroll.lines(n.index,n.length):this.scroll.lines(n,l)}getModule(n){return this.theme.modules[n]}getSelection(){return arguments.length>0&&arguments[0]!==void 0&&arguments[0]&&this.focus(),this.update(),this.selection.getRange()[0]}getSemanticHTML(){let n=arguments.length>0&&arguments[0]!==void 0?arguments[0]:0,l=arguments.length>1?arguments[1]:void 0;return typeof n=="number"&&(l=l??this.getLength()-n),[n,l]=c(n,l),this.editor.getHTML(n,l)}getText(){let n=arguments.length>0&&arguments[0]!==void 0?arguments[0]:0,l=arguments.length>1?arguments[1]:void 0;return typeof n=="number"&&(l=l??this.getLength()-n),[n,l]=c(n,l),this.editor.getText(n,l)}hasFocus(){return this.selection.hasFocus()}insertEmbed(n,l,o){let u=arguments.length>3&&arguments[3]!==void 0?arguments[3]:d.sources.API;return r.call(this,(()=>this.editor.insertEmbed(n,l,o)),u,n)}insertText(n,l,o,u,a){let A;return[n,,A,a]=c(n,0,o,u,a),r.call(this,(()=>this.editor.insertText(n,l,A)),a,n,l.length)}isEnabled(){return this.scroll.isEnabled()}off(){return this.emitter.off(...arguments)}on(){return this.emitter.on(...arguments)}once(){return this.emitter.once(...arguments)}removeFormat(n,l,o){return[n,l,,o]=c(n,l,o),r.call(this,(()=>this.editor.removeFormat(n,l)),o,n)}scrollRectIntoView(n){((l,o)=>{const u=l.ownerDocument;let a=o,A=l;for(;A;){const b=A===u.body,$=b?{top:0,right:window.visualViewport?.width??u.documentElement.clientWidth,bottom:window.visualViewport?.height??u.documentElement.clientHeight,left:0}:y(A),X=getComputedStyle(A),W=O(a.left,a.right,$.left,$.right,S(X.scrollPaddingLeft),S(X.scrollPaddingRight)),J=O(a.top,a.bottom,$.top,$.bottom,S(X.scrollPaddingTop),S(X.scrollPaddingBottom));if(W||J)if(b)u.defaultView?.scrollBy(W,J);else{const{scrollLeft:rt,scrollTop:lt}=A;J&&(A.scrollTop+=J),W&&(A.scrollLeft+=W);const Z=A.scrollLeft-rt,it=A.scrollTop-lt;a={left:a.left-Z,top:a.top-it,right:a.right-Z,bottom:a.bottom-it}}A=b||X.position==="fixed"?null:(x=A).parentElement||x.getRootNode().host||null}var x})(this.root,n)}scrollIntoView(){console.warn("Quill#scrollIntoView() has been deprecated and will be removed in the near future. Please use Quill#scrollSelectionIntoView() instead."),this.scrollSelectionIntoView()}scrollSelectionIntoView(){const n=this.selection.lastRange,l=n&&this.selection.getBounds(n.index,n.length);l&&this.scrollRectIntoView(l)}setContents(n){let l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:N.A.sources.API;return r.call(this,(()=>{n=new v.Ay(n);const o=this.getLength(),u=this.editor.deleteText(0,o),a=this.editor.insertContents(0,n),A=this.editor.deleteText(this.getLength()-1,1);return u.compose(a).compose(A)}),l)}setSelection(n,l,o){n==null?this.selection.setRange(null,l||d.sources.API):([n,l,,o]=c(n,l,o),this.selection.setRange(new C.Q(Math.max(0,n),l),o),o!==N.A.sources.SILENT&&this.scrollSelectionIntoView())}setText(n){let l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:N.A.sources.API;const o=new v.Ay().insert(n);return this.setContents(o,l)}update(){let n=arguments.length>0&&arguments[0]!==void 0?arguments[0]:N.A.sources.USER;const l=this.scroll.update(n);return this.selection.update(n),l}updateContents(n){let l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:N.A.sources.API;return r.call(this,(()=>(n=new v.Ay(n),this.editor.applyDelta(n))),l,!0)}}function e(i){return typeof i=="string"?document.querySelector(i):i}function t(i){return Object.entries(i??{}).reduce(((n,l)=>{let[o,u]=l;return{...n,[o]:u===!0?{}:u}}),{})}function s(i){return Object.fromEntries(Object.entries(i).filter((n=>n[1]!==void 0)))}function r(i,n,l,o){if(!this.isEnabled()&&n===N.A.sources.USER&&!this.allowReadOnlyEdits)return new v.Ay;let u=l==null?null:this.getSelection();const a=this.editor.delta,A=i();if(u!=null&&(l===!0&&(l=u.index),o==null?u=h(u,A,n):o!==0&&(u=h(u,l,o,n)),this.setSelection(u,N.A.sources.SILENT)),A.length()>0){const x=[N.A.events.TEXT_CHANGE,A,a,n];this.emitter.emit(N.A.events.EDITOR_CHANGE,...x),n!==N.A.sources.SILENT&&this.emitter.emit(...x)}return A}function c(i,n,l,o,u){let a={};return typeof i.index=="number"&&typeof i.length=="number"?typeof n!="number"?(u=o,o=l,l=n,n=i.length,i=i.index):(n=i.length,i=i.index):typeof n!="number"&&(u=o,o=l,l=n,n=0),typeof l=="object"?(a=l,u=o):typeof l=="string"&&(o!=null?a[l]=o:u=l),[i,n,a,u=u||N.A.sources.API]}function h(i,n,l,o){const u=typeof l=="number"?l:0;if(i==null)return null;let a,A;return n&&typeof n.transformPosition=="function"?[a,A]=[i.index,i.index+i.length].map((x=>n.transformPosition(x,o!==N.A.sources.USER))):[a,A]=[i.index,i.index+i.length].map((x=>x<n||x===n&&o===N.A.sources.USER?x:u>=0?x+u:Math.max(n,x+u))),new C.Q(a,A-a)}},298:function(j,U,p){p.d(U,{Q:function(){return q}});var m=p(3),v=p(200),w=p(78),Y=p(857),et=p(697);const B=(0,w.A)("quill:selection"),C=f=>{try{return"getSelection"in f&&typeof f.getSelection=="function"?f.getSelection():window.getSelection()}catch{return null}};class q{constructor(T){let _=arguments.length>1&&arguments[1]!==void 0?arguments[1]:0;this.index=T,this.length=_}}function R(f,T){try{T.parentNode}catch{return!1}return f.contains(T)}U.A=class{constructor(f,T){this.emitter=T,this.scroll=f,this.composing=!1,this.mouseDown=!1,this.root=this.scroll.domNode,this.rootDocument=this.root.getRootNode(),this.cursor=this.scroll.create("cursor",this),this.savedRange=new q(0,0),this.lastRange=this.savedRange,this.lastNative=null,this.handleComposition(),this.handleDragging(),this.emitter.listenDOM("selectionchange",this.rootDocument,(()=>{this.mouseDown||this.composing||setTimeout(this.update.bind(this,v.A.sources.USER),1)})),this.emitter.on(v.A.events.SCROLL_BEFORE_UPDATE,(()=>{if(!this.hasFocus())return;const _=this.getNativeRange();_!=null&&_.start.node!==this.cursor.textNode&&this.emitter.once(v.A.events.SCROLL_UPDATE,((L,H)=>{try{this.root.contains(_.start.node)&&this.root.contains(_.end.node)&&this.setNativeRange(_.start.node,_.start.offset,_.end.node,_.end.offset);const G=H.some((I=>I.type==="characterData"||I.type==="childList"||I.type==="attributes"&&I.target===this.root));this.update(G?v.A.sources.SILENT:L)}catch{}}))})),this.emitter.on(v.A.events.SCROLL_OPTIMIZE,((_,L)=>{if(L.range){const{startNode:H,startOffset:G,endNode:I,endOffset:k}=L.range;this.setNativeRange(H,G,I,k),this.update(v.A.sources.SILENT)}})),this.update(v.A.sources.SILENT)}handleComposition(){this.emitter.on(v.A.events.COMPOSITION_BEFORE_START,(()=>{this.composing=!0})),this.emitter.on(v.A.events.COMPOSITION_END,(()=>{if(this.composing=!1,this.cursor.parent){const f=this.cursor.restore();if(!f)return;setTimeout((()=>{this.setNativeRange(f.startNode,f.startOffset,f.endNode,f.endOffset)}),1)}}))}handleDragging(){this.emitter.listenDOM("mousedown",document.body,(()=>{this.mouseDown=!0})),this.emitter.listenDOM("mouseup",document.body,(()=>{this.mouseDown=!1,this.update(v.A.sources.USER)}))}focus(){this.hasFocus()||(this.root.focus({preventScroll:!0}),this.setRange(this.savedRange))}format(f,T){this.scroll.update();const _=this.getNativeRange();if(_!=null&&_.native.collapsed&&!this.scroll.query(f,m.Scope.BLOCK)){if(_.start.node!==this.cursor.textNode){const L=this.scroll.find(_.start.node,!1);if(L==null)return;if(L instanceof m.LeafBlot){const H=L.split(_.start.offset);L.parent.insertBefore(this.cursor,H)}else L.insertBefore(this.cursor,_.start.node);this.cursor.attach()}this.cursor.format(f,T),this.scroll.optimize(),this.setNativeRange(this.cursor.textNode,this.cursor.textNode.data.length),this.update()}}getBounds(f){let T=arguments.length>1&&arguments[1]!==void 0?arguments[1]:0;const _=this.scroll.length();let L;f=Math.min(f,_-1),T=Math.min(f+T,_-1)-f;let[H,G]=this.scroll.leaf(f);if(H==null)return null;if(T>0&&G===H.length()){const[F]=this.scroll.leaf(f+1);if(F){const[z]=this.scroll.line(f),[K]=this.scroll.line(f+1);z===K&&(H=F,G=0)}}[L,G]=H.position(G,!0);const I=document.createRange();if(T>0)return I.setStart(L,G),[H,G]=this.scroll.leaf(f+T),H==null?null:([L,G]=H.position(G,!0),I.setEnd(L,G),I.getBoundingClientRect());let k,N="left";if(L instanceof Text){if(!L.data.length)return null;G<L.data.length?(I.setStart(L,G),I.setEnd(L,G+1)):(I.setStart(L,G-1),I.setEnd(L,G),N="right"),k=I.getBoundingClientRect()}else{if(!(H.domNode instanceof Element))return null;k=H.domNode.getBoundingClientRect(),G>0&&(N="right")}return{bottom:k.top+k.height,height:k.height,left:k[N],right:k[N],top:k.top,width:0}}getNativeRange(){const f=(_=>{const L=C(_);return L?.anchorNode?!L||!("getComposedRanges"in L)||typeof L.getComposedRanges!="function"||_ instanceof ShadowRoot&&"getSelection"in _?L.getRangeAt(0):L.getComposedRanges(_)[0]:null})(this.rootDocument);if(f==null)return null;const T=this.normalizeNative(f);return B.info("getNativeRange",T),T}getRange(){const f=this.scroll.domNode;if("isConnected"in f&&!f.isConnected)return[null,null];const T=this.getNativeRange();return T==null?[null,null]:[this.normalizedToRange(T),T]}hasFocus(){const f=this.rootDocument;return f.activeElement===this.root||f.activeElement!=null&&R(this.root,f.activeElement)}normalizedToRange(f){const T=[[f.start.node,f.start.offset]];f.native.collapsed||T.push([f.end.node,f.end.offset]);const _=T.map((G=>{const[I,k]=G,N=this.scroll.find(I,!0),F=N.offset(this.scroll);return k===0?F:N instanceof m.LeafBlot?F+N.index(I,k):F+N.length()})),L=Math.min(Math.max(..._),this.scroll.length()-1),H=Math.min(L,..._);return new q(H,L-H)}normalizeNative(f){if(!R(this.root,f.startContainer)||!f.collapsed&&!R(this.root,f.endContainer))return null;const T={start:{node:f.startContainer,offset:f.startOffset},end:{node:f.endContainer,offset:f.endOffset},native:f};return[T.start,T.end].forEach((_=>{let{node:L,offset:H}=_;for(;!(L instanceof Text)&&L.childNodes.length>0;)if(L.childNodes.length>H)L=L.childNodes[H],H=0;else{if(L.childNodes.length!==H)break;L=L.lastChild,H=L instanceof Text?L.data.length:L.childNodes.length>0?L.childNodes.length:L.childNodes.length+1}_.node=L,_.offset=H})),T}rangeToNative(f){const T=this.scroll.length(),_=(L,H)=>{L=Math.min(T-1,L);const[G,I]=this.scroll.leaf(L);return G?G.position(I,H):[null,-1]};return[..._(f.index,!1),..._(f.index+f.length,!0)]}setNativeRange(f,T){let _=arguments.length>2&&arguments[2]!==void 0?arguments[2]:f,L=arguments.length>3&&arguments[3]!==void 0?arguments[3]:T,H=arguments.length>4&&arguments[4]!==void 0&&arguments[4];if(B.info("setNativeRange",f,T,_,L),f!=null&&(this.root.parentNode==null||f.parentNode==null||_.parentNode==null))return;const G=C(this.rootDocument);if(G!=null)if(f!=null){this.hasFocus()||this.root.focus({preventScroll:!0});const{native:I}=this.getNativeRange()||{};(I==null||H||f!==I.startContainer||T!==I.startOffset||_!==I.endContainer||L!==I.endOffset)&&(f instanceof Element&&f.tagName==="BR"&&(T=Array.from(f.parentNode.childNodes).indexOf(f),f=f.parentNode),_ instanceof Element&&_.tagName==="BR"&&(L=Array.from(_.parentNode.childNodes).indexOf(_),_=_.parentNode),f&&_&&typeof T=="number"&&typeof L=="number"&&G.setBaseAndExtent(f,T,_,L))}else G.removeAllRanges(),this.root.blur()}setRange(f){let T=arguments.length>1&&arguments[1]!==void 0&&arguments[1],_=arguments.length>2&&arguments[2]!==void 0?arguments[2]:v.A.sources.API;if(typeof T=="string"&&(_=T,T=!1),B.info("setRange",f),f!=null){const L=this.rangeToNative(f);this.setNativeRange(...L,T)}else this.setNativeRange(null);this.update(_)}update(){let f=arguments.length>0&&arguments[0]!==void 0?arguments[0]:v.A.sources.USER;const T=this.lastRange,[_,L]=this.getRange();if(this.lastRange=_,this.lastNative=L,this.lastRange!=null&&(this.savedRange=this.lastRange),!(0,et.A)(T,this.lastRange)){if(!this.composing&&L!=null&&L.native.collapsed&&L.start.node!==this.cursor.textNode){const G=this.cursor.restore();G&&this.setNativeRange(G.startNode,G.startOffset,G.endNode,G.endOffset)}const H=[v.A.events.SELECTION_CHANGE,(0,Y.A)(this.lastRange),(0,Y.A)(T),f];this.emitter.emit(v.A.events.EDITOR_CHANGE,...H),f!==v.A.sources.SILENT&&this.emitter.emit(...H)}}}},609:function(j,U){class p{static DEFAULTS={modules:{}};static themes={default:p};modules={};constructor(v,w){this.quill=v,this.options=w}init(){Object.keys(this.options.modules).forEach((v=>{this.modules[v]==null&&this.addModule(v)}))}addModule(v){const w=this.quill.constructor.import(`modules/${v}`);return this.modules[v]=new w(this.quill,this.options.modules[v]||{}),this.modules[v]}}U.A=p},857:function(j,U){U.A=function(p){return JSON.parse(JSON.stringify(p))}},697:function(j,U){function p(m){return m!==Object(m)}U.A=function m(v,w){if(v===w)return!0;if(p(v)||p(w))return v===w;if(Object.keys(v).length!==Object.keys(w).length)return!1;for(const Y in v)if(!(Y in w)||!m(v[Y],w[Y]))return!1;return!0}},276:function(j,U,p){p.d(U,{Hu:function(){return et},gS:function(){return w},qh:function(){return Y}});var m=p(3);const v={scope:m.Scope.BLOCK,whitelist:["right","center","justify"]},w=new m.Attributor("align","align",v),Y=new m.ClassAttributor("align","ql-align",v),et=new m.StyleAttributor("align","text-align",v)},922:function(j,U,p){p.d(U,{l:function(){return w},s:function(){return Y}});var m=p(3),v=p(638);const w=new m.ClassAttributor("background","ql-bg",{scope:m.Scope.INLINE}),Y=new v.a2("background","background-color",{scope:m.Scope.INLINE})},404:function(j,U,p){p.d(U,{Ay:function(){return R},Cy:function(){return f}});var m=p(698),v=p(36),w=p(541),Y=p(850),et=p(508),B=p(580),C=p(543);class q extends B.A{static create(_){const L=super.create(_);return L.setAttribute("spellcheck","false"),L}code(_,L){return this.children.map((H=>H.length()<=1?"":H.domNode.innerText)).join(`
`).slice(_,_+L)}html(_,L){return`<pre>
${(0,et.X)(this.code(_,L))}
</pre>`}}class R extends m.Ay{static TAB="  ";static register(){C.Ay.register(q)}}class f extends Y.A{}f.blotName="code",f.tagName="CODE",R.blotName="code-block",R.className="ql-code-block",R.tagName="DIV",q.blotName="code-block-container",q.className="ql-code-block-container",q.tagName="DIV",q.allowedChildren=[R],R.allowedChildren=[et.A,v.A,w.A],R.requiredContainer=q},638:function(j,U,p){p.d(U,{JM:function(){return Y},a2:function(){return v},g3:function(){return w}});var m=p(3);class v extends m.StyleAttributor{value(B){let C=super.value(B);return C.startsWith("rgb(")?(C=C.replace(/^[^\d]+/,"").replace(/[^\d]+$/,""),`#${C.split(",").map((q=>`00${parseInt(q,10).toString(16)}`.slice(-2))).join("")}`):C}}const w=new m.ClassAttributor("color","ql-color",{scope:m.Scope.INLINE}),Y=new v("color","color",{scope:m.Scope.INLINE})},912:function(j,U,p){p.d(U,{Mc:function(){return w},VL:function(){return et},sY:function(){return Y}});var m=p(3);const v={scope:m.Scope.BLOCK,whitelist:["rtl"]},w=new m.Attributor("direction","dir",v),Y=new m.ClassAttributor("direction","ql-direction",v),et=new m.StyleAttributor("direction","direction",v)},772:function(j,U,p){p.d(U,{q:function(){return w},z:function(){return et}});var m=p(3);const v={scope:m.Scope.INLINE,whitelist:["serif","monospace"]},w=new m.ClassAttributor("font","ql-font",v);class Y extends m.StyleAttributor{value(C){return super.value(C).replace(/["']/g,"")}}const et=new Y("font","font-family",v)},664:function(j,U,p){p.d(U,{U:function(){return v},r:function(){return w}});var m=p(3);const v=new m.ClassAttributor("size","ql-size",{scope:m.Scope.INLINE,whitelist:["small","large","huge"]}),w=new m.StyleAttributor("size","font-size",{scope:m.Scope.INLINE,whitelist:["10px","18px","32px"]})},584:function(j,U,p){p.d(U,{Ay:function(){return S}});var m=p(3),v=p(398),w=p(698),Y=p(78),et=p(266),B=p(543),C=p(276),q=p(922),R=p(404),f=p(638),T=p(912),_=p(772),L=p(664),H=p(123);const G=/font-weight:\s*normal/,I=["P","OL","UL"],k=r=>r&&I.includes(r.tagName),N=/\bmso-list:[^;]*ignore/i,F=/\bmso-list:[^;]*\bl(\d+)/i,z=/\bmso-list:[^;]*\blevel(\d+)/i,K=[function(r){r.documentElement.getAttribute("xmlns:w")==="urn:schemas-microsoft-com:office:word"&&(c=>{const h=Array.from(c.querySelectorAll("[style*=mso-list]")),i=[],n=[];h.forEach((u=>{(u.getAttribute("style")||"").match(N)?i.push(u):n.push(u)})),i.forEach((u=>u.parentNode?.removeChild(u)));const l=c.documentElement.innerHTML,o=n.map((u=>((a,A)=>{const x=a.getAttribute("style"),b=x?.match(F);if(!b)return null;const $=Number(b[1]),X=x?.match(z),W=X?Number(X[1]):1,J=new RegExp(`@list l${$}:level${W}\\s*\\{[^\\}]*mso-level-number-format:\\s*([\\w-]+)`,"i"),rt=A.match(J);return{id:$,indent:W,type:rt&&rt[1]==="bullet"?"bullet":"ordered",element:a}})(u,l))).filter((u=>u));for(;o.length;){const u=[];let a=o.shift();for(;a;)u.push(a),a=o.length&&o[0]?.element===a.element.nextElementSibling&&o[0].id===a.id?o.shift():null;const A=document.createElement("ul");u.forEach(($=>{const X=document.createElement("li");X.setAttribute("data-list",$.type),$.indent>1&&X.setAttribute("class","ql-indent-"+($.indent-1)),X.innerHTML=$.element.innerHTML,A.appendChild(X)}));const x=u[0]?.element,{parentNode:b}=x??{};x&&b?.replaceChild(A,x),u.slice(1).forEach(($=>{let{element:X}=$;b?.removeChild(X)}))}})(r)},function(r){r.querySelector('[id^="docs-internal-guid-"]')&&((c=>{Array.from(c.querySelectorAll('b[style*="font-weight"]')).filter((h=>h.getAttribute("style")?.match(G))).forEach((h=>{const i=c.createDocumentFragment();i.append(...h.childNodes),h.parentNode?.replaceChild(i,h)}))})(r),(c=>{Array.from(c.querySelectorAll("br")).filter((h=>k(h.previousElementSibling)&&k(h.nextElementSibling))).forEach((h=>{h.parentNode?.removeChild(h)}))})(r))}],nt=(0,Y.A)("quill:clipboard"),M=[[Node.TEXT_NODE,function(r,c,h){let i=r.data;if(r.parentElement?.tagName==="O:P")return c.insert(i.trim());if(!d(r)){if(i.trim().length===0&&i.includes(`
`)&&!(function(n,l){return n.previousElementSibling&&n.nextElementSibling&&!P(n.previousElementSibling,l)&&!P(n.nextElementSibling,l)})(r,h))return c;i=i.replace(/[^\S\u00a0]/g," "),i=i.replace(/ {2,}/g," "),(r.previousSibling==null&&r.parentElement!=null&&P(r.parentElement,h)||r.previousSibling instanceof Element&&P(r.previousSibling,h))&&(i=i.replace(/^ /,"")),(r.nextSibling==null&&r.parentElement!=null&&P(r.parentElement,h)||r.nextSibling instanceof Element&&P(r.nextSibling,h))&&(i=i.replace(/ $/,"")),i=i.replaceAll(" "," ")}return c.insert(i)}],[Node.TEXT_NODE,s],["br",function(r,c){return tt(c,`
`)||c.insert(`
`),c}],[Node.ELEMENT_NODE,s],[Node.ELEMENT_NODE,function(r,c,h){const i=h.query(r);if(i==null)return c;if(i.prototype instanceof m.EmbedBlot){const n={},l=i.value(r);if(l!=null)return n[i.blotName]=l,new v.Ay().insert(n,i.formats(r,h))}else if(i.prototype instanceof m.BlockBlot&&!tt(c,`
`)&&c.insert(`
`),"blotName"in i&&"formats"in i&&typeof i.formats=="function")return O(c,i.blotName,i.formats(r,h),h);return c}],[Node.ELEMENT_NODE,function(r,c,h){const i=m.Attributor.keys(r),n=m.ClassAttributor.keys(r),l=m.StyleAttributor.keys(r),o={};return i.concat(n).concat(l).forEach((u=>{let a=h.query(u,m.Scope.ATTRIBUTE);a!=null&&(o[a.attrName]=a.value(r),o[a.attrName])||(a=g[u],a==null||a.attrName!==u&&a.keyName!==u||(o[a.attrName]=a.value(r)||void 0),a=y[u],a==null||a.attrName!==u&&a.keyName!==u||(a=y[u],o[a.attrName]=a.value(r)||void 0))})),Object.entries(o).reduce(((u,a)=>{let[A,x]=a;return O(u,A,x,h)}),c)}],[Node.ELEMENT_NODE,function(r,c,h){const i={},n=r.style||{};return n.fontStyle==="italic"&&(i.italic=!0),n.textDecoration==="underline"&&(i.underline=!0),n.textDecoration==="line-through"&&(i.strike=!0),(n.fontWeight?.startsWith("bold")||parseInt(n.fontWeight,10)>=700)&&(i.bold=!0),c=Object.entries(i).reduce(((l,o)=>{let[u,a]=o;return O(l,u,a,h)}),c),parseFloat(n.textIndent||0)>0?new v.Ay().insert("	").concat(c):c}],["li",function(r,c,h){const i=h.query(r);if(i==null||i.blotName!=="list"||!tt(c,`
`))return c;let n=-1,l=r.parentNode;for(;l!=null;)["OL","UL"].includes(l.tagName)&&(n+=1),l=l.parentNode;return n<=0?c:c.reduce(((o,u)=>u.insert?u.attributes&&typeof u.attributes.indent=="number"?o.push(u):o.insert(u.insert,{indent:n,...u.attributes||{}}):o),new v.Ay)}],["ol, ul",function(r,c,h){const i=r;let n=i.tagName==="OL"?"ordered":"bullet";const l=i.getAttribute("data-checked");return l&&(n=l==="true"?"checked":"unchecked"),O(c,"list",n,h)}],["pre",function(r,c,h){const i=h.query("code-block");return O(c,"code-block",!i||!("formats"in i)||typeof i.formats!="function"||i.formats(r,h),h)}],["tr",function(r,c,h){const i=r.parentElement?.tagName==="TABLE"?r.parentElement:r.parentElement?.parentElement;return i!=null?O(c,"table",Array.from(i.querySelectorAll("tr")).indexOf(r)+1,h):c}],["b",t("bold")],["i",t("italic")],["strike",t("strike")],["style",function(){return new v.Ay}]],g=[C.gS,T.Mc].reduce(((r,c)=>(r[c.keyName]=c,r)),{}),y=[C.Hu,q.s,f.JM,T.VL,_.z,L.r].reduce(((r,c)=>(r[c.keyName]=c,r)),{});class S extends et.A{static DEFAULTS={matchers:[]};constructor(c,h){super(c,h),this.quill.root.addEventListener("copy",(i=>this.onCaptureCopy(i,!1))),this.quill.root.addEventListener("cut",(i=>this.onCaptureCopy(i,!0))),this.quill.root.addEventListener("paste",this.onCapturePaste.bind(this)),this.matchers=[],M.concat(this.options.matchers??[]).forEach((i=>{let[n,l]=i;this.addMatcher(n,l)}))}addMatcher(c,h){this.matchers.push([c,h])}convert(c){let{html:h,text:i}=c,n=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};if(n[R.Ay.blotName])return new v.Ay().insert(i||"",{[R.Ay.blotName]:n[R.Ay.blotName]});if(!h)return new v.Ay().insert(i||"",n);const l=this.convertHTML(h);return tt(l,`
`)&&(l.ops[l.ops.length-1].attributes==null||n.table)?l.compose(new v.Ay().retain(l.length()-1).delete(1)):l}normalizeHTML(c){(h=>{h.documentElement&&K.forEach((i=>{i(h)}))})(c)}convertHTML(c){const h=new DOMParser().parseFromString(c,"text/html");this.normalizeHTML(h);const i=h.body,n=new WeakMap,[l,o]=this.prepareMatching(i,n);return e(this.quill.scroll,i,l,o,n)}dangerouslyPasteHTML(c,h){let i=arguments.length>2&&arguments[2]!==void 0?arguments[2]:B.Ay.sources.API;if(typeof c=="string"){const n=this.convert({html:c,text:""});this.quill.setContents(n,h),this.quill.setSelection(0,B.Ay.sources.SILENT)}else{const n=this.convert({html:h,text:""});this.quill.updateContents(new v.Ay().retain(c).concat(n),i),this.quill.setSelection(c+n.length(),B.Ay.sources.SILENT)}}onCaptureCopy(c){let h=arguments.length>1&&arguments[1]!==void 0&&arguments[1];if(c.defaultPrevented)return;c.preventDefault();const[i]=this.quill.selection.getRange();if(i==null)return;const{html:n,text:l}=this.onCopy(i,h);c.clipboardData?.setData("text/plain",l),c.clipboardData?.setData("text/html",n),h&&(0,H.Xo)({range:i,quill:this.quill})}normalizeURIList(c){return c.split(/\r?\n/).filter((h=>h[0]!=="#")).join(`
`)}onCapturePaste(c){if(c.defaultPrevented||!this.quill.isEnabled())return;c.preventDefault();const h=this.quill.getSelection(!0);if(h==null)return;const i=c.clipboardData?.getData("text/html");let n=c.clipboardData?.getData("text/plain");if(!i&&!n){const o=c.clipboardData?.getData("text/uri-list");o&&(n=this.normalizeURIList(o))}const l=Array.from(c.clipboardData?.files||[]);if(!i&&l.length>0)this.quill.uploader.upload(h,l);else{if(i&&l.length>0){const o=new DOMParser().parseFromString(i,"text/html");if(o.body.childElementCount===1&&o.body.firstElementChild?.tagName==="IMG")return void this.quill.uploader.upload(h,l)}this.onPaste(h,{html:i,text:n})}}onCopy(c){const h=this.quill.getText(c);return{html:this.quill.getSemanticHTML(c),text:h}}onPaste(c,h){let{text:i,html:n}=h;const l=this.quill.getFormat(c.index),o=this.convert({text:i,html:n},l);nt.log("onPaste",o,{text:i,html:n});const u=new v.Ay().retain(c.index).delete(c.length).concat(o);this.quill.updateContents(u,B.Ay.sources.USER),this.quill.setSelection(u.length()-c.length,B.Ay.sources.SILENT),this.quill.scrollSelectionIntoView()}prepareMatching(c,h){const i=[],n=[];return this.matchers.forEach((l=>{const[o,u]=l;switch(o){case Node.TEXT_NODE:n.push(u);break;case Node.ELEMENT_NODE:i.push(u);break;default:Array.from(c.querySelectorAll(o)).forEach((a=>{h.has(a)?h.get(a)?.push(u):h.set(a,[u])}))}})),[i,n]}}function O(r,c,h,i){return i.query(c)?r.reduce(((n,l)=>{if(!l.insert)return n;if(l.attributes&&l.attributes[c])return n.push(l);const o=h?{[c]:h}:{};return n.insert(l.insert,{...o,...l.attributes})}),new v.Ay):r}function tt(r,c){let h="";for(let i=r.ops.length-1;i>=0&&h.length<c.length;--i){const n=r.ops[i];if(typeof n.insert!="string")break;h=n.insert+h}return h.slice(-1*c.length)===c}function P(r,c){if(!(r instanceof Element))return!1;const h=c.query(r);return!(h&&h.prototype instanceof m.EmbedBlot)&&["address","article","blockquote","canvas","dd","div","dl","dt","fieldset","figcaption","figure","footer","form","h1","h2","h3","h4","h5","h6","header","iframe","li","main","nav","ol","output","p","pre","section","table","td","tr","ul","video"].includes(r.tagName.toLowerCase())}const V=new WeakMap;function d(r){return r!=null&&(V.has(r)||(r.tagName==="PRE"?V.set(r,!0):V.set(r,d(r.parentNode))),V.get(r))}function e(r,c,h,i,n){return c.nodeType===c.TEXT_NODE?i.reduce(((l,o)=>o(c,l,r)),new v.Ay):c.nodeType===c.ELEMENT_NODE?Array.from(c.childNodes||[]).reduce(((l,o)=>{let u=e(r,o,h,i,n);return o.nodeType===c.ELEMENT_NODE&&(u=h.reduce(((a,A)=>A(o,a,r)),u),u=(n.get(o)||[]).reduce(((a,A)=>A(o,a,r)),u)),l.concat(u)}),new v.Ay):new v.Ay}function t(r){return(c,h,i)=>O(h,r,!0,i)}function s(r,c,h){if(!tt(c,`
`)){if(P(r,h)&&(r.childNodes.length>0||r instanceof HTMLParagraphElement))return c.insert(`
`);if(c.length()>0&&r.nextSibling){let i=r.nextSibling;for(;i!=null;){if(P(i,h))return c.insert(`
`);const n=h.query(i);if(n&&n.prototype instanceof w.zo)return c.insert(`
`);i=i.firstChild}}}return c}},123:function(j,U,p){p.d(U,{Ay:function(){return R},Xo:function(){return G}});var m=p(398),v=p(3),w=p(543),Y=p(78),et=p(266),B=p(697);const C=(0,Y.A)("quill:keyboard"),q=/Mac/i.test(navigator.platform)?"metaKey":"ctrlKey";class R extends et.A{static match(k,N){return!["altKey","ctrlKey","metaKey","shiftKey"].some((F=>!!N[F]!==k[F]&&N[F]!==null))&&(N.key===k.key||N.key===k.which)}constructor(k,N){super(k,N),this.bindings={},Object.keys(this.options.bindings).forEach((F=>{this.options.bindings[F]&&this.addBinding(this.options.bindings[F])})),this.addBinding({key:"Enter",shiftKey:null},this.handleEnter),this.addBinding({key:"Enter",metaKey:null,ctrlKey:null,altKey:null},(()=>{})),/Firefox/i.test(navigator.userAgent)?(this.addBinding({key:"Backspace"},{collapsed:!0},this.handleBackspace),this.addBinding({key:"Delete"},{collapsed:!0},this.handleDelete)):(this.addBinding({key:"Backspace"},{collapsed:!0,prefix:/^.?$/},this.handleBackspace),this.addBinding({key:"Delete"},{collapsed:!0,suffix:/^.?$/},this.handleDelete)),this.addBinding({key:"Backspace"},{collapsed:!1},this.handleDeleteRange),this.addBinding({key:"Delete"},{collapsed:!1},this.handleDeleteRange),this.addBinding({key:"Backspace",altKey:null,ctrlKey:null,metaKey:null,shiftKey:null},{collapsed:!0,offset:0},this.handleBackspace),this.listen()}addBinding(k){let N=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},F=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{};const z=(function(K){if(typeof K=="string"||typeof K=="number")K={key:K};else{if(typeof K!="object")return null;K={...K}}return K.shortKey&&(K[q]=K.shortKey,delete K.shortKey),K})(k);z!=null?(typeof N=="function"&&(N={handler:N}),typeof F=="function"&&(F={handler:F}),(Array.isArray(z.key)?z.key:[z.key]).forEach((K=>{const nt={...z,key:K,...N,...F};this.bindings[nt.key]=this.bindings[nt.key]||[],this.bindings[nt.key].push(nt)}))):C.warn("Attempted to add invalid keyboard binding",z)}listen(){this.quill.root.addEventListener("keydown",(k=>{if(k.defaultPrevented||k.isComposing||k.keyCode===229&&(k.key==="Enter"||k.key==="Backspace"))return;const N=(this.bindings[k.key]||[]).concat(this.bindings[k.which]||[]).filter((V=>R.match(k,V)));if(N.length===0)return;const F=w.Ay.find(k.target,!0);if(F&&F.scroll!==this.quill.scroll)return;const z=this.quill.getSelection();if(z==null||!this.quill.hasFocus())return;const[K,nt]=this.quill.getLine(z.index),[M,g]=this.quill.getLeaf(z.index),[y,S]=z.length===0?[M,g]:this.quill.getLeaf(z.index+z.length),O=M instanceof v.TextBlot?M.value().slice(0,g):"",tt=y instanceof v.TextBlot?y.value().slice(S):"",P={collapsed:z.length===0,empty:z.length===0&&K.length()<=1,format:this.quill.getFormat(z),line:K,offset:nt,prefix:O,suffix:tt,event:k};N.some((V=>{if(V.collapsed!=null&&V.collapsed!==P.collapsed||V.empty!=null&&V.empty!==P.empty||V.offset!=null&&V.offset!==P.offset)return!1;if(Array.isArray(V.format)){if(V.format.every((d=>P.format[d]==null)))return!1}else if(typeof V.format=="object"&&!Object.keys(V.format).every((d=>V.format[d]===!0?P.format[d]!=null:V.format[d]===!1?P.format[d]==null:(0,B.A)(V.format[d],P.format[d]))))return!1;return!(V.prefix!=null&&!V.prefix.test(P.prefix)||V.suffix!=null&&!V.suffix.test(P.suffix)||V.handler.call(this,z,P,V)===!0)}))&&k.preventDefault()}))}handleBackspace(k,N){const F=/[\uD800-\uDBFF][\uDC00-\uDFFF]$/.test(N.prefix)?2:1;if(k.index===0||this.quill.getLength()<=1)return;let z={};const[K]=this.quill.getLine(k.index);let nt=new m.Ay().retain(k.index-F).delete(F);if(N.offset===0){const[M]=this.quill.getLine(k.index-1);if(M&&!(M.statics.blotName==="block"&&M.length()<=1)){const g=K.formats(),y=this.quill.getFormat(k.index-1,1);if(z=m.xb.diff(g,y)||{},Object.keys(z).length>0){const S=new m.Ay().retain(k.index+K.length()-2).retain(1,z);nt=nt.compose(S)}}}this.quill.updateContents(nt,w.Ay.sources.USER),this.quill.focus()}handleDelete(k,N){const F=/^[\uD800-\uDBFF][\uDC00-\uDFFF]/.test(N.suffix)?2:1;if(k.index>=this.quill.getLength()-F)return;let z={};const[K]=this.quill.getLine(k.index);let nt=new m.Ay().retain(k.index).delete(F);if(N.offset>=K.length()-1){const[M]=this.quill.getLine(k.index+1);if(M){const g=K.formats(),y=this.quill.getFormat(k.index,1);z=m.xb.diff(g,y)||{},Object.keys(z).length>0&&(nt=nt.retain(M.length()-1).retain(1,z))}}this.quill.updateContents(nt,w.Ay.sources.USER),this.quill.focus()}handleDeleteRange(k){G({range:k,quill:this.quill}),this.quill.focus()}handleEnter(k,N){const F=Object.keys(N.format).reduce(((K,nt)=>(this.quill.scroll.query(nt,v.Scope.BLOCK)&&!Array.isArray(N.format[nt])&&(K[nt]=N.format[nt]),K)),{}),z=new m.Ay().retain(k.index).delete(k.length).insert(`
`,F);this.quill.updateContents(z,w.Ay.sources.USER),this.quill.setSelection(k.index+1,w.Ay.sources.SILENT),this.quill.focus()}}const f={bindings:{bold:L("bold"),italic:L("italic"),underline:L("underline"),indent:{key:"Tab",format:["blockquote","indent","list"],handler(I,k){return!(!k.collapsed||k.offset===0)||(this.quill.format("indent","+1",w.Ay.sources.USER),!1)}},outdent:{key:"Tab",shiftKey:!0,format:["blockquote","indent","list"],handler(I,k){return!(!k.collapsed||k.offset===0)||(this.quill.format("indent","-1",w.Ay.sources.USER),!1)}},"outdent backspace":{key:"Backspace",collapsed:!0,shiftKey:null,metaKey:null,ctrlKey:null,altKey:null,format:["indent","list"],offset:0,handler(I,k){k.format.indent!=null?this.quill.format("indent","-1",w.Ay.sources.USER):k.format.list!=null&&this.quill.format("list",!1,w.Ay.sources.USER)}},"indent code-block":T(!0),"outdent code-block":T(!1),"remove tab":{key:"Tab",shiftKey:!0,collapsed:!0,prefix:/\t$/,handler(I){this.quill.deleteText(I.index-1,1,w.Ay.sources.USER)}},tab:{key:"Tab",handler(I,k){if(k.format.table)return!0;this.quill.history.cutoff();const N=new m.Ay().retain(I.index).delete(I.length).insert("	");return this.quill.updateContents(N,w.Ay.sources.USER),this.quill.history.cutoff(),this.quill.setSelection(I.index+1,w.Ay.sources.SILENT),!1}},"blockquote empty enter":{key:"Enter",collapsed:!0,format:["blockquote"],empty:!0,handler(){this.quill.format("blockquote",!1,w.Ay.sources.USER)}},"list empty enter":{key:"Enter",collapsed:!0,format:["list"],empty:!0,handler(I,k){const N={list:!1};k.format.indent&&(N.indent=!1),this.quill.formatLine(I.index,I.length,N,w.Ay.sources.USER)}},"checklist enter":{key:"Enter",collapsed:!0,format:{list:"checked"},handler(I){const[k,N]=this.quill.getLine(I.index),F={...k.formats(),list:"checked"},z=new m.Ay().retain(I.index).insert(`
`,F).retain(k.length()-N-1).retain(1,{list:"unchecked"});this.quill.updateContents(z,w.Ay.sources.USER),this.quill.setSelection(I.index+1,w.Ay.sources.SILENT),this.quill.scrollSelectionIntoView()}},"header enter":{key:"Enter",collapsed:!0,format:["header"],suffix:/^$/,handler(I,k){const[N,F]=this.quill.getLine(I.index),z=new m.Ay().retain(I.index).insert(`
`,k.format).retain(N.length()-F-1).retain(1,{header:null});this.quill.updateContents(z,w.Ay.sources.USER),this.quill.setSelection(I.index+1,w.Ay.sources.SILENT),this.quill.scrollSelectionIntoView()}},"table backspace":{key:"Backspace",format:["table"],collapsed:!0,offset:0,handler(){}},"table delete":{key:"Delete",format:["table"],collapsed:!0,suffix:/^$/,handler(){}},"table enter":{key:"Enter",shiftKey:null,format:["table"],handler(I){const k=this.quill.getModule("table");if(k){const[N,F,z,K]=k.getTable(I),nt=(function(g,y,S,O){return y.prev==null&&y.next==null?S.prev==null&&S.next==null?O===0?-1:1:S.prev==null?-1:1:y.prev==null?-1:y.next==null?1:null})(0,F,z,K);if(nt==null)return;let M=N.offset();if(nt<0){const g=new m.Ay().retain(M).insert(`
`);this.quill.updateContents(g,w.Ay.sources.USER),this.quill.setSelection(I.index+1,I.length,w.Ay.sources.SILENT)}else if(nt>0){M+=N.length();const g=new m.Ay().retain(M).insert(`
`);this.quill.updateContents(g,w.Ay.sources.USER),this.quill.setSelection(M,w.Ay.sources.USER)}}}},"table tab":{key:"Tab",shiftKey:null,format:["table"],handler(I,k){const{event:N,line:F}=k,z=F.offset(this.quill.scroll);N.shiftKey?this.quill.setSelection(z-1,w.Ay.sources.USER):this.quill.setSelection(z+F.length(),w.Ay.sources.USER)}},"list autofill":{key:" ",shiftKey:null,collapsed:!0,format:{"code-block":!1,blockquote:!1,table:!1},prefix:/^\s*?(\d+\.|-|\*|\[ ?\]|\[x\])$/,handler(I,k){if(this.quill.scroll.query("list")==null)return!0;const{length:N}=k.prefix,[F,z]=this.quill.getLine(I.index);if(z>N)return!0;let K;switch(k.prefix.trim()){case"[]":case"[ ]":K="unchecked";break;case"[x]":K="checked";break;case"-":case"*":K="bullet";break;default:K="ordered"}this.quill.insertText(I.index," ",w.Ay.sources.USER),this.quill.history.cutoff();const nt=new m.Ay().retain(I.index-z).delete(N+1).retain(F.length()-2-z).retain(1,{list:K});return this.quill.updateContents(nt,w.Ay.sources.USER),this.quill.history.cutoff(),this.quill.setSelection(I.index-N,w.Ay.sources.SILENT),!1}},"code exit":{key:"Enter",collapsed:!0,format:["code-block"],prefix:/^$/,suffix:/^\s*$/,handler(I){const[k,N]=this.quill.getLine(I.index);let F=2,z=k;for(;z!=null&&z.length()<=1&&z.formats()["code-block"];)if(z=z.prev,F-=1,F<=0){const K=new m.Ay().retain(I.index+k.length()-N-2).retain(1,{"code-block":null}).delete(1);return this.quill.updateContents(K,w.Ay.sources.USER),this.quill.setSelection(I.index-1,w.Ay.sources.SILENT),!1}return!0}},"embed left":_("ArrowLeft",!1),"embed left shift":_("ArrowLeft",!0),"embed right":_("ArrowRight",!1),"embed right shift":_("ArrowRight",!0),"table down":H(!1),"table up":H(!0)}};function T(I){return{key:"Tab",shiftKey:!I,format:{"code-block":!0},handler(k,N){let{event:F}=N;const z=this.quill.scroll.query("code-block"),{TAB:K}=z;if(k.length===0&&!F.shiftKey)return this.quill.insertText(k.index,K,w.Ay.sources.USER),void this.quill.setSelection(k.index+K.length,w.Ay.sources.SILENT);const nt=k.length===0?this.quill.getLines(k.index,1):this.quill.getLines(k);let{index:M,length:g}=k;nt.forEach(((y,S)=>{I?(y.insertAt(0,K),S===0?M+=K.length:g+=K.length):y.domNode.textContent.startsWith(K)&&(y.deleteAt(0,K.length),S===0?M-=K.length:g-=K.length)})),this.quill.update(w.Ay.sources.USER),this.quill.setSelection(M,g,w.Ay.sources.SILENT)}}}function _(I,k){return{key:I,shiftKey:k,altKey:null,[I==="ArrowLeft"?"prefix":"suffix"]:/^$/,handler(N){let{index:F}=N;I==="ArrowRight"&&(F+=N.length+1);const[z]=this.quill.getLeaf(F);return!(z instanceof v.EmbedBlot&&(I==="ArrowLeft"?k?this.quill.setSelection(N.index-1,N.length+1,w.Ay.sources.USER):this.quill.setSelection(N.index-1,w.Ay.sources.USER):k?this.quill.setSelection(N.index,N.length+1,w.Ay.sources.USER):this.quill.setSelection(N.index+N.length+1,w.Ay.sources.USER),1))}}}function L(I){return{key:I[0],shortKey:!0,handler(k,N){this.quill.format(I,!N.format[I],w.Ay.sources.USER)}}}function H(I){return{key:I?"ArrowUp":"ArrowDown",collapsed:!0,format:["table"],handler(k,N){const F=I?"prev":"next",z=N.line,K=z.parent[F];if(K!=null){if(K.statics.blotName==="table-row"){let nt=K.children.head,M=z;for(;M.prev!=null;)M=M.prev,nt=nt.next;const g=nt.offset(this.quill.scroll)+Math.min(N.offset,nt.length()-1);this.quill.setSelection(g,0,w.Ay.sources.USER)}}else{const nt=z.table()[F];nt!=null&&(I?this.quill.setSelection(nt.offset(this.quill.scroll)+nt.length()-1,0,w.Ay.sources.USER):this.quill.setSelection(nt.offset(this.quill.scroll),0,w.Ay.sources.USER))}return!1}}}function G(I){let{quill:k,range:N}=I;const F=k.getLines(N);let z={};if(F.length>1){const K=F[0].formats(),nt=F[F.length-1].formats();z=m.xb.diff(nt,K)||{}}k.deleteText(N,w.Ay.sources.USER),Object.keys(z).length>0&&k.formatLine(N.index,1,z,w.Ay.sources.USER),k.setSelection(N.index,w.Ay.sources.SILENT)}R.DEFAULTS=f},398:function(j,U,p){p.d(U,{Ay:function(){return nt},Op:function(){return k},xb:function(){return I}});var m,v,w=Object.create,Y=Object.defineProperty,et=Object.getOwnPropertyDescriptor,B=Object.getOwnPropertyNames,C=Object.getPrototypeOf,q=Object.prototype.hasOwnProperty,R=((M,g,y)=>(y=M!=null?w(C(M)):{},((S,O,tt,P)=>{if(O&&typeof O=="object"||typeof O=="function")for(let V of B(O))q.call(S,V)||V===void 0||Y(S,V,{get:()=>O[V],enumerable:!(P=et(O,V))||P.enumerable});return S})(M&&M.__esModule?y:Y(y,"default",{value:M,enumerable:!0}),M)))((m={"node_modules/.pnpm/fast-diff@1.3.0/node_modules/fast-diff/diff.js"(M,g){var y=-1;function S(a,A,x,b,$){if(a===A)return a?[[0,a]]:[];if(x!=null){var X=(function(Z,it,gt){var ht=typeof gt=="number"?{index:gt,length:0}:gt.oldRange,mt=typeof gt=="number"?null:gt.newRange,st=Z.length,pt=it.length;if(ht.length===0&&(mt===null||mt.length===0)){var At=ht.index,vt=Z.slice(0,At),xt=Z.slice(At),Tt=mt?mt.index:null,Nt=At+pt-st;if((Tt===null||Tt===Nt)&&!(Nt<0||Nt>pt)){var Bt=it.slice(0,Nt);if((bt=it.slice(Nt))===xt){var Et=Math.min(At,Nt);if((ft=vt.slice(0,Et))===(at=Bt.slice(0,Et)))return o(ft,vt.slice(Et),Bt.slice(Et),xt)}}if(Tt===null||Tt===At){var ut=At,bt=(Bt=it.slice(0,ut),it.slice(ut));if(Bt===vt){var ot=Math.min(st-ut,pt-ut);if((dt=xt.slice(xt.length-ot))===(_t=bt.slice(bt.length-ot)))return o(vt,xt.slice(0,xt.length-ot),bt.slice(0,bt.length-ot),dt)}}}if(ht.length>0&&mt&&mt.length===0){var ft=Z.slice(0,ht.index),dt=Z.slice(ht.index+ht.length);if(!(pt<(Et=ft.length)+(ot=dt.length))){var at=it.slice(0,Et),_t=it.slice(pt-ot);if(ft===at&&dt===_t)return o(ft,Z.slice(Et,st-ot),it.slice(Et,pt-ot),dt)}}return null})(a,A,x);if(X)return X}var W=tt(a,A),J=a.substring(0,W);W=V(a=a.substring(W),A=A.substring(W));var rt=a.substring(a.length-W),lt=(function(Z,it){var gt;if(!Z)return[[1,it]];if(!it)return[[y,Z]];var ht=Z.length>it.length?Z:it,mt=Z.length>it.length?it:Z,st=ht.indexOf(mt);if(st!==-1)return gt=[[1,ht.substring(0,st)],[0,mt],[1,ht.substring(st+mt.length)]],Z.length>it.length&&(gt[0][0]=gt[2][0]=y),gt;if(mt.length===1)return[[y,Z],[1,it]];var pt=(function(ut,bt){var ot=ut.length>bt.length?ut:bt,ft=ut.length>bt.length?bt:ut;if(ot.length<4||2*ft.length<ot.length)return null;function dt(Dt,Ot,Ut){for(var Kt,wt,Rt,St,jt=Dt.substring(Ut,Ut+Math.floor(Dt.length/4)),yt=-1,Ct="";(yt=Ot.indexOf(jt,yt+1))!==-1;){var qt=tt(Dt.substring(Ut),Ot.substring(yt)),Ht=V(Dt.substring(0,Ut),Ot.substring(0,yt));Ct.length<Ht+qt&&(Ct=Ot.substring(yt-Ht,yt)+Ot.substring(yt,yt+qt),Kt=Dt.substring(0,Ut-Ht),wt=Dt.substring(Ut+qt),Rt=Ot.substring(0,yt-Ht),St=Ot.substring(yt+qt))}return 2*Ct.length>=Dt.length?[Kt,wt,Rt,St,Ct]:null}var at,_t,Lt,kt,Pt,Mt=dt(ot,ft,Math.ceil(ot.length/4)),Ft=dt(ot,ft,Math.ceil(ot.length/2));return Mt||Ft?(at=Ft?Mt&&Mt[4].length>Ft[4].length?Mt:Ft:Mt,ut.length>bt.length?(_t=at[0],Lt=at[1],kt=at[2],Pt=at[3]):(kt=at[0],Pt=at[1],_t=at[2],Lt=at[3]),[_t,Lt,kt,Pt,at[4]]):null})(Z,it);if(pt){var At=pt[0],vt=pt[1],xt=pt[2],Tt=pt[3],Nt=pt[4],Bt=S(At,xt),Et=S(vt,Tt);return Bt.concat([[0,Nt]],Et)}return(function(ut,bt){for(var ot=ut.length,ft=bt.length,dt=Math.ceil((ot+ft)/2),at=dt,_t=2*dt,Lt=new Array(_t),kt=new Array(_t),Pt=0;Pt<_t;Pt++)Lt[Pt]=-1,kt[Pt]=-1;Lt[at+1]=0,kt[at+1]=0;for(var Mt=ot-ft,Ft=Mt%2!=0,Dt=0,Ot=0,Ut=0,Kt=0,wt=0;wt<dt;wt++){for(var Rt=-wt+Dt;Rt<=wt-Ot;Rt+=2){for(var St=at+Rt,jt=($t=Rt===-wt||Rt!==wt&&Lt[St-1]<Lt[St+1]?Lt[St+1]:Lt[St-1]+1)-Rt;$t<ot&&jt<ft&&ut.charAt($t)===bt.charAt(jt);)$t++,jt++;if(Lt[St]=$t,$t>ot)Ot+=2;else if(jt>ft)Dt+=2;else if(Ft&&(qt=at+Mt-Rt)>=0&&qt<_t&&kt[qt]!==-1&&$t>=(Ct=ot-kt[qt]))return O(ut,bt,$t,jt)}for(var yt=-wt+Ut;yt<=wt-Kt;yt+=2){for(var Ct,qt=at+yt,Ht=(Ct=yt===-wt||yt!==wt&&kt[qt-1]<kt[qt+1]?kt[qt+1]:kt[qt-1]+1)-yt;Ct<ot&&Ht<ft&&ut.charAt(ot-Ct-1)===bt.charAt(ft-Ht-1);)Ct++,Ht++;if(kt[qt]=Ct,Ct>ot)Kt+=2;else if(Ht>ft)Ut+=2;else if(!Ft){var $t;if((St=at+Mt-yt)>=0&&St<_t&&Lt[St]!==-1&&(jt=at+($t=Lt[St])-St,$t>=(Ct=ot-Ct)))return O(ut,bt,$t,jt)}}}return[[y,ut],[1,bt]]})(Z,it)})(a=a.substring(0,a.length-W),A=A.substring(0,A.length-W));return J&&lt.unshift([0,J]),rt&&lt.push([0,rt]),c(lt,$),b&&(function(Z){for(var it=!1,gt=[],ht=0,mt=null,st=0,pt=0,At=0,vt=0,xt=0;st<Z.length;)Z[st][0]==0?(gt[ht++]=st,pt=vt,At=xt,vt=0,xt=0,mt=Z[st][1]):(Z[st][0]==1?vt+=Z[st][1].length:xt+=Z[st][1].length,mt&&mt.length<=Math.max(pt,At)&&mt.length<=Math.max(vt,xt)&&(Z.splice(gt[ht-1],0,[y,mt]),Z[gt[ht-1]+1][0]=1,ht--,st=--ht>0?gt[ht-1]:-1,pt=0,At=0,vt=0,xt=0,mt=null,it=!0)),st++;for(it&&c(Z),(function(ut){function bt(Ot,Ut){if(!Ot||!Ut)return 6;var Kt=Ot.charAt(Ot.length-1),wt=Ut.charAt(0),Rt=Kt.match(d),St=wt.match(d),jt=Rt&&Kt.match(e),yt=St&&wt.match(e),Ct=jt&&Kt.match(t),qt=yt&&wt.match(t),Ht=Ct&&Ot.match(s),$t=qt&&Ut.match(r);return Ht||$t?5:Ct||qt?4:Rt&&!jt&&yt?3:jt||yt?2:Rt||St?1:0}for(var ot=1;ot<ut.length-1;){if(ut[ot-1][0]==0&&ut[ot+1][0]==0){var ft=ut[ot-1][1],dt=ut[ot][1],at=ut[ot+1][1],_t=V(ft,dt);if(_t){var Lt=dt.substring(dt.length-_t);ft=ft.substring(0,ft.length-_t),dt=Lt+dt.substring(0,dt.length-_t),at=Lt+at}for(var kt=ft,Pt=dt,Mt=at,Ft=bt(ft,dt)+bt(dt,at);dt.charAt(0)===at.charAt(0);){ft+=dt.charAt(0),dt=dt.substring(1)+at.charAt(0),at=at.substring(1);var Dt=bt(ft,dt)+bt(dt,at);Dt>=Ft&&(Ft=Dt,kt=ft,Pt=dt,Mt=at)}ut[ot-1][1]!=kt&&(kt?ut[ot-1][1]=kt:(ut.splice(ot-1,1),ot--),ut[ot][1]=Pt,Mt?ut[ot+1][1]=Mt:(ut.splice(ot+1,1),ot--))}ot++}})(Z),st=1;st<Z.length;){if(Z[st-1][0]==y&&Z[st][0]==1){var Tt=Z[st-1][1],Nt=Z[st][1],Bt=P(Tt,Nt),Et=P(Nt,Tt);Bt>=Et?(Bt>=Tt.length/2||Bt>=Nt.length/2)&&(Z.splice(st,0,[0,Nt.substring(0,Bt)]),Z[st-1][1]=Tt.substring(0,Tt.length-Bt),Z[st+1][1]=Nt.substring(Bt),st++):(Et>=Tt.length/2||Et>=Nt.length/2)&&(Z.splice(st,0,[0,Tt.substring(0,Et)]),Z[st-1][0]=1,Z[st-1][1]=Nt.substring(0,Nt.length-Et),Z[st+1][0]=y,Z[st+1][1]=Tt.substring(Et),st++),st++}st++}})(lt),lt}function O(a,A,x,b){var $=a.substring(0,x),X=A.substring(0,b),W=a.substring(x),J=A.substring(b),rt=S($,X),lt=S(W,J);return rt.concat(lt)}function tt(a,A){if(!a||!A||a.charAt(0)!==A.charAt(0))return 0;for(var x=0,b=Math.min(a.length,A.length),$=b,X=0;x<$;)a.substring(X,$)==A.substring(X,$)?X=x=$:b=$,$=Math.floor((b-x)/2+x);return h(a.charCodeAt($-1))&&$--,$}function P(a,A){var x=a.length,b=A.length;if(x==0||b==0)return 0;x>b?a=a.substring(x-b):x<b&&(A=A.substring(0,x));var $=Math.min(x,b);if(a==A)return $;for(var X=0,W=1;;){var J=a.substring($-W),rt=A.indexOf(J);if(rt==-1)return X;W+=rt,rt!=0&&a.substring($-W)!=A.substring(0,W)||(X=W,W++)}}function V(a,A){if(!a||!A||a.slice(-1)!==A.slice(-1))return 0;for(var x=0,b=Math.min(a.length,A.length),$=b,X=0;x<$;)a.substring(a.length-$,a.length-X)==A.substring(A.length-$,A.length-X)?X=x=$:b=$,$=Math.floor((b-x)/2+x);return i(a.charCodeAt(a.length-$))&&$--,$}var d=/[^a-zA-Z0-9]/,e=/\s/,t=/[\r\n]/,s=/\n\r?\n$/,r=/^\r?\n\r?\n/;function c(a,A){a.push([0,""]);for(var x,b=0,$=0,X=0,W="",J="";b<a.length;)if(b<a.length-1&&!a[b][1])a.splice(b,1);else switch(a[b][0]){case 1:X++,J+=a[b][1],b++;break;case y:$++,W+=a[b][1],b++;break;case 0:var rt=b-X-$-1;if(A){if(rt>=0&&l(a[rt][1])){var lt=a[rt][1].slice(-1);if(a[rt][1]=a[rt][1].slice(0,-1),W=lt+W,J=lt+J,!a[rt][1]){a.splice(rt,1),b--;var Z=rt-1;a[Z]&&a[Z][0]===1&&(X++,J=a[Z][1]+J,Z--),a[Z]&&a[Z][0]===y&&($++,W=a[Z][1]+W,Z--),rt=Z}}n(a[b][1])&&(lt=a[b][1].charAt(0),a[b][1]=a[b][1].slice(1),W+=lt,J+=lt)}if(b<a.length-1&&!a[b][1]){a.splice(b,1);break}if(W.length>0||J.length>0){W.length>0&&J.length>0&&((x=tt(J,W))!==0&&(rt>=0?a[rt][1]+=J.substring(0,x):(a.splice(0,0,[0,J.substring(0,x)]),b++),J=J.substring(x),W=W.substring(x)),(x=V(J,W))!==0&&(a[b][1]=J.substring(J.length-x)+a[b][1],J=J.substring(0,J.length-x),W=W.substring(0,W.length-x)));var it=X+$;W.length===0&&J.length===0?(a.splice(b-it,it),b-=it):W.length===0?(a.splice(b-it,it,[1,J]),b=b-it+1):J.length===0?(a.splice(b-it,it,[y,W]),b=b-it+1):(a.splice(b-it,it,[y,W],[1,J]),b=b-it+2)}b!==0&&a[b-1][0]===0?(a[b-1][1]+=a[b][1],a.splice(b,1)):b++,X=0,$=0,W="",J=""}a[a.length-1][1]===""&&a.pop();var gt=!1;for(b=1;b<a.length-1;)a[b-1][0]===0&&a[b+1][0]===0&&(a[b][1].substring(a[b][1].length-a[b-1][1].length)===a[b-1][1]?(a[b][1]=a[b-1][1]+a[b][1].substring(0,a[b][1].length-a[b-1][1].length),a[b+1][1]=a[b-1][1]+a[b+1][1],a.splice(b-1,1),gt=!0):a[b][1].substring(0,a[b+1][1].length)==a[b+1][1]&&(a[b-1][1]+=a[b+1][1],a[b][1]=a[b][1].substring(a[b+1][1].length)+a[b+1][1],a.splice(b+1,1),gt=!0)),b++;gt&&c(a,A)}function h(a){return a>=55296&&a<=56319}function i(a){return a>=56320&&a<=57343}function n(a){return i(a.charCodeAt(0))}function l(a){return h(a.charCodeAt(a.length-1))}function o(a,A,x,b){return l(a)||n(b)?null:(function($){for(var X=[],W=0;W<$.length;W++)$[W][1].length>0&&X.push($[W]);return X})([[0,a],[y,A],[1,x],[0,b]])}function u(a,A,x,b){return S(a,A,x,b,!0)}u.INSERT=1,u.DELETE=y,u.EQUAL=0,g.exports=u}},function(){return v||(0,m[B(m)[0]])((v={exports:{}}).exports,v),v.exports})()),f=function(M){return JSON.parse(JSON.stringify(M))};function T(M){return M!==Object(M)}var _,L,H=function M(g,y){if(g===y)return!0;if(T(g)||T(y))return g===y;if(Object.keys(g).length!==Object.keys(y).length)return!1;for(let S in g)if(!(S in y)||!M(g[S],y[S]))return!1;return!0};(L=_||(_={})).compose=function(M={},g={},y=!1){typeof M!="object"&&(M={}),typeof g!="object"&&(g={});let S=f(g);y||(S=Object.keys(S).reduce(((O,tt)=>(S[tt]!=null&&(O[tt]=S[tt]),O)),{}));for(const O in M)M[O]!==void 0&&g[O]===void 0&&(S[O]=M[O]);return Object.keys(S).length>0?S:void 0},L.diff=function(M={},g={}){typeof M!="object"&&(M={}),typeof g!="object"&&(g={});const y=Object.keys(M).concat(Object.keys(g)).reduce(((S,O)=>(H(M[O],g[O])||(S[O]=g[O]===void 0?null:g[O]),S)),{});return Object.keys(y).length>0?y:void 0},L.invert=function(M={},g={}){M=M||{};const y=Object.keys(g).reduce(((S,O)=>(g[O]!==M[O]&&M[O]!==void 0&&(S[O]=g[O]),S)),{});return Object.keys(M).reduce(((S,O)=>(M[O]!==g[O]&&g[O]===void 0&&(S[O]=null),S)),y)},L.transform=function(M,g,y=!1){if(typeof M!="object")return g;if(typeof g!="object")return;if(!y)return g;const S=Object.keys(g).reduce(((O,tt)=>(M[tt]===void 0&&(O[tt]=g[tt]),O)),{});return Object.keys(S).length>0?S:void 0};var G,I=_;(G||(G={})).length=function(M){return typeof M.delete=="number"?M.delete:typeof M.retain=="number"?M.retain:typeof M.retain=="object"&&M.retain!==null?1:typeof M.insert=="string"?M.insert.length:1};var k=G,N=class{ops;index;offset;constructor(M){this.ops=M,this.index=0,this.offset=0}hasNext(){return this.peekLength()<1/0}next(M){M||(M=1/0);const g=this.ops[this.index];if(g){const y=this.offset,S=k.length(g);if(M>=S-y?(M=S-y,this.index+=1,this.offset=0):this.offset+=M,typeof g.delete=="number")return{delete:M};{const O={};return g.attributes&&(O.attributes=g.attributes),typeof g.retain=="number"?O.retain=M:typeof g.retain=="object"&&g.retain!==null?O.retain=g.retain:typeof g.insert=="string"?O.insert=g.insert.substr(y,M):O.insert=g.insert,O}}return{retain:1/0}}peek(){return this.ops[this.index]}peekLength(){return this.ops[this.index]?k.length(this.ops[this.index])-this.offset:1/0}peekType(){const M=this.ops[this.index];return M?typeof M.delete=="number"?"delete":typeof M.retain=="number"||typeof M.retain=="object"&&M.retain!==null?"retain":"insert":"retain"}rest(){if(this.hasNext()){if(this.offset===0)return this.ops.slice(this.index);{const M=this.offset,g=this.index,y=this.next(),S=this.ops.slice(this.index);return this.offset=M,this.index=g,[y].concat(S)}}return[]}},F="\0",z=(M,g)=>{if(typeof M!="object"||M===null)throw new Error("cannot retain a "+typeof M);if(typeof g!="object"||g===null)throw new Error("cannot retain a "+typeof g);const y=Object.keys(M)[0];if(!y||y!==Object.keys(g)[0])throw new Error(`embed types not matched: ${y} != ${Object.keys(g)[0]}`);return[y,M[y],g[y]]},K=class It{static Op=k;static OpIterator=N;static AttributeMap=I;static handlers={};static registerEmbed(g,y){this.handlers[g]=y}static unregisterEmbed(g){delete this.handlers[g]}static getHandler(g){const y=this.handlers[g];if(!y)throw new Error(`no handlers for embed type "${g}"`);return y}ops;inverted;constructor(g){Array.isArray(g)?this.ops=g:g!=null&&Array.isArray(g.ops)?(this.ops=g.ops,this.inverted=g.inverted):this.ops=[]}insert(g,y){const S={};return typeof g=="string"&&g.length===0?this:(S.insert=g,y!=null&&typeof y=="object"&&Object.keys(y).length>0&&(S.attributes=y),this.push(S))}delete(g){return g<=0?this:this.push({delete:g})}retain(g,y){if(typeof g=="number"&&g<=0)return this;const S={retain:g};return y!=null&&typeof y=="object"&&Object.keys(y).length>0&&(S.attributes=y),this.push(S)}push(g){let y=this.ops.length,S=this.ops[y-1];if(g=f(g),typeof S=="object"){if(typeof g.delete=="number"&&typeof S.delete=="number")return this.ops[y-1]={delete:S.delete+g.delete},this;if(typeof S.delete=="number"&&g.insert!=null&&(y-=1,S=this.ops[y-1],typeof S!="object"))return this.ops.unshift(g),this;if(H(g.attributes,S.attributes)){if(typeof g.insert=="string"&&typeof S.insert=="string")return this.ops[y-1]={insert:S.insert+g.insert},typeof g.attributes=="object"&&(this.ops[y-1].attributes=g.attributes),this;if(typeof g.retain=="number"&&typeof S.retain=="number")return this.ops[y-1]={retain:S.retain+g.retain},typeof g.attributes=="object"&&(this.ops[y-1].attributes=g.attributes),this}}return y===this.ops.length?this.ops.push(g):this.ops.splice(y,0,g),this}chop(){const g=this.ops[this.ops.length-1];return g&&typeof g.retain=="number"&&!g.attributes&&this.ops.pop(),this}filter(g){return this.ops.filter(g)}forEach(g){this.ops.forEach(g)}map(g){return this.ops.map(g)}partition(g){const y=[],S=[];return this.forEach((O=>{(g(O)?y:S).push(O)})),[y,S]}reduce(g,y){return this.ops.reduce(g,y)}changeLength(){return this.reduce(((g,y)=>y.insert?g+k.length(y):y.delete?g-y.delete:g),0)}length(){return this.reduce(((g,y)=>g+k.length(y)),0)}slice(g=0,y=1/0){const S=[],O=new N(this.ops);let tt=0;for(;tt<y&&O.hasNext();){let P;tt<g?P=O.next(g-tt):(P=O.next(y-tt),S.push(P)),tt+=k.length(P)}return new It(S)}compose(g){const y=new N(this.ops),S=new N(g.ops),O=[],tt=S.peek();if(tt!=null&&typeof tt.retain=="number"&&tt.attributes==null){let V=tt.retain;for(;y.peekType()==="insert"&&y.peekLength()<=V;)V-=y.peekLength(),O.push(y.next());tt.retain-V>0&&S.next(tt.retain-V)}const P=new It(O);for(;y.hasNext()||S.hasNext();)if(S.peekType()==="insert")P.push(S.next());else if(y.peekType()==="delete")P.push(y.next());else{const V=Math.min(y.peekLength(),S.peekLength()),d=y.next(V),e=S.next(V);if(e.retain){const t={};if(typeof d.retain=="number")t.retain=typeof e.retain=="number"?V:e.retain;else if(typeof e.retain=="number")d.retain==null?t.insert=d.insert:t.retain=d.retain;else{const r=d.retain==null?"insert":"retain",[c,h,i]=z(d[r],e.retain),n=It.getHandler(c);t[r]={[c]:n.compose(h,i,r==="retain")}}const s=I.compose(d.attributes,e.attributes,typeof d.retain=="number");if(s&&(t.attributes=s),P.push(t),!S.hasNext()&&H(P.ops[P.ops.length-1],t)){const r=new It(y.rest());return P.concat(r).chop()}}else typeof e.delete=="number"&&(typeof d.retain=="number"||typeof d.retain=="object"&&d.retain!==null)&&P.push(e)}return P.chop()}concat(g){const y=new It(this.ops.slice());return g.ops.length>0&&(y.push(g.ops[0]),y.ops=y.ops.concat(g.ops.slice(1))),y}diff(g,y){if(this.ops===g.ops)return new It;const S=[this,g].map((d=>d.map((e=>{if(e.insert!=null)return typeof e.insert=="string"?e.insert:F;throw new Error("diff() called "+(d===g?"on":"with")+" non-document")})).join(""))),O=new It,tt=(0,R.default)(S[0],S[1],y,!0),P=new N(this.ops),V=new N(g.ops);return tt.forEach((d=>{let e=d[1].length;for(;e>0;){let t=0;switch(d[0]){case R.default.INSERT:t=Math.min(V.peekLength(),e),O.push(V.next(t));break;case R.default.DELETE:t=Math.min(e,P.peekLength()),P.next(t),O.delete(t);break;case R.default.EQUAL:t=Math.min(P.peekLength(),V.peekLength(),e);const s=P.next(t),r=V.next(t);H(s.insert,r.insert)?O.retain(t,I.diff(s.attributes,r.attributes)):O.push(r).delete(t)}e-=t}})),O.chop()}eachLine(g,y=`
`){const S=new N(this.ops);let O=new It,tt=0;for(;S.hasNext();){if(S.peekType()!=="insert")return;const P=S.peek(),V=k.length(P)-S.peekLength(),d=typeof P.insert=="string"?P.insert.indexOf(y,V)-V:-1;if(d<0)O.push(S.next());else if(d>0)O.push(S.next(d));else{if(g(O,S.next(1).attributes||{},tt)===!1)return;tt+=1,O=new It}}O.length()>0&&g(O,{},tt)}invert(g){const y=new It;return this.reduce(((S,O)=>{if(O.insert)y.delete(k.length(O));else{if(typeof O.retain=="number"&&O.attributes==null)return y.retain(O.retain),S+O.retain;if(O.delete||typeof O.retain=="number"){const tt=O.delete||O.retain;return g.slice(S,S+tt).forEach((P=>{O.delete?y.push(P):O.retain&&O.attributes&&y.retain(k.length(P),I.invert(O.attributes,P.attributes))})),S+tt}if(typeof O.retain=="object"&&O.retain!==null){const tt=g.slice(S,S+1),P=new N(tt.ops).next(),[V,d,e]=z(O.retain,P.insert),t=It.getHandler(V);return y.retain({[V]:t.invert(d,e)},I.invert(O.attributes,P.attributes)),S+1}}return S}),0),y.chop()}transform(g,y=!1){if(y=!!y,typeof g=="number")return this.transformPosition(g,y);const S=g,O=new N(this.ops),tt=new N(S.ops),P=new It;for(;O.hasNext()||tt.hasNext();)if(O.peekType()!=="insert"||!y&&tt.peekType()==="insert")if(tt.peekType()==="insert")P.push(tt.next());else{const V=Math.min(O.peekLength(),tt.peekLength()),d=O.next(V),e=tt.next(V);if(d.delete)continue;if(e.delete)P.push(e);else{const t=d.retain,s=e.retain;let r=typeof s=="object"&&s!==null?s:V;if(typeof t=="object"&&t!==null&&typeof s=="object"&&s!==null){const c=Object.keys(t)[0];if(c===Object.keys(s)[0]){const h=It.getHandler(c);h&&(r={[c]:h.transform(t[c],s[c],y)})}}P.retain(r,I.transform(d.attributes,e.attributes,y))}}else P.retain(k.length(O.next()));return P.chop()}transformPosition(g,y=!1){y=!!y;const S=new N(this.ops);let O=0;for(;S.hasNext()&&O<=g;){const tt=S.peekLength(),P=S.peekType();S.next(),P!=="delete"?(P==="insert"&&(O<g||!y)&&(g+=tt),O+=tt):g-=Math.min(tt,g-O)}return g}},nt=K;Wt.exports=K,Wt.exports.default=K},3:function(j,U,p){p.r(U),p.d(U,{Attributor:function(){return v},AttributorStore:function(){return f},BlockBlot:function(){return nt},ClassAttributor:function(){return C},ContainerBlot:function(){return g},EmbedBlot:function(){return y},InlineBlot:function(){return z},LeafBlot:function(){return H},ParentBlot:function(){return N},Registry:function(){return et},Scope:function(){return m},ScrollBlot:function(){return tt},StyleAttributor:function(){return R},TextBlot:function(){return V}});var m=(d=>(d[d.TYPE=3]="TYPE",d[d.LEVEL=12]="LEVEL",d[d.ATTRIBUTE=13]="ATTRIBUTE",d[d.BLOT=14]="BLOT",d[d.INLINE=7]="INLINE",d[d.BLOCK=11]="BLOCK",d[d.BLOCK_BLOT=10]="BLOCK_BLOT",d[d.INLINE_BLOT=6]="INLINE_BLOT",d[d.BLOCK_ATTRIBUTE=9]="BLOCK_ATTRIBUTE",d[d.INLINE_ATTRIBUTE=5]="INLINE_ATTRIBUTE",d[d.ANY=15]="ANY",d))(m||{});class v{constructor(e,t,s={}){this.attrName=e,this.keyName=t;const r=m.TYPE&m.ATTRIBUTE;this.scope=s.scope!=null?s.scope&m.LEVEL|r:m.ATTRIBUTE,s.whitelist!=null&&(this.whitelist=s.whitelist)}static keys(e){return Array.from(e.attributes).map((t=>t.name))}add(e,t){return!!this.canAdd(e,t)&&(e.setAttribute(this.keyName,t),!0)}canAdd(e,t){return this.whitelist==null||(typeof t=="string"?this.whitelist.indexOf(t.replace(/["']/g,""))>-1:this.whitelist.indexOf(t)>-1)}remove(e){e.removeAttribute(this.keyName)}value(e){const t=e.getAttribute(this.keyName);return this.canAdd(e,t)&&t?t:""}}class w extends Error{constructor(e){super(e="[Parchment] "+e),this.message=e,this.name=this.constructor.name}}const Y=class te{constructor(){this.attributes={},this.classes={},this.tags={},this.types={}}static find(e,t=!1){if(e==null)return null;if(this.blots.has(e))return this.blots.get(e)||null;if(t){let s=null;try{s=e.parentNode}catch{return null}return this.find(s,t)}return null}create(e,t,s){const r=this.query(t);if(r==null)throw new w(`Unable to create ${t} blot`);const c=r,h=t instanceof Node||t.nodeType===Node.TEXT_NODE?t:c.create(s),i=new c(e,h,s);return te.blots.set(i.domNode,i),i}find(e,t=!1){return te.find(e,t)}query(e,t=m.ANY){let s;return typeof e=="string"?s=this.types[e]||this.attributes[e]:e instanceof Text||e.nodeType===Node.TEXT_NODE?s=this.types.text:typeof e=="number"?e&m.LEVEL&m.BLOCK?s=this.types.block:e&m.LEVEL&m.INLINE&&(s=this.types.inline):e instanceof Element&&((e.getAttribute("class")||"").split(/\s+/).some((r=>(s=this.classes[r],!!s))),s=s||this.tags[e.tagName]),s==null?null:"scope"in s&&t&m.LEVEL&s.scope&&t&m.TYPE&s.scope?s:null}register(...e){return e.map((t=>{const s="blotName"in t,r="attrName"in t;if(!s&&!r)throw new w("Invalid definition");if(s&&t.blotName==="abstract")throw new w("Cannot register abstract class");const c=s?t.blotName:r?t.attrName:void 0;return this.types[c]=t,r?typeof t.keyName=="string"&&(this.attributes[t.keyName]=t):s&&(t.className&&(this.classes[t.className]=t),t.tagName&&(Array.isArray(t.tagName)?t.tagName=t.tagName.map((h=>h.toUpperCase())):t.tagName=t.tagName.toUpperCase(),(Array.isArray(t.tagName)?t.tagName:[t.tagName]).forEach((h=>{(this.tags[h]==null||t.className==null)&&(this.tags[h]=t)})))),t}))}};Y.blots=new WeakMap;let et=Y;function B(d,e){return(d.getAttribute("class")||"").split(/\s+/).filter((t=>t.indexOf(`${e}-`)===0))}const C=class extends v{static keys(d){return(d.getAttribute("class")||"").split(/\s+/).map((e=>e.split("-").slice(0,-1).join("-")))}add(d,e){return!!this.canAdd(d,e)&&(this.remove(d),d.classList.add(`${this.keyName}-${e}`),!0)}remove(d){B(d,this.keyName).forEach((e=>{d.classList.remove(e)})),d.classList.length===0&&d.removeAttribute("class")}value(d){const e=(B(d,this.keyName)[0]||"").slice(this.keyName.length+1);return this.canAdd(d,e)?e:""}};function q(d){const e=d.split("-"),t=e.slice(1).map((s=>s[0].toUpperCase()+s.slice(1))).join("");return e[0]+t}const R=class extends v{static keys(d){return(d.getAttribute("style")||"").split(";").map((e=>e.split(":")[0].trim()))}add(d,e){return!!this.canAdd(d,e)&&(d.style[q(this.keyName)]=e,!0)}remove(d){d.style[q(this.keyName)]="",d.getAttribute("style")||d.removeAttribute("style")}value(d){const e=d.style[q(this.keyName)];return this.canAdd(d,e)?e:""}},f=class{constructor(d){this.attributes={},this.domNode=d,this.build()}attribute(d,e){e?d.add(this.domNode,e)&&(d.value(this.domNode)!=null?this.attributes[d.attrName]=d:delete this.attributes[d.attrName]):(d.remove(this.domNode),delete this.attributes[d.attrName])}build(){this.attributes={};const d=et.find(this.domNode);if(d==null)return;const e=v.keys(this.domNode),t=C.keys(this.domNode),s=R.keys(this.domNode);e.concat(t).concat(s).forEach((r=>{const c=d.scroll.query(r,m.ATTRIBUTE);c instanceof v&&(this.attributes[c.attrName]=c)}))}copy(d){Object.keys(this.attributes).forEach((e=>{const t=this.attributes[e].value(this.domNode);d.format(e,t)}))}move(d){this.copy(d),Object.keys(this.attributes).forEach((e=>{this.attributes[e].remove(this.domNode)})),this.attributes={}}values(){return Object.keys(this.attributes).reduce(((d,e)=>(d[e]=this.attributes[e].value(this.domNode),d)),{})}},T=class{constructor(d,e){this.scroll=d,this.domNode=e,et.blots.set(e,this),this.prev=null,this.next=null}static create(d){if(this.tagName==null)throw new w("Blot definition missing tagName");let e,t;return Array.isArray(this.tagName)?(typeof d=="string"?(t=d.toUpperCase(),parseInt(t,10).toString()===t&&(t=parseInt(t,10))):typeof d=="number"&&(t=d),e=typeof t=="number"?document.createElement(this.tagName[t-1]):t&&this.tagName.indexOf(t)>-1?document.createElement(t):document.createElement(this.tagName[0])):e=document.createElement(this.tagName),this.className&&e.classList.add(this.className),e}get statics(){return this.constructor}attach(){}clone(){const d=this.domNode.cloneNode(!1);return this.scroll.create(d)}detach(){this.parent!=null&&this.parent.removeChild(this),et.blots.delete(this.domNode)}deleteAt(d,e){this.isolate(d,e).remove()}formatAt(d,e,t,s){const r=this.isolate(d,e);if(this.scroll.query(t,m.BLOT)!=null&&s)r.wrap(t,s);else if(this.scroll.query(t,m.ATTRIBUTE)!=null){const c=this.scroll.create(this.statics.scope);r.wrap(c),c.format(t,s)}}insertAt(d,e,t){const s=t==null?this.scroll.create("text",e):this.scroll.create(e,t),r=this.split(d);this.parent.insertBefore(s,r||void 0)}isolate(d,e){const t=this.split(d);if(t==null)throw new Error("Attempt to isolate at end");return t.split(e),t}length(){return 1}offset(d=this.parent){return this.parent==null||this===d?0:this.parent.children.offset(this)+this.parent.offset(d)}optimize(d){this.statics.requiredContainer&&!(this.parent instanceof this.statics.requiredContainer)&&this.wrap(this.statics.requiredContainer.blotName)}remove(){this.domNode.parentNode!=null&&this.domNode.parentNode.removeChild(this.domNode),this.detach()}replaceWith(d,e){const t=typeof d=="string"?this.scroll.create(d,e):d;return this.parent!=null&&(this.parent.insertBefore(t,this.next||void 0),this.remove()),t}split(d,e){return d===0?this:this.next}update(d,e){}wrap(d,e){const t=typeof d=="string"?this.scroll.create(d,e):d;if(this.parent!=null&&this.parent.insertBefore(t,this.next||void 0),typeof t.appendChild!="function")throw new w(`Cannot wrap ${d}`);return t.appendChild(this),t}};T.blotName="abstract";let _=T;const L=class extends _{static value(d){return!0}index(d,e){return this.domNode===d||this.domNode.compareDocumentPosition(d)&Node.DOCUMENT_POSITION_CONTAINED_BY?Math.min(e,1):-1}position(d,e){let t=Array.from(this.parent.domNode.childNodes).indexOf(this.domNode);return d>0&&(t+=1),[this.parent.domNode,t]}value(){return{[this.statics.blotName]:this.statics.value(this.domNode)||!0}}};L.scope=m.INLINE_BLOT;const H=L;class G{constructor(){this.head=null,this.tail=null,this.length=0}append(...e){if(this.insertBefore(e[0],null),e.length>1){const t=e.slice(1);this.append(...t)}}at(e){const t=this.iterator();let s=t();for(;s&&e>0;)e-=1,s=t();return s}contains(e){const t=this.iterator();let s=t();for(;s;){if(s===e)return!0;s=t()}return!1}indexOf(e){const t=this.iterator();let s=t(),r=0;for(;s;){if(s===e)return r;r+=1,s=t()}return-1}insertBefore(e,t){e!=null&&(this.remove(e),e.next=t,t!=null?(e.prev=t.prev,t.prev!=null&&(t.prev.next=e),t.prev=e,t===this.head&&(this.head=e)):this.tail!=null?(this.tail.next=e,e.prev=this.tail,this.tail=e):(e.prev=null,this.head=this.tail=e),this.length+=1)}offset(e){let t=0,s=this.head;for(;s!=null;){if(s===e)return t;t+=s.length(),s=s.next}return-1}remove(e){this.contains(e)&&(e.prev!=null&&(e.prev.next=e.next),e.next!=null&&(e.next.prev=e.prev),e===this.head&&(this.head=e.next),e===this.tail&&(this.tail=e.prev),this.length-=1)}iterator(e=this.head){return()=>{const t=e;return e!=null&&(e=e.next),t}}find(e,t=!1){const s=this.iterator();let r=s();for(;r;){const c=r.length();if(e<c||t&&e===c&&(r.next==null||r.next.length()!==0))return[r,e];e-=c,r=s()}return[null,0]}forEach(e){const t=this.iterator();let s=t();for(;s;)e(s),s=t()}forEachAt(e,t,s){if(t<=0)return;const[r,c]=this.find(e);let h=e-c;const i=this.iterator(r);let n=i();for(;n&&h<e+t;){const l=n.length();e>h?s(n,e-h,Math.min(t,h+l-e)):s(n,0,Math.min(l,e+t-h)),h+=l,n=i()}}map(e){return this.reduce(((t,s)=>(t.push(e(s)),t)),[])}reduce(e,t){const s=this.iterator();let r=s();for(;r;)t=e(t,r),r=s();return t}}function I(d,e){const t=e.find(d);if(t)return t;try{return e.create(d)}catch{const s=e.create(m.INLINE);return Array.from(d.childNodes).forEach((r=>{s.domNode.appendChild(r)})),d.parentNode&&d.parentNode.replaceChild(s.domNode,d),s.attach(),s}}const k=class Gt extends _{constructor(e,t){super(e,t),this.uiNode=null,this.build()}appendChild(e){this.insertBefore(e)}attach(){super.attach(),this.children.forEach((e=>{e.attach()}))}attachUI(e){this.uiNode!=null&&this.uiNode.remove(),this.uiNode=e,Gt.uiClass&&this.uiNode.classList.add(Gt.uiClass),this.uiNode.setAttribute("contenteditable","false"),this.domNode.insertBefore(this.uiNode,this.domNode.firstChild)}build(){this.children=new G,Array.from(this.domNode.childNodes).filter((e=>e!==this.uiNode)).reverse().forEach((e=>{try{const t=I(e,this.scroll);this.insertBefore(t,this.children.head||void 0)}catch(t){if(t instanceof w)return;throw t}}))}deleteAt(e,t){if(e===0&&t===this.length())return this.remove();this.children.forEachAt(e,t,((s,r,c)=>{s.deleteAt(r,c)}))}descendant(e,t=0){const[s,r]=this.children.find(t);return e.blotName==null&&e(s)||e.blotName!=null&&s instanceof e?[s,r]:s instanceof Gt?s.descendant(e,r):[null,-1]}descendants(e,t=0,s=Number.MAX_VALUE){let r=[],c=s;return this.children.forEachAt(t,s,((h,i,n)=>{(e.blotName==null&&e(h)||e.blotName!=null&&h instanceof e)&&r.push(h),h instanceof Gt&&(r=r.concat(h.descendants(e,i,c))),c-=n})),r}detach(){this.children.forEach((e=>{e.detach()})),super.detach()}enforceAllowedChildren(){let e=!1;this.children.forEach((t=>{e||this.statics.allowedChildren.some((s=>t instanceof s))||(t.statics.scope===m.BLOCK_BLOT?(t.next!=null&&this.splitAfter(t),t.prev!=null&&this.splitAfter(t.prev),t.parent.unwrap(),e=!0):t instanceof Gt?t.unwrap():t.remove())}))}formatAt(e,t,s,r){this.children.forEachAt(e,t,((c,h,i)=>{c.formatAt(h,i,s,r)}))}insertAt(e,t,s){const[r,c]=this.children.find(e);if(r)r.insertAt(c,t,s);else{const h=s==null?this.scroll.create("text",t):this.scroll.create(t,s);this.appendChild(h)}}insertBefore(e,t){e.parent!=null&&e.parent.children.remove(e);let s=null;this.children.insertBefore(e,t||null),e.parent=this,t!=null&&(s=t.domNode),(this.domNode.parentNode!==e.domNode||this.domNode.nextSibling!==s)&&this.domNode.insertBefore(e.domNode,s),e.attach()}length(){return this.children.reduce(((e,t)=>e+t.length()),0)}moveChildren(e,t){this.children.forEach((s=>{e.insertBefore(s,t)}))}optimize(e){if(super.optimize(e),this.enforceAllowedChildren(),this.uiNode!=null&&this.uiNode!==this.domNode.firstChild&&this.domNode.insertBefore(this.uiNode,this.domNode.firstChild),this.children.length===0)if(this.statics.defaultChild!=null){const t=this.scroll.create(this.statics.defaultChild.blotName);this.appendChild(t)}else this.remove()}path(e,t=!1){const[s,r]=this.children.find(e,t),c=[[this,e]];return s instanceof Gt?c.concat(s.path(r,t)):(s!=null&&c.push([s,r]),c)}removeChild(e){this.children.remove(e)}replaceWith(e,t){const s=typeof e=="string"?this.scroll.create(e,t):e;return s instanceof Gt&&this.moveChildren(s),super.replaceWith(s)}split(e,t=!1){if(!t){if(e===0)return this;if(e===this.length())return this.next}const s=this.clone();return this.parent&&this.parent.insertBefore(s,this.next||void 0),this.children.forEachAt(e,this.length(),((r,c,h)=>{const i=r.split(c,t);i!=null&&s.appendChild(i)})),s}splitAfter(e){const t=this.clone();for(;e.next!=null;)t.appendChild(e.next);return this.parent&&this.parent.insertBefore(t,this.next||void 0),t}unwrap(){this.parent&&this.moveChildren(this.parent,this.next||void 0),this.remove()}update(e,t){const s=[],r=[];e.forEach((c=>{c.target===this.domNode&&c.type==="childList"&&(s.push(...c.addedNodes),r.push(...c.removedNodes))})),r.forEach((c=>{if(c.parentNode!=null&&c.tagName!=="IFRAME"&&document.body.compareDocumentPosition(c)&Node.DOCUMENT_POSITION_CONTAINED_BY)return;const h=this.scroll.find(c);h!=null&&(h.domNode.parentNode==null||h.domNode.parentNode===this.domNode)&&h.detach()})),s.filter((c=>c.parentNode===this.domNode&&c!==this.uiNode)).sort(((c,h)=>c===h?0:c.compareDocumentPosition(h)&Node.DOCUMENT_POSITION_FOLLOWING?1:-1)).forEach((c=>{let h=null;c.nextSibling!=null&&(h=this.scroll.find(c.nextSibling));const i=I(c,this.scroll);(i.next!==h||i.next==null)&&(i.parent!=null&&i.parent.removeChild(this),this.insertBefore(i,h||void 0))})),this.enforceAllowedChildren()}};k.uiClass="";const N=k,F=class Qt extends N{static create(e){return super.create(e)}static formats(e,t){const s=t.query(Qt.blotName);if(s==null||e.tagName!==s.tagName){if(typeof this.tagName=="string")return!0;if(Array.isArray(this.tagName))return e.tagName.toLowerCase()}}constructor(e,t){super(e,t),this.attributes=new f(this.domNode)}format(e,t){if(e!==this.statics.blotName||t){const s=this.scroll.query(e,m.INLINE);if(s==null)return;s instanceof v?this.attributes.attribute(s,t):t&&(e!==this.statics.blotName||this.formats()[e]!==t)&&this.replaceWith(e,t)}else this.children.forEach((s=>{s instanceof Qt||(s=s.wrap(Qt.blotName,!0)),this.attributes.copy(s)})),this.unwrap()}formats(){const e=this.attributes.values(),t=this.statics.formats(this.domNode,this.scroll);return t!=null&&(e[this.statics.blotName]=t),e}formatAt(e,t,s,r){this.formats()[s]!=null||this.scroll.query(s,m.ATTRIBUTE)?this.isolate(e,t).format(s,r):super.formatAt(e,t,s,r)}optimize(e){super.optimize(e);const t=this.formats();if(Object.keys(t).length===0)return this.unwrap();const s=this.next;s instanceof Qt&&s.prev===this&&(function(r,c){if(Object.keys(r).length!==Object.keys(c).length)return!1;for(const h in r)if(r[h]!==c[h])return!1;return!0})(t,s.formats())&&(s.moveChildren(this),s.remove())}replaceWith(e,t){const s=super.replaceWith(e,t);return this.attributes.copy(s),s}update(e,t){super.update(e,t),e.some((s=>s.target===this.domNode&&s.type==="attributes"))&&this.attributes.build()}wrap(e,t){const s=super.wrap(e,t);return s instanceof Qt&&this.attributes.move(s),s}};F.allowedChildren=[F,H],F.blotName="inline",F.scope=m.INLINE_BLOT,F.tagName="SPAN";const z=F,K=class ee extends N{static create(e){return super.create(e)}static formats(e,t){const s=t.query(ee.blotName);if(s==null||e.tagName!==s.tagName){if(typeof this.tagName=="string")return!0;if(Array.isArray(this.tagName))return e.tagName.toLowerCase()}}constructor(e,t){super(e,t),this.attributes=new f(this.domNode)}format(e,t){const s=this.scroll.query(e,m.BLOCK);s!=null&&(s instanceof v?this.attributes.attribute(s,t):e!==this.statics.blotName||t?t&&(e!==this.statics.blotName||this.formats()[e]!==t)&&this.replaceWith(e,t):this.replaceWith(ee.blotName))}formats(){const e=this.attributes.values(),t=this.statics.formats(this.domNode,this.scroll);return t!=null&&(e[this.statics.blotName]=t),e}formatAt(e,t,s,r){this.scroll.query(s,m.BLOCK)!=null?this.format(s,r):super.formatAt(e,t,s,r)}insertAt(e,t,s){if(s==null||this.scroll.query(t,m.INLINE)!=null)super.insertAt(e,t,s);else{const r=this.split(e);if(r==null)throw new Error("Attempt to insertAt after block boundaries");{const c=this.scroll.create(t,s);r.parent.insertBefore(c,r)}}}replaceWith(e,t){const s=super.replaceWith(e,t);return this.attributes.copy(s),s}update(e,t){super.update(e,t),e.some((s=>s.target===this.domNode&&s.type==="attributes"))&&this.attributes.build()}};K.blotName="block",K.scope=m.BLOCK_BLOT,K.tagName="P",K.allowedChildren=[z,K,H];const nt=K,M=class extends N{checkMerge(){return this.next!==null&&this.next.statics.blotName===this.statics.blotName}deleteAt(d,e){super.deleteAt(d,e),this.enforceAllowedChildren()}formatAt(d,e,t,s){super.formatAt(d,e,t,s),this.enforceAllowedChildren()}insertAt(d,e,t){super.insertAt(d,e,t),this.enforceAllowedChildren()}optimize(d){super.optimize(d),this.children.length>0&&this.next!=null&&this.checkMerge()&&(this.next.moveChildren(this),this.next.remove())}};M.blotName="container",M.scope=m.BLOCK_BLOT;const g=M,y=class extends H{static formats(d,e){}format(d,e){super.formatAt(0,this.length(),d,e)}formatAt(d,e,t,s){d===0&&e===this.length()?this.format(t,s):super.formatAt(d,e,t,s)}formats(){return this.statics.formats(this.domNode,this.scroll)}},S={attributes:!0,characterData:!0,characterDataOldValue:!0,childList:!0,subtree:!0},O=class extends N{constructor(d,e){super(null,e),this.registry=d,this.scroll=this,this.build(),this.observer=new MutationObserver((t=>{this.update(t)})),this.observer.observe(this.domNode,S),this.attach()}create(d,e){return this.registry.create(this,d,e)}find(d,e=!1){const t=this.registry.find(d,e);return t?t.scroll===this?t:e?this.find(t.scroll.domNode.parentNode,!0):null:null}query(d,e=m.ANY){return this.registry.query(d,e)}register(...d){return this.registry.register(...d)}build(){this.scroll!=null&&super.build()}detach(){super.detach(),this.observer.disconnect()}deleteAt(d,e){this.update(),d===0&&e===this.length()?this.children.forEach((t=>{t.remove()})):super.deleteAt(d,e)}formatAt(d,e,t,s){this.update(),super.formatAt(d,e,t,s)}insertAt(d,e,t){this.update(),super.insertAt(d,e,t)}optimize(d=[],e={}){super.optimize(e);const t=e.mutationsMap||new WeakMap;let s=Array.from(this.observer.takeRecords());for(;s.length>0;)d.push(s.pop());const r=(i,n=!0)=>{i==null||i===this||i.domNode.parentNode!=null&&(t.has(i.domNode)||t.set(i.domNode,[]),n&&r(i.parent))},c=i=>{t.has(i.domNode)&&(i instanceof N&&i.children.forEach(c),t.delete(i.domNode),i.optimize(e))};let h=d;for(let i=0;h.length>0;i+=1){if(i>=100)throw new Error("[Parchment] Maximum optimize iterations reached");for(h.forEach((n=>{const l=this.find(n.target,!0);l!=null&&(l.domNode===n.target&&(n.type==="childList"?(r(this.find(n.previousSibling,!1)),Array.from(n.addedNodes).forEach((o=>{const u=this.find(o,!1);r(u,!1),u instanceof N&&u.children.forEach((a=>{r(a,!1)}))}))):n.type==="attributes"&&r(l.prev)),r(l))})),this.children.forEach(c),h=Array.from(this.observer.takeRecords()),s=h.slice();s.length>0;)d.push(s.pop())}}update(d,e={}){d=d||this.observer.takeRecords();const t=new WeakMap;d.map((s=>{const r=this.find(s.target,!0);return r==null?null:t.has(r.domNode)?(t.get(r.domNode).push(s),null):(t.set(r.domNode,[s]),r)})).forEach((s=>{s!=null&&s!==this&&t.has(s.domNode)&&s.update(t.get(s.domNode)||[],e)})),e.mutationsMap=t,t.has(this.domNode)&&super.update(t.get(this.domNode),e),this.optimize(d,e)}};O.blotName="scroll",O.defaultChild=nt,O.allowedChildren=[nt,g],O.scope=m.BLOCK_BLOT,O.tagName="DIV";const tt=O,P=class he extends H{static create(e){return document.createTextNode(e)}static value(e){return e.data}constructor(e,t){super(e,t),this.text=this.statics.value(this.domNode)}deleteAt(e,t){this.domNode.data=this.text=this.text.slice(0,e)+this.text.slice(e+t)}index(e,t){return this.domNode===e?t:-1}insertAt(e,t,s){s==null?(this.text=this.text.slice(0,e)+t+this.text.slice(e),this.domNode.data=this.text):super.insertAt(e,t,s)}length(){return this.text.length}optimize(e){super.optimize(e),this.text=this.statics.value(this.domNode),this.text.length===0?this.remove():this.next instanceof he&&this.next.prev===this&&(this.insertAt(this.length(),this.next.value()),this.next.remove())}position(e,t=!1){return[this.domNode,e]}split(e,t=!1){if(!t){if(e===0)return this;if(e===this.length())return this.next}const s=this.scroll.create(this.domNode.splitText(e));return this.parent.insertBefore(s,this.next||void 0),this.text=this.statics.value(this.domNode),s}update(e,t){e.some((s=>s.type==="characterData"&&s.target===this.domNode))&&(this.text=this.statics.value(this.domNode))}value(){return this.text}};P.blotName="text",P.scope=m.INLINE_BLOT;const V=P}},E={};function D(j){var U=E[j];if(U!==void 0)return U.exports;var p=E[j]={exports:{}};return ct[j](p,p.exports,D),p.exports}D.d=function(j,U){for(var p in U)D.o(U,p)&&!D.o(j,p)&&Object.defineProperty(j,p,{enumerable:!0,get:U[p]})},D.o=function(j,U){return Object.prototype.hasOwnProperty.call(j,U)},D.r=function(j){typeof Symbol<"u"&&Symbol.toStringTag&&Object.defineProperty(j,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(j,"__esModule",{value:!0})};var Q={};return(function(){D.d(Q,{default:function(){return n}});var j=D(729),U=D(276),p=D(912),m=D(3);class v extends m.ClassAttributor{add(o,u){let a=0;if(u==="+1"||u==="-1"){const A=this.value(o)||0;a=u==="+1"?A+1:A-1}else typeof u=="number"&&(a=u);return a===0?(this.remove(o),!0):super.add(o,a.toString())}canAdd(o,u){return super.canAdd(o,u)||super.canAdd(o,parseInt(u,10))}value(o){return parseInt(super.value(o),10)||void 0}}var w=new v("indent","ql-indent",{scope:m.Scope.BLOCK,whitelist:[1,2,3,4,5,6,7,8]}),Y=D(698);class et extends Y.Ay{static blotName="blockquote";static tagName="blockquote"}var B=et;class C extends Y.Ay{static blotName="header";static tagName=["H1","H2","H3","H4","H5","H6"];static formats(o){return this.tagName.indexOf(o.tagName)+1}}var q=C,R=D(580),f=D(543);class T extends R.A{}T.blotName="list-container",T.tagName="OL";class _ extends Y.Ay{static create(o){const u=super.create();return u.setAttribute("data-list",o),u}static formats(o){return o.getAttribute("data-list")||void 0}static register(){f.Ay.register(T)}constructor(o,u){super(o,u);const a=u.ownerDocument.createElement("span"),A=x=>{if(!o.isEnabled())return;const b=this.statics.formats(u,o);b==="checked"?(this.format("list","unchecked"),x.preventDefault()):b==="unchecked"&&(this.format("list","checked"),x.preventDefault())};a.addEventListener("mousedown",A),a.addEventListener("touchstart",A),this.attachUI(a)}format(o,u){o===this.statics.blotName&&u?this.domNode.setAttribute("data-list",u):super.format(o,u)}}_.blotName="list",_.tagName="LI",T.allowedChildren=[_],_.requiredContainer=T;var L=D(922),H=D(638),G=D(772),I=D(664),k=D(850);class N extends k.A{static blotName="bold";static tagName=["STRONG","B"];static create(){return super.create()}static formats(){return!0}optimize(o){super.optimize(o),this.domNode.tagName!==this.statics.tagName[0]&&this.replaceWith(this.statics.blotName)}}var F=N;class z extends k.A{static blotName="link";static tagName="A";static SANITIZED_URL="about:blank";static PROTOCOL_WHITELIST=["http","https","mailto","tel","sms"];static create(o){const u=super.create(o);return u.setAttribute("href",this.sanitize(o)),u.setAttribute("rel","noopener noreferrer"),u.setAttribute("target","_blank"),u}static formats(o){return o.getAttribute("href")}static sanitize(o){return K(o,this.PROTOCOL_WHITELIST)?o:this.SANITIZED_URL}format(o,u){o===this.statics.blotName&&u?this.domNode.setAttribute("href",this.constructor.sanitize(u)):super.format(o,u)}}function K(l,o){const u=document.createElement("a");u.href=l;const a=u.href.slice(0,u.href.indexOf(":"));return o.indexOf(a)>-1}class nt extends k.A{static blotName="script";static tagName=["SUB","SUP"];static create(o){return o==="super"?document.createElement("sup"):o==="sub"?document.createElement("sub"):super.create(o)}static formats(o){return o.tagName==="SUB"?"sub":o.tagName==="SUP"?"super":void 0}}var M=nt;class g extends k.A{static blotName="underline";static tagName="U"}var y=g;const S=["alt","height","width"];class O extends m.EmbedBlot{static blotName="image";static tagName="IMG";static create(o){const u=super.create(o);return typeof o=="string"&&u.setAttribute("src",this.sanitize(o)),u}static formats(o){return S.reduce(((u,a)=>(o.hasAttribute(a)&&(u[a]=o.getAttribute(a)),u)),{})}static match(o){return/\.(jpe?g|gif|png)$/.test(o)||/^data:image\/.+;base64/.test(o)}static sanitize(o){return K(o,["http","https","data"])?o:"//:0"}static value(o){return o.getAttribute("src")}format(o,u){S.indexOf(o)>-1?u?this.domNode.setAttribute(o,u):this.domNode.removeAttribute(o):super.format(o,u)}}var tt=O;const P=["height","width"];class V extends Y.zo{static blotName="video";static className="ql-video";static tagName="IFRAME";static create(o){const u=super.create(o);return u.setAttribute("frameborder","0"),u.setAttribute("allowfullscreen","true"),u.setAttribute("src",this.sanitize(o)),u}static formats(o){return P.reduce(((u,a)=>(o.hasAttribute(a)&&(u[a]=o.getAttribute(a)),u)),{})}static sanitize(o){return z.sanitize(o)}static value(o){return o.getAttribute("src")}format(o,u){P.indexOf(o)>-1?u?this.domNode.setAttribute(o,u):this.domNode.removeAttribute(o):super.format(o,u)}html(){const{video:o}=this.value();return`<a href="${o}">${o}</a>`}}var d=V,e=D(404),t=D(398),s=D(78),r=D(266);const c=(0,s.A)("quill:toolbar");class h extends r.A{constructor(o,u){if(super(o,u),Array.isArray(this.options.container)){const a=document.createElement("div");a.setAttribute("role","toolbar"),(function(A,x){Array.isArray(x[0])||(x=[x]),x.forEach((b=>{const $=document.createElement("span");$.classList.add("ql-formats"),b.forEach((X=>{if(typeof X=="string")i($,X);else{const W=Object.keys(X)[0],J=X[W];Array.isArray(J)?(function(rt,lt,Z){const it=document.createElement("select");it.classList.add(`ql-${lt}`),Z.forEach((gt=>{const ht=document.createElement("option");gt!==!1?ht.setAttribute("value",String(gt)):ht.setAttribute("selected","selected"),it.appendChild(ht)})),rt.appendChild(it)})($,W,J):i($,W,J)}})),A.appendChild($)}))})(a,this.options.container),o.container?.parentNode?.insertBefore(a,o.container),this.container=a}else if(typeof this.options.container=="string"){const a=o.container.getRootNode();this.container=a.querySelector(this.options.container)}else this.container=this.options.container;this.container instanceof HTMLElement?(this.container.classList.add("ql-toolbar"),this.controls=[],this.handlers={},this.options.handlers&&Object.keys(this.options.handlers).forEach((a=>{const A=this.options.handlers?.[a];A&&this.addHandler(a,A)})),Array.from(this.container.querySelectorAll("button, select")).forEach((a=>{this.attach(a)})),this.quill.on(f.Ay.events.EDITOR_CHANGE,(()=>{const[a]=this.quill.selection.getRange();this.update(a)}))):c.error("Container required for toolbar",this.options)}addHandler(o,u){this.handlers[o]=u}attach(o){let u=Array.from(o.classList).find((A=>A.indexOf("ql-")===0));if(!u)return;if(u=u.slice(3),o.tagName==="BUTTON"&&o.setAttribute("type","button"),this.handlers[u]==null&&this.quill.scroll.query(u)==null)return void c.warn("ignoring attaching to nonexistent format",u,o);const a=o.tagName==="SELECT"?"change":"click";o.addEventListener(a,(A=>{let x;if(o.tagName==="SELECT"){if(o.selectedIndex<0)return;const $=o.options[o.selectedIndex];x=!$.hasAttribute("selected")&&($.value||!1)}else x=!o.classList.contains("ql-active")&&(o.value||!o.hasAttribute("value")),A.preventDefault();this.quill.focus();const[b]=this.quill.selection.getRange();if(this.handlers[u]!=null)this.handlers[u].call(this,x);else if(this.quill.scroll.query(u).prototype instanceof m.EmbedBlot){if(x=prompt(`Enter ${u}`),!x)return;this.quill.updateContents(new t.Ay().retain(b.index).delete(b.length).insert({[u]:x}),f.Ay.sources.USER)}else this.quill.format(u,x,f.Ay.sources.USER);this.update(b)})),this.controls.push([u,o])}update(o){const u=o==null?{}:this.quill.getFormat(o);this.controls.forEach((a=>{const[A,x]=a;if(x.tagName==="SELECT"){let b=null;if(o==null)b=null;else if(u[A]==null)b=x.querySelector("option[selected]");else if(!Array.isArray(u[A])){let $=u[A];typeof $=="string"&&($=$.replace(/"/g,'\\"')),b=x.querySelector(`option[value="${$}"]`)}b==null?(x.value="",x.selectedIndex=-1):b.selected=!0}else if(o==null)x.classList.remove("ql-active"),x.setAttribute("aria-pressed","false");else if(x.hasAttribute("value")){const b=u[A],$=b===x.getAttribute("value")||b!=null&&b.toString()===x.getAttribute("value")||b==null&&!x.getAttribute("value");x.classList.toggle("ql-active",$),x.setAttribute("aria-pressed",$.toString())}else{const b=u[A]!=null;x.classList.toggle("ql-active",b),x.setAttribute("aria-pressed",b.toString())}}))}}function i(l,o,u){const a=document.createElement("button");a.setAttribute("type","button"),a.classList.add(`ql-${o}`),a.setAttribute("aria-pressed","false"),u!=null?(a.value=u,a.setAttribute("aria-label",`${o}: ${u}`)):a.setAttribute("aria-label",o),l.appendChild(a)}h.DEFAULTS={},h.DEFAULTS={container:null,handlers:{clean(){const l=this.quill.getSelection();if(l!=null)if(l.length===0){const o=this.quill.getFormat();Object.keys(o).forEach((u=>{this.quill.scroll.query(u,m.Scope.INLINE)!=null&&this.quill.format(u,!1,f.Ay.sources.USER)}))}else this.quill.removeFormat(l.index,l.length,f.Ay.sources.USER)},direction(l){const{align:o}=this.quill.getFormat();l==="rtl"&&o==null?this.quill.format("align","right",f.Ay.sources.USER):l||o!=="right"||this.quill.format("align",!1,f.Ay.sources.USER),this.quill.format("direction",l,f.Ay.sources.USER)},indent(l){const o=this.quill.getSelection(),u=this.quill.getFormat(o),a=parseInt(u.indent||0,10);if(l==="+1"||l==="-1"){let A=l==="+1"?1:-1;u.direction==="rtl"&&(A*=-1),this.quill.format("indent",a+A,f.Ay.sources.USER)}},link(l){l===!0&&(l=prompt("Enter link URL:")),this.quill.format("link",l,f.Ay.sources.USER)},list(l){const o=this.quill.getSelection(),u=this.quill.getFormat(o);l==="check"?u.list==="checked"||u.list==="unchecked"?this.quill.format("list",!1,f.Ay.sources.USER):this.quill.format("list","unchecked",f.Ay.sources.USER):this.quill.format("list",l,f.Ay.sources.USER)}}},j.default.register({"attributors/attribute/direction":p.Mc,"attributors/class/align":U.qh,"attributors/class/background":L.l,"attributors/class/color":H.g3,"attributors/class/direction":p.sY,"attributors/class/font":G.q,"attributors/class/size":I.U,"attributors/style/align":U.Hu,"attributors/style/background":L.s,"attributors/style/color":H.JM,"attributors/style/direction":p.VL,"attributors/style/font":G.z,"attributors/style/size":I.r},!0),j.default.register({"formats/align":U.qh,"formats/direction":p.sY,"formats/indent":w,"formats/background":L.s,"formats/color":H.JM,"formats/font":G.q,"formats/size":I.U,"formats/blockquote":B,"formats/code-block":e.Ay,"formats/header":q,"formats/list":_,"formats/bold":F,"formats/code":e.Cy,"formats/italic":class extends F{static blotName="italic";static tagName=["EM","I"]},"formats/link":z,"formats/script":M,"formats/strike":class extends F{static blotName="strike";static tagName=["S","STRIKE"]},"formats/underline":y,"formats/image":tt,"formats/video":d,"modules/toolbar":h},!0);var n=j.default})(),Q.default})()}))})(Yt)),Yt.exports}Le();/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 *
 * This program is available under Vaadin Commercial License and Service Terms.
 *
 *
 * See https://vaadin.com/commercial-license-and-service-terms for the full
 * license.
 */const Vt=window.Quill,Se=Vt.import("formats/code-block-container");class Te extends Se{html(ct,E){const D=super.html(ct,E),Q=document.createElement("div");Q.innerHTML=D;const j=Q.querySelector("pre");return j?(j.setAttribute("spellcheck","false"),j.outerHTML):D}}Vt.register("formats/code-block-container",Te,!0);const Oe=["bold","italic","underline","strike","header","script","list","align","blockquote","code-block"],zt={API:"api",USER:"user",SILENT:"silent"},Jt={DEFAULT:0,FOCUSED:1,CLICKED:2},Re={undo:"undo",redo:"redo",bold:"bold",italic:"italic",underline:"underline",strike:"strike",color:"color",background:"background",h1:"h1",h2:"h2",h3:"h3",subscript:"subscript",superscript:"superscript",listOrdered:"list ordered",listBullet:"list bullet",outdent:"outdent",indent:"indent",alignLeft:"align left",alignCenter:"align center",alignRight:"align right",image:"image",link:"link",blockquote:"blockquote",codeBlock:"code block",clean:"clean",linkDialogTitle:"Link address",ok:"OK",cancel:"Cancel",remove:"Remove"},Ie=Wt=>class extends be(Re,Wt){static get properties(){return{value:{type:String,notify:!0,value:"",sync:!0},htmlValue:{type:String,notify:!0,readOnly:!0},disabled:{type:Boolean,value:!1,reflectToAttribute:!0},readonly:{type:Boolean,value:!1,reflectToAttribute:!0},colorOptions:{type:Array,value:()=>["#000000","#e60000","#ff9900","#ffff00","#008a00","#0066cc","#9933ff","#ffffff","#facccc","#ffebcc","#ffffcc","#cce8cc","#cce0f5","#ebd6ff","#bbbbbb","#f06666","#ffc266","#ffff66","#66b966","#66a3e0","#c285ff","#888888","#a10000","#b26b00","#b2b200","#006100","#0047b2","#6b24b2","#444444","#5c0000","#663d00","#666600","#003700","#002966","#3d1466"]},_editor:{type:Object,sync:!0},__oldValue:String,__lastCommittedChange:{type:String,value:""},_linkEditing:{type:Boolean,value:!1},_linkRange:{type:Object,value:null},_linkIndex:{type:Number,value:null},_linkUrl:{type:String,value:""},_colorEditing:{type:Boolean,value:!1},_colorValue:{type:String,value:""},_backgroundEditing:{type:Boolean,value:!1},_backgroundValue:{type:String,value:""}}}static get observers(){return["_valueChanged(value, _editor)","_disabledChanged(disabled, readonly, _editor)"]}get i18n(){return super.i18n}set i18n(E){super.i18n=E}get _toolbarButtons(){return Array.from(this.shadowRoot.querySelectorAll('[part="toolbar"] button')).filter(E=>E.clientHeight>0)}attributeChangedCallback(E,D,Q){super.attributeChangedCallback(E,D,Q),E==="dir"&&(this.__dir=Q,this.__setDirection(Q))}disconnectedCallback(){super.disconnectedCallback(),this._editor.emitter.disconnect()}__setDirection(E){if(!this._editor)return;const D=Vt.import("attributors/class/align");D.whitelist=[E==="rtl"?"left":"right","center","justify"],Vt.register(D,!0);const Q=this._toolbar.querySelector('[part~="toolbar-group-alignment"]');E==="rtl"?(Q.querySelector('[part~="toolbar-button-align-left"]').value="left",Q.querySelector('[part~="toolbar-button-align-right"]').value=""):(Q.querySelector('[part~="toolbar-button-align-left"]').value="",Q.querySelector('[part~="toolbar-button-align-right"]').value="right"),this._editor.getModule("toolbar").update(this._editor.getSelection())}connectedCallback(){super.connectedCallback(),this._editor.emitter.connect()}ready(){super.ready(),this._toolbarConfig=this._prepareToolbar(),this._toolbar=this._toolbarConfig.container,this._addToolbarListeners();const E=this.shadowRoot.querySelector('[part="content"]');this._editor=new Vt(E,{modules:{toolbar:this._toolbarConfig}}),this.__patchToolbar(),this.__patchKeyboard(),this.__setDirection(this.__dir);const D=E.querySelector(".ql-editor");D.setAttribute("role","textbox"),D.setAttribute("aria-multiline","true"),this._editor.on("text-change",()=>{this.__debounceSetValue=se.debounce(this.__debounceSetValue,oe.after(200),()=>{this.value=JSON.stringify(this._editor.getContents().ops)})}),this._editor.on("editor-change",()=>{const j=this._editor.getSelection();if(j){const U=this._editor.getFormat(j.index,j.length);this._toolbar.style.setProperty("--_color-value",U.color||null),this._toolbar.style.setProperty("--_background-value",U.background||null)}}),D.addEventListener("keydown",j=>{j.key==="Escape"?this.__tabBindings||(this.__tabBindings=this._editor.keyboard.bindings.Tab,this._editor.keyboard.bindings.Tab=null):this.__tabBindings&&(this._editor.keyboard.bindings.Tab=this.__tabBindings,this.__tabBindings=null)}),D.addEventListener("blur",()=>{this.__tabBindings&&(this._editor.keyboard.bindings.Tab=this.__tabBindings,this.__tabBindings=null)}),D.addEventListener("focusout",()=>{this._toolbarState===Jt.FOCUSED?this._cleanToolbarState():this.__emitChangeEvent()}),D.addEventListener("focus",()=>{this._toolbarState===Jt.CLICKED&&!this._linkEditing&&this._cleanToolbarState()}),this._editor.on("selection-change",this.__announceFormatting.bind(this)),this.__flushPendingHtmlValue(),this.querySelector('[slot="color-popup"]').target=this.shadowRoot.querySelector("#btn-color"),this.querySelector('[slot="background-popup"]').target=this.shadowRoot.querySelector("#btn-background"),this._tooltip=document.createElement("vaadin-tooltip"),this._tooltip.slot="tooltip",this._tooltip.ariaTarget=null,this.append(this._tooltip),this.shadowRoot.querySelectorAll('[part~="toolbar-button"]').forEach(j=>{j.addEventListener("mouseenter",this.__showTooltip.bind(this)),j.addEventListener("focusin",this.__showTooltip.bind(this))})}__showTooltip({type:E,target:D}){E==="focusin"&&!ue()||(this._tooltip.target=D,this._tooltip.text=D.ariaLabel,this._tooltip._stateController.open({focus:E==="focusin",hover:E==="mouseenter"}))}_prepareToolbar(){const E=Vt.imports["modules/toolbar"].DEFAULTS.handlers.clean,D=this,Q={container:this.shadowRoot.querySelector('[part="toolbar"]'),handlers:{clean(){D._markToolbarClicked(),E.call(this)}}};return Oe.forEach(j=>{Q.handlers[j]=U=>{this._markToolbarClicked(),this._editor.format(j,U,zt.USER)}}),Q}_addToolbarListeners(){const E=this._toolbarButtons,D=this._toolbar;E.forEach((Q,j)=>j>0&&Q.setAttribute("tabindex","-1")),D.addEventListener("keydown",Q=>{if([37,39].indexOf(Q.keyCode)>-1){Q.preventDefault();let j=E.indexOf(Q.target);E[j].setAttribute("tabindex","-1");let U;Q.keyCode===39?U=1:Q.keyCode===37&&(U=-1),j=(E.length+j+U)%E.length,E[j].removeAttribute("tabindex"),E[j].focus()}(Q.keyCode===27||Q.key==="Tab"&&!Q.shiftKey)&&(Q.preventDefault(),this._editor.focus())}),D.addEventListener("mousedown",Q=>{E.indexOf(Q.composedPath()[0])>-1&&this._markToolbarFocused()})}_markToolbarClicked(){this._toolbarState=Jt.CLICKED}_markToolbarFocused(){this._toolbarState=Jt.FOCUSED}_cleanToolbarState(){this._toolbarState=Jt.DEFAULT}__patchToolbar(){const E=this._editor.getModule("toolbar"),D=E.update;E.controls.push(["link",this.shadowRoot.querySelector('[part~="toolbar-button-link"]')]),E.update=function(Q){D.call(E,Q),E.controls.forEach(j=>{const U=j[1],p=U.classList.contains("ql-active");U.part.toggle("toolbar-button-pressed",p)})}}__patchKeyboard(){const E=()=>{this._markToolbarFocused(),this._toolbar.querySelector("button:not([tabindex])").focus()},D=this._editor.keyboard;D.addBinding({key:"Tab",shiftKey:!0,handler:E}),D.addBinding({key:"F10",altKey:!0,handler:E})}__emitChangeEvent(){let E=this.__lastCommittedChange;this.__debounceSetValue&&this.__debounceSetValue.isActive()&&(E=this.value,this.__debounceSetValue.flush()),E!==this.value&&(this.dispatchEvent(new CustomEvent("change",{bubbles:!0,cancelable:!1})),this.__lastCommittedChange=this.value)}_onLinkClick(){const E=this._editor.getSelection();if(E){const D=Vt.imports["formats/link"],[Q,j]=this._editor.scroll.descendant(D,E.index);Q!=null?(this._linkRange={index:E.index-j,length:Q.length()},this._linkUrl=D.formats(Q.domNode)):E.length===0&&(this._linkIndex=E.index),this._linkEditing=!0}}_applyLink(E){E&&(this._markToolbarClicked(),this._editor.focus(),this._editor.format("link",E,zt.USER),this._editor.getModule("toolbar").update(this._editor.selection.savedRange)),this._closeLinkDialog()}_insertLink(E,D){E&&(this._markToolbarClicked(),this._editor.insertText(D,E,{link:E}),this._editor.setSelection(D,E.length)),this._closeLinkDialog()}_updateLink(E,D){this._markToolbarClicked(),this._editor.formatText(D,"link",E,zt.USER),this._closeLinkDialog()}_removeLink(){this._markToolbarClicked(),this._linkRange!=null&&this._editor.formatText(this._linkRange,{link:!1,color:!1},zt.USER),this._closeLinkDialog()}_closeLinkDialog(){this._linkEditing=!1,this._linkUrl="",this._linkIndex=null,this._linkRange=null}_onLinkEditConfirm(){this._linkIndex!=null?this._insertLink(this._linkUrl,this._linkIndex):this._linkRange?this._updateLink(this._linkUrl,this._linkRange):this._applyLink(this._linkUrl)}_onLinkEditCancel(){this._closeLinkDialog(),this._editor.focus()}_onLinkEditRemove(){this._removeLink(),this._closeLinkDialog()}_onLinkKeydown(E){E.keyCode===13&&(E.preventDefault(),E.stopPropagation(),this._onLinkEditConfirm(),this._closeLinkDialog())}__onColorClick(){this._tooltip.opened=!1,this._colorEditing=!0}__onColorSelected(E){const D=E.detail.color;this._colorValue=D==="#000000"?null:D,this._markToolbarClicked(),this._editor.focus(),this._editor.format("color",this._colorValue,zt.USER),this._toolbar.style.setProperty("--_color-value",this._colorValue),this._colorEditing=!1}__onBackgroundClick(){this._tooltip.opened=!1,this._backgroundEditing=!0}__onBackgroundSelected(E){const D=E.detail.color;this._backgroundValue=D==="#ffffff"?null:D,this._markToolbarClicked(),this._editor.focus(),this._editor.format("background",this._backgroundValue,zt.USER),this._toolbar.style.setProperty("--_background-value",this._backgroundValue),this._backgroundEditing=!1}__updateHtmlValue(){let E=this._editor.getSemanticHTML();E=E.replace(/class="([^"]*)"/gu,(D,Q)=>`class="${Q.split(" ").filter(U=>!U.startsWith("ql-")||U.startsWith("ql-align")||U.startsWith("ql-indent")).join(" ")}"`),E=this.__processQuillClasses(E),this._setHtmlValue(E)}__processQuillClasses(E){const D=document.createElement("div");return D.innerHTML=E,D.querySelectorAll('[class*="ql-align"], [class*="ql-indent"]').forEach(j=>{this.__processAlignClasses(j),this.__processIndentClasses(j),j.removeAttribute("class")}),D.innerHTML}__processAlignClasses(E){let D=E.getAttribute("style")||"";[this.__dir==="rtl"?"left":"right","center","justify"].forEach(j=>{if(E.classList.contains(`ql-align-${j}`)){const U=`text-align: ${j}`;D=D?`${D}; ${U}`:U,E.setAttribute("style",D),E.classList.remove(`ql-align-${j}`)}})}__processIndentClasses(E){const D=Array.from(E.classList).find(Q=>Q.startsWith("ql-indent-"));if(D){const Q=parseInt(D.replace("ql-indent-","").trim(),10),j="	".repeat(Q),U=E.firstChild;if(U&&U.nodeType===Node.TEXT_NODE)U.textContent=j+U.textContent;else if(E.childNodes.length>0){const p=document.createTextNode(j);E.insertBefore(p,E.firstChild)}else E.textContent=j;E.classList.remove(D)}}dangerouslySetHtmlValue(E){if(!this._editor){this.__savePendingHtmlValue(E);return}if(!getComputedStyle(this).display){this.__savePendingHtmlValue(E);const j=new IntersectionObserver(()=>{getComputedStyle(this).display&&(this.__flushPendingHtmlValue(),j.disconnect())});j.observe(this);return}const D={"	":"__VAADIN_RICH_TEXT_EDITOR_TAB","  ":"__VAADIN_RICH_TEXT_EDITOR_DOUBLE_SPACE"};Object.entries(D).forEach(([j,U])=>{E=E.replaceAll(/>[^<]*</gu,p=>p.replaceAll(j,U))});const Q=this._editor.clipboard.convert({html:E});Object.entries(D).forEach(([j,U])=>{Q.ops.forEach(p=>{typeof p.insert=="string"&&(p.insert=p.insert.replaceAll(U,j))})}),this._editor.setContents(Q,zt.API)}__savePendingHtmlValue(E){this.__pendingHtmlValue=E,this.value=""}__flushPendingHtmlValue(){this.__pendingHtmlValue&&this.dangerouslySetHtmlValue(this.__pendingHtmlValue)}__announceFormatting(){const D=this.shadowRoot.querySelector(".announcer");D.textContent="",this.__debounceAnnounceFormatting=se.debounce(this.__debounceAnnounceFormatting,oe.after(200),()=>{const Q=Array.from(this.shadowRoot.querySelectorAll('[part="toolbar"] .ql-active')).map(j=>j.getAttribute("aria-label")).join(", ");D.textContent=Q})}_clear(){this._editor.deleteText(0,this._editor.getLength(),zt.SILENT),this.__updateHtmlValue()}_undo(E){E.preventDefault(),this._editor.history.undo(),this._editor.focus()}_redo(E){E.preventDefault(),this._editor.history.redo(),this._editor.focus()}_toggleToolbarDisabled(E){const D=this._toolbarButtons;E?D.forEach(Q=>Q.setAttribute("disabled","true")):D.forEach(Q=>Q.removeAttribute("disabled"))}_onImageTouchEnd(E){E.preventDefault(),this._onImageClick()}_onImageClick(){this.$.fileInput.value="",this.$.fileInput.click()}_uploadImage(E){const D=E.target;if(D.files!=null&&D.files[0]!=null){const Q=new FileReader;Q.onload=j=>{const U=j.target.result,p=this._editor.getSelection(!0);this._editor.updateContents(new Vt.imports.delta().retain(p.index).delete(p.length).insert({image:U}),zt.USER),this._markToolbarClicked(),this._editor.setSelection(p.index+1,zt.SILENT),D.value=""},Q.readAsDataURL(D.files[0])}}_disabledChanged(E,D,Q){E===void 0||D===void 0||Q===void 0||(E||D?(Q.enable(!1),E&&this._toggleToolbarDisabled(!0)):(Q.enable(),this.__oldDisabled&&this._toggleToolbarDisabled(!1)),this.__oldDisabled=E)}_valueChanged(E,D){if(E&&this.__pendingHtmlValue&&(this.__pendingHtmlValue=void 0),D===void 0)return;if(E==null||E==='[{"insert":"\\n"}]'){this.value="";return}if(E===""){this._clear();return}let Q;try{if(Q=JSON.parse(E),Array.isArray(Q))this.__oldValue=E;else throw new Error(`expected JSON string with array of objects, got: ${E}`)}catch(U){this.value=this.__oldValue,console.error("Invalid value set to rich-text-editor:",U);return}const j=new Vt.imports.delta(Q);JSON.stringify(D.getContents())!==JSON.stringify(j)&&D.setContents(j,zt.SILENT),this.__updateHtmlValue(),this._toolbarState===Jt.CLICKED?(this._cleanToolbarState(),this.__emitChangeEvent()):this._editor.hasFocus()||(this.__lastCommittedChange=this.value)}};/**
 * @license
 * Copyright (c) 2000 - 2026 Vaadin Ltd.
 *
 * This program is available under Vaadin Commercial License and Service Terms.
 *
 *
 * See https://vaadin.com/commercial-license-and-service-terms for the full
 * license.
 */class Be extends Ie(ve(ae(ne(ce(re))))){static get is(){return"vaadin-rich-text-editor"}static get cvdlName(){return"vaadin-rich-text-editor"}static get styles(){return qe}static get lumoInjector(){return{...super.lumoInjector,includeBaseStyles:!0}}render(){return Zt`
      <div class="vaadin-rich-text-editor-container">
        <!-- Create toolbar container -->
        <div part="toolbar" role="toolbar">
          <span part="toolbar-group toolbar-group-history">
            <!-- Undo and Redo -->
            <button
              id="btn-undo"
              type="button"
              part="toolbar-button toolbar-button-undo"
              aria-label="${this.__effectiveI18n.undo}"
              @click="${this._undo}"
            ></button>

            <button
              id="btn-redo"
              type="button"
              part="toolbar-button toolbar-button-redo"
              aria-label="${this.__effectiveI18n.redo}"
              @click="${this._redo}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-emphasis">
            <!-- Bold -->
            <button
              id="btn-bold"
              class="ql-bold"
              part="toolbar-button toolbar-button-bold"
              aria-label="${this.__effectiveI18n.bold}"
            ></button>

            <!-- Italic -->
            <button
              id="btn-italic"
              class="ql-italic"
              part="toolbar-button toolbar-button-italic"
              aria-label="${this.__effectiveI18n.italic}"
            ></button>

            <!-- Underline -->
            <button
              id="btn-underline"
              class="ql-underline"
              part="toolbar-button toolbar-button-underline"
              aria-label="${this.__effectiveI18n.underline}"
            ></button>

            <!-- Strike -->
            <button
              id="btn-strike"
              class="ql-strike"
              part="toolbar-button toolbar-button-strike"
              aria-label="${this.__effectiveI18n.strike}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-style">
            <!-- Color -->
            <button
              id="btn-color"
              type="button"
              part="toolbar-button toolbar-button-color"
              aria-label="${this.__effectiveI18n.color}"
              @click="${this.__onColorClick}"
            ></button>
            <!-- Background -->
            <button
              id="btn-background"
              type="button"
              part="toolbar-button toolbar-button-background"
              aria-label="${this.__effectiveI18n.background}"
              @click="${this.__onBackgroundClick}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-heading">
            <!-- Header buttons -->
            <button
              id="btn-h1"
              type="button"
              class="ql-header"
              value="1"
              part="toolbar-button toolbar-button-h1"
              aria-label="${this.__effectiveI18n.h1}"
            ></button>
            <button
              id="btn-h2"
              type="button"
              class="ql-header"
              value="2"
              part="toolbar-button toolbar-button-h2"
              aria-label="${this.__effectiveI18n.h2}"
            ></button>
            <button
              id="btn-h3"
              type="button"
              class="ql-header"
              value="3"
              part="toolbar-button toolbar-button-h3"
              aria-label="${this.__effectiveI18n.h3}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-glyph-transformation">
            <!-- Subscript and superscript -->
            <button
              id="btn-subscript"
              class="ql-script"
              value="sub"
              part="toolbar-button toolbar-button-subscript"
              aria-label="${this.__effectiveI18n.subscript}"
            ></button>
            <button
              id="btn-superscript"
              class="ql-script"
              value="super"
              part="toolbar-button toolbar-button-superscript"
              aria-label="${this.__effectiveI18n.superscript}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-list">
            <!-- List buttons -->
            <button
              id="btn-ol"
              type="button"
              class="ql-list"
              value="ordered"
              part="toolbar-button toolbar-button-list-ordered"
              aria-label="${this.__effectiveI18n.listOrdered}"
            ></button>
            <button
              id="btn-ul"
              type="button"
              class="ql-list"
              value="bullet"
              part="toolbar-button toolbar-button-list-bullet"
              aria-label="${this.__effectiveI18n.listBullet}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-indent">
            <!-- Decrease -->
            <button
              id="btn-outdent"
              type="button"
              class="ql-indent"
              value="-1"
              part="toolbar-button toolbar-button-outdent"
              aria-label="${this.__effectiveI18n.outdent}"
            ></button>
            <!-- Increase -->
            <button
              id="btn-indent"
              type="button"
              class="ql-indent"
              value="+1"
              part="toolbar-button toolbar-button-indent"
              aria-label="${this.__effectiveI18n.indent}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-alignment">
            <!-- Align buttons -->
            <button
              id="btn-left"
              type="button"
              class="ql-align"
              value=""
              part="toolbar-button toolbar-button-align-left"
              aria-label="${this.__effectiveI18n.alignLeft}"
            ></button>
            <button
              id="btn-center"
              type="button"
              class="ql-align"
              value="center"
              part="toolbar-button toolbar-button-align-center"
              aria-label="${this.__effectiveI18n.alignCenter}"
            ></button>
            <button
              id="btn-right"
              type="button"
              class="ql-align"
              value="right"
              part="toolbar-button toolbar-button-align-right"
              aria-label="${this.__effectiveI18n.alignRight}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-rich-text">
            <!-- Image -->
            <button
              id="btn-image"
              type="button"
              part="toolbar-button toolbar-button-image"
              aria-label="${this.__effectiveI18n.image}"
              @touchend="${this._onImageTouchEnd}"
              @click="${this._onImageClick}"
            ></button>
            <!-- Link -->
            <button
              id="btn-link"
              type="button"
              part="toolbar-button toolbar-button-link"
              aria-label="${this.__effectiveI18n.link}"
              @click="${this._onLinkClick}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-block">
            <!-- Blockquote -->
            <button
              id="btn-blockquote"
              type="button"
              class="ql-blockquote"
              part="toolbar-button toolbar-button-blockquote"
              aria-label="${this.__effectiveI18n.blockquote}"
            ></button>
            <!-- Code block -->
            <button
              id="btn-code"
              type="button"
              class="ql-code-block"
              part="toolbar-button toolbar-button-code-block"
              aria-label="${this.__effectiveI18n.codeBlock}"
            ></button>
          </span>

          <span part="toolbar-group toolbar-group-format">
            <!-- Clean -->
            <button
              id="btn-clean"
              type="button"
              class="ql-clean"
              part="toolbar-button toolbar-button-clean"
              aria-label="${this.__effectiveI18n.clean}"
            ></button>
          </span>

          <input
            id="fileInput"
            type="file"
            accept="image/png, image/gif, image/jpeg, image/bmp, image/x-icon"
            @change="${this._uploadImage}"
          />
        </div>

        <div part="content"></div>

        <div class="announcer" aria-live="polite"></div>
      </div>

      <slot name="tooltip"></slot>

      <slot name="link-dialog"></slot>

      <slot name="color-popup"></slot>

      <slot name="background-popup"></slot>
    `}update(ct){super.update(ct),this.__renderSlottedOverlays()}__renderSlottedOverlays(){de(Zt`
        <vaadin-confirm-dialog
          slot="link-dialog"
          cancel-button-visible
          reject-theme="error"
          .opened="${this._linkEditing}"
          .header="${this.__effectiveI18n.linkDialogTitle}"
          .confirmText="${this.__effectiveI18n.ok}"
          .rejectText="${this.__effectiveI18n.remove}"
          .cancelText="${this.__effectiveI18n.cancel}"
          .rejectButtonVisible="${!!this._linkRange}"
          @confirm="${this._onLinkEditConfirm}"
          @cancel="${this._onLinkEditCancel}"
          @reject="${this._onLinkEditRemove}"
          @opened-changed="${this._onLinkEditingChanged}"
        >
          <vaadin-text-field
            .value="${this._linkUrl}"
            style="width: 100%;"
            @keydown="${this._onLinkKeydown}"
            @value-changed="${this._onLinkUrlChanged}"
          ></vaadin-text-field>
        </vaadin-confirm-dialog>

        <vaadin-rich-text-editor-popup
          slot="color-popup"
          .colors="${["#000000",...[...this.colorOptions].filter(ct=>ct!=="#000000")]}"
          .opened="${this._colorEditing}"
          @color-selected="${this.__onColorSelected}"
          @opened-changed="${this.__onColorEditingChanged}"
        ></vaadin-rich-text-editor-popup>

        <vaadin-rich-text-editor-popup
          slot="background-popup"
          .colors="${["#ffffff",...[...this.colorOptions].filter(ct=>ct!=="#ffffff")]}"
          .opened="${this._backgroundEditing}"
          @color-selected="${this.__onBackgroundSelected}"
          @opened-changed="${this.__onBackgroundEditingChanged}"
        ></vaadin-rich-text-editor-popup>
      `,this,{host:this})}__onBackgroundEditingChanged(ct){this._backgroundEditing=ct.detail.value}__onColorEditingChanged(ct){this._colorEditing=ct.detail.value}_onLinkEditingChanged(ct){if(ct.detail.value){const E=ct.target,D=E.querySelector("vaadin-text-field");E.$.overlay.addEventListener("vaadin-overlay-open",()=>{D.focus({focusVisible:ue()})},{once:!0})}this._linkEditing=ct.detail.value}_onLinkUrlChanged(ct){this._linkUrl=ct.detail.value}}ie(Be);
