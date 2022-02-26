<template>
  <div class="grid grid-cols-2 h-1/2 w-1/2">

    <div class="col-span-2">
      <canvas id="chart"></canvas>
    </div>

    <div class="flex justify-center">
      <div class="flex flex-col w-1/2">
        <input v-model="slopeValue" id="slopeSlider"
               type="range" class="form-range"
               min="0" max="20" step="1">
        <div class="flex justify-center">
          <label for="slopeSlider" class="form-label">slope</label>
        </div>
      </div>
    </div>

    <div class="flex justify-center">
      <div class="flex flex-col w-1/2">
        <input v-model="intersectValue" id="intersectSlider"
               type="range" class="form-range"
               min="0" max="20" step="1">
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
      xMax: 0
    }
  },
  methods: {
    loadDatapoints(datapoints) {
      this.chart.data.datasets[0].data = datapoints;
      this.xMax = Math.max(...datapoints.map(o=>o.x));  // get largest x-value of the datapoints
      this.chart.update();
    }
  },
  mounted() {
    Chart.register(...registerables)
    const context = document.getElementById("chart");
    this.chart = new Chart(context, HousingChartConfig);

    d3.csv("dataset/Housing.csv", function (data) {
      // return dictionary with:
      //   - keys (x,y): data format of the chart.js scatter-chart
      //   - values (price,area): csv header names
      return {
        x: data.price,
        y: data.area
      }
    }).then(this.loadDatapoints)
  },
  updated() {
    let a = this.slopeValue
    let b = this.intersectValue

    // TODO: make these values dependent on the dataset values
    a /= 10000 // tweak slope slider accuracy
    b *= 1000 // tweak intersect slider accuracy

    this.chart.data.datasets[1].data = [
      {x: 0, y: b},
      {x: this.xMax, y: a * this.xMax + b}
    ]
    this.chart.update();
  }
}
</script>
