<template>
  <div class="chart" id="myChart" >
    <div class="emcs_charts" :id="id1" ></div>
  </div>
</template>
<script>
// 引入highCharts模块
import HighCharts from "highcharts";
// 引入这个图表的外部资源数据

export default {
  props: {
    tmpData: Object,
    tmps: Array,
  },
  data() {
    return {
      id1:'chart',
    }
  },
  watch: {
    tmps: function(newdata) {
      this.tmpData['series'] = [{
            name: '室内温度',
            data: newdata
        }];
      HighCharts.chart(this.id1, this.tmpData);
    }
  }
};
</script>
<style scoped >

</style>