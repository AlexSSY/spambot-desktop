<template>
  <div class="grid-container">
    <Left />
    <Right />
    <Header />
    <Sidebar />
    <Content />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Left from "./components/Left.vue";
import Right from "./components/Right.vue";
import Content from "./components/Content.vue";
import Sidebar from "./components/Sidebar.vue";

export default {
  components: {
    Header,
    Left,
    Right,
    Content,
    Sidebar,
  },
};
</script>
