<template>
  <div style="grid-area: content" class="bg-white flex flex-col">
    <!-- <router-view></router-view> -->
     <div class="flex-1"></div>
    <TextArea />
  </div>
</template>

<script>
import TextArea from "./TextArea.vue";

export default {
  components: { TextArea },
};
</script>
