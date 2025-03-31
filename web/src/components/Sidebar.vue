<template>
  <div style="grid-area: sidebar" class="relative bg-white">
    <div class="h-10 border-b w-full flex justify-end items-center px-3">
      <font-awesome-icon
        :icon="['fa', 'rotate']"
        class="text-xl text-gray-300 hover:text-gray-400 cursor-pointer"
        @click.stop="refresh"
      />
    </div>
    <div v-if="!isLoading && count == 0" class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">
      <span class="block text-sm text-black/60 text-center">No Accounts</span>
      <span class="block text-center">
        <a href="#" class="text-sky-300 text-sm underline">add</a>
        <span class="text-sm text-black/60"> or </span>
        <a href="#" @click.prevent="refresh" class="text-sky-300 text-sm underline">refresh</a>
      </span>
    </div>
    <div
      v-if="isLoading"
      class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2"
    >
      <div class="loader !w-12 !h-12 !border-8"></div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.refresh();
  },
  data() {
    return {
      isLoading: true,
      count: 0,
      accounts: [],
    };
  },
  methods: {
    refresh() {
      this.isLoading = true;

      fetch("/api/accounts")
        .then((response) => {
          return response.json();
        })
        .then((jsonResponse) => {
          this.count = jsonResponse.count;
          this.accounts = jsonResponse.data;
        })
        .catch((reason) => {
          console.error(reason);
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
  },
};
</script>
