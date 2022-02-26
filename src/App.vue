<template>
  <div>

    <div class="flex justify-center">
      <LinearRegression
          titleLabel="Housing"
          xScaleLabel="price"
          yScaleLabel="area"
          dataset="dataset/Housing.csv">
      </LinearRegression>
    </div>

    <div class="flex justify-center">
      <LinearRegression
          titleLabel="Housing"
          xScaleLabel="price"
          yScaleLabel="area"
          dataset="dataset/Housing.csv">
      </LinearRegression>
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

