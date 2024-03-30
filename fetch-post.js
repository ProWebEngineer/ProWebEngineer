const contentful = require('contentful');

// 環境変数からContentfulの設定を読み込む
const client = contentful.createClient({
  space: process.env.CONTENTFUL_SPACE_ID,
  accessToken: process.env.CONTENTFUL_ACCESS_TOKEN
});

client.getEntries({
  content_type: process.env.CONTENTFUL_CONTENT_TYPE_ID,
  limit: 5
})
.then((response) => {
  const posts = response.items.map((item) => {
    return `- [${item.fields.title}](https://pwe-tech.com/post/${item.fields.slug})`;
  });
  console.log(posts.join('\n'));
})
.catch(console.error);
