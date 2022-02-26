<template>
  <div>

    <div class="flex justify-center">
      <div class="w-2/5">
        <LinearRegression
            title-label="Housing"
            x-scale-label="Price"
            y-scale-label="Area"
            x-csv-header="price"
            y-csv-header="area"
            dataset="dataset/Housing.csv">
        </LinearRegression>
      </div>
    </div>

    <div class="flex justify-center">
      <div class="w-2/5">
        <LinearRegression
            title-label="Poison"
            x-scale-label="Weigth"
            y-scale-label="survival time"
            x-csv-header="Weight"
            y-csv-header="Surv_time"
            dataset="dataset/Poison.csv">
        </LinearRegression>
      </div>
    </div>

    <div class="flex justify-center">
      <div class="w-2/5">
        <LinearRegression
            title-label="Points"
            x-scale-label="Area"
            y-scale-label="Price"
            x-csv-header="area"
            y-csv-header="price"
            dataset="dataset/points.csv">
        </LinearRegression>
      </div>
    </div>

  </div>
</template>

<script>
import LinearRegression from './components/LinearRegression.vue'

export default {
  name: 'App',
  components: {
    LinearRegression
  }
}
</script>

