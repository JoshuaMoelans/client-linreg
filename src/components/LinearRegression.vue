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

// todo: fix scaling on y-axis; difficult bc drawn LR line is probably used for y-axis too

export default {
  name: "LinearRegression",
  data() {
    return {
      slopeValue: 10,
      intersectValue: 10,
      chart: null,
      xMax: 0
    }
  },
  methods: {
    loadDatapoints(datapoints) {
      this.chart.data.datasets[0].data = datapoints;
      this.xMax = Math.max(...datapoints.map(o=>o.x));  // get largest x-value of the datapoints
      this.xMin = Math.min(...datapoints.map(o=>o.x)); // get smallest x-value of the datapoints
      this.chart.update();
    }
  },
  mounted() {
    Chart.register(...registerables)
    const context = document.getElementById("chart");
    this.chart = new Chart(context, HousingChartConfig);

    // todo: ideally, we won't use csv files -> for now it is okay though
    // todo: rename price and area to more general terms (x,y)
    d3.csv("dataset/points.csv", function (data) {
      // return dictionary with:
      //   - keys (x,y): data format of the chart.js scatter-chart
      //   - values (price,area): csv header names
      return {
        x: data.area,
        y: data.price
      }
    }).then(this.loadDatapoints)
  },
  updated() {
    let a = this.slopeValue
    let b = this.intersectValue

    // TODO: make these values dependent on the dataset values
    a *= 300 // tweak slope slider accuracy
    b *= 5000 // tweak intersect slider accuracy

    this.chart.data.datasets[1].data = [
      {x: this.xMin, y: a * this.xMin + b},
      {x: this.xMax, y: a * this.xMax + b}
    ]
    this.chart.update();
  }
}
</script>
