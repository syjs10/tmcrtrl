<template>
  <div class="chart" id="myChart" >
    <div class="emcs_charts" :id="id" ></div>
  </div>
</template>
<script>
// 引入highCharts模块
import HighCharts from "highcharts";
// 引入这个图表的外部资源数据

export default {
  props: {
    data: Object,
  },
  data:function() {
    // 将引入的数据写在自己的组件中
    let dataObj = this.data;
    return {
      id: "chart",
      dataObj: dataObj
    };
  },
  mounted() {
    //钩子函数挂载时实例化这个图表
    // chart(参数1,参数2);第一个参数挂载组件的容器，第二个参数为图表所需要的数据对象
    HighCharts.chart(this.id, this.dataObj);
  }
};
</script>
<style scoped >

</style>