/**
 * TIOBE Interactive Chart — reusable component for reveal.js slides.
 *
 * Prerequisites (load before this script):
 *   - Highcharts: https://code.highcharts.com/highcharts.js
 *   - TIOBE data: lib/tiobe-data.js (defines TIOBE_SERIES global)
 *
 * Usage in a slide:
 *   <div id="tiobe-chart" style="width:100%; height:400px;"></div>
 *
 * The chart auto-starts when the slide becomes active (via Reveal event).
 * Dark theme, matching presentation background.
 */
(function () {
  'use strict';

  function initTiobeChart(containerId) {
    containerId = containerId || 'tiobe-chart';
    Highcharts.chart(containerId, {
      chart: {
        type: 'spline',
        backgroundColor: 'transparent',
        style: { fontFamily: 'system-ui, -apple-system, sans-serif' },
        animation: { duration: 1500 }
      },
      title: {
        text: 'TIOBE Programming Community Index',
        style: { color: '#e6edf3', fontSize: '14px', fontWeight: '600' }
      },
      subtitle: {
        text: 'Source: www.tiobe.com',
        style: { color: '#8899aa', fontSize: '10px' }
      },
      xAxis: {
        type: 'datetime',
        labels: {
          style: { color: '#8899aa', fontSize: '9px' },
          format: '{value:%Y}'
        },
        lineColor: 'rgba(255,255,255,0.1)',
        tickColor: 'rgba(255,255,255,0.1)',
        gridLineColor: 'rgba(255,255,255,0.03)'
      },
      yAxis: {
        title: {
          text: 'Ratings (%)',
          style: { color: '#8899aa', fontSize: '10px' }
        },
        labels: {
          style: { color: '#8899aa', fontSize: '9px' },
          format: '{value}%'
        },
        gridLineColor: 'rgba(255,255,255,0.05)',
        min: 0
      },
      legend: {
        itemStyle: { color: '#e6edf3', fontSize: '10px', fontWeight: '400' },
        itemHoverStyle: { color: '#00d2ff' },
        itemHiddenStyle: { color: '#444' }
      },
      tooltip: {
        backgroundColor: 'rgba(13,17,23,0.95)',
        borderColor: 'rgba(255,255,255,0.1)',
        style: { color: '#e6edf3', fontSize: '11px' },
        shared: false,
        headerFormat: '<span style="font-size:10px;color:#8899aa">{point.key:%B %Y}</span><br/>',
        pointFormat: '<span style="color:{series.color}">\u25CF</span> {series.name}: <b>{point.y:.2f}%</b>'
      },
      plotOptions: {
        spline: {
          lineWidth: 2,
          states: {
            hover: { lineWidth: 4 }
          },
          marker: { enabled: false },
          animation: { duration: 2000 }
        },
        series: {
          states: {
            inactive: { opacity: 0.15 }
          }
        }
      },
      credits: { enabled: false },
      series: TIOBE_SERIES.map(function (s) {
        return {
          name: s.name,
          color: s.color,
          data: s.data,
          lineWidth: s.name === 'Python' ? 3 : 1.5
        };
      })
    });
  }

  // Auto-init when Reveal slide containing the chart becomes active
  if (typeof Reveal !== 'undefined') {
    Reveal.on('slidechanged', function (event) {
      var container = event.currentSlide.querySelector('#tiobe-chart');
      if (container && !container.dataset.initialized) {
        container.dataset.initialized = 'true';
        setTimeout(function () { initTiobeChart('tiobe-chart'); }, 200);
      }
    });
    Reveal.on('ready', function (event) {
      var container = event.currentSlide.querySelector('#tiobe-chart');
      if (container && !container.dataset.initialized) {
        container.dataset.initialized = 'true';
        setTimeout(function () { initTiobeChart('tiobe-chart'); }, 200);
      }
    });
  }

  // Export for manual use
  window.initTiobeChart = initTiobeChart;
})();
