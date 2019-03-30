<template>
  <div class="charts" id="myChart" >
    <x-chart :data="this.data"></x-chart>
  </div>
</template>

<script>
import XChart from "./chart.vue";
import Vue from 'vue';
// import testdata from "../testdata.js";
import axios from 'axios';
export default {
  name: "Showtmp",
  data() {
      return {
          data:{},
      };
  },
  props: {
    msg: String,
  },
  components: {
    XChart,
  },
  mounted: function() {
    this.$nextTick(function () {
      setInterval(this.getTmpData(), 1000);
    })
  },
  methods: {
    getTmpData: function () {
      axios({
        method: 'get',
        url: 'http://localhost:5000',
      })
      .then((response) => {
        console.log(response.data);
        var times = [];
        var tmps = [];
        response.data.forEach(function (one) {
            var time = new Date(one.time)
            times.push(time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds());
            tmps.push(one.tmp);
        });
        console.log(times);
        console.log(tmps);

        var bar = {
            chart: {
                type: 'line'
            },
            title: {
                text: 'Monthly Average Temperature'
            },
            subtitle: {
                text: 'Source: WorldClimate.com'
            },
            xAxis: {
                categories: times
            },
            yAxis: {
                title: {
                    text: 'Temperature (°C)'
                }
            },
            plotOptions: {
                line: {
                    dataLabels: {
                        enabled: true
                    },
                    enableMouseTracking: false
                }
            },
            series: [{
                name: '室内温度',
                data: tmps
            }]
        };
        this.$set(this.data, 'bar', bar);

      });

    }
  }
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
