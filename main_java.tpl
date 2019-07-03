		/*
		 * {{NAME}}
		 */
		if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_enabled)))
		{
		    if (listCmd)
			{
				displayCurrencyPairs(Exchanges.{{NAME}}, ep.getExchange(Exchanges.{{NAME}}).getCurrencyPairs());
			} else {

                ArrayList<CurrencyPair> {{Name}}_cp = cp;
                String bscp = Config.getInstance().get(Constants.{{name}}_currency_pairs);
                if(bscp != null)
                {
                        {{Name}}_cp = new ArrayList<>();
                        for(String pair : bscp.split(",")){
                            {{Name}}_cp.add(new CurrencyPair(pair));
                        }
                } else {
                    {{Name}}_cp = ep.getExchange(Exchanges.{{NAME}}).getCurrencyPairs();
                }

                //Create a ticker from {{Name}}
                if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_ticker_enabled)))
                {
                    thds.addAll(ExchangesFactory.get{{Name}}Factory().create_ticker_feeders(ep, ctx, {{Name}}_cp));
                }

                //Create a orderbook from {{Name}}
                if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_orderbook_enabled)))
                {
                    thds.addAll(ExchangesFactory.get{{Name}}Factory().create_orderbook_feeders(ep, ctx, {{Name}}_cp));
                }
			}
		}

