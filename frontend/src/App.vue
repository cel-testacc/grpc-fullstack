<script>
export default {
  data() {
    return {
      selected: '',
      listItems: [],
      bookDetails: {}
    }
  },
  methods: {
    async getData() {
      const res = await fetch("http://127.0.0.1:5000/authors");
      const finalRes = await res.json();
      this.listItems = finalRes;
    },
    async onChange(event) {
      const res = await fetch("http://127.0.0.1:5000/topBookQuotes?author=" + event.target.value);
      const finalRes = await res.json();
      this.bookDetails = finalRes;
    }
  },
  mounted() {
    this.getData()
  }
}

</script>

<template>
  <div>
  <p><span>Select Author: </span>
  <select v-model="selected" @change=onChange>
    <option disabled value="">Please select one</option>
    <option v-for="item in listItems" v-bind:value="item">
        {{item}}
    </option>
    <div>{{bookDetails}}</div>
  </select>
  </p>
  </div>
  <div>
  <h2 v-if="selected">Top Quotes by {{selected}}</h2>
  <div style="display: block;" v-for="books in bookDetails">
    <span>{{books[2]}}</span>
    <span style="font-weight: bold;"> - {{books[1]}}</span>
    <br /><br />
  </div>
  </div>
</template>
