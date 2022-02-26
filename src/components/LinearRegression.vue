<template>
  <div class="grid grid-cols-2 h-1/2 w-1/2">

    <div class="col-span-2">
      <canvas id="chart"></canvas>
    </div>

    <div class="flex justify-center">
      <div class="flex flex-col w-1/2">
        <input v-model.number="slopeValue" id="slopeSlider"
               type="range" class="form-range"
               min="0" max="21" step="1">
        <div class="flex justify-center">
          <label for="slopeSlider" class="form-label">slope</label>
        </div>
      </div>
    </div>

    <div class="flex justify-center">
      <div class="flex flex-col w-1/2">
        <input v-model.number="intersectValue" id="intersectSlider"
               type="range" class="form-range"
               min="0" max="21" step="1">
        <div class="flex justify-center">
          <label for="intersectSlider" class="form-label">intersect</label>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import * as d3 from "d3"
import {Chart, registerables} from "chart.js"
import {HousingChartConfig} from "@/assets/chart.config.js"

export default {
  name: "LinearRegression",
  data() {
    return {
      slopeValue: 0,
      intersectValue: 0,
      chart: null,
      xMax: 0,
      xMin: 0,
      ymin: 0,
      yMax: 0,
      slopeMax: 0,
      slopeMin: 0
    }
  },
  methods: {
    plotDatapoints(datapoints) {
      // DEBUG: custom datapoints
      // datapoints = [
      //   {x: 1, y: 1},
      //   {x: 2, y: 2},
      //   {x: 3, y: 2},
      //   {x: 2, y: 1},
      // ]

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

      // DEBUG: lower and upper bound helper lines
      // this.chart.data.datasets[2].data = [
      //   {x: 0, y: 0},
      //   {x: this.xMax, y: this.slopeMin * this.xMax}
      // ]
      // this.chart.data.datasets[3].data = [
      //   {x: 0, y: 0},
      //   {x: this.xMax, y: this.slopeMax * this.xMax}
      // ]

      // 2. plot the datapoints
      this.chart.data.datasets[0].data = datapoints;
      this.chart.update();
    }
  },
  mounted() {
    Chart.register(...registerables)
    const context = document.getElementById("chart");
    this.chart = new Chart(context, HousingChartConfig);

    d3.csv("dataset/Housing.csv", function (data) {
      // return dictionary:
      //   - keys (x,y): data format of the chart.js scatter-chart
      //   - values: data[csv header name]
      return {
        x: data['price'],
        y: data['area']
      }
    }).then(this.plotDatapoints)
  },
  updated() {
    let a = this.slopeValue * (this.slopeMax - this.slopeMin) / 20
    let b = this.intersectValue * (this.yMax - this.yMin) / 20

    // plot the linear regression line
    this.chart.data.datasets[1].data = [
      {x: 0, y: b},
      {x: this.xMax, y: a * this.xMax + b}
    ]
    this.chart.update();
  }
}
</script>
