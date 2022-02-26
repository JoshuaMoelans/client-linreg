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
import * as chartjs from "chart.js"

export default {
  name: "LinearRegression",
  data() {
    return {
      slopeValue: 0,
      intersectValue: 0,
      chart: null,
    }
  },
  methods: {
    makeChart(xyValues) {
      chartjs.Chart.register(...chartjs.registerables)

      const context = document.getElementById("chart");

      const data = {
        datasets: [{
          type: "scatter",
          data: xyValues,
          backgroundColor: 'rgb(61,57,57)'
        }, {
          type: "line",
          data: [],
          backgroundColor: 'rgb(91,204,204)'
        }],
      };

      const config = {
        data: data,
        options: {
          animation: false,
          responsive: true,
          scales: {
            x: {
              display: true,
              title: {
                display: true,
                text: "price",
                color: 'rgb(0,0,0)',
                font: {
                  size: 15
                }
              }
            },
            y: {
              display: true,
              title: {
                display: true,
                text: "area",
                color: 'rgb(0,0,0)',
                font: {
                  size: 15
                }
              }
            }
          },
          plugins: {
            legend: {
              display: false
            },
            title: {
              display: true,
              text: "housing",
              font: {
                size: 20
              }
            }
          }
        }
      };

      this.chart = new chartjs.Chart(context, config);
    }
  },
  mounted() {
    d3.csv("dataset/Housing.csv", function (d) {
      return {
        x: d.price,
        y: d.area
      }
    }).then(this.makeChart)
  },
  updated() {
    let a = this.slopeValue
    let b = this.intersectValue

    // TODO: make these values dependent on the dataset values
    const xMax = 14000000
    a /= 10000 // tweak slope slider accuracy
    b *= 1000 // tweak intersect slider accuracy

    this.chart.data.datasets[1].data = [
      {x: 0, y: b},
      {x: xMax, y: a * xMax + b}
    ]
    this.chart.update();
  }
}
</script>
