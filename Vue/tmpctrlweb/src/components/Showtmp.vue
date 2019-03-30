<template>
  <div class="charts" id="myChart" >
    <x-chart :tmpData="this.data.tmpData"></x-chart>
  </div>
</template>

<script>
import XChart from "./chart.vue";
import Vue from 'vue';
import tpldata from "../testdata.js";
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
  created() {
    this.$nextTick(function () {
      setInterval(
          () => {
            this.getTmpData();
          }, 1000
      );
    })
  },
  methods: {
    getTmpData: function () {
      axios({
        method: 'get',
        url: 'http://localhost:5000',
      })
      .then((response) => {
        var times = [];
        var tmps = [];
        response.data.forEach(function (one) {
            var time = new Date(one.time)
            times.push(time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds());
            tmps.push(one.tmp);
        });
        tpldata['series'] = [{
            name: '室内温度',
            data: tmps
        }];
        this.$set(this.data, 'tmpData', tpldata);
      });

    }
  }
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
