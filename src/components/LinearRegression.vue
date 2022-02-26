<template>
  <div class="grid grid-cols-2 h-1/2 w-1/2">

    <div class="col-span-2">
      <canvas ref="canvas"></canvas>
    </div>

    <div class="flex justify-center">
      <div class="flex flex-col w-1/2">
        <input v-model.number="slopeValue" id="slopeSlider"
               type="range" class="form-range appearance-none bg-blue-100"
               :min="minRangeValue" :max="maxRangeValue">
        <div class="flex justify-center">
          <label for="slopeSlider" class="form-label">slope</label>
        </div>
      </div>
    </div>

    <div class="flex justify-center">
      <div class="flex flex-col w-1/2">
        <input v-model.number="intersectValue" id="intersectSlider"
               type="range" class="form-range appearance-none bg-blue-100"
               :min="minRangeValue" :max="maxRangeValue">
        <div class="flex justify-center">
          <label for="intersectSlider" class="form-label">intersect</label>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import * as d3 from "d3"
import {v4 as uuid4} from 'uuid';
import {Chart, registerables} from "chart.js"
import {ChartConfig} from "@/assets/chart.config.js"

export default {
  name: "LinearRegression",
  data() {
    return {
      slopeValue: 0,
      intersectValue: 0,
      minRangeValue: -20,
      maxRangeValue: 20,
      xMax: 0,
      xMin: 0,
      yMin: 0,
      yMax: 0,
      slopeMax: 0,
      slopeMin: 0
    }
  },
  props: {
    titleLabel: String,
    xScaleLabel: String,
    yScaleLabel: String,
    dataset: String
  },
  methods: {
    plotDatapoints(datapoints) {
      // 1. calculate datapoint-dependent values that will help plot the linear regression line

      // 1.1 get smallest and largest x-value
      this.xMin = Math.min(...datapoints.map(o => o.x));
      this.xMax = Math.max(...datapoints.map(o => o.x));

      // 1.2 get smallest and largest y-value
      this.yMin = Math.min(...datapoints.map(o => o.y));
      this.yMax = Math.max(...datapoints.map(o => o.y));

      // 1.3 get smallest and largest slope
      this.slopeMin = Math.min(...datapoints.map(o => (o.y / o.x)))
      this.slopeMax = Math.max(...datapoints.map(o => (o.y / o.x)))

      // 2. plot the datapoints
      this.chart.data.datasets[0].data = datapoints;
      this.chart.update();
    }
  },
  mounted() {
    Chart.register(...registerables)
    const context = this.$refs.canvas;

    ChartConfig.options.scales.x.title.text = this.xScaleLabel;
    ChartConfig.options.scales.y.title.text = this.yScaleLabel;
    ChartConfig.options.plugins.title.text = this.titleLabel;

    this.chart = new Chart(context, ChartConfig);

    d3.csv(this.dataset, (data) => {
      // return dictionary:
      //   - keys (x,y): data format of the chart.js scatter-chart
      //   - values: data[csv header name]
      return {
        x: data[this.xScaleLabel],
        y: data[this.yScaleLabel]
      }
    }).then(this.plotDatapoints)
  },
  updated() {
    let a = this.slopeValue
    a *= this.slopeMax - this.slopeMin // scale slope up
    a /= this.maxRangeValue - this.minRangeValue  // scale slope down
    a *= 1.5 // small tweak

    let b = this.intersectValue
    b *= this.yMax - this.yMin // scale intersect up
    b /= this.maxRangeValue - this.minRangeValue  // scale intersect down
    b *= 1.5 // small tweak

    // plot the linear regression line
    this.chart.data.datasets[1].data = [
      {x: 0, y: b},
      {x: this.xMax, y: a * this.xMax + b}
    ]
    this.chart.update();
  }
}
</script>
