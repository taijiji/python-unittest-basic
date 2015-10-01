テスト駆動開発の正しい流れ
1. まずは、あえて誤った内容で関数を作成し、テストが正常にNGが返してくれてるかを確認する
2. 関数を正しく作成し、テストでOKを出してくれるかを確認
3. 関数を綺麗にして、テストでOKになるかを確認(リファクタリング)

テストを先に書くと、関数のゴールを先に定義できることと同義なので
小さくテストできる。実装がとてもやりやすい。無駄なトラブルシュートを排除できる

初心者にも向いてる開発方法


unittestの実行
```
% python -m unittest tests.test_ex1
```

ブランチを切る -> commit -> pushの流れ

```
git branch a_branch
git checkout a_branch

git add .
git commit -m "initail commit"
git push origin a_branch
```
